
"""
youtube transcript summarizer 
"""
import sys
import argparse
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound , NoTranscriptAvailable, \
    TranscriptsDisabled ,VideoUnavailable , TooManyRequests
    
from youtube_transcript_api.formatters import TextFormatter
import pytube     
import sumy 
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.tokenizers import Tokenizer

# Usage function 

    

# arguments to be passed in the command line 
def get_parser():
    parser = argparse.ArgumentParser(description='Youtube Transcript Summarizer')
    parser.add_argument('-i', '--input', type=str, help='Youtube video link')
    return parser


# get the transcript of the video
def get_video_id():
    print("Getting video id from youtube link ........")
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
    print("Getting transcript...")
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
    
def main():
    transcript = get_transcript()
    # get the text from the transcript
    formatter = TextFormatter()
    text = formatter.format_transcript(transcript).strip()
    # summarize the text using sumy library algorithm used is LexRankSummarizer
    summarize = LexRankSummarizer()
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summary = summarize(parser.document, 3)
    print("Summarising text...")
    for sentence in summary:
        # write the summary to a file
        with open("summary.txt", "w") as f:
            f.write(str(sentence))
    print("Thank you for using our application , your summary is saved in summary.txt")
    
if __name__ == "__main__":
    main()
    
# https://www.youtube.com/watch?v=a5xs8_YBmPo 
    #  https://www.youtube.com/watch?v=__oCUzwL7i0
    #  https://www.youtube.com/watch?v=J_SQoOjv8aM
    # https://www.youtube.com/watch?v=WcIcVapfqXw 