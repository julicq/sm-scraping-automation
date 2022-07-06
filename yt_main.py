from youtube_stats import YTstats
  
API_KEY = "<key>"
channel_id = "<id>" 
  
yt = YTstats(API_KEY, channel_id)
# yt.get_channel_stats()
# yt.dump()
yt.extract_all()
yt.dump()
