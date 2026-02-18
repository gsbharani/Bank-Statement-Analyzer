def summarize(df):

    total_spent = df[df["type"]=="debit"]["amount"].astype(float).sum()
    total_income = df[df["type"]=="credit"]["amount"].astype(float).sum()

    return {
        "total_spent": total_spent,
        "total_income": total_income,
        "net_balance": total_income - total_spent
    }
