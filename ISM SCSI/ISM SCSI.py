from flask import Flask , render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    mylist = [1,2,3,4,5,6];
    return render_template('index.html', data = mylist )

if __name__ == '__main__':
    app.run()



