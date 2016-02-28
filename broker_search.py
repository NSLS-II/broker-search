from flask import Flask, jsonify, render_template, request
from metadatastore.mds import MDSRO
app = Flask(__name__)


@app.route('/search')
def search():
    """Add two numbers server side, ridiculous but well..."""
    db = MDSRO({'host': 'localhost', 'port': 27017,
           'database': 'test',
           'timezone': 'US/Eastern'})
    q = request.args.get('q', '')
    if not q:
        return jsonify(result={'runs': [], 'count': 0})
    query = {'$text': {'$search': q}}
    docs = list(db.find_run_starts(**query))
    count = len(docs)
    if len(docs) > 10:
        docs = docs[:10]
    runs = [render_template('header.html', run=run, abbrev_uid=run['uid'][:8])
            for run in docs]
    return jsonify(result={'runs': runs, 'count': count})


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
