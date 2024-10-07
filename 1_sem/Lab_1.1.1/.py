def GetSigmaSr (arr, R_sr, n):
    sigma_sr = 0
    for i in range(n):
        sigma_sr += (arr[i] - R_sr)**2

    sigma_sr = sigma_sr**(0.5)
    sigma_sr /= n

    return sigma_sr

def GetArrR (arr_U, arr_I):
    arr_R = len(arr_U)*[0]
    for i in range (len(arr_U)):
        arr_R[i] = arr_U[i] / arr_I[i] 

    return arr_R
    
arr_U_10 = [71, 76, 81, 86, 95, 92, 100, 113, 123, 134]
arr_I_10 = [65, 69, 74, 79, 87, 84, 91,  102, 113, 123]

arr_U_20 = [132, 140, 160, 180, 200, 170, 210, 250, 280, 302]
arr_I_20 = [63,  67,  75,  84,  94,  81,  102, 118, 133, 144]

arr_U_30 = [196, 220, 250, 280, 310, 250, 280, 310, 380, 480]
arr_I_30 = [62,  67,  77,  86,  96,  78,  87,  98,  116, 148]

arr_U_50 = [316, 360, 480, 540, 620, 416, 460, 540, 620, 1000]
arr_I_50 = [59,  68,  90,  103, 117, 78,  87,  100, 115, 190]

arr_R_10 = GetArrR (arr_U_10, arr_I_10)
arr_R_20 = GetArrR (arr_U_20, arr_I_20)
arr_R_30 = GetArrR (arr_U_30, arr_I_30)
arr_R_50 = GetArrR (arr_U_50, arr_I_50)

R_sr_10 = sum (arr_R_10) / 10
R_sr_20 = sum (arr_R_20) / 10
R_sr_30 = sum (arr_R_30) / 10
R_sr_50 = sum (arr_R_50) / 10

print (R_sr_10, R_sr_20, R_sr_30, R_sr_50)

print (GetSigmaSr(arr_R_10, R_sr_10, 10), GetSigmaSr(arr_R_20, R_sr_20, 10), 
       GetSigmaSr(arr_R_30, R_sr_30, 10), GetSigmaSr(arr_R_50, R_sr_50, 10)) 

print (sum (arr_U_10) / sum (arr_I_10), sum (arr_U_20) / sum (arr_I_20), 
       sum (arr_U_30) / sum (arr_I_30), sum (arr_U_50) / sum (arr_I_50))

