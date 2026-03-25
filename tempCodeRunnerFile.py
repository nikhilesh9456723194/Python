for col in df.columns:
    if df[col].nunique() < 20:
        print(col)
        print(df[col].value_counts())
        print('-' * 50)
