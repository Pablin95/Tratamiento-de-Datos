from bs4 import BeautifulSoup
import requests
import schedule



def bot_send_text(bot_message):
    bot_token = 'bot5400299704:AAFDm3QkSdd86zZlfWx0xSY_yeZDgyRjX6'
    bot_chatID = '873567754'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def btc_scraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'text-larger text-price'})
    format_result = result.text

    return format_result

def report():
    btc_price = f'El precio de Bitcoin es de {btc_scraping()}'
    bot_send_text(btc_price)


if __name__ == '__main__':

    schedule.every().day.at("23:31").do(report)

    """while True:
        schedule.run_pending()"""
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
