#Task 4: Word Frequency Finder
import string 
count={}
para=input("Enter the paragraph:")
for k in para.split():
   k=k.strip(string.punctuation)
   k=k.lower()
   if k:
     count[k]=count.get(k,0)+1
count= sorted(count.items(),key=lambda x: x[1], reverse=True)
print(f"Top 3 most frequent words are:{count[0]},{count[1]},{count[2]}")
