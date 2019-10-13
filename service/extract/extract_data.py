# encoding=utf-8

from constant import constant
from util.fileUtils import get_contents


def extract_data():
    # 1.将文本读出来，封装对象
    contents = get_contents(constant.txt_path)
    literature_list = []
    content_dict = {}
    literature_id = 0
    for c in range(len(contents)):
        if contents[c] == '\n':
            if 0 == len(content_dict):
                continue
            # 一个对象封装完，重置相关数据
            literature_list.append(content_dict)
            literature_id = literature_id + 1
            content_dict = {}
            continue
        # 按顺序封装对象
        content_dict['literature_id'] = literature_id
        content = contents[c].replace('\n', '')
        get_literature_model(content_dict, content)

    # 2.提取结果
    for i in range(len(literature_list)):
        print(literature_list[i])

    # 3.计算关键词出现次数
    key_word_count = {}
    for i in range(len(literature_list)):
        literature = literature_list[i]
        key_word = literature['Keyword']
        for j in range(len(key_word)):
            try:
                key_word_count[key_word[j]] = key_word_count[key_word[j]] + 1
            except KeyError:
                key_word_count[key_word[j]] = 1
    print(key_word_count)
    # 排序
    # TODO
    return key_word_count


def get_literature_model(content_dict, content):
    if content.startswith('SrcDatabase'):
        content_dict['SrcDatabase'] = get_value('SrcDatabase', content)
    if content.startswith('Title'):
        content_dict['Title'] = get_value('Title', content)
    if content.startswith('Author'):
        content_dict['Author'] = get_value('Author', content)
    if content.startswith('Organ'):
        content_dict['Organ'] = get_value('Organ', content)
    if content.startswith('Source'):
        content_dict['Source'] = get_value('Source', content)
    if content.startswith('Keyword'):
        key_word = get_value('Keyword', content).replace(';;', ' ').replace(';', ' ').strip(' ')
        key_word = key_word.split(' ')
        content_dict['Keyword'] = key_word
    if content.startswith('Summary'):
        content_dict['Summary'] = get_value('Summary', content)
    if content.startswith('PubTime'):
        content_dict['PubTime'] = get_value('PubTime', content)


def get_value(key, origin_value):
    if origin_value.startswith(key):
        value = origin_value[origin_value.find(':') + 1:].strip(' ')
    return value


if __name__ == '__main__':
    extract_data()
