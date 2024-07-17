class Loan:
    def __init__(self,bankname,type):
        self.bankname=bankname
        self.type=type
    def loandetails(self):
        print('Loan details',self.bankname,self.type)


class HousingLoan(Loan):
    def housingdetails(self):
        print(' sub class')

l=Loan('ICICI','P')
l.loandetails()

hl=HousingLoan()
hl.loandetails()
hl.housingdetails()
print(hl.bankname)
print(hl.type)



