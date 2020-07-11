from .api import Api
import argparse
import os


parser = argparse.ArgumentParser("nhk-easy")
parser.add_argument(
    "-M",
    "--mp3",
    help="Download mp3 audio instead of m3u8 playlist (ffmpeg required)",
    action="store_true",
)
parser.add_argument("-d", "--directory", help="output directory")
parser.add_argument(
    "-F", "--furigana", action="store_true", help="enable furigana",
)
parser.add_argument(
    "-H", "--html", action="store_true", help="HTML output (default is txt)"
)
args = parser.parse_args()


def main():
    if args.directory:
        os.chdir(args.directory)
    api = Api()
    api.download_top_news(args.furigana, args.html, args.mp3)


if __name__ == "__main__":
    main()
