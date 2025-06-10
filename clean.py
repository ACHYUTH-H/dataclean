import pandas as pd
from urllib.parse import urlparse

# Step 1: Load your CSV
df = pd.read_csv("your_input_file.csv")  # replace with your filename

# Step 2: Extract headline (assume first sentence or first line of 'Content')
df['headline'] = df['Content'].apply(lambda x: x.split('.')[0] if pd.notna(x) else '')

# Step 3: Set timestamp as blank (not present in data)
df['timestamp'] = ""

# Step 4: Set content (already present)
df['content'] = df['Content']

# Step 5: Extract source from URL
def extract_domain(url):
    try:
        domain = urlparse(url).netloc
        return domain.replace("www.", "").split('.')[0].capitalize()
    except:
        return ""

df['source'] = df['URL'].apply(extract_domain)

# Step 6: Set ticker to blank (not present)
df['ticker'] = ""

# Step 7: Keep only the required columns in order
final_df = df[['headline', 'timestamp', 'content', 'source', 'ticker']]

# Step 8: Save to new CSV
final_df.to_csv("converted_financial_news.csv", index=False)

print("✅ Cleaned file saved as 'converted_financial_news.csv'")
