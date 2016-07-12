import json
import os

class JsonSerializer:
    def serializeToFile(self, toSerialize, filePath):
        with open(filePath) as f:
            json.dump(toSerialize, f)

    def deserializeFromFile(self, filePath):
        configJson = None
        
        with open(filePath) as f:
            configJson = json.load(f)

        return configJson