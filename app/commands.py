from flask_script import Command
from app.models import URLs
from app.scraper import scrape
from app import db
import code

class REPL(Command):
    "runs the shell"

    def run(self):
        code.interact(local=locals())

class ScrapeCrisisTextLineIndex(Command):
    "runs the scraper"

    def run(self):
        urls = scrape_crisis_text_line()
        for url in urls:
            url_obj = URLs(url[0], url[1], url[2])
            db.session.add(url_obj)
            db.session.commit()

