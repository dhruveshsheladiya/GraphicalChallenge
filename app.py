import os
import glob
import random
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import csv
import sqlite3 as lite
import requests
import threading
import sys
import xUtilities
sys.path.insert(0, 'pythonFiles/')
app = Flask(__name__)

@app.route('/Jan1/', methods=['GET'])
def Jan1():
	import Jan1
	return render_template("Jan1.html", DATABASE=Jan1.genDatabase(), BUSNUM="4012715")
#This is template for all sites

@app.route('/Jan2/', methods=['GET'])
def Jan2():
	import Jan2
	return render_template("Jan2.html", DATABASE=Jan2.returnDatabase())
#This is template for all sites

@app.route('/Jan3', methods=['GET'])
@app.route('/Jan3/<stock>', methods=['GET'])
def Jan3(stock="TSLA"):
	import Jan3
	return render_template("Jan3.html", DATABASE=Jan3.returnData(stock))
#This is template for all sites

@app.route('/Jan4/', methods=['GET'])
def Jan4():
	import Jan4
	return render_template("Jan4.html", DATABASE=Jan4.getDatabase())
#This is template for all sites

@app.route('/Jan5/', methods=['GET'])
def Jan5():
	import Jan5
	return render_template("Jan5.html", DATABASE=Jan5.getDatabase())
#This is template for all sites

@app.route('/Jan6/', methods=['GET'])
def Jan6():
	import Jan6
	belowAveragePrice, aboveAveragePrice = Jan6.getDatabase()
	return render_template("Jan6.html", belowAveragePrice=belowAveragePrice, aboveAveragePrice=aboveAveragePrice)
#This is template for all sites

@app.route('/Jan7/', methods=['GET'])
def Jan7():
	return render_template("Jan7.html")
#This is template for all sites

@app.route('/Jan8/', methods=['GET'])
def Jan8():
	import Jan8
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan8.html", DATABASE=Jan8.getDatabase())
#This is template for all sites

@app.route('/Jan9/', methods=['GET'])
def Jan9():
	import Jan9
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	DATABASE = Jan9.getDatabase()
	return render_template("Jan9.html", DATABASE=DATABASE, DATA=range(1,len(DATABASE) / 4))
#This is template for all sites

@app.route('/Jan10/', methods=['GET'])
def Jan10():
	import Jan10
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan10.html", DATABASE=Jan10.getDatabase())
#This is template for all sites

@app.route('/Jan11/', methods=['GET'])
def Jan11():
	import Jan11
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan11.html", DATABASE=Jan11.getDatabase())
#This is template for all sites

@app.route('/Jan12/', methods=['GET'])
def Jan12():
	import Jan12
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan12.html", DATABASE=Jan12.getDatabase())
#This is template for all sites

@app.route('/Jan13/', methods=['GET'])
def Jan13():
	import Jan13
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan13.html", DATABASE=Jan13.getDatabase())
#This is template for all sites

@app.route('/Jan14/', methods=['GET'])
def Jan14():
	import Jan14
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan14.html", DATABASE=Jan14.getDatabase())
#This is template for all sites

@app.route('/Jan15/', methods=['GET'])
def Jan15():
	import Jan15
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	#if 
	DATABASE = Jan15.getDatabase()
	return render_template("Jan15.html", WSB=DATABASE['WSB'], ALL=DATABASE['ALL'])
#This is template for all sites

@app.route('/Jan16/', methods=['GET'])
def Jan16():
	date = sys._getframe().f_code.co_name
	if xUtilities.checkForScreenshot(date) == False:
		threading.Thread(target=xUtilities.saveScreenshot, args=(date,)).start()
		return "Getting Screenshot"
	return render_template("Jan16.html")

@app.route('/Jan17/', methods=['GET'])
def Jan17():
	import Jan17
	DATABASE=Jan17.getDatabase()
	for data in DATABASE:
		if data['Nootropics']["Sentiment"] == 0 or data['StackAdvice']["Sentiment"] == 0:
			DATABASE.remove(data)
	DATABASE = sorted(DATABASE, key=lambda k: k['Nootropics']['Occurances'])
	return render_template("Jan17.html", DATABASE=DATABASE[::-1][:15])

@app.route('/Jan18/', methods=['GET'])
def Jan18():
	import Jan17
	DATABASE=Jan17.getDatabase()
	for data in DATABASE:
		if data['Nootropics']["Sentiment"] == 0 or data['StackAdvice']["Sentiment"] == 0:
			DATABASE.remove(data)
	DATABASE = sorted(DATABASE, key=lambda k: k['Nootropics']['Occurances'])
	return render_template("Jan18.html", DATABASE=DATABASE[::-1][:10])

@app.route('/Jan19/', methods=['GET'])
def Jan19():
	import Jan17
	DATABASE=Jan17.getDatabase()
	for data in DATABASE:
		if data['Nootropics']["Sentiment"] == 0 or data['StackAdvice']["Sentiment"] == 0:
			DATABASE.remove(data)
	DATABASE = sorted(DATABASE, key=lambda k: k['StackAdvice']['Occurances'])
	return render_template("Jan19.html", DATABASE=DATABASE[::-1][:10])

@app.route('/Jan20/', methods=['GET'])
def Jan20():
	import Jan17
	DATABASE=Jan17.getDatabase()
	for data in DATABASE:
		if data['Nootropics']["Sentiment"] == 0 or data['StackAdvice']["Sentiment"] == 0:
			DATABASE.remove(data)
	for data in DATABASE:
		data['TotalOccurances'] = data['StackAdvice']['Occurances'] + data['Nootropics']['Occurances']
		data['ColorVal'] = {"Name": xUtilities.random_char(5), "Color": xUtilities.genColor()}
	DATABASE = sorted(DATABASE, key=lambda k: k['TotalOccurances'])
	return render_template("Jan20.html", DATABASE=DATABASE[::-1][:30])

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5000)