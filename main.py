import copy
import time
import random
import sys
sys.setrecursionlimit(3000)

def bubbleSort(v):
    ok = 1
    poz = 0
    while ok == 1:
        ok = 0
        for i in range(1, len(v) - poz):
            if v[i - 1] > v[i]:
                v[i], v[i - 1] = v[i - 1], v[i]
                ok = 1
        poz += 1
    return v

#---------------------------------------

def mergeSort(v):
    if len(v) < 2:
        return v
    r = []
    mid = len(v) // 2
    arr1 = mergeSort(v[:mid])
    arr2 = mergeSort(v[mid:])
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            r.append(arr2[j])
            j += 1
        else:
            r.append(arr1[i])
            i += 1
    r += arr1[i:]
    r += arr2[j:]
    return r

#---------------------------------------

def pozitie(v, st, dr, tip):
    if tip == 1:
        rand = random.randint(st, dr)
        v[rand], v[dr] = v[dr], v[rand]
        pivot = v[dr]
    else:
        mid = (st + dr) // 2
        if v[st] > v[mid] ^ v[st] > v[dr]:
            pivot = v[st]
            k = st
        elif v[mid] < v[st] ^ v[mid] < v[dr]:
            pivot = v[mid]
            k = mid
        else:
            pivot = v[dr]
            k = dr
        v[k], v[dr] = v[dr], v[k]
    i = st - 1
    j = dr
    while i < j:
        i += 1
        while i <= dr and v[i] < pivot:
            i += 1  # elementele mai mici decat pivotul
        j -= 1
        while j >= st and v[j] > pivot:
            j -= 1  # elementele mai mari decat pivotul
        if i < j:
            v[i], v[j] = v[j], v[i]
    v[i], v[dr] = v[dr], v[i]

    return i

def quickSort(v, st, dr, tip):
    if st < dr:
        piv = pozitie(v, st, dr, tip)
        quickSort(v, st, piv - 1, tip)
        quickSort(v, piv + 1, dr, tip)
    return v


def quicksort(vect, st, dr, tip_pivot):
    if st <= dr:
        if st == dr:
            return vect
        elif dr == st + 1:
            if vect[st] > vect[dr]:
                vect[st], vect[dr] = vect[dr], vect[st]
            return vect
        else:
            if tip_pivot == 1:      # alegem pivot random
                k = random.randint(st, dr)
                piv = vect[k]
            else:                   # alegem pivot cu mediana din 3
                k = (st + dr) // 2
                if vect[st] <= vect[k] <= vect[dr] or vect[dr] <= vect[k] <= vect[st]:
                    piv = vect[k]
                elif vect[k] <= vect[st] <= vect[dr] or vect[dr] <= vect[st] <= vect[k]:
                    piv = vect[st]
                    k = st
                else:
                    piv = vect[dr]
                    k = dr
            i = st - 1
            j = dr
            vect[k], vect[dr] = vect[dr], vect[k]       # pivotul este mutat pe ultima pozitie
            while i < j:
                i += 1
                while i <= dr and vect[i] < piv:
                    i += 1      # elementele mai mici decat pivotul, care se afla deja in stanga, sunt bine pozitionate
                j -= 1
                while j >= st and vect[j] > piv:
                    j -= 1      # elementele mai mari decat pivotul, care se afla in dreapta, sunt bine pozitionate
                if i < j:
                    vect[i], vect[j] = vect[j], vect[i]     # interschimbam elementele care nu sunt bine pozitionate
            vect[i], vect[dr] = vect[dr], vect[i]           # aducem pivotul pe pozitia buna
            quicksort(vect, st, i - 1, tip_pivot)
            quicksort(vect, i + 1, dr, tip_pivot)
            return vect

#---------------------------------------

def countSort(v):
    maxim = max(v)
    fr = [0 for i in range(maxim + 1)]
    for i in v:
        fr[i] += 1
    for i in range(maxim):
        fr[i + 1] += fr[i]
    for i in range(maxim, 0, -1):
        fr[i] = fr[i - 1]
    fr[0] = 0
    arr = [0 for i in range(len(v))]
    for i in v:
        arr[fr[i]] = i
        fr[i] += 1
    return arr

#---------------------------------------

def cnt(v, exp, baza):
    output = [0 for i in range(len(v) + 1)]
    numara = [0 for i in range(baza)]
    for i in range(len(v)):
        numara[(v[i] // exp) % baza] += 1
    for i in range(baza):
        numara[i] += numara[i - 1]
    for i in range(len(v) - 1, -1, -1):
        output[numara[(v[i] // exp) % baza] - 1] = v[i]
        numara[(v[i] // exp) % baza] -= 1

def radixSort(v, baza):
    maxim = max(v)
    exp = 1
    while maxim // exp > 0:
        output = [0 for i in range(len(v))]
        numara = [0 for i in range(baza)]
        for i in range(len(v)):
            numara[(v[i] // exp) % baza] += 1
        for i in range(1, baza):
            numara[i] += numara[i - 1]
        for i in range(len(v) - 1, -1, -1):
            output[numara[(v[i] // exp) % baza] - 1] = v[i]
            numara[(v[i] // exp) % baza] -= 1
        v = copy.deepcopy(output)
        exp *= baza
    return v

#---------------------------------------

def testSort(v):
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return 0
    return 1

def generate(n, max):
    v = []
    for i in range(n):
        v.append(random.randint(0, max))
    return v

#---------------------------------------


f = open("sortari.in")
g = open("sortari.out", "w")

nTeste = int(f.readline())

for i in range(nTeste):
    s = f.readline()
    N, MAX = [int(x) for x in s.split()]
    g.write(f'{i + 1}) '"n = " + str(N) + ", max = " + str(MAX) + "\n")
    v1 = generate(N, MAX)
    v2 = copy.deepcopy(v1)

    sortari = ["bubble_sort", "merge_sort", "quick_sort_rand", "quick_sort_3", "count_sort", "radix_sort_10", "radix_sort_256", "python_sort"]
    sort = 0

    while sort < len(sortari):
        start = time.time()

        if sort == 0:
            if N < 10000:
                v2 = bubbleSort(v2)
        elif sort == 1:
            v2 = mergeSort(v2)
        elif sort == 2:
            v2 = quickSort(v2, 0, N - 1, 1)
        elif sort == 3:
            v2 = quickSort(v2, 0, N - 1, 2)
        elif sort == 4:
            if MAX < 10000000:
                v2 = countSort(v2)
        elif sort == 5:
            v2 = radixSort(v2, 10)
        elif sort == 6:
            v2 = radixSort(v2, 256)
        else:
            v2.sort()
        stop = time.time()
        print("gata")
        if testSort(v2):
            g.write(sortari[sort] + ": sortate in " + str(stop - start) + '\n')
        else:
            g.write(sortari[sort] + " EROARE!!" + '\n')

        sort += 1
        v2 = copy.deepcopy(v1)
    g.write('\n')

f.close()
g.close()