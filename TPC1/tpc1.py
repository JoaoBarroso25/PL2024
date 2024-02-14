import pandas as pd

# Read CSV file
df = pd.read_csv('emd.csv')

# List of modalidades desportivas ordered alphabetically
modalidades_ordenadas = sorted(df['modalidade'].unique())

# Percentages of atletas aptos (federado=True) and inaptos (federado=False)
total_atletas = df.shape[0]
aptos = df[df['federado'] == True].shape[0]
inaptos = df[df['federado'] == False].shape[0]
percent_aptos = (aptos / total_atletas) * 100
percent_inaptos = (inaptos / total_atletas) * 100

# Distribution of atletas by escalão etário up to '[35,39]'
bins = [20, 25, 30, 35, 40]
df['escalao_etario'] = pd.cut(df['idade'], bins=bins, right=False)
escalao_distribution = df['escalao_etario'].value_counts().sort_index().to_dict()

# Format the keys in the dictionary to the desired string format
formatted_escalao_distribution = {
    f'[{interval.left},{interval.right - 1}]': count
    for interval, count in escalao_distribution.items()
}

# Print the results
print("Lista ordenada alfabeticamente das modalidades desportivas:")
print(modalidades_ordenadas)
print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
print(f"Atletas aptos: {percent_aptos:.2f}%")
print(f"Atletas inaptos: {percent_inaptos:.2f}%")
print("\nDistribuição de atletas por escalão etário:")
print(formatted_escalao_distribution)