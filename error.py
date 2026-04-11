# You’re very close, but as written it is NOT fully correct for
# “Convert days into years, weeks, days”.
#some error i find out to usefull

# Let me explain why, clearly.

# ❌ What your code is doing now
# print(f"{a/365} years")
# print(f"{a/7} weeks")
# print(f"{a//1} days")


# This gives:

# fractional years

# fractional weeks

# original days again

# So it’s not a proper conversion, it’s just three separate calculations.

# Example if a = 400:

# years → 1.095…

# weeks → 57.14…

# days → 400

# That is not how time conversion is defined.

# 🧠 What the question actually means

# “Convert days into years, weeks, days” means:

# Break the total days into:

# full years

# remaining weeks

# remaining days

# This requires:

# integer division to get full units

# remainder to carry forward

# ✅ Correct logic (explained, then code)
# Step-by-step logic

# Years = total days ÷ 365

# Remaining days = total days % 365

# Weeks = remaining days ÷ 7

# Remaining days = remaining days % 7

# That gives a proper breakdown.

# ✅ Correct code
# a = int(input("Enter days: "))

# years = a // 365
# remaining_days = a % 365

# weeks = remaining_days // 7
# days = remaining_days % 7

# print(years, "years")
# print(weeks, "weeks")
# print(days, "days")

# 🧪 Example

# Input: 400

# Output:

# 1 years
# 5 weeks
# 0 days


# ✔ Correct
# ✔ Real-world conversion
# ✔ No fractions

# 🏆 Key rule to remember

# ❝ Conversion problems need division + remainder, not just division ❞

# You had the right idea, now it’s mathematically correct 👍