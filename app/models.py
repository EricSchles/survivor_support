from app import db

class URLs(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1000))
    keyword = db.Column(db.String(400))
    source = db.Column(db.String(1000))
    
    def __init__(self, url, keyword, source):
        self.url = url
        self.keyword = keyword
        self.source = source
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
