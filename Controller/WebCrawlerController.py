from Business.Page.PageBusinessController import PageBusinessController


def main():
    pageBusCtrl = PageBusinessController()
    page_info = pageBusCtrl.Select()


if __name__ == "__main__":
    main()