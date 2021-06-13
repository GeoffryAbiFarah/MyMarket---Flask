from market import db

#models
class Item(db.Model):
    id =db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)

    def __repr__(self): # to change the way we see the items in the terminal
        '''
        db.create_all()
        from market import db
        from market import Item
        item1 = Item(name="iphone10", price=500, barcode="734587443444", description="what a wonderfull phone...")
        db.session.add(item1)
        db.session.commit()
        Item.query.all()
        for item in Item.query.filter_by(price=500):
            print(item)
        '''
        return f'Item {self.name}'
