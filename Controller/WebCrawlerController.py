from Business.Page.PageBusinessController import PageBusinessController


def main():
    pageBusCtrl = PageBusinessController()
    page_info = pageBusCtrl.Select(1)


if __name__ == "__main__":
    main()