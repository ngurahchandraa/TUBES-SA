import pandas as pd
import time
from tabulate import tabulate

# Load data pekerjaan dari file CSV
jobs = pd.read_csv('Jobs_Data_25.csv')

def greedy_max_profit(jobs, max_duration):
    start_time = time.time()  # Mulai pengukuran waktu
    
    # Hitung rasio profit terhadap durasi
    jobs['Profit_to_Duration_Ratio'] = jobs['Profit'] / jobs['Duration']
    
    # Urutkan pekerjaan berdasarkan rasio dari tinggi ke rendah
    jobs_sorted = jobs.sort_values(by='Profit_to_Duration_Ratio', ascending=False)
    
    total_duration = 0
    total_profit = 0
    best_combination = []
    
    # Pilih pekerjaan berdasarkan urutan rasio profit terhadap durasi
    for job in jobs_sorted.itertuples(index=False):
        if total_duration + job.Duration <= max_duration:
            total_duration += job.Duration
            total_profit += job.Profit
            best_combination.append(job)
        else:
            break
    
    end_time = time.time()  # Akhiri pengukuran waktu
    execution_time = end_time - start_time  # Hitung waktu eksekusi
    
    return best_combination, total_profit, execution_time

# Eksekusi fungsi dengan durasi maksimum 10 jam
best_combination, best_profit, execution_time = greedy_max_profit(jobs, 10)

# Buat DataFrame untuk kombinasi terbaik
output_data = []
for job in best_combination:
    output_data.append([job[0], job[1], job[2]])

output_df = pd.DataFrame(output_data, columns=['Job Name', 'Duration', 'Profit'])

# Tambahkan total profit dan waktu eksekusi ke DataFrame
output_df.loc[len(output_df)] = ['Total', sum(job.Duration for job in best_combination), best_profit]
output_df.loc[len(output_df)] = ['Execution Time (s)', '', execution_time]

# Cetak hasil menggunakan tabulate untuk output yang lebih rapi
print("Greedy Results:")
print(tabulate(output_df, headers='keys', tablefmt='pretty'))
