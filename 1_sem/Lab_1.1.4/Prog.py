def print_tex_tabular (arr):
    n = 0
    
    for i in range (0, len (arr)):
        if (n % 10 == 0):
            print (int (n / 10) * 10, end = '')
            if   (n == 0):
                print (2 * ' ', '& ', end = '')
            elif (n / 10 < 10):
                print (1 * ' ', '& ', end = '')
            else:
                print (0 * ' ', '& ', end = '')

        print (arr[i], end = '')
        
        n += 1

        if (n % 10 == 0):
            print (' \\\\ \hline')
        else:
            print (' & ', end = '')

def print_tex_dict (arr, mn, mx):
    for i in range (mn, mx + 1):
        if (i in arr):
            print (arr[i], end = '')

            if (i != mx):
                print (' & ', end = '')
        
        if (i == mx):
            print (' \\\\ \hline')

def num_repeated (arr):
    arrRepeated = {}
    mn = min (arr)
    mx = max (arr)

    for i in range (0, len (arr)):
        if (arr[i] not in arrRepeated):
            arrRepeated[arr[i]]  = 1
        else:
            arrRepeated[arr[i]] += 1

    for i in range (mn, mx + 1):
        if (i in arrRepeated):
            print (i, end = '')

            if (i != mx):
                print (' & ', end = '')
        
        if (i == mx):
            print (' \\\\ \hline')

    print_tex_dict (arrRepeated, mn, mx)

    arrParts = {}

    for i in range (mn, mx + 1):
        if (i in arrRepeated):
            arrParts[i] = arrRepeated[i] / len (arr)

    print_tex_dict (arrParts, mn, mx)

def sig_percentage (array, sig, mid):
    one_sig = 0
    two_sig = 0
    three_sig = 0

    for num in array:
        if abs (mid - num) < sig:
            one_sig += 1
        if abs (mid - num) < 2*sig:
            two_sig += 1
        if abs (mid - num) < 3*sig:
            three_sig += 1

    print ("В пределах 1 sigma = ", one_sig   / len (array))
    print ("В пределах 2 sigma = ", two_sig   / len (array))
    print ("В пределах 3 sigma = ", three_sig / len (array))
        
arr = [21, 15, 22, 16, 16, 25, 15, 21, 25, 23, 
       18, 27, 14, 18, 18, 21, 24, 20, 24, 13,
       20, 17, 21, 18, 18, 15, 15, 18, 13, 21, 
       17, 16, 22, 29, 19, 22, 23, 25, 20, 11,
       29, 22, 18, 25, 17, 22, 25, 24, 19, 26,
       27, 31, 25, 15, 17, 26, 24, 25, 20, 22, 
       23, 23, 20, 19, 20, 17, 15, 31, 24, 17, 
       28, 19, 19, 18, 26, 31, 22, 26, 23, 29,
       10, 20, 32, 14, 14, 18, 31, 25, 24, 22,
       22, 20, 21, 13, 23, 30, 13, 13, 17, 21,
       18, 25, 22, 15, 17, 18, 22, 27, 20, 20,
       20, 19, 18, 28, 14, 12, 17, 18, 19, 25,
       25, 20, 21, 19, 29, 22, 25, 14, 28, 16,
       13, 19, 14, 13, 17, 19, 22, 19, 22, 20,
       29, 25, 18, 23, 23, 16, 29, 19, 20, 21, 
       25, 19, 16, 26, 15, 14, 24, 21, 25, 26,
       24, 25, 19, 19, 20, 15, 24, 23, 12, 18,
       23, 22, 17, 24, 24, 34, 21, 19, 18, 18,
       18, 16, 29, 10, 22, 28, 21, 16, 16, 18,
       19, 24, 15, 27, 17, 14, 28, 24, 16, 23]

arr40 = 100* [0]

for i in range (1, len(arr), 2):
    arr40[int((i - 1)/2)] = int(arr[i] + arr[i - 1]) 

    
num_repeated (arr40)

print_tex_tabular (arr40)