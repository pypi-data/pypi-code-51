#!/usr/bin/env python

__author__ = "Christopher Hahne"
__email__ = "info@christopherhahne.de"
__license__ = """
    Copyright (c) 2019 Christopher Hahne <info@christopherhahne.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# local imports
from plenopticam.misc import safe_get
from plenopticam.misc.status import PlenopticamStatus
from plenopticam.cfg import PlenopticamConfig
from plenopticam.lfp_aligner.cfa_processor import CfaProcessor

# external libs
import json
from os.path import join, exists, isdir, dirname
from os import listdir
import tarfile


class CaliFinder(object):

    def __init__(self, cfg=None, sta=None):

        # input variables
        self.cfg = cfg if sta is not None else PlenopticamConfig()
        self.sta = sta if sta is not None else PlenopticamStatus()

        # internal variables
        self._lfp_json = {}
        self._georef = None
        self._serial = None
        self._cal_fn = None
        self._raw_data = None
        self._file_found = None
        self._opt_prnt = False if sta is not None else self.cfg.params[self.cfg.opt_prnt]
        self._path = self.cfg.params[self.cfg.cal_path]

        # output variables
        self._wht_bay = None

    def main(self):

        # auto calibration can only be used if calibration source path is either directory or tar archive
        if isdir(self._path) or self._path.lower().endswith('.tar'):

            # read JSON file from selected *.lfp image
            self._lfp_json = self.cfg.load_json(self.cfg.params[self.cfg.lfp_path])

            # extract calibration reference data
            frames = safe_get(self._lfp_json, 'frames')
            self._georef = safe_get(frames[0], 'frame', 'geometryCorrectionRef') if frames else ''

            # extract serial number to support search
            self._serial = safe_get(self._lfp_json, 'camera', 'serialNumber')

            # print status
            if not self._serial and isdir(self._path):
                self.sta.status_msg('No serial number found in JSON file. Provide calibration file instead of folder',
                                    self._opt_prnt)
                self.sta.interrupt = True

            # when path is directory
            if isdir(self._path):

                # look for geo data in calibration folders
                self._search_cal_dirs()

                # look for geo data in calibration tar-files (skip if already found in folders with file_found==True)
                self._search_cal_file()

            elif self._path.lower().endswith('.tar'):

                # look for geo data in provided calibration tar-file
                self._search_tar_file(self._path)

            if not self._file_found:
                # print status and interrupt process
                self.sta.status_msg('White image file not found. Revise calibration path settings', self._opt_prnt)
                self.sta.error = True

            # load and keep white image if found and options are set or meta data is missing
            cond = self.cfg.params[self.cfg.opt_cali] or \
                   self.cfg.params[self.cfg.opt_vign] or \
                   not self.cfg.cond_meta_file()
            if self._file_found and cond:
                # convert raw data to image array and get metadata
                self._raw2img()

        return True

    def _raw2img(self):
        ''' decode raw data to obtain bayer image and settings data '''

        # skip if calibrated json file already exists, otherwise perform centroid calibration
        if self._raw_data:

            from plenopticam.lfp_reader.lfp_decoder import LfpDecoder

            # decode raw data
            obj = LfpDecoder(self._raw_data, self.cfg, self.sta)
            obj.decode_raw()
            self._wht_bay = obj.bay_img
            del obj

            # balance Bayer channels in white image
            try:
                wht_json = json.loads(self._wht_json.read())
                frame_arr = safe_get(wht_json, 'master', 'picture', 'frameArray')[0]
                self.cfg.lfpimg['ccm_wht'] = safe_get(frame_arr, 'frame', 'metadata', 'image', 'color', 'ccmRgbToSrgbArray')
                awb = safe_get(frame_arr, 'frame', 'metadata', 'devices', 'sensor', 'normalizedResponses')[0]
                gains = [1./awb['b'], 1./awb['r'], 1./awb['gr'], 1./awb['gb']]
                self.cfg.lfpimg['awb_wht'] = gains
            except ValueError:
                gains = [1/0.74476742744445801, 1/0.76306647062301636, 1, 1]

            # apply white balance gains to calibration file
            cfa_obj = CfaProcessor(bay_img=self._wht_bay, cfg=self.cfg, sta=self.sta)
            cfa_obj.set_gains(gains)
            self._wht_bay = cfa_obj.apply_awb()
            del cfa_obj

        return True

    def _match_georef(self, json_dict):
        ''' compare georef hash value with that in provided json dictionary '''

        # search for georef hash value in geometry files of calibration folder
        for item in json_dict['calibrationFiles']:
            if item['hash'] == self._georef:  # stop when hash values match
                self._cal_fn = item['name'].replace('.GCT', '.RAW')     # save calibration file
                break

        return True

    def _search_cal_dirs(self):
        ''' look for geo data in calibration folders '''

        # skip if file already found or if provided path is not a directory
        if not self._file_found:
            onlydirs = [d for d in listdir(self._path)]
            dirnames = [self._serial] if onlydirs.count(self._serial) else onlydirs

            # iterate through directories
            for dirname in dirnames:
                cali_manifest = join(join(self._path, dirname), 'cal_file_manifest.json')
                if exists(cali_manifest):
                    with open(cali_manifest, 'r') as f:
                        json_dict = json.load(f)
                        self._match_georef(json_dict)
                        if self._cal_fn is not None:
                            self._file_found = True

                            # update config
                            self.cfg.params[self.cfg.cal_meta] = join(join(self._path.split('.')[0], self._serial), self._cal_fn)

                            # load raw data
                            self._raw_data = open(self.cfg.params[self.cfg.cal_meta], mode='rb')

                            break

        return True

    def _search_cal_file(self):
        ''' look for geo data in calibration tar-files '''

        # skip if file already found
        if not self._file_found:
            onlyfiles = [f for f in listdir(self._path) if f.lower().endswith('.tar')]
            tarstring = 'caldata-'+str(self._serial)+'.tar'
            tarnames = [tarstring] if onlyfiles.count(tarstring) else onlyfiles

            # iterate through tar-files
            for tarname in tarnames:
                self._search_tar_file(tarname)
                break

        return True

    def _search_tar_file(self, tarname):

        # read mla_calibration JSON file from tar archive
        try:
            tar_obj = tarfile.open(join(self._path, tarname), mode='r')
            cal_manifest = tar_obj.extractfile('unitdata/cal_file_manifest.json')
            json_dict = json.loads(cal_manifest.read().decode('utf-8'))
            self._match_georef(json_dict)
            if self._cal_fn:
                self._file_found = True

                # update config
                self._serial = tarname.split('-')[-1].split('.')[0]
                tar_path = dirname(self._path) if self._path.lower().endswith('tar') else self._path
                self.cfg.params[self.cfg.cal_meta] = join(tar_path, self._serial,
                                                          self._cal_fn.lower().replace('.raw', '.json'))

                # load raw data
                self._raw_data = tar_obj.extractfile('unitdata/' + self._cal_fn)
                self._wht_json = tar_obj.extractfile('unitdata/' + self._cal_fn.upper().replace('.RAW', '.TXT'))

        except FileNotFoundError:
            self.sta.status_msg('Did not find calibration file.', opt=True)
        except KeyError:
            self.sta.status_msg('Did not find "cal_file_manifest.json" in tar archive', opt=True)
        except Exception:
            pass

    @property
    def raw_data(self):

        return self._raw_data

    @property
    def wht_bay(self):

        return self._wht_bay
