import pandas as pd

df = pd.read_csv('fruits.csv')

len(df.columns)

df.head()

average_vitamin_c = df['vitamin_c_mg'].mean()
average_dietary_fiber = df['dietary_fiber_g'].mean()

print(f"Average Vitamin C: {average_vitamin_c} mg")
print(f"Average Dietary Fiber: {average_dietary_fiber} g")

high_vitamin_c = df[df['vitamin_c_mg'] > 50]
print(high_vitamin_c)

sorted_df = df.sort_values(by='vitamin_c_mg', ascending=False)
print(sorted_df)

# Group by category and calculate the average vitamin C and dietary fiber for
# each category
average_by_category = df.groupby('category')[['vitamin_c_mg',
    'dietary_fiber_g']].mean()
print(average_by_category)

def filter_by_category(data, category):
    return data[data['category'] == category]

# Call the filter_by_category function and print the result
berries_df = filter_by_category(df, 'berries')
print(berries_df)
