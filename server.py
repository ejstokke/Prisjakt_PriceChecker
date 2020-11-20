from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import re


app = Flask(__name__)
CORS(app)


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/price/<product_code>")
def get_price(product_code):
    try:
        URL = f"https://www.google.com/search?q={'prisjakt_' + product_code}&num=10"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content)

        links = soup.findAll('a')

        for link in links:
            
            link_href = link.get('href')

            if isinstance(link_href, str) and 'www.prisjakt.no' in link_href and not "webcache" in link_href:
                product_url = link_href

        product_page = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(product_page.content)
        tab = soup.find("a", { "data-test" : 'TabButton' })
        price = tab.findAll('div')

        product_title = soup.find("h1", { "data-test" : 'ProductTitle' })
        img_location = soup.find("div", { "class" : 'product-media-first-image' })
        img_src = img_location.find('img').get('src')

        product_data = {
            'price': price[1].contents,
            'title': product_title.contents,
            'img_src': img_src,
            'url': product_url,
        }

        return jsonify(product_data)
    except:
        return 'Product not found...', 404


if __name__ == '__main__':
    app.run(debug=True)