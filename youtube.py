
"""
youtube transcript summarizer 
"""
import sys
import argparse
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound , NoTranscriptAvailable, \
    TranscriptsDisabled ,VideoUnavailable , TooManyRequests
    
from youtube_trancript_api.formatters import TextFormatter
import pytube     

# Usage function 

    

# arguments to be passed in the command line 



# get the transcript of the video
def get_video_id():
    parser = get_parser()
    args = parser.parse_args()
    if args is None:
        Usage()
        sys.exit(1)
    else:
        video = pytube.YouTube(args.i)
        video_id = video.video_id
        return video_id

