months = {
    "January": '01', "February": '02', "March": '03', "April": '04', "May": '05', "June": '06', "July": '07', "August": '08',
    "September": '09', "October": '10',  "November": '11', "December": '12'
    }


def main():
    right_date = convert()
    print(right_date)


def convert():
    while True:
        users_year = input('Date: ')
        try:
            month, day, year = users_year.split('/')
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
        except:
            try:
                month, day, year = users_year.split(' ')
                if month in months and 1 and day[-1] == ',':
                    month = months[month]
                    day = day.replace(',', '')
                    if 1 <= int(day) <= 31:
                        break
            except:
                pass


    final_date = f'{int(year)}-{int(month):02}-{int(day):02}'
    return final_date


main()
