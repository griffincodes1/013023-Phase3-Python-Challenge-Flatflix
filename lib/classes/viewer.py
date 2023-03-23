class Viewer:
    all =[]
    def __init__(self, username):
          self.username = username
        Viewer.all.append(self)
        self._reviews = []

    def setusername(self, username):        
        if username in [viewer.username for viewer in Viewer.all]:
            raise Exception("usernames must be special")
        if not 6 <= len(username) <= 16:
            raise Exception("usernames must be 6 to 16 letters") 
        self._username = username

    def getusername(self):
        return self._username
    username = property(getusername, setusername)

     def add_review(self, review):
        self._reviews.append(review)

    def getreviews(self):
        return self._reviews
    reviews = property(getreviews)

    # username property goes here!

    def reviewed_movie(self, movie):
        pass

    def rate_movie(self, movie, rating):
        pass