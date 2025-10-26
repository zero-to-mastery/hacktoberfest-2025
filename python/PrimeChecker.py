# Problem Statement: Check if a given number is prime.
# Time Complexity: O(sqrt(N))
# Space Complexity: O(1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(29))  # Output: True
