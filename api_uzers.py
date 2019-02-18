import tweepy
import geocoder
import folium


def authorization(user_name, number_fol):
    """
    This function make the autorization for twitter api and get the information about user friends
    """
    auth = tweepy.OAuthHandler('yq4RZKHGXQnohK7veKupRWU8J', 'McpwlC3pRRUP5mZnEIZtTokAUTWXKWwrKHXgZ7u3fs24nyoMDp')
    auth.set_access_token('2337068480-DIXBN7WvscmmmW7nV0fwANxK7nevWFYbpHQzGYx',
    'yqI3dLTSSwknDXsVOTNqlzDktT8VcuW0LzBrgr7M92Iss')
    api = tweepy.API(auth)
    user = api.get_user(user_name)
    user_inf = dict()
    for friend in user.friends(count=number_fol):
        if friend.location:
            user_inf[str(friend.name)] = geocoder.arcgis(friend.location).latlng
    return user_inf


def map(dict_coord):
    """
    This function makes an html file(map) with markeres as followers of the user
    """
    tweeter_map = folium.Map(zoom_start = 3)
    for loc in dict_coord:
        tweeter_map.add_child(folium.Marker(location=dict_coord[loc], popup=loc, icon=folium.Icon()))
    return tweeter_map.get_root().render()


if __name__ == "__main__":
    user = input("Please, enter the name of the user\n")
    number = int(input("Please enter the number of followers\n"))
    map(authorization(user, number))

