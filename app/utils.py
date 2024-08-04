from datetime import datetime, timezone, timedelta

def get_current_month():
    return datetime.now(timezone.utc).strftime('%Y-%m')

def get_previous_next_months(current_month):
    date_obj = datetime.strptime(current_month, "%Y-%m")
    first_day_current_month = date_obj.replace(day=1)

    previous_month = (first_day_current_month - timedelta(days=1)).strftime("%Y-%m")
    next_month = (first_day_current_month + timedelta(days=31)).replace(day=1).strftime("%Y-%m")

    return previous_month, next_month

def format_month(month_str):
    return datetime.strptime(month_str, "%Y-%m").strftime("%B %Y")

def format_date(date):
    return date.strftime('%B %-d')

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
        budget_total = sum(e.amount for e in expenses if e.category_id == budget.category_id)
        budget_difference = budget.amount - budget_total
        formatted_budget_info.append({
            'category': budget.category,
            'amount': f"{budget.amount:.2f}",
            'budget_total': f"{budget_total:.2f}",
            'budget_difference': f"{budget_difference:.2f}"
        })
    return formatted_budget_info
