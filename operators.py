def calc(a,b,o="*"):
 if o=='+':
  c=a+b
  print("result =",c)
 elif o=='-':
  c=a-b
  print("result =",c)
 elif o=='*':
  c=a*b
  print("result =",c)
 elif o=='/':
  c=a/b
  print("result=",c)
 else:
  print("invalid operator")
calc(8,2)
