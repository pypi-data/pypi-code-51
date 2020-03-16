#
#  --------------------------------------------------------------------------
#   Gurux Ltd
#
#
#
#  Filename: $HeadURL$
#
#  Version: $Revision$,
#                   $Date$
#                   $Author$
#
#  Copyright (c) Gurux Ltd
#
# ---------------------------------------------------------------------------
#
#   DESCRIPTION
#
#  This file is a part of Gurux Device Framework.
#
#  Gurux Device Framework is Open Source software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2 of the License.
#  Gurux Device Framework is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  More information of Gurux products: http://www.gurux.org
#
#  This code is licensed under the GNU General Public License v2.
#  Full text may be retrieved at http://www.gnu.org/licenses/gpl-2.0.txt
# ---------------------------------------------------------------------------
#pylint: disable=broad-except,no-name-in-module
try:
    from enum import IntEnum
    __base = IntEnum
except Exception:
    __base = object

class AutoAnswerMode(__base):
    #pylint: disable=too-few-public-methods

    #
    # Line dedicated to the device.
    #
    DEVICE = 0
    #
    # Shared line management with a limited number of calls allowed.  Once the
    # number of calls is reached, the window status becomes inactive until the
    # next start date, whatever the result of the call,
    #
    CALL = 1
    #
    # Shared line management with a limited number of successful calls
    # allowed.
    # Once the number of successful communications is reached, the window
    # status becomes inactive until the next start date,
    #
    CONNECTED = 2
    #
    # Currently no modem connected.
    #
    NONE = 4
