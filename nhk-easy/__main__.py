from .api import Api


def main():
    api = Api()
    api.download_top_news()


if __name__ == "__main__":
    main()
