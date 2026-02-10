import pdfplumber
import pandas as pd

def parse_pdf(path):

    rows = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()

            for table in tables:
                for r in table[1:]:
                    rows.append(r)

    df = pd.DataFrame(rows)
    df.columns = ["Date","Description","Debit","Credit","Balance"]

    df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce").fillna(0)
    df["Credit"] = pd.to_numeric(df["Credit"], errors="coerce").fillna(0)

    return df
