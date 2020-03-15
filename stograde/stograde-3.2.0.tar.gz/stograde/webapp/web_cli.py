import os

from . import server
from ..common import chdir
from ..student import stash, pull, checkout_date
from ..student.markdownify.process_file import process_file
from ..student.markdownify.supporting import import_supporting, remove_supporting
from PyInquirer import style_from_dict, Token, prompt


def launch_cli(basedir, date, no_update, spec, spec_id, usernames):
    """Start the web grading CLI"""
    usernames = [
        '{} NO SUBMISSION'.format(user)
        if not os.path.exists('{}/{}'.format(user, spec['assignment']))
        else user
        for user in usernames
    ]

    while True:
        student = ask_student(usernames)

        if not student or student == 'QUIT':
            return False
        elif student == 'LOG and QUIT':
            return True
        elif 'NO SUBMISSION' in student:
            continue

        stash(student, no_update=no_update)
        pull(student, no_update=no_update)

        checkout_date(student, date=date)

        files = check_student(student, spec, spec_id, basedir)

        if files:
            ask_file(files, student, spec, spec_id, basedir)


def ask_student(usernames):
    """Ask user to select a student"""
    style = style_from_dict({
        Token.QuestionMark: '#959ee7 bold',
        Token.Selected: '#959ee7',
        Token.Pointer: '#959ee7 bold',
        Token.Answer: '#959ee7 bold',
    })
    questions = [
        {
            'type': 'list',
            'name': 'student',
            'message': 'Choose student',
            'choices': ['QUIT', 'LOG and QUIT', *usernames]
        }
    ]

    student = prompt(questions, style=style)

    if not student:
        return None

    return student['student']


def check_student(student, spec, spec_id, basedir):
    """Process student's files and populate file list"""
    files = []
    if os.path.exists('{}/{}'.format(student, spec['assignment'])):
        print('Processing...')
        with chdir('{}/{}'.format(student, spec['assignment'])):
            # prepare the current folder
            supporting_dir, written_files = import_supporting(spec=spec,
                                                              spec_id=spec_id,
                                                              basedir=basedir)

            for file in spec['files']:
                if 'web' in file['options']:
                    # Process file just enough to determine if it exists and/or is optional
                    result = process_file(file['filename'],
                                          steps=[],             # Thus, run no compile commands
                                          options=file['options'],
                                          tests=[],             # And no tests
                                          spec=spec,
                                          cwd=os.getcwd(),
                                          supporting_dir=supporting_dir,
                                          interact=False,
                                          skip_web_compile=False)

                    description = file['filename']

                    if result['missing']:
                        if 'optional' in file['options']:
                            description = '{} MISSING (OPTIONAL)'.format(file['filename'])
                        else:
                            description = '{} MISSING'.format(file['filename'])

                    files = files + [description]
                else:
                    continue
            # and we remove any supporting files
            remove_supporting(written_files)

    return files


def ask_file(files, student, spec, spec_id, basedir):
    """Ask user to select a file to view"""
    style = style_from_dict({
        Token.QuestionMark: '#e3bd27 bold',
        Token.Selected: '#e3bd27',
        Token.Pointer: '#e3bd27 bold',
        Token.Answer: '#e3bd27 bold',
    })

    while True:
        questions = [
            {
                'type': 'list',
                'name': 'file',
                'message': 'Choose file',
                'choices': ['BACK'] + files,
            }
        ]
        file = prompt(questions, style=style)

        # File has been selected so process and display it
        if file and file['file'] != 'BACK':
            file_spec = {}
            for f in spec['files']:
                if f['filename'] == file['file']:
                    file_spec = f
                    break
            if file_spec:
                with chdir('{}/{}'.format(student, spec['assignment'])):
                    # prepare the current folder
                    supporting_dir, written_files = import_supporting(spec=spec,
                                                                      spec_id=spec_id,
                                                                      basedir=basedir)
                    process_file(file_spec['filename'],
                                 steps=file_spec['commands'],
                                 options=file_spec['options'],
                                 tests=file_spec['tests'],
                                 spec=spec,
                                 cwd=os.getcwd(),
                                 supporting_dir=supporting_dir,
                                 interact=False,
                                 skip_web_compile=False)

                    server.work_dir = os.getcwd()

                    # and we remove any supporting files
                    remove_supporting(written_files)

        else:
            return


def check_web_spec(spec):
    """Check if the spec contains any web files"""
    web_spec = False
    for file in spec['files']:
        if 'web' in file['options']:
            web_spec = True
            break
    return web_spec
