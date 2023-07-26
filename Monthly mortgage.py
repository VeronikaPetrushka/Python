def monthly_mortgage(loan, term):
    interest = 0
    if loan <= 10000:
        interest = 0.02
    elif loan > 10000 and loan <= 50000:
        interest = 0.07
    elif loan > 50000 and loan <= 150000:
        interest = 0.12
    else:
        interest = 0.15
    monthly_rate = interest/12
    m_payment = loan*monthly_rate/(1 - (1 + monthly_rate) ** (-term))
    return m_payment

loan = float(input("Enter loan amount: "))
term = int(input("Enter loan term in months: "))

m_payment = monthly_mortgage(loan, term)

print("Monthly mortgage payment: $%.2f" % m_payment)
#OR
print("Monthly mortgage payment: " + "$" + str((round(m_payment,2))))


