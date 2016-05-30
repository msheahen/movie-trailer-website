#To Run: make sure python is installedin your computer
# run 'python generate_movies.py

import media
import fresh_tomatoes


# initialize our movie data and put into the movies list
movie1=media.Movie(
	"Jumanji",
	"The Jungle comes to America",
	"http://dvdmedia.ign.com/dvd/image/object/771/771856/jumanjiboxart_160w.jpg",
    "https://www.youtube.com/watch?v=8WaAUE4MXs8")

movie2=media.Movie(
	"Big",
	"Have you ever had a really big secret?",
	"http://ecx.images-amazon.com/images/I/513YB9TBQRL._SY445_.jpg",
	"https://www.youtube.com/watch?v=J62jciQ1PbY")
                   
movie3=media.Movie(
	"Rocky",
	"The fighter who keeps on fighting",
	"https://lh3.googleusercontent.com/cbTaiSimzpHfNA_WiDoAhtpAqNeFgCjq8lN3ongcMtJxLCSIoxW5DcBDw5X87hP5I2bi=w300",
	"https://www.youtube.com/watch?v=3VUblDwa648")

movie4=media.Movie(
	"Goonies",
	"friends get themselves into shenanigans",
	"https://jasonvorhees.files.wordpress.com/2012/06/the-goonies-movie-cover.jpg",
	"https://www.youtube.com/watch?v=hJ2j4oWdQtU")

movie5=media.Movie(
	"Never Ending Story",
	"Was it real or imagined?",    
	"http://www.bluraywire.com/wp-content/uploads/2009/12/theneverendingstorybluraypg.jpg",
	"https://www.youtube.com/watch?v=UeFni9dOv7c")

movie6=media.Movie(
	"Willy Wonka and the Chocolate Factory",
	"A creepy chocolatier causes trouble",               
	"https://lh4.ggpht.com/8g-ABwLRirI4X0eI1EOXW_mqk5BWtQk7d-JHOBIKJJoaDBKBTFtk5VRIC8MEnuYW6Eo=w300",
	"https://www.youtube.com/watch?v=2cBja3AbahY")

movies=[movie1,movie2,movie3,movie4,movie5,movie6]

# generate the html page!
fresh_tomatoes.open_movies_page(movies)