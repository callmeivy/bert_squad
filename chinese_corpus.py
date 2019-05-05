# coding=utf-8
import json
input_file = "F:\work\QA\dureader_preprocessed\preprocessed\\trainset\\search.train.json"
with open(input_file, 'r', encoding='utf-8') as load_f:
    try:
        while True:
            text_line = load_f.readline()
            if text_line:
                print(type(text_line), text_line)
                exit(0)
            else:
                break
    finally:
        load_f.close()




    # dic = json.load(load_f)
    # i=0
    # for k, v in dic.items():
    #     print(k, v)
    #     i += 1
    #     if i > 5:
    #         break






    # load_dict = json.load(load_f)
    # for k, v in load_dict.items():
    #     print(k, v)
    #     print(type(v))
    #     for k1, v1 in v.items():
    #         if k1 == "zh":
    #             print(k1, v1)
    # print(type(load_f.read()))
    # print(load_f.read())