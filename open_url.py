import webbrowser, time

number1 = 1
number2 = 2
url_list = ["www.youtube.com", "www.amazon.com", "www.google.com"]


def add_number(num1, num2):
    return num1+num2


def open_url(list_of_urls):
    for url in list_of_urls:
        webbrowser.open_new_tab(url)
        time.sleep(2)


def main():
    print(add_number(number1, number2))
    webbrowser.open("www.amazon.com", new=0, autoraise=False)
    open_url(url_list)


main()
