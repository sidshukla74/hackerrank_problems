n = int(input())
spacing = len(bin(n)[2:])

for i in range(1,n+1):
    print(str(i).rjust(spacing, ' '),str(oct(i)[2:]).rjust(spacing, ' '),str(hex(i)[2:].upper()).rjust(spacing, ' '),str(bin(i)[2:]).rjust(spacing, ' '))


"""
for i in range(1,n+1):
  print(str(i).ljust(spacing, " "), str(oct(i)[2:].ljust(spacing," ")), str(hex(i)[2:].ljust(spacing," ")), str(bin(i)[2:].ljust(spacing, " ")))
  """