import create_map
import locations
from flask import Flask, render_template, request


app=Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/create_map')
def map_generation():
    # print(request.args.get('name'))
    create_map.create_map(locations.get_friends_locations(request.args.get('name'), request.args.get('number')))
    return render_template('Map.html')
