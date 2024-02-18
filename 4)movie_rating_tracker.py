def rate_movie(movie_ratings):
    movie_title = input("Enter the movie title:")
    rating = int(input("Rate the movie (1-5):"))

    if movie_title in movie_ratings:
        current_rating , num_ratings = movie_ratings[movie_title]
        new_rating = (current_rating * num_ratings + rating / (num_ratings + 1))
    else:
        movie_ratings[movie_title] = (rating,1)

def display_ratings(movie_ratings):
    print("\nMovie Ratings:")
    print("--------")
    for movie_title, (average_rating, num_ratings) in movie_ratings.items():
        print(f"{movie_title}: Average Rating-{average_rating:.2f} (Based on {num_ratings} ratings)")

movie_ratings = {}

while True:
    print("\n1. Rate a movie")
    print("2. Display ratings")
    print("3. Quit")
    choice = input("Enter your choice:")

    if choice == "1":
        rate_movie(movie_ratings)
    elif choice == "2":
        display_ratings(movie_ratings)
    elif choice == "3":
        break
    else:
        print("Invalid choice. please try again.")