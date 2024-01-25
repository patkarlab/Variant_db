#!/usr/bin/python3
import sqlite3

def create_database():
    conn = sqlite3.connect('variants.db')
    cursor = conn.cursor()

    # Create the Variants table without the GT column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Variants (
            CHROM TEXT,
            POS INTEGER,
            REF TEXT,
            ALT TEXT,
            SAMPLE_NAME TEXT,
            ALT_NUM INTEGER,
            PRIMARY KEY (CHROM, POS, REF, ALT)
        );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database 'variants.db' created with 'Variants' table")

