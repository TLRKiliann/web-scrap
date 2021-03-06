#!/usr/bin/python3
# -*- encoding:Utf-8 -*-


import matplotlib.pyplot as plt


list_date = ['01', '02', '03',
'04', '05', '06', '07',
'08', '09', '10', '11',
'12', '13', '14', '15',
'16', '17', '18', '19',
'20', '21', '22', '23',
'24', '25', '26', '27',
'28', '29', '30', '31']

list_2011 = [3,2,5,5,3,3,6,8,8,9,11,9,11,12,13,11,7,9,8,7,7,10,12,15,15,13,12,11,13,11,9]

list_2016 = [6,6,3,5,4,2,2,1,3,4,4,4,5,5,8,5,9,10,10,10,9,8,7,9,7,11,7,11,12,15,16]

list_2020 = [10,5,5,7,7,7,6,8,6,5,14,15,10,9,11,13,15,16,16,14,13,9,7,7,6,8,10,12,9,4,8]

show_grid = True
with plt.style.context('seaborn-darkgrid'):
    plt.plot(list_date, list_2011, 'co--')
    plt.plot(list_date, list_2016, 'bo--')
    plt.plot(list_date, list_2020, 'ro-')
    plt.ylabel('Temperatures (°C)', fontsize=14)
    plt.xlabel('Days', fontsize=14)
    plt.xticks(rotation=45)
    plt.title('Temperatures for March 2011-2016-2020 (after-noon)',
        fontsize=16)
    plt.legend(['temp 2011', 'temp 2016', 'temp 2020'])
    plt.grid(show_grid)

    plt.show()