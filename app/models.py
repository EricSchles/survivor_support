from app import db

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.String(400))
    
    def __init__(self, row):
        self.row = row

    def __repr__(self):
        return '<id {}>'.format(self.id)

class URLs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1000))
    keyword = db.Column(db.String(400))
    
    def __init__(self, url, keyword):
        self.url = url
        self.keyword = keyword
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
