dict1 = {
    'star': 
         {
            "tino": {
                "age": 20,
                "height": '180cm',
                "weight": '75kg'
            },
            "nice": {
                "age": 22,
                "height": '172cm',
                "weight": '73kg'
            },
            "tomas": {
                "age": 24,
                "height": '170cm'
            },
         }
    }

dict1['star']['tomas']['weight'] = '70kg'

del dict1['star']['nice']

dict1['star']['tino']['age'] = '22'

print(dict1)