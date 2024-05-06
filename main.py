"""main file"""
from src.http.app import app

from src.http.views.post import app



if __name__=='__main__':
    app.run(debug=True, port=1414)
