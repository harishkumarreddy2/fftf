from fftf.configs_adopter import ConfigsAdopter as gConf


def readRawFile(file: str = None):
    if file is None:
        file = gConf.get("raw_file")

    content = []
    with open(file, 'r') as f:
        content = f.readlines()
        f.close()
    gConf.set("raw_file_content", content)


def readKeyMapFile(file: str = None):
    if file is None:
        file = gConf.get("key_map")

    with open(file, 'r') as f:
        key_maps = f.readlines()
        f.close()

    final_map = {}
    for key_map in key_maps:
        key, value = key_map.split("=")
        value = value.split("-")
        value = {"start": int(value[0]), "end": int(value[1].strip())}
        print(key, value)
        final_map[key.strip()] = value
    gConf.set("key_map_dict", final_map)


def writeToOutputFile(row: str, file: str = None):
    if file is None:
        file = gConf.get("output_file")

    with open(file, 'a') as f:
        f.writelines([row])
        f.close()
