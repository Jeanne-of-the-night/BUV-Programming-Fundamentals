budget = 1000
budget_cap = 1500

costs = {
    "storage": 200,
    "marketing": 300,
    "utilities": 150,
    "website": 100,
    "staff_salaries": 400
}

def check_budget():
    total_costs = sum(costs.values())
    if total_costs > budget_cap:
        return "Budget exceeded!"
    elif total_costs > budget:
        return "Warning: Approaching budget limit!"
    else:
        return "Within budget."