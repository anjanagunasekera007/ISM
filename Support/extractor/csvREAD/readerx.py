import csv
import numpy

filename = 'pima-indians-diabetes.data.csv'
raw_data = open("groceries.csv", 'rb')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)