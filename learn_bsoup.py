html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b><a class='' id=''>The Dormouse's story</a></b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<span itemprop="ratingValue ratingStar">Rating</span>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')

# print(soup.prettify())

#---------------------------------------------------------BASIC TASKS--------------------------------------------------


#to get the entire tag
print(soup.title)

#to get the tag name
print(soup.title.name)

print()

#to get the parent full tag with its content
print(soup.title.parent)



#to get the attribute value of a tag
print(soup.a['id'])
print(soup.a['class'])

#Note, this will only return the first matching tag, if you want tags matching criteria present in soup, then use find_all()
links = soup.find_all('a') # this will return the list of bs4.element.Tag
for a in links:
	# print(type(a))
	print(a.get_text())


#above example is also very common task is to extract all links in the page

#To extract all text from page
print(soup.get_text())


#To get all attributes of a tag as dictionary
print(soup.a.attrs)

# Since it is a dictionary, You can also add, remove or modify the attribute.
# soup.a['class'] = 'sister_a'
# print(soup.a.attrs)

#There are multivalued attributes in HTML such as 'class', 'rel', 'headers', etc.
# For.eg. class="container container_box"
#Beautiful Soup presents the value(s) of a multi-valued attribute as a list

print(soup.a['class']) # a list will returned having class values

#Some attributes have multiple values, though it may not be a multi-valued attribute
# E.g: itemprop="ratingValue ratingStar" (here itemprop is not a multi-valued but having multiple values)

print(soup.span['itemprop']) #will not be returned as list

#You can use `get_attribute_list to get a value that’s always a list, whether or not it’s a multi-valued atribute
print(soup.span.get_attribute_list('itemprop'))

#To get the text from the tag
print(soup.a.string)


#-----------------------------------------------NAVIGATING TREE(important)------------------------------------

#Navitaging using tag names(clumsy)

#For.eg. soup.parent.child.child.child and so on
#You can do use this trick again and again to zoom in on a certain part of the parse tree.
print(soup.body.b)


# Using .contents and .children (tech-savvy)
#---------------------------------------------
# A tag’s children are available in a list called .contents

#p[class='story'], all it's children (with descendants) are in .contents list

print(soup.p.contents)

#---------------------------------------------

#The .descendants attribute lets you iterate over all of a tag’s children(as element), recursively: its direct children, the children of its direct children, and so on:

for e in soup.p.descendants:
	print(e)







