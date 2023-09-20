from math import gcd, log2

z_star = [i for i in range(26) if gcd(i, 26) == 1]

print("z* =", z_star)
print("length of z* is ", len(z_star))

def affine_encrypt(a, b, p):
    return (a * p + b) % 26

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