import pandas as pd

books = pd.read_csv('books.csv',delimiter=';')
print("Full table version:\n\n", books.head())
print("\n\nOnly titles filter:\n\n",books[['Title']])
print("\n\nFilter by title:\n\n", books[books.Title == "Under the red hood"])
print("\n\nExample of combination of filters(showing titles and length of books with rating 4):\n\n", books[books.Rating == 4][['Title', 'Lengths']])
print("\n\nExample of count function usage:\n\n",books[books.Rating == 4][['Rating']].count())
print("\n\nExample of min, max and sum functions usage:\n\n", books.Lengths.max(), books.Lengths.min(), books.Lengths.sum())
print("\n\nOther examples:\n\n", books[books.Lengths > books.Lengths.mean()])
print("\n\nOther examples:\n\n", books.groupby('Rating').Lengths.mean())
print("\n\nOther examples:\n\n", books.groupby('Rating').Lengths.min(), books.groupby('Rating').Lengths.max())
# На жаль останній приклад з лекції про тип об'єктів видає помилку:
# print("\n\nOther examples:\n\n", books.groupby('Rating').min().Lengths, books.groupby('Rating').max()[['Lengths']])
