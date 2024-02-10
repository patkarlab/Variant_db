# Variant Database Management Scripts

These scripts manage an SQLite database to store genetic variant information from the VCF files

## Creating the database 

`./create_database.py` will create the database.
Usage: `create_database.py <database_name>`

The database has 6 columns.
1. CHROM - Chromosome
2. POS - The reference position
3. REF - Reference base
4. ALT - Alternate base
5. SAMPLE NAME - Samples in which the variant is present.
6. ALT NUM - Number of alleles in which the alternate base is present 

## Adding the variant information to the database

`./append_to_database.py` will append the variant info to the database.
Usage: `./append_to_database.py <database_name> <vcf_file1> <vcf_file2> ...`

## Calculating the frequency of each variant in the database

`./freq.py` will calculate the frequency of each variant in the database.
Usage: `./add_comment.py <db_name> <chrom> <pos> <ref> <alt> <comments>`

Frequency is calculated by 
`Number of samples in which the variant is present / Total number of samples`

## Comments for annotating the variants

`./comment_column.py` adds a new column for comments in the database
Usage: `./comment_column.py <database_name>`

`./add_comment.py` will add a comment
Usage: `./add_comment.py <db_name> <chrom> <pos> <ref> <alt> <comments>`

`./remove_comment.py` will remove the comment
Usage: `./remove_comment.py <db_name> <chrom> <pos> <ref> <alt> <comment_to_remove>`

1. For removing a specific comment, type the comment as it is in place of `<comment_to_remove>`
2. For removing all comments, type `all` in small letters in place of `<comment_to_remove>`


# Databases

- Currently there are two databases `ALP.db` and `ICMR_project.db`. 
- `ALP_db_list.txt` contains the list of vcf files appended to the `ALP.db`.
- `ICMR_db_list.txt` contains the list of vcf files appended to the `ICMR_project.db`.   

