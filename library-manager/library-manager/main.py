import streamlit as st
import json
import os

# Load the library data from a JSON file
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save the library data to a JSON file
def save_library():
    with open("library.json", "w") as file:
        json.dump(library_data, file, indent=4)

# Initialize library data
library_data = load_library()

st.set_page_config(page_title="Library Manager", page_icon="📚", layout="wide")

st.title("📚 Library Manager")
st.sidebar.header("📖 Menu")
menu = st.sidebar.radio("Select an option", ["View Books", "Add Book", "Remove Book", "Search"])

if menu == "View Books":
    st.sidebar.subheader("Your Library")
    if library_data:
        st.table(library_data)
    else:
        st.write("Your library is empty. Add some books.")

elif menu == "Add Book":
    st.sidebar.subheader("Add a new book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    publication_year = st.number_input("Publication Year", min_value=1000, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.selectbox("Read Status", ["Not Read", "Reading", "Completed"])
    book_image = st.file_uploader("Upload Book Cover", type=["jpg", "png", "jpeg"])
    
    if st.button("Add Book"):
        if title and author:
            image_path = None
            if book_image is not None:
                image_path = os.path.join("images", book_image.name)
                with open(image_path, "wb") as f:
                    f.write(book_image.getbuffer())
            
            new_book = {"title": title, "author": author, "publication_year": publication_year, "genre": genre, "read_status": read_status, "image": image_path}
            library_data.append(new_book)
            save_library()
            st.success(f'Book "{title}" by {author} added!')
        else:
            st.error("Please enter both title and author.")

elif menu == "Remove Book":
    st.sidebar.subheader("Remove a book")
    book_titles = [book["title"] for book in library_data]
    book_to_remove = st.selectbox("Select a book to remove", book_titles if book_titles else ["No books available"])
    
    if st.button("Remove Book") and book_to_remove != "No books available":
        library_data = [book for book in library_data if book["title"] != book_to_remove]
        save_library()
        st.success(f'Book "{book_to_remove}" removed!')

elif menu == "Search":
    st.sidebar.subheader("Search for a book")
    search_query = st.text_input("Enter book title or author")
    
    if search_query:
        filtered_books = [book for book in library_data if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
        if filtered_books:
            st.table(filtered_books)
        else:
            st.write("No books found matching your search query.")

