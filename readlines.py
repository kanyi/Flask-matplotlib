from datetime import datetime

"""
Nem teljes kudarc. Egyes elemek használhatóak.
Ha valahogy sikerül egy qrva tuple-t generálnom a beolvasott fájlból akkor jó lesz.
OK, fut. Csak nem kell semmi flancolás, ahogy bejön úgy add tovább.
"""

def read_data(filename):
    infile = open(filename, 'r')
    data = []
    for line in infile:
        column = line.split()
        date = column[0] + " " + column[1]
        timestamp = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f") #'2020-03-19 00:45'
        timestamp_str = str('{:%Y-%m-%d %H:%M}'.format(timestamp))
        temp = column[2]
        temp = round(float(temp), 2)
        pressure = column[3]
        pressure = round(float(pressure), 2)
        humidity = column[4]
        humidity = round(float(humidity), 2)
        #tdata = tuple(['{}, {:.2f}, {:.2f}, {:.2f}'.format(timestamp_str, temp, pressure, humidity)])
        tdata = (date, column[2], column[3], column[4])
        data.append(tdata)
    infile.close()
    return data

if __name__ == '__main__':
    wtf = read_data('weather_BME280_sensor_data.txt')
    print(wtf)