from itertools import count


nums = [1,1,1,2,2,3,2,3,2,3,3,3,1]

maxnum =[]
def max_count(nums):
    counts={}
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = i
    return counts

counts  = max_count(nums)
print(counts)
first = []
max_num = max(counts.values())
print(max_num)

for name,count in counts.items():
    print(name,":",count,"번")
    if count == max_num:
        first.append(name)
print('1등 :',first)

def sum(num):
    hap = 0
    for i in range(num+1):
        hap += i
    return(hap)

print(sum(10))
