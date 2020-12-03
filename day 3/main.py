def main():
    f = open("input.txt", "r")
    fields = f.readlines()

    for i in range(len(fields)):
        fields[i] = fields[i].strip("\n")
        fields[i] = fields[i]*(len(fields))
    return trees_hit(fields,1,3)
    # return trees_hit(fields,1,3)*trees_hit(fields,1,1)*trees_hit(fields,1,5)*trees_hit(fields,1,7)*trees_hit(fields,2,1)


def trees_hit(fields,step_ver,step_hor):
    count=0
    length_fields = len(fields)
    j=k=0
    if step_ver ==2:
        length_fields-=1
    while j<length_fields-1:
        j=j+step_ver
        k=k+step_hor
        if fields[j][k] == "#":
            count+=1
    return count
    

print(main())