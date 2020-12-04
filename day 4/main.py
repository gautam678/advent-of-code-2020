import re
def main():
    f = open("input.txt", "r")
    count=0
    input = f.read()
    for i in input.split("\n\n"):
        batch_agent=" ".join([line for line in i.split("\n")])
        flag = process_batch_with_validation(batch_agent)
        if flag:
            count+=1            
    return count


def process_batch(entry):
    fields = sorted(["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"])
    passport=dict(x.split(":") for x in entry.split(" "))
    length_fields = len(passport.keys())
    fields_to_validate = sorted(list(passport.keys()))
    if fields_to_validate == fields:
        return True
    elif "cid" not in fields_to_validate and length_fields ==7:
        return True
    else:
        return False


def process_batch_with_validation(entry):
    fields = sorted(["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"])
    passport=dict(x.split(":") for x in entry.split(" "))
    length_fields = len(passport.keys())
    fields_to_validate = sorted(list(passport.keys()))
    count_val = 0
    for i in fields_to_validate:
        count_val+= int(validate(i,passport[i]))
    if "cid" not in fields_to_validate:
        count_val+=1
    if count_val ==8:
        return True
    else:
        return False

def validate(key,value):
    switcher = { 
        "byr": func_1(value), 
        "iyr": func_2(value), 
        "eyr": func_3(value), 
        "hgt": func_4(value), 
        "hcl": func_5(value), 
        "ecl": func_6(value), 
        "pid": func_7(value),
        "cid": func_8(value), 
    }
    return switcher[key]


def func_1(value):
    if value.isdigit():
        input = int(value)
    else:
        return False
    return input>=1920 and input <= 2002

def func_2(value):
    if value.isdigit():
        input = int(value)
    else:
        return False
    return input>=2010 and input <= 2020

def func_3(value):
    if value.isdigit():
        input = int(value)
    else:
        return False
    return input>=2020 and input <= 2030

def func_4(val):
    if ("cm" in val or "in" in val) and val[0:1].isdigit():
        if "cm" in val:
            input = int(val.split("c")[0])
            return input>=150 and input<=193
        else:
            input = int(val.split("i")[0])
            return input>=59 and input<=76
    else:
        return False


def func_5(value):
    if "#" in value:
        input = value.split("#")[1]
        reg=re.compile('^[a-f0-9]{6}$')
    else:
        return False
    return bool(reg.match(input))

def func_6(value):
    enums = ["amb" ,"blu" ,"brn" ,"gry" ,"grn","hzl" ,"oth"]
    return value in enums

def func_7(value):
    return len(value) == 9

def func_8(value):
    return True


print(main())