import sqlite3, random
conn = sqlite3.connect('Movies.db')
cur = conn.cursor()
# Create a table
cur.execute('''CREATE TABLE IF NOT EXISTS movie_list
             (id INTEGER PRIMARY KEY, title TEXT, publisher TEXT, published_date TEXT, format TEXT, rating FLOAT)''')

# Add movie
def add_movie(title, author, published_date, format, rating):
    cur.execute("INSERT INTO movie_list (title, publisher, published_date, format, rating) VALUES (?, ?, ?, ?, ?)", 
              (title, author, published_date, format, rating))
    conn.commit()

# Get ID from the name
def get_id_from_name(title):
    cur.execute("SELECT id FROM movie_list WHERE title=?", (title,))
    result = cur.fetchone()
    return result[0] if result else None

# Edit data in the table
def edit_movie(user_id, title, author, published_date, format, rating):
    cur.execute("UPDATE movie_list SET title=?, publisher=?, published_date=?, format=?, rating=? WHERE id=?", 
              (title, author, published_date, format, rating, user_id))
    conn.commit()
 
# Show all movies
def show_all_movies():
    cur.execute("SELECT * FROM movie_list")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# suggest
def suggest_movie():
	suggest_movie_list = []
	cur.execute("SELECT * FROM movie_list")
	rows = cur.fetchall()
	for row in rows:
		suggest_movie_list.append(row)
	print(random.choice(suggest_movie_list))

# Remove movie by ID
def remove_movie(movie_id):
    cur.execute("DELETE FROM movie_list WHERE id=?", (movie_id,))
    conn.commit()

# Clear the table
def clear_table():
    cur.execute("DELETE FROM movie_list")
    conn.commit()
    
# loop
danger_zone = False		
while True:
	print("Welcome")
	print("\tAdd a new movie \n\tEdit a movieinformation \n\tShow movie list \n\tSuggest a random movie \n\tDanger zone \n\tExit")
	pick = input("> ")
	if "exit" in pick:
		break
	elif "add" in pick:
		print("If you don't have the information please type 'None'")
		Title, Author, Date, Format, Rating = str(input("Title > ")), str(input("Author > ")), str(input("Date > ")), str(input("physical/online > ")), float(input("Rating (put 0 if unknown) > "))
		add_movie(Title, Author, Date, Format, Rating)
		print(f"you have successfully add a movie called {Title}". format(Title))
	elif "edit" in pick:
		movie_id = get_id_from_name(input("Title of the movie > "))
		print("input new information")
		Title, Author, Date, Format, Rating = str(input("Title > ")), str(input("Author > ")), str(input("Date > ")), str(input("physical/online > ")), float(input("Rating (put 0 if unknown) > "))
		edit_movie(movie_id, Title, Author, Date, Format, Rating)
	elif "show" in pick:
		show_all_movies()
	elif "suggest" in pick:
		suggest_movie()
	elif "danger" in pick:
		danger_zone = True
	else:
		print(f"sorry '{pick}' is not an option".format(pick))
	while danger_zone:			
		print("would you like to: \n\tRemove movie \n\tClear all data \n\tBack")
		danger_pick = input("> ")
		if "back" in danger_pick:
			danger_zone = False
		elif "remove" in danger_pick:
			movie_id = get_id_from_name(input("Title of the movie > "))
			remove_movie(movie_id)
			print(f"{movie_id} Has been removed".format(movie_id))
		elif "clear" in danger_pick:
			clear_table()
			print("your movie list is now empty")
		else:
			print(f"sorry '{danger_pick}' is not an option".format(danger_pick))
try:
	# close
	conn.close()
	cur.close()
except:
	pass
