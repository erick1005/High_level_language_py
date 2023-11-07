# Define the function longest_mountain that takes an array as input
def longest_mountain(arr):
    # Get the length of the array
    n = len(arr)
    # Initialize the length of the longest mountain to 0
    mountainlen = 0

    # Loop through the array from the second element to the second last element
    for i in range(1, n - 1):
        # Check if the current element is a peak (greater than its neighbors)
        if arr[i-1] < arr[i] > arr[i+1]:
            # Initialize the left boundary of the mountain at the peak
            left = i - 1
            # Expand the left boundary until a number larger than or equal to the next number is found
            while left > 0 and arr[left-1] < arr[left]:
                left -= 1

            # Initialize the right boundary of the mountain at the peak
            right = i + 1
            # Expand the right boundary until a number larger than or equal to the previous number is found
            while right < n - 1 and arr[right] > arr[right+1]:
                right += 1

            # If the length of the current mountain is greater than the length of the longest mountain found so far, update the longest mountain length
            if (right - left + 1) > mountainlen:
                mountainlen = right - left + 1

    # Return the length of the longest mountain
    return mountainlen
