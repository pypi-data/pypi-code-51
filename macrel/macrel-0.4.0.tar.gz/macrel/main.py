import argparse
import subprocess
import tempfile
import gzip
import logging
import os
from os import path

def makedirs(dname, exist_ok=False):
    '''Reimplement os.makedirs for Python 2 compatibility'''
    import os
    import sys
    if sys.version_info.major >= 3:
        return os.makedirs(dname, exist_ok=exist_ok)
    if exist_ok and path.exists(dname):
        return
    os.makedirs(dname)


def error_exit(args, errmessage):
    import sys
    sys.stderr.write(errmessage+'\n')
    sys.exit(1)

def data_file(fname):
    return path.join(path.dirname(__file__),
                    'data',
                    fname)


def parse_args(args):
    from .macrel_version import __version__
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='macrel v{}'.format(__version__))

    parser.add_argument('command', nargs=1,
            help='Macrel command to execute (see documentation)')
    parser.add_argument('-t', '--threads', required=False, action='store',
            help='Number of threads to use',
            default='1', dest='threads')
    parser.add_argument('-o', '--output', required=False, default=None,
            help='path to the output directory', dest='output')
    parser.add_argument('--file-output', required=False, default=None,
            help='path to the output file', dest='output_file')
    parser.add_argument('--tag', required=False, default='macrel.out',
            help='Set output tag', dest='outtag')
    parser.add_argument('-f', '--fasta', required=False,
            help='path to the input FASTA file. This is used in both the peptides command (where the file is expected to contain short amino-acid sequences) and in the contigs command (where the file is expected to contain longer nucleotide contigs)', dest='fasta_file')
    parser.add_argument('-1', '--reads1', required=False, action='store',
            dest='reads1')
    parser.add_argument('-2', '--reads2', required=False, action='store',
            default=None, dest='reads2')
    parser.add_argument('--mem', required=False, action='store', default='0.75', )
    parser.add_argument('--cluster', required=False, action='store_true', default=False, dest='cluster',
            help='Whether to pre-cluster the smORFs (at 100%% identity) to avoid repeats')
    parser.add_argument('--force', required=False, action='store_true')
    parser.add_argument('--keep-fasta-headers', required=False, action='store_true', default=False, dest='keep_fasta_headers',
            help='Keep complete FASTA headers [get-smorfs command]')
    parser.add_argument('--tmpdir', required=False, default=None, dest='tmpdir', action='store',
            help='Temporary directory to use (default: $TMPDIR in the environment or /tmp)')
    parser.add_argument('--keep-negatives', required=False, default=False, dest='keep_negatives', action='store_true',
            help='Whether to keep non-AMPs in the output')
    parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s {version}'.format(version=__version__))
    return parser.parse_args()


def validate_args(args):
    from os import path
    if len(args.command) != 1:
        error_exit(args, 'Could not parse argument list (multiple commands given?)')
    [args.command] = args.command
    if args.command == 'get-examples':
        return
    if args.command == 'peptides':
        if not args.fasta_file:
            error_exit(args, "PEPTIDE File is necessary for 'peptides' command.")
    elif args.command == 'contigs':
        if not args.fasta_file:
            error_exit(args, "FASTA File is necessary for 'contigs' command.")
    elif args.command == 'reads':
        if not args.reads1:
            error_exit(args, "FQ file is necessary for 'reads' command.")
    elif args.command == 'abundance':
        if not args.reads1:
            error_exit(args, "FQ file is necessary for 'abundance' command.")
        if not args.fasta_file:
            error_exit(args, "Fasta file is necessary for 'abundance' command.")
    elif args.command == 'get-smorfs':
        if not args.fasta_file:
            error_exit(args, "Fasta file is necessary for 'get-smorfs' command.")
    else:
        error_exit(args, "Unknown command {}".format(args.command))
    if not args.output and not args.output_file:
        error_exit(args, "Either --output or --file-output argument must be used")

    if args.keep_fasta_headers and args.command != 'get-smorfs':
        error_exit(args, '--keep-fasta-headers is only available for get-smorfs command')

    args.output_dir = args.output
    if args.output_dir:
        if not path.exists(args.output_dir):
            makedirs(args.output, exist_ok=True)
        elif args.force:
            import sys
            sys.stderr("Output folder already exists, but --force flag was used")
        else:
            error_exit(args, "Output folder [{}] already exists".format(args.output_dir))
    elif args.command != 'get-smorfs':
        error_exit(args, '--file-output is only possible for `get-smorfs` command')


def do_smorfs(args, tdir):
    from .filter_smorfs import filter_smorfs
    if args.output_dir:
        all_peptide_file = path.join(args.output, args.outtag+'.all_orfs.faa')
        peptide_file = path.join(args.output, args.outtag+'.smorfs.faa')
    else:
        all_peptide_file = path.join(tdir, 'all_orfs.faa')
        peptide_file = (args.output_file if args.output_file != '-' else '/dev/stdout')
    fasta_file = link_or_uncompress_fasta_file(
                    args.fasta_file,
                    path.join(tdir, 'contigs.fna'))
    subprocess.check_call(
            ['prodigal_sm',
                '-c', # Closed ends.  Do not allow genes to run off edges.
                '-m', # Treat runs of N as masked sequence; don't build genes across them.
                '-n', # Bypass Shine-Dalgarno trainer and force a full motif scan.

                '-p', 'meta',

                # -f:  Select output format (gbk, gff, or sco).  Default is gbk.
                '-f', 'sco',

                # -a:  Write protein translations to the selected file.
                '-a', all_peptide_file,

                # input file
                '-i', fasta_file],
            )
    filter_smorfs(all_peptide_file, peptide_file, args.cluster, args.keep_fasta_headers)
    args.fasta_file = peptide_file

