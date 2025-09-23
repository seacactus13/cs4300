def check_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def first_n_primes(count=10):
    primes = []
    num = 2
    while len(primes) < count:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def sum_1_to_100():
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total

def main():
    print("Check number example:", check_number(5))
    print("First 10 primes:", first_n_primes())
    print("Sum 1 to 100:", sum_1_to_100())

if __name__ == "__main__":
    main()
