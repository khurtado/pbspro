# coding: utf-8

# Copyright (C) 1994-2016 Altair Engineering, Inc.
# For more information, contact Altair at www.altair.com.
#
# This file is part of the PBS Professional ("PBS Pro") software.
#
# Open Source License Information:
#
# PBS Pro is free software. You can redistribute it and/or modify it under the
# terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# PBS Pro is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Commercial License Information:
#
# The PBS Pro software is licensed under the terms of the GNU Affero General
# Public License agreement ("AGPL"), except where a separate commercial license
# agreement for PBS Pro version 14 or later has been executed in writing with
# Altair.
#
# Altair’s dual-license business model allows companies, individuals, and
# organizations to create proprietary derivative works of PBS Pro and
# distribute them - whether embedded or bundled with other software - under a
# commercial license agreement.
#
# Use of Altair’s trademarks, including but not limited to "PBS™",
# "PBS Professional®", and "PBS Pro™" and Altair’s logos is subject to Altair's
# trademark licensing policies.

from tests.functional import *


class Test_periodic_constant(TestFunctional):
    """
    Test if pbs.PERIODIC constant is available in pbs module.
    """
    hook_script = """
import pbs
e = pbs.event()
if e.type == pbs.PERIODIC:
    pbs.logmsg(pbs.EVENT_DEBUG,"This hook is using pbs.PERIODIC")
"""

    def test_periodic_constant_via_server_log(self):
        """
        Create periodic hook. The hook will test the availability of
        pbs.PERIODIC. If constant is available the hook will write a log
        message to the server_log.
        """
        hook_name = "periodic_constant"
        hook_attrib = {'event': 'periodic', 'freq': 5}
        retval = self.server.create_import_hook(hook_name,
                                                hook_attrib,
                                                self.hook_script,
                                                overwrite=True)
        self.assertTrue(retval)

        retval = self.server.log_match("This hook is using pbs.PERIODIC",
                                       max_attempts=10)
        self.assertTrue(retval)
