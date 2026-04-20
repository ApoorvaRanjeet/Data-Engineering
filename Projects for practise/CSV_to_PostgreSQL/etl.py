import pandas as pd
from sqlalchemy import create_engine

'Step 1 : extract '
'Read the CSV FILE'

df = pd.read_csv(r'C:\Users\apoor\OneDrive\Documents\data engineer\Projects\train.csv', encoding='latin1')
print("Raw data shape",df.shape)

print(df.head())
print(df.info())

'step 2 : Transform'

print(df.isnull().sum())
print(df.duplicated().sum())

df.dropna(subset=['Postal Code'],inplace=True)
print(df.isnull().sum())

# df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
# df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# print(df["Order Date"].isnull().sum())

# print(df["Order Date"].tail(15))


# print(df["Order Date"].head(20))
# print("______________________________")
# print(df["Order Date"].tail(20))

'fixing the date issue'
def parse_mixed_dates(date_series):
    formats = ["%m/%d/%Y", "%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"]
    
    def try_parse(val):
        if pd.isnull(val):
            return pd.NaT
        for fmt in formats:
            try:
                return pd.to_datetime(val, format=fmt)
            except:
                continue
        return pd.NaT  # if nothing works
    
    return date_series.apply(try_parse)

df["Order Date"] = parse_mixed_dates(df["Order Date"])
df["Ship Date"] = parse_mixed_dates(df["Ship Date"])

print("Nulls after fix:", df["Order Date"].isnull().sum())
print(df["Ship Date"].isnull().sum())


df.columns = df.columns.str.lower().str.replace(" ", "_")

# Remove negative sales values if any (data quality issue)
df = df[df["sales"] > 0]

print(df.shape)


'Step 3: LOAD'
# Push clean data into PostgreSQL
engine = create_engine("postgresql://postgres:password@localhost:5433/sales_db")

df.to_sql("sales", engine, if_exists="replace", index=False)

print("Data loaded successfully into PostgreSQL!")
