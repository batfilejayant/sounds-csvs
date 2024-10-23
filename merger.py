import pandas as pd
import numpy as np

def create_mixed_train_set(normal_csv, emergency_csv, output_csv, n_samples=2000, random_seed=100):
    # Load both datasets
    normal_df = pd.read_csv(normal_csv)
    emergency_df = pd.read_csv(emergency_csv)
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Calculate the number of samples to take from each dataset
    n_per_class = n_samples // 2
    
    # Sample from both datasets
    sampled_normal = normal_df.sample(n=n_per_class, random_state=random_seed)
    sampled_emergency = emergency_df.sample(n=n_per_class, random_state=random_seed)
    
    # Concatenate the sampled data
    mixed_df = pd.concat([sampled_normal, sampled_emergency], ignore_index=True)
    
    # Shuffle the mixed dataset
    mixed_df = mixed_df.sample(frac=1, random_state=random_seed).reset_index(drop=True)
    
    # Save the mixed dataset
    mixed_df.to_csv(output_csv, index=False)
    
    print(f"Mixed dataset saved to {output_csv}")

# Usage
normal_csv_path = 'D:/college/Capstone Project/normal sounds/normal sounds_merged.csv'
emergency_csv_path = 'D:/college/Capstone Project/emergency sounds/emergency sounds_merged.csv'
output_csv_path = 'MT.csv'

create_mixed_train_set(normal_csv_path, emergency_csv_path, output_csv_path, n_samples=2000)
