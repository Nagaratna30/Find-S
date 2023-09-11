import random
import csv

attributes = [['Sunny','Rainy'],
              ['Warm',"Cold"],
              ['Normal','High'],
              ['Strong','Weak'],
              ['Warm','Cool'],
              ['Same','Change']]
a=[]
with open("/data.csv","r") as csvFile:
  reader = csv.reader(csvFile)
  for row in reader:
    a.append(row)

num_a = len(attributes)
hyp = [0]*num_a
print(hyp)

for i in range(0,num_a):
  hyp[i]=a[1][i]



for i in range(1,len(a)):
  if a[i][num_a] == 'Yes':
    for j in range(0,num_a):
      if a[i][j]!=hyp[j]:
        hyp[j]='?'
      else:
        hyp[j]=a[i][j]
  print(hyp)

print(hyp)
