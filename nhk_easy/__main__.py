from .api import Api
import argparse
import os


parser = argparse.ArgumentParser("Download today's NHK easy news")
parser.add_argument(
    "-m",
    "--mp3",
    help="Download mp3 audio instead of m3u8 playlist (ffmpeg required)",
    action="store_true",
)
parser.add_argument("-d", "--directory", help="directory")
args = parser.parse_args()


def main():

    if args.directory:
        os.chdir(args.directory)
    api = Api()
    if args.mp3:
        api.download_top_news(m3u8=False, mp3=True)
    else:
        api.download_top_news()


if __name__ == "__main__":
    main()
