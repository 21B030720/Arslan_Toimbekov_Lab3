from lab3_3_data import movies
class Data:
    def __init__(self, movies):
        self.movies = movies
    def bests(self, min):
        for i in self.movies:
            if float(i["imdb"]) >= min:
                print(i["name"])
        print()
    def category(self, cat):
        for i in self.movies:
            if i["category"] == cat:
                print(i["name"])
        print()
    def average_imdb(self):
        sum = 0
        num = 0
        for i in self.movies:
            sum += float(i["imdb"])
            num += 1
        print(sum/num)
    def average_imdb_category(self, cat):
        sum = 0
        num = 0
        for i in self.movies:
            if i["category"] == cat:
                sum += float(i["imdb"])
                num += 1
        print(sum / num)

m = Data(movies)
m.bests(float(input()))
m.category(input())
m.average_imdb()
m.average_imdb_category(input())