import csv
from bloom_filter import BloomFilter

# number of spam email addresses
n = 10000

# number of bits in the bitarray
m = 1000000

bloomfilter = BloomFilter(n, m)

# adding items to bloomfilter
with open("spam_emails.csv") as spam:
    csvreader = csv.reader(spam)
    for row in csvreader:
        bloomfilter.add(row[0])

count = 0
false_positive = 0
false_negative = 0

# checking whether email addresses were present in the spam email list
with open("emails.csv") as email:
    csvreader = csv.reader(email)
    for row in csvreader:
        found = bloomfilter.check(row[0])
        if found and row[1] != 'SPAM':
            # counting false positives
            false_positive += 1
        elif not found and row[1] == 'SPAM':
            # counting false negatives
            false_negative += 1
        # counting total emails
        count += 1

print(f"total email address : {count}")
print(f"false positives : {false_positive}")
print(f"false negatives : {false_negative}")
