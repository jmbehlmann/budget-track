def format_transactions(transactions):
    formatted_transactions = [
        {
            'id': t.id,
            'description': t.description,
            'amount': f"{t.amount:.2f}",
            'transaction_type': t.transaction_type,
            'category': t.category,
            'date': t.date
        }
        for t in transactions
    ]
    return formatted_transactions

def format_budget_info(budgets, expenses):
    formatted_budget_info = []
    for budget in budgets:
        budget_total = sum(float(e['amount']) for e in expenses if e['category'].id == budget.category_id)
        budget_difference = budget.amount - budget_total
        formatted_budget_info.append({
            'category': budget.category,
            'amount': f"{budget.amount:.2f}",
            'budget_total': f"{budget_total:.2f}",
            'budget_difference': f"{budget_difference:.2f}"
        })
    return formatted_budget_info
