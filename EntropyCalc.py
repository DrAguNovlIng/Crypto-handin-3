from math import gcd, log2

z_star = [i for i in range(26) if gcd(i, 26) == 1]

print("z* =", z_star)
print("length of z* is ", len(z_star))

def affine_encrypt(a, b, p):
    return (a * p + b) % 26

def calculate_entropy(p):
    return p * log2(1/p)

unique_keys = []
total_keys: int = 0

for plaintext_letter in range(26):
    for i in z_star:
        for j in range(26):
            if affine_encrypt(i, j, plaintext_letter) == 8:
                total_keys = total_keys + 1
                if (i, j) not in unique_keys:
                    unique_keys.append((i, j))

print("total amount of keys", total_keys)
print("amount of unique keys", len(unique_keys))
print("H(K|C) = ", 12*calculate_entropy(1/12))
print("H(K|P,C) = ",total_keys * calculate_entropy(1/total_keys))