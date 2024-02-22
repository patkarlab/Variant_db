#!/usr/bin/python
import sqlite3

def find_unique_samples():
    conn = sqlite3.connect('ICMR_project.db')
    cursor = conn.cursor()

    cursor.execute('SELECT SAMPLE_NAME FROM Variants;')
    all_samples = cursor.fetchall()

    unique_samples_set = set()

    # Split samples by commas and add them to the set
    for sample_row in all_samples:
        sample_names = sample_row[0].split(',')
        unique_samples_set.update(sample_names)

    # Print the unique sample names on separate lines
    print("Unique Samples:")
    for unique_sample in unique_samples_set:
        print(unique_sample)

    conn.close()

if __name__ == "__main__":
    find_unique_samples()

