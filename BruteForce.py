import itertools
import pandas as pd
import time
from tabulate import tabulate

# Load data pekerjaan dari file CSV
jobs = pd.read_csv('Jobs_Data_15.csv')

def brute_force_max_profit(jobs, max_duration):
    start_time = time.time()  # Mulai pengukuran waktu
    best_profit = 0  # Inisialisasi profit terbaik
    best_combination = None  # Inisialisasi kombinasi terbaik
    
    # Iterasi melalui semua kombinasi pekerjaan untuk setiap ukuran subset
    for r in range(1, len(jobs) + 1):
        for combination in itertools.combinations(jobs.itertuples(index=False), r):
            total_duration = sum(job.Duration for job in combination)  # Hitung total durasi
            if total_duration <= max_duration:  # Periksa apakah total durasi sesuai
                total_profit = sum(job.Profit for job in combination)  # Hitung total profit
                if total_profit > best_profit:  # Jika profit lebih besar dari yang sebelumnya
                    best_profit = total_profit  # Perbarui profit terbaik
                    best_combination = combination  # Perbarui kombinasi terbaik
    
    end_time = time.time()  # Akhiri pengukuran waktu
    execution_time = end_time - start_time  # Hitung waktu eksekusi
    
    return best_combination, best_profit, execution_time

# Eksekusi fungsi dengan durasi maksimum 10 jam
best_combination, best_profit, execution_time = brute_force_max_profit(jobs, 10)

# Buat DataFrame untuk kombinasi terbaik
output_data = []
for job in best_combination:
    output_data.append([job[0], job[1], job[2]])

output_df = pd.DataFrame(output_data, columns=['Job Name', 'Duration', 'Profit'])

# Tambahkan total profit dan waktu eksekusi ke DataFrame
output_df.loc[len(output_df)] = ['Total', sum(job.Duration for job in best_combination), best_profit]
output_df.loc[len(output_df)] = ['Execution Time (s)', '', execution_time]

# Cetak hasil menggunakan tabulate untuk output yang lebih rapi
print("Brute Force Results:")
print(tabulate(output_df, headers='keys', tablefmt='pretty'))
