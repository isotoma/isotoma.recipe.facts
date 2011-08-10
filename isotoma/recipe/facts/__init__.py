# Copyright 2011 Isotoma Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import socket
import fcntl
import array
import struct
import platform
import subprocess
from zc.buildout import UserError

SIOCGIFCONF = 0x8912
MAXBYTES = 8096


class Facts(object):

    def __init__(self, buildout, name, options):
        self.name = name
        self.options = options
        self.buildout = buildout

        options['hostname'] = socket.gethostname()
        options['fqdn'] = socket.getfqdn()

        self.set_interfaces()
        self.set_vcs()

    def set_interfaces(self):
        if platform.system() != "Linux":
            return

        arch = platform.architecture()[0]

        if arch == '32bit':
            recordlen = 32
        elif arch == '64bit':
            recordlen = 40
        else:
            return

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        buffer = array.array('B', '\0' * MAXBYTES)
        size, ptr = struct.unpack('iL', fcntl.ioctl(
            sock.fileno(),
            SIOCGIFCONF,
            struct.pack('iL', MAXBYTES, buffer.buffer_info()[0])
            ))

        namestr = buffer.tostring()

        for i in range(0, size, recordlen):
            iface = namestr[i:].split('\0', 1)[0]
            ip = socket.inet_ntoa(namestr[i+20:i+24])
            self.options["interfaces.%s.address" % iface] = ip

        sock.close()

    def set_vcs(self):
        vcs_dir = self.buildout["buildout"].get("cwd", self.buildout["buildout"]["directory"])

        if os.path.exists(os.path.join(vcs_dir, ".svn")):
            self.options["vcs.type"] = "svn"

            p = subprocess.Popen(["svn", "info", vcs_dir], stdout=subprocess.PIPE)
            s, e = p.communicate()

            for line in s.split("\n"):
                if ":" in line:
                    k, v = line.split(": ")
                    k = "vcs." + k.strip().lower().replace(" ", "-")
                    v = v.strip()

                    self.options[k] = v

            self.options['vcs.branch'] = self.options['vcs.url'].replace(self.options['vcs.repository-root'], '')

        elif os.path.exists(os.path.join(vcs_dir, ".git")):
            self.options["vcs.type"] = "git"

    def install(self):
        return ()

    update = install

