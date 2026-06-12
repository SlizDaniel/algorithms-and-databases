import time

def naive_search (S: str, W: str):
    t_start = time.perf_counter()
    m=0
    i=0
    try_ = 0
    match_found = 0
    operations = 0
    while(m<len(S)):
        current_letter = S[m]
        current_match = W[i]
        operations+=1
        if current_letter == current_match:
            m+=1
            i+=1
            if i==len(W):
                match_found+=1
                i=0
                try_+=1
                m = try_
        elif(len(S)-try_<len(W)):
            t_stop = time.perf_counter()
            return(f"{match_found};{operations};{t_stop-t_start}")
        else:
            try_+=1
            i=0
            m=try_

def hash(word, N, d, q):
    hw = 0
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw

def rolling_hash_karp(S:str, W:str):
    t_start = time.perf_counter()
    operations = 0
    matches_found = 0
    colisions = 0
    N=len(W)
    M=len(S)
    d=256
    q=101    
    h = 1
    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q
    hW = hash(W[0:N], N, d, q)
    hS = hash(S[0:N], N, d, q)
    for m in range(0, M-N+1):
        if hS<0:
            hS+=q
        operations+=1
        if hS == hW:
            if S[m:m+N]==W[0:N]:
                matches_found+=1
            else:
                colisions+=1
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
        if hS < 0:
            hS+=q
    t_stop = time.perf_counter()
    return f"{matches_found};{operations};{colisions};{t_stop-t_start}"
# hash(S[m+1..m+N]) = (d * (hash(S[m..m+N-1]) - ord(S[m]) * h) + ord(S[m + N])) % q
def rabin_karp(S:str, W:str):
    t_start = time.perf_counter()
    operations = 0
    matches_found = 0
    colisions = 0
    N=len(W)
    M=len(S)
    d=256
    q=101
    hW = hash(W[0:N], N, d, q)
    for m in range(0, M-N+1):
        hS = hash(S[m:m+N], N, d, q)
        operations+=1
        if hS == hW:
            if S[m:m+N]==W[0:N]:
                matches_found+=1
            else:
                colisions+=1
    t_stop = time.perf_counter()
    return f"{matches_found};{operations};{colisions};{t_stop-t_start}"

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()
    W = 'time.'
    print(naive_search(S, W))
    print(rabin_karp(S, W))
    print(rolling_hash_karp(S, W))

if __name__ == "__main__":
    main()
          
          

        