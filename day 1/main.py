
def main():
    # f = open("input.txt", "r")
    f = open("input.txt", "r")
    input=[]
    for x in f:
        input.append(int(x))
    second=0
    for i in range(len(input)):
        for j in range(i,len(input)):
            if 2020-(input[i]+input[j]) in input:
                third = input.index(2020-(input[i]+input[j]))
                first = i
                second = j

    print(first,second)
    return input[second]*input[first]*input[third]



print(main())