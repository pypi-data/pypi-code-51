
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: ./nb/common.ipynb

import os
IN_TRAVIS=os.getenv('TRAVIS', False)

#https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook
def isnotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter
IN_JUPYTER = isnotebook()


# use those only in jupyter
from IPython.display import display, Javascript
import time

def save_notebook(): display(Javascript('IPython.notebook.save_checkpoint();'))

def restart_kernel():display(Javascript('IPython.notebook.kernel.restart();'))

def save_and_export_notebook(name):

    assert IN_JUPYTER

    save_notebook()
    NOTEBOOK_EXTEND_NAME='.ipynb'
    if NOTEBOOK_EXTEND_NAME not in name:
        name += NOTEBOOK_EXTEND_NAME
    time.sleep(1)

    # support import complie
    ip = get_ipython()
    ip.run_cell(f'!python notebook2script.py {name}')
    ip.run_cell(f'!python notebook2test_script.py {name}')

    save_notebook() # for exitting



# https://docs.python.org/3/library/asyncio-subprocess.html
import asyncio
import sys
import datetime
import time

# https://stackoverflow.com/questions/44633458/why-am-i-getting-notimplementederror-with-async-and-await-on-windows
# asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

async def async_run(run_args=[sys.executable, '-c', "import time;print('ing',  flush=True);time.sleep(2);print('done')",]
                   , wait_child_sec=3):

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        *run_args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    await asyncio.wait_for(proc.wait(), timeout=wait_child_sec)

    line=''

    data = await proc.stdout.read()
    line += data.decode('ascii').rstrip()

    line += '\n'

    data = await proc.stderr.read()
    line += data.decode('ascii').rstrip()

    if line: print(line)
