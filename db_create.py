from app import db
from models import BlogPost

# create the database and tables
db.create_all()


#add stuff
db.session.add(BlogPost("Rad", "I\'m rad."))
db.session.add(BlogPost("Stoked", "I\'m stoked."))


#commit
db.session.commit()