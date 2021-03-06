import collections
import json

from libcobblersignatures.models.osversion import Osversion


class OsBreed:

    def __init__(self, name):
        self._name = name
        self._osversions = collections.OrderedDict()

    def __eq__(self, other):
        if not isinstance(other, OsBreed):
            return NotImplemented
        return self.name == other.name and self.osversions == other.osversions

    @property
    def osversions(self):
        return self._osversions

    @osversions.setter
    def osversions(self, value):
        self._osversions = value

    @osversions.deleter
    def osversions(self):
        self._osversions = collections.OrderedDict()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise TypeError("Name cannot be an empty string.")
        else:
            self._name = value

    @name.deleter
    def name(self):
        raise TypeError("The name of this error cannot be deleted.")

    def encode(self):
        versionsdict = {}
        return {self.name: versionsdict}

    def decode(self, data):
        for k, v in data:
            version = Osversion()
            version.decode(v)
            self.osversion_add(k, version)

    def osversion_add(self, name, version):
        if isinstance(name, str) and isinstance(version, Osversion):
            self.osversions[name] = version
        else:
            raise ValueError("Name must be str and Version must be Osversion.")

    def osversion_remove(self, key):
        self.osversions.pop(key)
