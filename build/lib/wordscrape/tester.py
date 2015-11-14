from wordscrape import read_dir, write_csv

path = '/temp'
d = read_dir(path)
write_csv(d, 'report.csv')
