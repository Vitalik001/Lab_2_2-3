'''
map.py
'''
import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster
import locations

def get_coordinates(place):
    '''
    returns coordinates of place
    >>> get_coordinates('Lviv, Ukraine')
    (49.841952, 24.0315921)
    '''
    plc=place
    if not place:
        return None
    try:
        geolocator = Nominatim(user_agent="my_request")
        location = geolocator.geocode(place)
        second_point=(location.latitude, location.longitude)
        return second_point
    except AttributeError:
        return get_coordinates(','.join(plc.split(',')[1:]))


def create_map(friends):
    '''
    creates the map with markers of films
    '''
    mapp=folium.Map()
    # print(friends)
    group=folium.FeatureGroup(name='Friends')
    mapp.add_child(group)
    marker_cluster = MarkerCluster().add_to(group)
    for friend in friends:
        name=friend[0]
        location=get_coordinates(friend[1])
        if not location:
            continue
        folium.Marker(location=location, popup=name+', '+friend[1],\
 icon=folium.Icon(color='darkblue', icon_color='white', icon='male',\
 angle=0, prefix='fa')).add_to(marker_cluster)
    folium.TileLayer('cartodbdark_matter').add_to(mapp)
    folium.TileLayer('Stamen Terrain').add_to(mapp)
    mapp.add_child(folium.LayerControl())
    mapp.save('templates/Map.html')
if __name__=='__main__':
    create_map(locations.get_friends_locations('elon'))
