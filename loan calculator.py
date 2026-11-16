# Project Title: Bank Loan Calculator
# PS No.: 54

# Function to calculate monthly EMI
def calculate_emi(principal, annual_rate, tenure):

    n = tenure
    r = annual_rate / (12 * 100)

    # Zero interest condition
    if r == 0:
        emi = principal / n
    else:
        emi = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)

    return round(emi, 2)


# Function to calculate total payable amount
def calculate_total_payable(emi, tenure):
    return round(emi * tenure, 2)


# Function to calculate total interest
def calculate_total_interest(principal, total_payable):
    return round(total_payable - principal, 2)


# Function to check loan eligibility
def check_eligibility(emi, monthly_income):

    max_emi = monthly_income * 0.40

    if emi <= max_emi:
        return True, max_emi
    else:
        return False, max_emi


# Main function
def main():

    print("===================================")
    print("       BANK LOAN CALCULATOR")
    print("===================================")

    try:
        # Taking input from user
        principal = float(input("Enter Loan Amount: Rs. "))
        annual_rate = float(input("Enter Annual Interest Rate (%): "))
        tenure = int(input("Enter Loan Tenure (months): "))
        monthly_income = float(input("Enter Monthly Income: Rs. "))

        # Input validation
        if principal <= 0:
            print("Invalid loan amount. Enter a positive amount.")
            return

        if annual_rate < 0 or annual_rate > 30:
            print("Invalid interest rate. Enter rate between 0 and 30.")
            return

        if tenure < 1 or tenure > 360:
            print("Invalid tenure. Enter between 1 and 360 months.")
            return

        if monthly_income <= 0:
            print("Invalid monthly income. Enter a positive amount.")
            return

        # Calculations
        emi = calculate_emi(principal, annual_rate, tenure)

        total_payable = calculate_total_payable(emi, tenure)

        total_interest = calculate_total_interest(
            principal, total_payable
        )

        eligible, max_emi = check_eligibility(
            emi, monthly_income
        )

        # Display result
        print("\n========== LOAN DETAILS ==========")

        print(f"EMI: Rs. {emi:.2f}")

        print(f"Total Payable: Rs. {total_payable:.2f}")

        print(f"Total Interest: Rs. {total_interest:.2f}")

        if eligible:
            print("Eligible: Yes")
        else:
            print(f"Maximum allowed EMI (40% of income): Rs. {max_emi:.2f}")
            print("Loan not eligible: EMI exceeds the allowed limit.")

        print("===================================")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


# Calling main function
if __name__ == "__main__":
    main()