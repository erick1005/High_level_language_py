#CHECKING AND PILING BLOCKS

res = []
T = int(input())
for _ in range(T):
    n = int(input())
    block = list(map(int, input().split()))
    for _ in range(n-1):
        if block[0] >= block[-1]:
            a = block[0]
            block.pop(0)
        elif block[0] < block[-1]:
            a = block[-1]
            block.pop(len(block)-1)
        else:
            pass
        if len(block) == 1:
            res.append("Yes")
        if((block[0] > a) or (block[-1] > a)):
            res.append("No")
            break
print("\n".join(res))