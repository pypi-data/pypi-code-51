# (C) Copyright 2018 by Rocky Bernstein
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""Python disassembly functions specific to wordcode from Python 3.6+
"""
from xdis import PYTHON3
from xdis.bytecode import op_has_argument

def unpack_opargs_wordcode(code, opc):
    extended_arg = 0
    try:
        n = len(code)
    except TypeError:
        code = code.co_code
        n = len(code)

    if isinstance(code[0], str):
        # This happens handling Python 3.x on a 2.x interpreter
        for i in range(0, n, 2):
            op = ord(code[i])
            if op_has_argument(op, opc):
                arg = ord(code[i+1]) | extended_arg
                if op == opc.EXTENDED_ARG:
                    extended_arg = (arg << 8)
                else:
                    extended_arg = 0
                    pass
            else:
                arg = None
            yield (i, op, arg)
    else:
        for i in range(0, n, 2):
            op = code[i]
            if op_has_argument(op, opc):
                arg = code[i+1] | extended_arg
                if op == opc.EXTENDED_ARG:
                    extended_arg = (arg << 8)
                else:
                    extended_arg = 0
                    pass
            else:
                arg = None
                pass
            yield (i, op, arg)

def findlinestarts(code, dup_lines=False):
    """Find the offsets in a byte code which are start of lines in the source.

    Generate pairs (offset, lineno) as described in Python/compile.c.

    """
    if PYTHON3:
        byte_increments = code.co_lnotab[0::2]
        line_increments = code.co_lnotab[1::2]
    else:
        byte_increments = [ord(c) for c in code.co_lnotab[0::2]]
        line_increments = [ord(c) for c in code.co_lnotab[1::2]]

    lastlineno = None
    lineno = code.co_firstlineno
    addr = 0
    for byte_incr, line_incr in zip(byte_increments, line_increments):
        if byte_incr:
            if (lineno != lastlineno or
                (not dup_lines and 0 < byte_incr < 255)):
                yield (addr, lineno)
                lastlineno = lineno
            addr += byte_incr
        if line_incr >= 0x80:
            # line_increments is an array of 8-bit signed integers
            line_incr -= 0x100
        lineno += line_incr
    if (lineno != lastlineno or
        (not dup_lines and 0 < byte_incr < 255)):
        yield (addr, lineno)


def get_jump_targets(code, opc):
    """Returns a list of instruction offsets in the supplied bytecode
    which are the targets of some sort of jump instruction.
    """
    offsets = []
    for offset, op, arg in unpack_opargs_wordcode(code, opc):
        if arg is not None:
            if op in opc.JREL_OPS:
                jump_offset = offset + 2 + arg
            elif op in opc.JABS_OPS:
                jump_offset = arg
            else:
                continue
            if jump_offset not in offsets:
                offsets.append(jump_offset)
    return offsets

def get_jump_target_maps(code, opc):
    """Returns a dictionary where the key is an offset and the values are
    a list of instruction offsets which can get run before that
    instruction. This includes jump instructions as well as non-jump
    instructions. Therefore, the keys of the dictionary are reachible
    instructions. The values of the dictionary may be useful in control-flow
    analysis.
    """
    offset2prev = {}
    prev_offset = -1
    for offset, op, arg in unpack_opargs_wordcode(code, opc):
        if prev_offset >= 0:
            prev_list = offset2prev.get(offset, [])
            prev_list.append(prev_offset)
            offset2prev[offset] = prev_list
        prev_offset = offset
        if op in opc.NOFOLLOW:
            prev_offset = -1
        if arg is not None:
            jump_offset = -1
            if op in opc.JREL_OPS:
                jump_offset = offset + 2 + arg
            elif op in opc.JABS_OPS:
                jump_offset = arg
            if jump_offset >= 0:
                prev_list = offset2prev.get(jump_offset, [])
                prev_list.append(offset)
                offset2prev[jump_offset] = prev_list
    return offset2prev


findlabels = get_jump_targets
