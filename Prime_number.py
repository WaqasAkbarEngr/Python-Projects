limit = input("Enter number upto which you want to get list of prime numbers? ")
limit = int(limit)
limit_half = limit // 2
composites = []
primes = []

for i in range (2, limit+1):
    if i%2==0:
        composites.append(i)
    else:
        i_half = i//2
        for x in range (2, i_half):
            if i % x == 0:
                composites.append(i)
                break
        else:
            primes.append(i)
print("Composites numbers are",composites)
print("Prime numbers are",primes)

count = 0

prime_numbers = open("Prime Numbers.txt","w")
prime_numbers.write("Prime Numbers are (")
for entry in primes:
    if count % 10 == 0 and count !=0 :
        prime_numbers.write("\n\n                   ")
    entry = str(entry)
    if count > 0 and count < (len(primes)+1) and count % 10 != 0 :
        prime_numbers.write(",  ")
    prime_numbers.write(entry)
    count += 1
count = 0
prime_numbers.write(")\n\n\n\nComposite Numbers are (")
for entry in composites:
    if count % 10 == 0 and count !=0 :
        prime_numbers.write("\n\n                        ")
    entry = str(entry)
    if count > 0 and count < (len(composites)+1) and count % 10 != 0 :
        prime_numbers.write(",  ")
    prime_numbers.write(entry)
    count += 1
prime_numbers.write(")")