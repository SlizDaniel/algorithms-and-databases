import time
import math

def hash(word, N, d, q):
    hw = 0
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw

def get_primes(k):
    primes = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
    return primes[:k]

def rolling_hash_karp(S:str, W:str| list[str]):
    t_start = time.perf_counter()
    operations = 0
    matches_found = 0
    colisions = 0
    N=len(W[0])
    M=len(S)
    bloom_table, k = bloom_filter(W)
    b = len(bloom_table)   
    primes = get_primes(k)
    q=10007
    h=1
    muls = []
    for d in primes:
        h=1
        for i in range(N-1):  # N - jak wyżej - długość wzorca
            h = (h*d) % q
        muls.append(h)
    hashs = []
    for d in primes:
        hashs.append(hash(S[0:N], N, d, q))
    for m in range(0, M-N+1):
        operations+=1
        ones = True
        for i in range (k):
            idx = hashs[i]%b
            if bloom_table[idx] == 0:
                ones = False
                break
        if ones:
            if S[m:m+N] in W:
                matches_found+=1
            else:
                colisions+=1
        if m < M - N:
            for i in range (k):
                d = primes[i]
                hashs[i] = (d * (hashs[i] - ord(S[m]) * muls[i]) + ord(S[m + N])) % q
    t_stop = time.perf_counter()
    return f"{matches_found};{operations};{colisions};{t_stop-t_start}"

def bloom_filter(W_list: list[str]|str):
    P = 0.001
    n = len(W_list)
    b = -n*math.log(P)/(math.log(2))**2
    b = math.ceil(b)
    k = (b/n)*math.log(2)
    k = round(k)
    N = len(W_list[0])
    bloom_table = [0 for _ in range (b)]
    primes = get_primes(k)
    q=10007
    for string in W_list:
        for prime in primes:
            idx = hash(string,N,prime,q) % b
            bloom_table[idx] = 1
    return bloom_table, k

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()
    W_list = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 
     'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 
     'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']
    W=['welcome']
    # print(bloom_filter(W))
    print(rolling_hash_karp(S, W))
    print(rolling_hash_karp(S, W_list))



if __name__ == "__main__":
    main()