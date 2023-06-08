import pandas as pd
filename="preliminary_medication.csv"
data = pd.read_csv(filename)
s=data.iloc[:,0]
idx=0
def prelim_medi(disease):
    for i in range(0,s.size):
#     print(i)
        if  s[i]==disease:
            idx=i
            return data.iloc[:,1][idx]

# print(prelim_medi("Fungal infection"))
# print(data.iloc[:,1][9])