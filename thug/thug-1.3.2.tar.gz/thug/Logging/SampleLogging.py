#!/usr/bin/env python
#
# SampleLogging.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA

import os
import base64
import logging
import hashlib
import zipfile
import tempfile
import pefile
import magic

SSDEEP = True

try:
    import ssdeep
except ImportError:  # pragma: no cover
    SSDEEP = False

from thug.Magic.Magic import Magic

log = logging.getLogger("Thug")


class SampleLogging(object):
    def __init__(self):
        self.types = ('PE',
                      'PDF',
                      'JAR',
                      'SWF',
                      'DOC',
                      'RTF', )

    def is_pe(self, data):
        try:
            pefile.PE(data = data, fast_load = True)
        except Exception:
            return False

        return True

    def get_imphash(self, data):
        try:
            pe = pefile.PE(data = data)
        except Exception:
            return None

        return pe.get_imphash()

    def is_pdf(self, data):
        if isinstance(data, str):
            data = data.encode()

        return (data[:1024].find(b'%PDF') != -1)

    def is_jar(self, data):
        if isinstance(data, str):
            data = data.encode()

        fd, jar = tempfile.mkstemp()

        with open(jar, 'wb') as fd:
            fd.write(data)

        try:
            z = zipfile.ZipFile(jar)
            if [t for t in z.namelist() if t.endswith('.class')]:
                os.remove(jar)
                return True
        except Exception as e:
            log.info("[ERROR][is_jar] %s", str(e))

        os.remove(jar)
        return False

    def is_swf(self, data):
        if isinstance(data, str):
            data = data.encode()

        return data.startswith(b'CWS') or data.startswith(b'FWS')

    def is_doc(self, data):
        if isinstance(data, str):
            data = data.encode()

        doc_mime_types = (
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        )

        return Magic(data).get_mime() in doc_mime_types

    def is_rtf(self, data):
        rtf_mime_types = (
            'text/rtf',
            'application/rtf',
        )

        return magic.from_buffer(data, mime = True) in rtf_mime_types

    def get_sample_type(self, data):
        for t in self.types:
            p = getattr(self, 'is_%s' % (t.lower(), ), None)
            if p and p(data):
                return t

        return None

    def build_sample(self, data, url = None, sampletype = None):
        if not data:
            return None

        p = dict()

        if sampletype:
            p['type'] = sampletype
            if isinstance(data, str):
                data = data.encode()
        else:
            p['type'] = self.get_sample_type(data)

        if p['type'] is None:
            return None

        p['md5']    = hashlib.md5(data).hexdigest()
        p['sha1']   = hashlib.sha1(data).hexdigest()
        p['sha256'] = hashlib.sha256(data).hexdigest()

        if SSDEEP:
            p['ssdeep'] = ssdeep.hash(data)

        if p['type'] in ('PE', ):
            imphash = self.get_imphash(data)
            if imphash:
                p['imphash'] = imphash

        if url:
            p['url'] = url

        p['data'] = base64.b64encode(data).decode()
        return p
