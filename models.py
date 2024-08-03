from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)


class Folders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder_name = db.Column(db.String(255), nullable=False)
    parent_folder_id = db.Column(db.Integer, db.ForeignKey('folders.id'))
    sub_folders = db.relationship('Folders', backref=db.backref('parent_folder', remote_side=[id]))
    files = db.relationship('Files', backref='folder')


class Files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255), nullable=False)
    extension = db.Column(db.String(10), nullable=False)
    size = db.Column(db.BigInteger, nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('folders.id'))


class Range(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    range_name = db.Column(db.String(255), nullable=True)
    position = db.Column(db.String(10), nullable=True)
    vs_position = db.Column(db.String(10), nullable=True)
    stack_size = db.Column(db.BigInteger, nullable=True)
    fold = db.Column(db.Text, nullable=True)
    preflop_raise = db.Column(db.Text, nullable=True)
    call = db.Column(db.Text, nullable=True)
    all_in = db.Column(db.Text, nullable=True)
    training_hand = db.Column(db.Text, nullable=True)


def add_folder(folder_name, parent_folder_id=None):
    with app.app_context():
        new_folder = Folders(folder_name=folder_name, parent_folder_id=parent_folder_id)
        db.session.add(new_folder)
        db.session.commit()
        return new_folder


def update_preflop_raise(range_name, preflop_raise, fold, all_in, call, position=None, vs_position=None):
    with app.app_context():
        range_to_update = Range.query.filter_by(range_name=range_name).first()
        if range_to_update:
            range_to_update.preflop_raise = ' '.join(preflop_raise)
            range_to_update.fold = ' '.join(fold)
            range_to_update.all_in = ' '.join(all_in)
            range_to_update.call = ' '.join(call)
            range_to_update.position = position
            range_to_update.vs_position = vs_position

            db.session.commit()
            return 'Preflop raise updated successfully.'
        else:
            return 'Range not found.'


def add_file(file_name, extension, size, folder_id):
    with app.app_context():
        new_file = Files(file_name=file_name, extension=extension, size=size, folder_id=folder_id)
        db.session.add(new_file)
        db.session.commit()
        return new_file


def add_range(range_name, position, vs_position=None, stack_size=None, fold=None, preflop_raise=None, three_bet=None, all_in=None, training_hand=None):
    with app.app_context():
        new_range = Range(
            range_name=range_name,
            position=position,
            vs_position=vs_position,
            stack_size=stack_size,
            fold=fold,
            preflop_raise=','.join(preflop_raise) if preflop_raise else None,
            three_bet=three_bet,
            all_in=all_in,
            training_hand=training_hand
        )
        db.session.add(new_range)
        db.session.commit()
        return new_range


def delete_file(file_id):
    with app.app_context():
        file_to_delete = Files.query.get(file_id)
        if file_to_delete:
            db.session.delete(file_to_delete)
            db.session.commit()
            return True
        else:
            return False


def delete_range(range_name):
    with app.app_context():
        range1 = Files.query.get(range_name)
        if range1:
            db.session.delete(range1)
            db.session.commit()
            return True
        else:
            return False


def find_range_by_name(range_name):
    with app.app_context():
        range1 = Range.query.filter_by(range_name=range_name).first()

        return range1


with app.app_context():
    db.create_all()
