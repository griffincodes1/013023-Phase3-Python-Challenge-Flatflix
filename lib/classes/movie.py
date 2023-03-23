class Movie:
    all =[]
    def __init__(self, title):
         if len(title) <= 0:
            raise Exception("title must be one character")
        self.title = title
    # title property goes here!

    def average_rating(self):
        return sum(list(map(lambda review: review.rating, self._reviews)))/len(self._reviews)

    @classmethod
    def highest_rated(cls):
         return Movie("Rashomon")
         def settitle(self, title):
        self._title = title

    def gettitle(self):
        return self._title

    title = property(gettitle, settitle)

    def add_review(self, review):
        Movie._reviews.append(review)

   
