from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)



@app.route("/",methods=['GET','POST'])
def index():
	data=[{'gen':'action'},{'gen':'romance'},{'gen':'sci-fi'},{'gen':'superhero'},{'gen':'mystery'},{'gen':'comedy'},{'gen':'horror'},{'gen':'thriller'},{'gen':'adventure'},{'gen':'fantasy'},{'gen':'animation'},{'gen':'crime'},{'gen':'drama'}]
	language=[{'lang':'English'},{'lang':'Hindi'},{'lang':'Telugu'},{'lang':'Tamil'}]
	return(render_template('open.html',data=data,language=language))


@app.route("/res",methods=['GET','POST'])	
def scrape():
	genre=request.form.get('genre') #get genre from user
	language=request.form.get('language') #get language from user
	language1=language
	if(language=='English'):
		language='en'
	elif(language=='Hindi'):
		language='hi'
	elif(language=='Telugu'):
		language='te'
	else:
		language='ta'
		
	#url as per the selection of genre and language from the user
	url="https://www.imdb.com/search/title?title_type=feature&genres="+genre+"&languages="+language+"&sort=user_rating,desc"
	response=requests.get(url)# response stored in variable response
	soup=BeautifulSoup(response.text, 'lxml')
	x=soup.find_all('div',class_="lister-item mode-advanced") #for each and every movie parent tag is <div>
	final_result=[]#empty list to store result
	for res in x[:5]:
		final_result+=[res.h3.a.get_text()] #movie name from the result is in anchor tag
		
	return(render_template('res.html',result=final_result,genre=genre,language=language1))#displaying first 5 movies of the selected genre and language based on user rating

if(__name__=="__main__"):
	app.run(debug=True)#debug to backtrack and check in case of errors