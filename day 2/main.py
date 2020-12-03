# 1-14 b: bbbbbbbbbbbbbbbbbbb
from collections import defaultdict
def main():
    f = open("input.txt", "r")
    count=0
    for x in f:
        raw_text = x.split(" ")
        min_val,max_val= raw_text[0].split("-")
        key = raw_text[1][0]
        flag = calc_index(raw_text[2].strip('\n'),key,int(min_val)-1,int(max_val)-1) 
        # flag = calc_occurance(raw_text[2].strip('\n'),key,min_val,max_val,count)
        if flag:
            count+=1
    return count


def calc_index(word,key,index_1,index_2):
    flag_1,flag_2 =  word[index_1]==key,word[index_2]==key
    return bool(flag_1) != bool(flag_2)




def calc_occurance(word,key,min_val,max_val,count):
    map_letter = defaultdict(int)
    for i in word:
        map_letter[i]+=1
    if key in map_letter.keys() and map_letter[key] >= int(min_val) and map_letter[key] <= int(max_val):
        return True
    else:
        return False



print(main())