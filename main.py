from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 
    'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 
    'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 
    'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 
    'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 
    'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 
    'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 
    'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 
    'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 
    'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 
    'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 
    'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 
    'end': 1564627800, 'start': 1564626000}
]

def price_calculated(begin, end):
    begin = datetime.fromtimestamp(int(begin))
    end = datetime.fromtimestamp(int(end))
    fixedfee = 0.36
    fee = 0.09
    duration = int((end - begin).seconds/60)
    totalprice = fixedfee + (duration * fee)

    if begin.hour >= 22 or end.hour < 6:
        return fixedfee

    elif begin.hour >= 6 and end.hour < 22:
        return totalprice

    else:
        if begin.hour < 6:
            begin = datetime(begin.year, begin.month, begin.day, 6)
            return totalprice

        elif end.hour >= 22 and end.minute >=1:
            end = datetime(end.year, end.month, end.day, 22)
            return totalprice

def classify_by_phone_number(records):
    new_records = []

    for record in records:
        i = 0
        pre_price = price_calculated(record['start'], record['end'])

        for new_record in new_records:

            if new_record['source'] == record['source']:
                i = 1
                price_one = new_record['total']
                pricefinal = round((pre_price + price_one), 2)
                new_record['total'] = pricefinal

        if i == 0:
            price = round(pre_price,2)
            new_records.append(
                {'source': record['source'], 'total': price})
                
    final_records = sorted(
        new_records, key=lambda i: i['total'], reverse=True)
    return final_records