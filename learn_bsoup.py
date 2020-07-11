import requests

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

page = requests.get("https://www.amazon.com/Modern-Robotics-Mechanics-Planning-Control/dp/1107156300")
soup = BeautifulSoup(page.text, 'lxml')

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


# Using .contents and .children (tech-savvy approach)
#---------------------------------------------
# A tag’s children are available in a list called .contents

#p[class='story'], all it's immediate children (not descendants) are in .contents list as tags

#it simply means .contents 

print(soup.p.contents)


#---------------------------------------------

#Instead of getting them as a list, you can iterate over a tag’s children using the .children generator:

for item in soup.p.children:
	print(item)

#---------------------------------------------

#The .descendants attribute lets you iterate over all of a tag’s children(as element), recursively: its direct children + the children of its direct children, and so on:

print('.descendants')

for e in soup.p.descendants:
	print(e)

#---------------------------------------------

# .string,   If a tag has only one child, and that child is a NavigableString, the child is made available as .string:

# print(title_tag.string)


###------------------------------------------------------ Super useful stuff --------------

#.strings and stripped_strings

# If there’s more than one thing (usually lot of whitespaces) inside a tag, you can still look at just the strings. Use the .strings generator:

for s in soup.strings:
	print(repr(s))


# for example:

"""
The Dormouse's story"
'\n'
'\n'
"The Dormouse's story"
'\n'
'Once upon a time there were three little sisters; and their names were\n'
'Elsie'
',\n'
'Lacie'
' and\n'
'Tillie'
';\nand they lived at the bottom of a well.'
'\n'
'Rating'
'\n'
"""

#These strings tend to have a lot of extra whitespace, which you can remove by using the .stripped_strings generator instead:


for s in soup.stripped_strings:
	print(s)



#--------------------------Let's move inside a document structure from top, bottom and sideways


#Go up
#----------------------- .parent ----------

print("------------- 1 -----------")

#Continuing the “family tree” analogy, every tag and every string has a parent: the tag that contains it.

title_tag = soup.title

print(title_tag.parent)

# Here, string inside title_tag also has it's parent tag as <title>

print(title_tag.string.parent)


# The parent of a top-level tag like <html> is the BeautifulSoup object itself:

# html_tag = soup.html
# type(html_tag.parent)
# # <class 'bs4.BeautifulSoup'>
# And the .parent of a BeautifulSoup object is defined as None:

# print(soup.parent)
# # None

#--------------------------------  .parents

link = soup.a

for parent in link.parents:
	print(link)
	# print(link.name)



# Going sideways
#-------------------------------

newsoup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'lxml')

print(newsoup.prettify())


#The <b> tag and the <c> are siblings as both are at the same level


#------------------------------- .next_sibling and .previous_sibling

print(newsoup.b.next_sibling)
print(newsoup.b.previous_sibling) # -> Will return None as there is no previous sibling of <b>


print(newsoup.c.previous_sibling)
print(newsoup.c.next_sibling) # -> Will return None as there is no next sibling of <c>


# NOTE:  In real documents, the .next_sibling or .previous_sibling of a tag will usually be a string containing whitespace(that separate tags)

# in soup old one, the previous and next siblings of  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a> 
# is the comma and newline that separate the first <a> tag from the second:

# print(soup.prettify())

link = soup.find('a', {'class':'sister'})

print(repr(link.next_sibling)) # --> will return ',\n'

# the second a tag is actually the .next_sibling of ','(comma)


# So, if you actually need to reach the second sibling, then: .next_sibling.next_sibling.next_sibling...and so on.

print(link.next_sibling.next_sibling)

# ----------------------------------------------------- .next_siblings and .previous_siblings

# or a more tech-savvy approach is Using .next_siblings and .previous_siblings to iterate over all the tag's siblings.

for sibling in link.next_siblings:
	print(sibling)

for sibling in link.previous_siblings:
	print(sibling)


# Very useful in some cases (in the goodread book's description example)
# Going back and forth (from parser point of view, sequence of tags and it's contents) 
# ----------------------------------------------------- .next_element(s) and .previous_element(s)

# An HTML parser takes this string of characters and turns it into a series of events: “open an <html> tag”, “open a <head> tag”, “open a <title> tag”, “add a string”, “close the <title> tag”, “open a <p> tag”, and so on. 
# Beautiful Soup offers tools for reconstructing the initial parse of the document.

# for eg:

# <a href=''>Hello world</a><p>This is a beautiful planet</p>

# .next_sibling of <a> is <p> but .next_element of <a> is 'Hello world' string

# this is how parser intepreted the document

print(link.next_element)

# ----------- .next_elements and .previous_elements

for t in link.next_elements:
	print(t)

#************************************************** Searching a tree using find() and find_all()

#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree
















