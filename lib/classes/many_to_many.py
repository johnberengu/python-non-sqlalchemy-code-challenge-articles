class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        self.author = author
        self.magazine = magazine
        self._title = title
        
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
class Author:
    def __init__(self, name):

        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name


    @property
    def name(self):
        return self._name
    

    def articles(self):
        return [article for article in Article.all if article.author == self]
    

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
    

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines())) if self.magazines() else None
    

class Magazine:
    all = []

    
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        
        
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        
        self.name = name
        self.category = category

        Magazine.all.append(self)


    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    

    def contributors(self):
        return list(set(article.author for article in self.articles()))
    

    def article_titles(self):
        return [article.title for article in self.articles()] if self.articles() else None
    

    def contributing_authors(self):

        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        
        frequent_authors = [author for author, count in author_counts.items() if count > 2]
        return frequent_authors if frequent_authors else None\


    @classmethod
    def top_publisher(cls):
        return max(cls.all, key=lambda mag: len(mag.articles()), default=None)
    
