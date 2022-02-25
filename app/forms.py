from logging.handlers import WatchedFileHandler
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class UploadForm (FlaskForm):
    fileField = FileField('image', validators = [FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'File error detected. Ensure the format of the file is jpg, jpeg or png')])