def summary(df):

    inflow = df["Credit"].sum()
    outflow = df["Debit"].sum()

    grouped = (
        df.groupby("Category")["Debit"]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )

    return {
        "Total Inflow": float(inflow),
        "Total Outflow": float(outflow),
        "Net": float(inflow - outflow),
        "Spending": grouped
    }
