# Write a recursive program to determine if a string s of numbers has more even digits than odd digits
# Function to count digits
def countEvenOdd(n):
    even_count = 0
    odd_count = 0
    while (n > 0):
        rem = n % 10
        if (rem % 2 == 0):
            even_count += 1
        else:
            odd_count += 1

        n = int(n / 10)

    print("Even count : ", even_count)
    print("\nOdd count : ", odd_count)
    if (even_count % 2 == 0 and
            odd_count % 2 != 0):
        return 1
    else:
        return 0


# Driver code
n = 9876502
t = countEvenOdd(n);

if (t == 1):
    print("There are more even digits than odd digits")
