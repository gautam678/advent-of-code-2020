import re
from collections import defaultdict
#light red bags contain 1 bright white bag, 2 muted yellow bags.
#faded blue bags contain no other bags.
def main():
    f = open("input.txt", "r").read()
    bag_rules={}
    for line in f.split("\n"):
        outer,inner = line.split(" bags contain")
        bag_rules[outer] = re.findall(r'([0-9+]) ([a-z ]+) bag[s]?',inner.strip())
    ans = sum_shiny_bag(bag_rules,'shiny gold')
    return ans

def num_shiny_bag(input,start):
    reverse_bag = defaultdict(list)
    for i,j in input.items():
        for count, bag in j:
            reverse_bag[bag].append(i)
    visited =set()
    queue = [start]
    while queue:
        bag = queue.pop()
        for bag_i in reverse_bag[bag]:
            if bag_i not in visited:
                visited.add(bag_i)
                queue.append(bag_i)
    return len(visited)


def sum_shiny_bag(input,start):
    reverse_bag = defaultdict(list)
    sum_bags=0
    return recursive_count(input,'shiny gold')


def recursive_count(input,index):
    val =[]
    return sum((int(c) + (int(c) * recursive_count(input,bag)) for c,bag in input[index]))



print(main())