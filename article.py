class Article:

    def __init__(self , title , link , summary) -> None:
        self.title = title
        self.link = link
        self.summary = summary
    
    def __str__(self) -> str:
        return f"Title :{self.title}\nLink:{self.link}\nSummary:{self.summary}"
    
    def to_dict(self):
        return {
            'title':self.title,
            'link':self.link,
            'summary':self.summary
        }