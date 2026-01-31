def hcf(x,y):
  small_num=0
  if x>y:
    small_num=y
  else:
    small_num=x

 for i in range(1, small_num+1):
   if(x%i==0) and (y%i==0):
     hcf=i
