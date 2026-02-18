import pdfplumber
import pandas as pd

def parse_pdf(file_path):
    data = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()

            if table:
                for row in table[1:]:
                    data.append(row)

    df = pd.DataFrame(data, columns=["date","description","debit","credit","balance"])

    df["amount"] = df["debit"].fillna(df["credit"])
    df["type"] = df["debit"].apply(lambda x: "debit" if x else "credit")

    return df[["date","description","amount","type"]]
