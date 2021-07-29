import sys
import time
from fftf.configs_adopter import ConfigsAdopter as gConf
from fftf.util import readRawFile, readKeyMapFile, writeToOutputFile


def main():
    # Read raw file
    readRawFile()
    readKeyMapFile()
    final_data_as_text = ""
    keymap = gConf.get('key_map_dict')

    writeToOutputFile('"|"'.join(keymap.keys()) + "\n")
    for row in gConf.get('raw_file_content'):
        final_data = {}
        for col, ranges in keymap.items():
            final_data[col] = row[ranges["start"]:ranges['end']]
        final_data_as_text = '"|"'.join(final_data.values())
        writeToOutputFile(final_data_as_text + "\n")


def collect_inputs(args):
    # Collecting the required inputs
    for i in range(0, len(args), 2):
        if args[i] in ("-ff", "--flat-file"):
            gConf.set("raw_file", args[i + 1])

        if args[i] in ("-km", "--key-map"):
            gConf.set("key_map", args[i + 1])

        if args[i] in ("-o", "--output"):
            gConf.set("output_file", args[i + 1])

    # print(gConf.get_all())
    has_error = False
    if gConf.get("raw_file") is None:
        print('Raw file input (-ff / --flat-file) is required.')
        has_error = True

    if gConf.get("key_map") is None:
        print('Key map input (-km / --key-map) is required.')
        has_error = True

    if gConf.get("output_file") is None:
        print('Output file path (-o / --output) is required.')
        has_error = True

    if has_error is True:
        raise Exception("Required inputs are missing.")


if __name__ == '__main__':
    start_time = time.perf_counter()
    try:
        collect_inputs(sys.argv[1:])
        main()
    except Exception as e:
        print("Exception found:", e)
    finally:
        elapsed = time.perf_counter() - start_time
        print(f"FlatFile transformation completed in {elapsed:0.2f}.")
