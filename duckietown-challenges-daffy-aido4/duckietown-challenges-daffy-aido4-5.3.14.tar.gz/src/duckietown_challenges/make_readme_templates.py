# coding=utf-8
import argparse
import os
import sys

from .submission_read import read_submission_info
from . import dclogger, DEFAULT_DTSERVER


def make_readmes_templates_main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-C", dest="cwd", default=".", help="Base directory")

    parsed = parser.parse_args(sys.argv[1:])

    d = parsed.cwd

    f = os.path.join(d, "submission.yaml")
    if not os.path.exists(f):
        msg = 'Please run in a directory containing "submission.yaml".'
        raise Exception(msg)

    basedir, si = read_submission_info(f)

    out = ""

    # language=markdown
    base = """    
<!-- do not modify - autogenerated -->
 
# AI Driving Olympics

<a href="http://aido.duckietown.org"><img width="200" src="https://www.duckietown.org/wp-content/uploads/2018/07/AIDO-768x512.png"/></a>


## Template "{si.user_label}" for challenge `{si.challenge_name}`

This is a template for one of the challenges in the [the AI Driving Olympics](http://aido.duckietown.org/).

The [online description of this challenge is here][online].

For submitting, please follow [the instructions available in the book][book].
 
[book]: http://docs.duckietown.org/DT18/AIDO/out/

[online]: {DTSERVER}/humans/challenges/{si.challenge_name}

## Description

{si.description}

""".format(
        si=si, DTSERVER=DEFAULT_DTSERVER
    ).strip()

    out += base

    fn = os.path.join(d, "README.md")
    with open(fn, "w") as f:
        f.write(out)

    dclogger.info("written to %s" % fn)


if __name__ == "__main__":
    make_readmes_templates_main()