def link_or_uncompress_fasta_file(orig, dest):
    '''
    If the input is compress, uncompress it. Otherwise, link it to `dest`
    '''
    if orig.endswith('.gz'):
        logging.debug('Uncompressing FASTA file ({})'.format(orig))
        with open(dest, 'wb') as ofile:
            with gzip.open(orig, 'rb') as ifile:
                while True:
                    chunk = ifile.read(32*1024)
                    if not chunk:
                        break
                    ofile.write(chunk)
    else:
        os.symlink(path.abspath(orig), dest)
    return dest

def do_abundance(args, tdir):
    do_read_trimming(args, tdir)
    sam_file = path.join(tdir, 'paladin.out.sam')
    fasta_file = link_or_uncompress_fasta_file(
                        args.fasta_file,
                        path.join(tdir, 'paladin.faa'))

    subprocess.check_call([
        'paladin', 'index',

        # -r<#>  Reference type:
        #     1: Reference contains nucleotide sequences (requires corresponding .gff annotation)
        #     2: Reference contains nucleotide sequences (coding only, eg curated transcriptome)
        #     3: Reference contains protein sequences (UniProt or other source)
        #     4: Development tests
        '-r3',
        fasta_file])
    logging.debug('Mapping reads against references')
    with open(sam_file, 'wb') as sout:
        subprocess.check_call([
            'paladin', 'align',

            # -t INT        number of threads [1]
            '-t', str(args.threads),

            # -T INT        minimum score to output [15]
            '-T', '20',

            # -f INT        minimum ORF length accepted (as constant value) [250]
            '-f', '10',

            # -z INT[,...]  Genetic code used for translation (-z ? for full list) [1]
            '-z', '11',

            # -a            output all alignments for SE or unpaired PE
            '-a',

            #-V            output the reference FASTA header in the XR tag
            '-V',

            # -M            mark shorter split hits as secondary
            '-M',
            fasta_file,
            path.join(tdir, 'preproc.pair.1.fq.gz')],
            stdout=sout)
    subprocess.check_call([
        'ngless',
        '--no-create-report',
        '--quiet',
        '-j', str(args.threads),
        data_file('scripts/count.ngl'),
        sam_file,
        path.join(args.output, args.outtag + '.abundance.txt')])

def do_read_trimming(args, tdir):
    ofile = path.join(tdir, 'preproc.fq.gz')
    if args.reads2:
        ngl_file = data_file('scripts/trim.pe.ngl')
        ngl_args = [args.reads1, args.reads2, ofile]
    else:
        ngl_file = data_file('scripts/trim.se.ngl')
        ngl_args = [args.reads1, ofile]
    subprocess.check_call([
        'ngless',
        '--no-create-report',
        '--quiet',
        '-j', str(args.threads),
        ngl_file,
        ] + ngl_args)

def do_assembly(args, tdir):
    if args.reads2:
        megahit_args = ['-1', path.join(tdir, 'preproc.pair.1.fq.gz'),
                        '-2', path.join(tdir, 'preproc.pair.2.fq.gz')]
    else:
        megahit_args = ['-r', path.join(tdir, 'preproc.pair.1.fq.gz')]
    megahit_output = path.join(args.output, args.outtag + '.megahit_output')
    do_read_trimming(args, tdir)
    subprocess.check_call([
        'megahit',
        '--presets', 'meta-large',
        '-o', megahit_output, # output directory
        '-t', str(args.threads),
        '-m', str(args.mem),
        '--min-contig-len', '1000',
        ] + megahit_args)
    args.fasta_file = path.join(megahit_output, 'final.contigs.fa')

def do_predict(args, tdir):
    # These imports are slow, so we do them inside the functions
    from .AMP_features import features
    from .AMP_predict import predict
    fs = features(args.fasta_file)
    prediction = predict(
                    data_file("models/AMP.pkl.gz"),
                    data_file("models/Hemo.pkl.gz"),
                    fs,
                    args.keep_negatives)
    ofile = path.join(args.output, args.outtag + '.prediction.gz')
    prediction.to_csv(ofile, sep='\t', index_label='Access', float_format="%.3f")

def do_get_examples(args):
    try:
        from urllib.request import urlretrieve
    except:
        from urllib2 import urlretrieve

    DATA_FILES = [
        'excontigs.fna.gz',
        'expep.faa.gz',
        'R1.fq.gz',
        'R2.fq.gz',
        'ref.faa.gz',
        ]
    BASEURL = 'https://github.com/BigDataBiology/macrel/raw/master/example_seqs/'
    if path.exists('example_seqs') and not args.force:
        error_exit(args, 'example_seqs/ directory already exists')
    makedirs('example_seqs', exist_ok=True)
    for f in DATA_FILES:
        print('Retrieving {}...'.format(f))
        urlretrieve(BASEURL + f, 'example_seqs/'+f)


def main(args=None):
    if args is None:
        import sys
        args = sys.argv
    args = parse_args(args)
    validate_args(args)
    if args.command == 'get-examples':
        do_get_examples(args)
        return
    with tempfile.TemporaryDirectory(dir=args.tmpdir) as tdir:
        if args.command == 'reads':
            do_assembly(args, tdir)
        if args.command in ['reads', 'contigs', 'get-smorfs']:
            do_smorfs(args, tdir)
        if args.command in ['reads', 'contigs', 'peptides']:
            do_predict(args, tdir)
        if args.command == 'abundance':
            do_abundance(args, tdir)

if __name__ == '__main__':
    import sys
    main(sys.argv)
