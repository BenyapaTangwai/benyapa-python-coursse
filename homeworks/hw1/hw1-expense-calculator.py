"""
Personal Finance Calculator
Student: Benyapa Tangwai
Date: 26 July 2025
Purpose: Calculate monthly budget and savings
"""

monthly_income = float(input("Enter your Monthly income(THB): "))#รับค่า รายได้ต่อเดือนจากผู้ใช้
rent_cost = float(input("Enter your Monthly rent/housing cost: "))#รับค่า ค่าเช่าต่อเดือนของผู้ใช้
food_budget = int(input("Enter your Monthly food budget(THB): "))#รับค่า ค่ากินต่อเดือนของผู้ใช้
transportation_cost = float(input("Enter your Monthly transportation expenses: "))#รับค่า ค่าเดินทางต่างๆต่อเดือนของผู้ใช้
entertainment_budget = int(input("Enter your Monthly entertainment budget: "))#รับค่า ค่าพักผ่อนต่อเดือนของผู้ใช้
emergency_fund_percent = float(input("Enter Percentage to save for emergency: "))#รับค่า เปอร์เซ็นต์ที่ต้องการเก็บสำรอง
investment_percent = float(input("Enter Percentage to invest: "))#รับค่า เปอร์เซ็นต์ที่ต้องการเอาไว้ลงทุน

#คำนวณค่าใช้จ่ายและเงินที่เหลือ
total_fixed_expenses = rent_cost + transportation_cost
total_variable_expenses = food_budget + entertainment_budget
total_expenses = total_fixed_expenses + total_variable_expenses
remaining_income = monthly_income - total_expenses

#คำนวณเงินออมและการลงทุน
emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)
available_for_savings = remaining_income - emergency_fund_amount - investment_amount

#คำนวณสัดส่วนค่าใช้จ่ายเทียบกับรายได้ทั้งหมดเป็นเปอร์เซ็นต์
expense_ratio = (total_expenses / monthly_income) * 100

#แสดงผลค่าใช้จ่ายและเงินที่เหลือ
print(f"\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB\n")

#แสดงผลเงินออมและการลงทุน
print(f"=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund({emergency_fund_percent:.0f}%): {emergency_fund_amount:.2f} THB")
print(f"Investment({investment_percent:.0f}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB\n")

#แสดงผลสัดส่วนค่าใช้จ่ายเทียบกับรายได้ทั้งหมด
print(f"=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%\n")

#เสร็จสิ้นการทำงาน