
def letter_count (str):
    character_dic = {}
    text_list = list(str)
    for c in text_list:
        T = str.count(c)
        character_dic[c] = T

    print (character_dic)
