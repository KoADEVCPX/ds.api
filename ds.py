from yt_dlp import YoutubeDL
from flask import Flask, jsonify, request
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('Oasis Wonderwall', limit = 2)

app = Flask(__name__)

options = {
    'format': 'mp3/bestaudio/best',
    'keepvideo': False,
    'outtmpl': 'teste.mp3'
}

@app.route('/DreamScripts/getYoutubeMusic/<string:search>', methods=['GET'])
def getYoutubeMusic(search):
    if search:
        videosSearch = VideosSearch(search, limit = 2)
        with YoutubeDL(options) as ydl:
            infos = ydl.extract_info(
                url = videosSearch.result()['result'][0]['link']
            )
            data = {
                'name': infos['title'],
                'url': infos['url'],
                'thumbnail': videosSearch.result()['result'][0]['thumbnails'][0],
            }
            return jsonify(data)

app.run(host='0.0.0.0', debug=True)
