import argparse
import json


def parse_clopt():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input_file",
        help="Input file",
        type=str,
        nargs='*',
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Name of output file",
        type=str,
        required=True,
    )

    args = parser.parse_args()
    return args


def merge(file_paths: list):
    assert(len(file_paths) > 0)

    # parse as json
    json_data_list = []
    for file_path in file_paths:
        with open(file_path, mode='r') as f:
            json_data_list.append(json.load(f))

    # check version consistency
    if len(set(map(lambda d: str(d['__version__']), json_data_list))) != 1:
        print('There are logs taken by different versions of lit.')
        exit(1)

    # FIXME :
    #   This process make 'name' dirty when applying this script many times.
    # llvm's compare.py does not accept same named result.
    # To avoid the error, add suffix to 'name'.
    for i, json_data in enumerate(json_data_list):
        for test in json_data['tests']:
            test['name'] += f' ({i})'

    # make merged json
    merged = json_data_list[0]
    json_data_list = json_data_list[1:]
    for json_data in json_data_list:
        merged['elapsed'] += json_data['elapsed']
        merged['tests'].extend(json_data['tests'])

    return json.dumps(merged, indent=2)


if __name__ == '__main__':
    args = parse_clopt()
    merged = merge(args.input_file)
    with open(args.output, mode='w') as f:
        f.write(merged)
