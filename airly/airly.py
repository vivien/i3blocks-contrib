#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2019 Kudlaty 01 <kudlok@mail.ru>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import getopt, requests, urllib, yaml, sys, os

gconfig = {
    'apikey': 'example_api_key',
    'installationId': 2955,
    # uncomment if lat/long is preferred instead of sensorId
    # 'lat': '',
    # 'lng': ''
}

class AirlyApiClient:
    def __init__(self, config=None):
        """init with optionally config"""
        self.config = config or self.parseConfig(self.parseInstance())
        self.apiUrl = 'https://airapi.airly.eu/v2/measurements/%s?' % ('installation' if 'installationId' in self.config else 'point')

    def parseInstance(self):
        """ parse the instance environment variable """
        instance = ''
        try:
            instance = os.environ['BLOCK_INSTANCE']
        except KeyError:
            return None
        finally:
            if len(instance):
                return instance
        return None

    def parseConfig(self, instance):
        """parse the instance-specific config file or a default one"""
        _instance = instance or self.parseInstance()
        xdgHome = os.environ['XDG_CONFIG_HOME'] or os.environ['HOME'] + '/.config'
        configPath = xdgHome + '/i3blocks-airly/%s.yml' % (_instance or 'config')
        try:
            with open(configPath, 'r') as stream:
                config=yaml.load(stream)
                return config
        except:
            global gconfig
            return gconfig

    def getMeasurement(self, config=None):
        """get the measurements for the place"""
        cfg = config or self.config
        r = requests.get(self.apiUrl + urllib.parse.urlencode(self.config))
        self.lastResult = r.json()
        return self.lastResult

    def getCurrentMeasurement(self, measurement=None):
        """get only the current measurement"""
        m = measurement or self.getMeasurement()
        return m['current']['indexes']

    def getCaqiMeasurement(self, measurement=None):
        """get only the current CAQUI measurement"""
        m = measurement or self.getCurrentMeasurement()
        caqi=next(c for c in m if c['name'] == 'AIRLY_CAQI')
        return caqi

    def getAirQualityIndex(self, caqiMeasurement=None):
        """get the air quality index value from given CAQI measurement
        it's current measuement by default"""
        m = caqiMeasurement or self.getCaqiMeasurement()
        index = m['value']
        return index

    def getColor(self, measurement=None):
        """get color for given air quality indes"""
        m = measurement or self.getCaqiMeasurement()
        return m['color']

    def displayResult(self,jsonData=None):
        """display the measurement result"""
        result = self.getAirQualityIndex()
        print(round(result,2))
        print(round(result))
        print(self.getColor())

def main(argv):
    args=argv
    client = AirlyApiClient()
    client.displayResult()

if __name__ == "__main__":
   main(sys.argv[1:])
