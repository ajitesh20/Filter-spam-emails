# Filter Spam Emails

### Used Bloom Filter data structure to check whether an email address is marked as spam or not.

#### **Bloom Fliter** -

> A bloom filter is a space efficient data structure that is used to test whether an element is a member of a set.
> It is a probabilistic data structure in which false-positive matches are possible but false-negative matches are not possible.
> This technique finds its application where the amount of source data would require an impractically large amount of memory if "conventional" error-free hashing techniques were applied.

#### **total email addresses** - 1000000
#### **false positives** - 7783
#### **false negatives** - 0

#### all the email address data is taken from [here](https://www.kaggle.com/rowhitswami/all-indian-companies-registration-data-1900-2019)