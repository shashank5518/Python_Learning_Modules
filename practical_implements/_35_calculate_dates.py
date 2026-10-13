import datetime
import calendar
import math

balance = 500000
interest_rate = 0.13
monthly_payment = 50000

today = datetime.date.today()
days_current_month = calendar.monthrange(today.year, today.month)[1]
print(days_current_month)

days_until_end_of_month = days_current_month - today.day
print(days_until_end_of_month)

start_date = today + datetime.timedelta(days=days_until_end_of_month + 1)
print(start_date)

end_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    print(end_date, balance)

    days_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_current_month)

current_weight = 220
goal_weight = 180
avg_lbs_week = 1.5

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week

print(f"Reached goal in {(end_date - start_date).days // 7} weeks")

goal_subs = 1000000
current_subs = 85000
subs_to_go = goal_subs - current_subs

avg_subs_day = 2000

days_to_go = math.ceil(subs_to_go / avg_subs_day)

today = datetime.date.today()
print(today + datetime.timedelta(days_to_go))
