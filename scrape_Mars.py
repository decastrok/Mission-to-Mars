from splinter import Browser
from bs4 import BeautifulSoup


def init_browswer():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    article = soup.find("div", class_='list_text').get_text()
    newsTitle = article.find("div", class_="content_title").get_text()
    newsParagraph = article.find(
        "div", class_="article_teaser_body").get_text()
    print(newsTitle)
    print(newsParagraph)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image_url = soup.find('article')['style'].replace(
        'background-image: url(', '').replace(');', '')[1:-1]
    main_url = 'https://www.jpl.nasa.gov'
    featured_image_url = main_url + featured_image_url
    featured_image_url

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find_all('div', class_='js-tweet-text-container')
    for tweet in mars_weather:
        weather_tweet = tweet.find('p').text
        if 'winds' and 'pressure' in weather_tweet:
            print(weather_tweet)
            break
        else:
            pass

    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    tables

    type(tables)

    mars_facts = tables[0]
    mars_facts.head()
    mars_facts.set_index('Mars - Earth Comparison', inplace=True)
    mars_facts.head()

    mars_facts_html = mars_facts.to_html()
    mars_facts_html
    mars_facts_html.replace('\n', '')

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images = soup.find_all("div", class_='item')
    images_urls = []
    main_url = 'https://astrogeology.usgs.gov'

    for i in images:
        title = i.find('h3').text
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
        browser.visit(main_url + partial_img_url)
        partial_img_html = browser.html
        soup = BeautifulSoup(partial_img_html, 'html.parser')
        img_urls = main_url + soup.find('img', class_='wide-image')['src']
        images_urls.append({"title": title, "img_url": img_urls})
    images_urls
    browser.quit()
    return
