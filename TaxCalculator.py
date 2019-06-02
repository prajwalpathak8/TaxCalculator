def init():
	name=input("Enter your Name: ")
	print("Welcome %s\n\nIncome Tax Calculator" % name)
	basic=checkNumber("Basic")
	hra=checkNumber("Housing Rent Allowance")
	da=checkNumber("Dearness Allowance")
	other= checkNumber("Other")
	salary=basic+hra+da+other
	print("Your salary is %s" % salary)
	deduction=checkNumber("Deduction from")
	taxable_income=salary-deduction
	print("Taxable Income: %s" % taxable_income)
	calculateTax(taxable_income)
	
def calculateTax(taxable):
	tax=0
	if(taxable>=0 and taxable<=250000):
		tax=0
	elif(taxable>=250000and taxable<=500000):
		tax=(taxable-250000)*0.05
	elif(taxable>=500000and taxable<=1000000):
		tax=(taxable-500000)*0.2+(500000-250000)*0.05
	elif(taxable>1000000):
		tax=(taxable-1000000)*0.3+(1000000-500000)*0.2+(500000-250000)*0.05
	else:
		print("Invalid input")
	print("Tax : %s" % tax)
	
def checkNumber(component):
	temp=input("Enter your %s Salary Component: "%component)
	if (temp.isdigit()):
		return int(temp)
	else:
		print("Enter Valid Input. Considering 0 as Input.")
		return 0

init()
