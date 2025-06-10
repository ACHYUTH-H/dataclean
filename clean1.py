import pandas as pd

# Step 1: Load the original CSV file
df = pd.read_csv("financial_news_train.csv")  # replace with your actual filename

# Step 2: Rename columns to match required output
df_cleaned = df.rename(columns={
    'headline': 'headline',
    'date': 'timestamp',
    'publisher': 'source',
    'stock': 'ticker'
})

# Step 3: Add missing 'content' column with blank values
df_cleaned['content'] = ""

# Step 4: Reorder the columns
df_cleaned = df_cleaned[['headline', 'timestamp', 'content', 'source', 'ticker']]

# Step 5: Save the cleaned data to a new CSV
df_cleaned.to_csv("cleaned_financial_news.csv", index=False)

print("✅ Cleaned CSV saved as 'cleaned_financial_news.csv'")
