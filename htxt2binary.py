import sys


def proc():
    args = sys.argv
    # ファイル名取得
    file_name = args[1]
    output_file = file_name.split(".")[0] + ".bin"

    with open(file_name, mode="r", encoding="utf-8") as input_f:
        input_string = input_f.read().replace("\n", "")

    with open(output_file, mode="wb") as output_f:
        print(bytes.fromhex(input_string))
        output_f.write(bytes.fromhex(input_string))


proc()
