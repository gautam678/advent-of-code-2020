from collections import defaultdict

def main():
    f = open("input.txt", "r").read()
    input = f.split("\n\n")
    sum_form = 0
    for i in input:
        ans = calc_form_everyone(i)
        sum_form+=ans
    return sum_form
        

def calc_form(input):
    calc_dup = []
    for i in input.split("\n"):
        for j in list(i):
            if j not in calc_dup:
                calc_dup.append(j)
    return len(calc_dup)

def calc_form_everyone(input):
    calc_dup = []
    entry = input.split("\n")
    print(entry)
    count=0
    hashMap=defaultdict(int)
    for i in entry:
        for j in list(i):
            hashMap[j]+=1
    print(hashMap)
    for key,val in hashMap.items():
        if val == len(entry):
            count+=1
    return count


print(main())