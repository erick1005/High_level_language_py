
def ninjaAndRangeMax(n: int, x: int, y: int, a: List[int]) -> int:
    # Define the start and end positions of the subarray.
    startpos = x
    endpos = y + 1

    # Return the maximum element in the subarray of 'a' from index 'startpos' to 'endpos'.
    return max(a[startpos:endpos])

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x, y = list(map(int, input().split()))
        a = list(map(int, input().split()))
        print(ninjaAndRangeMax(n, x, y, a))