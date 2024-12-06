from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pandas as pd

# Load dataset
file_path = 'Python/Alin/Moana2/datasetss_for_dump.xlsx'
sheet_name = 'animated_movies_data_beneran_fi'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Inisialisasi kolom baru untuk nilai dinamis
df['Total Studio Oscar Wins'] = 0

# Buat dictionary untuk melacak jumlah penghargaan setiap studio
studio_wins_tracker = {}

# Iterasi melalui dataset
for index, row in df.iterrows():
    studio = row['Studio Produksi']
    
    # Ambil jumlah Oscar sebelumnya (default 0 jika studio belum pernah menang)
    previous_wins = studio_wins_tracker.get(studio, 0)
    
    # Set nilai Dynamic Oscar Wins
    df.at[index, 'Total Studio Oscar Wins'] = previous_wins
    
    # Jika film ini menang Oscar, tambahkan 1 ke tracker
    if row['Menang oscar'] == 1:
        studio_wins_tracker[studio] = previous_wins + 1

# Features (Input) and Target (Output)
X = df[['IMDb Rating', 'Pendapatan Box Office (juta USD)', 'Penghargaan Utama', 'Durasi (menit)', 'Trailer views on youtube', 'Total Studio Oscar Wins']] # Fitur
y = df['Menang oscar']

# Standarisasi Fitur
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Logistic regression model
log_model = LogisticRegression()
log_model.fit(X_train, y_train)

# Input
input_studio = 'Studio Ghibli'
input_year = 2023
total_studio_wins_input = studio_wins_tracker.get(input_studio, 0)

input_data = [7.4, 294, 8, 124, 19282409, total_studio_wins_input]

# Step 1: Predict the probability for the input film
input_data_scaled = scaler.transform([input_data])
input_probability = log_model.predict_proba(input_data_scaled)[0][1]

# Step 2: Filter dataset for the same year and update 'Total Studio Oscar Wins'
if 'Tahun' in df.columns:
    same_year_movies = df[df['Tahun'] == input_year]
    
    # Update 'Total Studio Oscar Wins' for same year movies
    for index, row in same_year_movies.iterrows():
        studio = row['Studio Produksi']
        df.at[index, 'Total Studio Oscar Wins'] = studio_wins_tracker.get(studio, 0)
    
    # Select features for prediction
    same_year_features = same_year_movies[['IMDb Rating', 'Pendapatan Box Office (juta USD)', 
                                           'Penghargaan Utama', 'Durasi (menit)', 
                                           'Trailer views on youtube', 'Total Studio Oscar Wins']]
    
    # Step 3: Predict probabilities for all films in the same year
    same_year_features_scaled = scaler.transform(same_year_features)
    same_year_probabilities = log_model.predict_proba(same_year_features_scaled)[:, 1]
    
    # Step 4: Calculate the maximum probability in the same year
    max_probability_same_year = max(same_year_probabilities)
    
    # Step 5: Compare the input film's probability with the maximum
    relative_probability = (input_probability / max_probability_same_year) * 100
    if relative_probability > 100:
        relative_probability = 100

# Output results
print(f"Input Film Probability: {input_probability * 100:.2f}%")
print(f"Maximum Probability in {input_year}: {max_probability_same_year * 100:.2f}%")
print(f"Relative Probability for Input Film: {relative_probability:.2f}%")
