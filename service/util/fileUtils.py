# encoding=utf-8
from constant.constant import txt_path


def get_contents(p):
    with open(p) as file_object:
        content = file_object.readlines()
    return content


if __name__ == '__main__':
    path = txt_path
    contents = get_contents(path)
    print(contents)
    print("**************************************************")
    for c in range(len(contents)):
        if contents[c] == "\n":
            print()
        else:
            print(contents[c].replace("\n", ""))
