import spotipy
import spotipy.util as util
# import spotipy.util i

token = util.prompt_for_user_token("onfld0wcw4jmrobqasq9gl0xj","user-library-read",client_id='e5dc70c1a984472f888c93032327a9f5',client_secret='22c2782e5e7f45c6898dcb8bb34a4ee0',redirect_uri='localhost')

spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + "Malone", type='artist')
print results

# import spotipy
# import sys

# spotify = spotipy.Spotify()

# if len(sys.argv) > 1:
#     name = ' '.join(sys.argv[1:])
# else:
#     name = 'Radiohead'

# results = spotify.search(q='artist:' + name, type='artist')
# items = results['artists']['items']
# if len(items) > 0:
#     artist = items[0]
#     print artist['name'], artist['images'][0]['url']