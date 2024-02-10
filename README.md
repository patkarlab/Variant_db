# Variant Database Management Scripts

These scripts manage an SQLite database to store genetic variant information from the VCF files

## Creating the database 

`./create_database.py` will create the database.
Usage: `create_database.py <database_name>` 

## Adding the variant information to the database
 
`./append_to_database.py` will append the variant info to the database.
Usage: `./append_to_database.py <database_name> <vcf_file1> <vcf_file2> ...`

## Calculating the frequency of each variant in the database

`./freq.py` will calculate the frequency of each variant in the database.
Usage: `./add_comment.py <db_name> <chrom> <pos> <ref> <alt> <comments>`

## Comments for annotating the variants

`./comment_column.py` creates a new column for comments in the database   
Usage: `./comment_column.py <database_name>`
 
`./add_comment.py` will add a comment
Usage: `./add_comment.py <db_name> <chrom> <pos> <ref> <alt> <comments>`

`./remove_comment.py` will remove the comment
Usage: `./remove_comment.py <db_name> <chrom> <pos> <ref> <alt> <comment_to_remove>`


# Databases


