def top_selling_books(data):
    book_sales = {}
    for book in data:
        title = book['title']
        if title in book_sales:
            book_sales[title] += book['copies_sold']
        else:
            book_sales[title] = book['copies_sold']
    top_books = sorted(book_sales.items(), key=lambda x: x[1], reverse=True)
    return top_books

def author_revenue(data):
    author_sales = {}
    for book in data:
        author = book['author']
        if author in author_sales:
            author_sales[author] += book['price'] * book['copies_sold']
        else:
            author_sales[author] = book['price'] * book['copies_sold']
    top_authors = sorted(author_sales.items(), key=lambda x: x[1], reverse=True)
    return top_authors

def genre_popularity(data):
    genre_sales = {}
    for book in data:
        genre = book['genre']
        if genre in genre_sales:
            genre_sales[genre] += book['copies_sold']
        else:
            genre_sales[genre] = book['copies_sold']
    return genre_sales

def print_summary(data):
    top_books = top_selling_books(data)
    top_authors = author_revenue(data)
    genre_sales = genre_popularity(data)

    print("Top Selling Books:")
    for book, copies_sold in top_books:
        print(f"{book}: {copies_sold} copies sold")

    print("\nTop Authors by Revenue:")
    for author, revenue in top_authors:
        print(f"{author}: ${revenue}")

    print("\nGenre Popularity:")
    for genre, copies_sold in genre_sales.items():
        print(f"{genre}: {copies_sold} copies sold")

# Пример данных о продажах книг
book_sales_data = [
    {'title': 'Book1', 'author': 'Author1', 'genre': 'Fiction', 'price': 20, 'copies_sold': 100},
    {'title': 'Book2', 'author': 'Author2', 'genre': 'Fantasy', 'price': 25, 'copies_sold': 150},
    {'title': 'Book3', 'author': 'Author1', 'genre': 'Non-Fiction', 'price': 18, 'copies_sold': 80},
    {'title': 'Book4', 'author': 'Author3', 'genre': 'Fantasy', 'price': 22, 'copies_sold': 120},
    {'title': 'Book5', 'author': 'Author2', 'genre': 'Fiction', 'price': 20, 'copies_sold': 90}
]

def print_solution():
    print_summary(book_sales_data)
