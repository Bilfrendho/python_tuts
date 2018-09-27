#M=Monthly payments
#L=Loan amount
#i=Interest rate 
#n=Number of payments
#LoanAmount=input("Enter the Loan Amount ")
L=input("Enter the Loan Amount ")
#interest=input("Enter the Interest Rate ")
i=input("Enter the Interest Rate ")
#numberOfPayments=input("Enter the Number of Payments ")
n=input("Enter the Number of Payments ")
L=int(L)
i=int(i)
i=i/100
n=int(n)
M=0
M=(L*(i*(i+1)*n))/((i+1)*(n-1))
print("Hello, your loan monthly payment is {0:f} ".format(M))