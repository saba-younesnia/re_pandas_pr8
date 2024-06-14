import pandas as pd
import matplotlib.pyplot as plt

file=open('C:\\Users\\YOONES-NIA\\PycharmProjects\\pythonProject4,1\\students2.txt','r')

line1=file.readline()
names=line1.split()
names.remove('name:')

line2=file.readline()
familynames=line2.split()
familynames.remove('familyname:')

line3=file.readline()
scores=line3.split()
scores.remove('score:')
intsocres=[]
for s in scores:
    intsocres.append(float(s))

alllists=list(zip(names,familynames,scores))
df=pd.DataFrame(alllists)
df.columns=['name','familyname','average score']
print(df)

plt.bar(names,intsocres)
plt.show()

