# ZADANIE 1
class Time:
    """Class definig time"""

    def __init__(self, hour, minute):
        if isinstance(hour, int) and isinstance(minute, int):
            self.hour = hour
            self.minute = minute
        else:
            raise TypeError("Hour and minute should be integers")

    def is_valid (self):
        """Check if hour and minute are valid"""
        return (0 <= self.hour < 24) and (0 <= self.minute < 60)

    def add_times(self, other):
        """Adds two times"""
        new_hour = self.hour + other.hour
        new_minute = self.minute + other.minute

        if new_minute >= 60:
            new_minute -= 60
            new_hour += 1

        if new_hour >= 24:
            new_hour -= 24

        return f'{new_hour}:{new_minute}'

    def __lt__(self, other):
        """Defines order"""
        if self.hour == other.hour:
            return self.minute < other.minute
        return self.hour < other.hour

    def __repr__(self):
        """Returns representation of time"""
        return f'{self.hour}:{self.minute}'


time1 = Time(24,12)
time2 = Time(12, 34)
time3 = Time(0, 49)

print(f'Is {time1} valid time: {time1.is_valid()}')
print(f'Is {time2} valid time: {time2.is_valid()}')
print(f'Is {time3} valid time: {time3.is_valid()}')

print(f'Adding {time3} and {time2} Result {time3.add_times(time2)}')

times = [time1, time2, time3]
times.sort()
for time in times:
    print(time)

# ZADANIE 2
class Movie:
    """Defining movie"""

    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating


movies = [
    Movie("The Matrix", 1999, 8.7),
    Movie("Blade Runner", 1982, 8.1),
    Movie("Star Wars: Episode IV - A New Hope", 1977, 8.6),
    Movie("Inception", 2010, 8.8),
    Movie("Interstellar", 2014, 8.6),
    Movie("The Terminator", 1984, 8.0),
    Movie("Alien", 1979, 8.4),
    Movie("Jurassic Park", 1993, 8.1),
    Movie("Avatar", 2009, 7.8),
    Movie("The Fifth Element", 1997, 7.7)
]

# Sorting the list by movie title (ascending)
sorted_by_title = sorted(movies, key=lambda x: x.title.lower())

# Sorting the list by release year (ascending)
sorted_by_year = sorted(movies, key=lambda x: x.year)

# Sorting the list by movie rating (descending)
sorted_by_rating_desc = sorted(movies, key=lambda x: x.rating, reverse=True)

# Sorting the list by release year, then by rating (ascending)
sorted_by_year_and_rating = sorted(movies, key=lambda x: (x.year, x.rating))

# Sorting the list by rating, then by release year (descending)
sorted_by_rating_and_year_desc = sorted(movies, key=lambda x: (x.rating, x.year), reverse=True)

print("Sorting by title (ascending):")
for movie in sorted_by_title:
    print(movie.title)

print("\nSorting by release year (ascending):")
for movie in sorted_by_year:
    print(movie.title, movie.year)

print("\nSorting by rating (descending):")
for movie in sorted_by_rating_desc:
    print(movie.title, movie.rating)

print("\nSorting by release year, then by rating (ascending):")
for movie in sorted_by_year_and_rating:
    print(movie.title, movie.year, movie.rating)

print("\nSorting by rating, then by release year (descending):")
for movie in sorted_by_rating_and_year_desc:
    print(movie.title, movie.year, movie.rating)