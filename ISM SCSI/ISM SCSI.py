from flask import Flask , render_template
from Sales_Calculator import returnSales



app = Flask(__name__)
app.config['DEBUG'] = True

ItemList = returnSales()
print ("  6969696969696969696969696969696969 ")
print str(len(ItemList))

for i in ItemList:
    print i.name
    print type(i)
print ("  6969696969696969696969696969696969 ")

@app.route('/', methods=['GET', 'POST'])
def main():
    mylist = [1,2,3,4,5,6];
    return render_template('index.html', data = mylist,name="the name" )

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None;
    listx  = [2,4,6,8,10]
    return render_template('item_sales.html', error=error,datalist=ItemList)

if __name__ == '__main__':
    app.run(debug=True)






#External Functions

