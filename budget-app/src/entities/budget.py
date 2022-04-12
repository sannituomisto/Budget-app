class Budget:
    def __init__(self, amount, category, user=None, budget_id=None):
        self.amount=amount
        self.category=category
        self.user=user
        self.budget_id=budget_id