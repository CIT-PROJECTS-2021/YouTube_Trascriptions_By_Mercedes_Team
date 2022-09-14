
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


def get_transcript():
    video_id = get_video_id()
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except VideoUnavailable:
        return f"Video is unavailable."
    except TooManyRequests:
        return f"Too many requests. Please try again after some time."
    except TranscriptsDisabled:
        return f"TranscriptsDisabled: Transcripts are disabled for this video."
    except NoTranscriptAvailable:
        return f"NoTranscriptAvailable: No transcript available for this video."
    except NoTranscriptFound:
        return f"NoTranscriptFound: No transcript found for this video."
    except Exception as e:
        print(e)
        return f"Unknown Error Occurred. Please try again after some time."
