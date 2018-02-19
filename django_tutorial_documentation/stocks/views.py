from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
import pandas as pd
import tensorflow as tf
from my_site.settings import STOCKS_DATA_FOLDER


def index(request):
    df = pd.read_excel(STOCKS_DATA_FOLDER + 'fdata.xls')
    numbers = df['CLOSE_PRICE'].values
    # numbers = [1, 2, 3]
    x1 = tf.constant(3)
    x2 = tf.constant(4)
    op = x1 + x2
    with tf.Session() as sess:
        res = op.eval()
    # return HttpResponse(open('myxmlfile.xml').read())
    # return render(request, 'stocks/index.html')
    data = []
    dates = df['TRADE_DATE'].values.tolist()
    for index, row in df.iterrows():
        data.append([dates[index], row['CLOSE_PRICE']])
    context = {'numbers': numbers, 'res': res, 'data': data}
    return render(request, 'stocks/index.html', context)


def get_data(request):
    df = pd.read_excel(STOCKS_DATA_FOLDER + 'fdata.xls')
    # data = {
    #     'date': 10,
    #     'x': 'asdf',
    # }
    print(df['TRADE_DATE'].values[:5])
    dates = []
    for date in df['TRADE_DATE'].values:
        dates.append(str(date)[:10])
    data = {
        'labels': dates,
        'datasets': [{
            'data': df['CLOSE_PRICE'].values.tolist(),
            'label': "Close Price",
            'borderColor': "#3e95cd",
            'fill': 'false'
        }]
    }

    # data = {
    #     'labels': [1, 2, 3, 4, 5],
    #     'datasets': [{
    #         'data': [1, 4, 5, 6, 3],
    #         'label': "Close Price",
    #         'borderColor': "#3e95cd",
    #         'fill': 'false'
    #     }]
    # }
    return JsonResponse(data)
