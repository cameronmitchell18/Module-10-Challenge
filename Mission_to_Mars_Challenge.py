# %%
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# %%
executable_path = {'executable_path': ChromeDriverManager().install()}

browser = Browser('chrome', **executable_path, headless=False)

# %%
url = 'https://redplanetscience.com/'

browser.visit(url)

# Optional delay for loading the page 

# NOTE: The optional delay is useful because sometimes dynamic pages take a little while to load, 
# especially if they are image-heavy.

browser.is_element_present_by_css('div.list_test' , wait_time = 1)

# %%
html = browser.html

news_soup = soup(html , 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

# slide_elem as the variable to look for the <div /> tag and its descendent. This is our parent element.

# 'div.list_text' pinpoints the <div /> tag with the class of list_text.


# %%
slide_elem.find('div' , class_ = 'content_title')

# we chained .find onto our previously assigned variable, slide_elem.
# When we do this, we're saying, "This variable holds a ton of information, 
# so look inside of that information to find this specific data."

# %%
# Use the parent element to find the first `a` tag and save it as `news_title`

news_title = slide_elem.find('div', class_='content_title').get_text()

news_title

# .get_text(). When this new method is chained onto .find(), only the text of the element is returned. 

# %%
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# %% [markdown]
# ### Featured Images

# %%
# Visit URL

url = 'https://spaceimages-mars.com'

browser.visit(url)

# %%
# Find and click the full image button

full_image_elem = browser.find_by_tag('button')[1]

full_image_elem.click()

# %%
# Parse the resulting html with soup

html = browser.html

img_soup = soup(html, 'html.parser')

# %%
# Find the relative image url

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

img_url_rel

# NOTE: .get('src') pulls the link to the image.

# %%
# Use the base URL to create an absolute URL

img_url = f'https://spaceimages-mars.com/{img_url_rel}'

img_url

# %%
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# %%
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df.to_html()

# %%
browser.quit()

# %%
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# %%
# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %% [markdown]
# ### Visit the NASA Mars News Site
# 

# %%
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# %%
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# %%
slide_elem.find('div', class_='content_title')


# %%
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# %%
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# %% [markdown]
# ### JPL Space Images Featured Image
# 

# %%
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# %%
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# %%
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# %%
# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# %%
# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# %% [markdown]
# ### Mars Facts

# %%
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

# %%
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

# %%
df.to_html()

# %% [markdown]
# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# %% [markdown]
# ### Hemispheres

# %%
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# %%
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):

    hemispheres = {}

    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.find_link_by_text('Sample').first

    img_url = element['href']
    title = browser.find_by_css("h2.title").text

    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()

# %%
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# %%
# 5. Quit the browser
browser.quit()


