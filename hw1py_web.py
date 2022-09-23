from abc import ABCMeta, abstractmethod
from pathlib import Path
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):

    @abstractmethod
    def serialization(self, file, data):
        pass

    @abstractmethod
    def deserialization(self, file):
        pass


class SerializationJson(SerializationInterface):

    def serialization(self, file, data):

        with open(file, 'w') as fh:
            json.dump(data, fh)
        print(f"Serializing the {file} file in JSON was successful.")

    def deserialization(self, file):

        with open(file, "r") as fh:
            unpacked = json.load(fh)
            return unpacked


class SerializationBin(SerializationInterface):

    def serialization(self, file, data):

        with open(file, 'wb') as fh:
            pickle.dump(data, fh)
        print(f"Serializing the {file} file in BIN was successful.")
   
    def deserialization(self, file):

        with open(file, "rb") as fh:
            unpacked = pickle.load(fh)
            return unpacked



# ex1 = SerializationJson()
# file = "/Users/suprunetsvladymyr/Documents/GitHub/hw1web/555.json"
# data = ["111", "bchdnj"]

# ex1.serialization(file, data)
# print(ex1.deserialization(file))

# ex2 = SerializationBin()
# file = "/Users/suprunetsvladymyr/Documents/GitHub/hw1web/222.bin"
# data = {"222": "54g32", "67": "rtydn"}

# ex2.serialization(file, data)
# print(ex2.deserialization(file))