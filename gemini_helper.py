def get_ai_response(income, expenses, goal, product_price, months):

    income = int(income)
    expenses = int(expenses)
    product_price = int(product_price)
    months = int(months)

    savings = income - expenses
    expense_percent = (expenses / income) * 100
    recommended_saving = income * 0.20
    monthly_target = product_price / months

    response = f"💰 Monthly Income: ₹{income}\n"
    response += f"💸 Monthly Expenses: ₹{expenses}\n"
    response += f"🏦 Remaining Savings: ₹{savings}\n\n"

    response += f"🎯 Product Goal: {goal}\n"
    response += f"🛒 Product Price: ₹{product_price}\n"
    response += f"📅 Buy Within: {months} months\n"
    response += f"💡 Need to Save Every Month: ₹{monthly_target:.0f}\n\n"

    response += f"✅ Recommended Monthly Saving: ₹{recommended_saving:.0f}\n\n"

    if savings >= monthly_target:
        response += "🎉 Great! You can buy this product within your target time.\n\n"
    else:
        extra = monthly_target - savings
        response += f"⚠ You need to save ₹{extra:.0f} more every month.\n\n"

    if expenses > income:
        response += "🚨 ALERT: Your expenses are more than your income.\n"
        response += "👉 Reduce unnecessary expenses immediately.\n\n"

    elif expense_percent >= 80:
        response += "⚠ You are spending almost all your income.\n"
        response += "📉 Try to reduce shopping, food delivery, and entertainment expenses.\n\n"

    elif expense_percent >= 60:
        response += "🙂 Your spending is moderate.\n"
        response += "💡 Try to increase your monthly savings.\n\n"

    else:
        response += "✅ Excellent! Your budget management is healthy.\n\n"

    response += "🤖 AI Financial Advice:\n"

    if monthly_target > recommended_saving:
        response += "📌 Your goal is ambitious. Try increasing savings or extending the time period."
    else:
        response += "🚀 Your goal is achievable with consistent monthly savings."

    return response