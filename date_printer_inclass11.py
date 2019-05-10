def main():
    user_date = get_user_date()
    split_user_date(user_date)

def get_user_date():
    print('Enter a date in mm/dd/yyyy: ')
    user_date = input('Enter date: ')

    return user_date

def split_user_date(user_date):
    date_list = user_date.split('/')
    month_index = (int(date_list[0])) - 1
    list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    user_month = list_of_months[month_index]

    print(user_month,' ', date_list[1],',', date_list[2], sep='')

    print(date_list[0], date_list[1], date_list[2])

    print(date_list[0])
    print(date_list[1])
    print(date_list[2])

main()
