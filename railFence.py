while True:
 print("Enter 1 for encryption")
 print("Enter 2 for decryption")
 n=int(input("Enter your chioice:"))
 if(n==1):
  x=input("Enter PlainText:");
  x=x.replace(" ", "")
  x=list(x);
  l1=[]
  l2=[]
  for i in range(0,len(x)):
   if(i%2==0):
    l1.append(x[i])
   else:
    l2.append(x[i])
  cipherText1 = ''.join(l1)
  cipherText2 = ''.join(l2)
  print("The cipher text for the given plain text is:")
  print(cipherText1+cipherText2)
 elif(n==2):
  x=cipherText1+cipherText2
  x=x.replace(" ", "")
  x=list(x);
  l=len(x)
  m=int(l/2)
  l1=[]
  l2=[]
  if(l%2!=0):
   for i in range(0,m+1): 
    l1.append(x[i])
   for i in range(m+1,len(x)):
    l2.append(x[i])
  else:
   for i in range(0,m):
    l1.append(x[i])
   for i in range(m,len(x)):
    l2.append(x[i])
 #print l1,l2
  len1=len(l1)
  len2=len(l2)
  plain=[]
  if(len1>len2):
   for i in range(0,len1):
    if(i<=len(l2)-1):
     plain.append(l1[i])
     plain.append(l2[i])
    else:
     plain.append(l1[i])
  else:
   for i in range(0,len2):
    if(i<=len(l1)-1):
     plain.append(l1[i])
     plain.append(l2[i])
    else:
     plain.append(l2[i])
  plainText = ''.join(plain)
  print("The plain text is:")
  print(plainText)
 else:
  print("wrong input") 
 
