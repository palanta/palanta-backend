from backend import app
from flask import request


@app.route('/programs', methods=['GET', 'POST'])
def kek():
    if request.method == 'GET':
        return 'get'
    return 'kek lel'
