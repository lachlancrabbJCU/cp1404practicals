"""Search Wikipedia page from users prompt and returns details about page."""

import wikipedia


def main():
    """Gets Wiki page title from user and displays page info."""
    page_title = input("Enter page title: ")

    while page_title != "":
        try:
            page = wikipedia.page(page_title, auto_suggest=False)
            is_valid_page = True
        except wikipedia.exceptions.DisambiguationError as disambiguation_error:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(disambiguation_error)
        except wikipedia.exceptions.PageError as page_error:
            print(f'Page id "{page_title}" does not match any pages. Try another id!')
        print(page.title)
        print(page.summary)
        print(page.url)
        print()
        page_title = input("Enter page title: ")
    print("Thank you.")




if __name__ == '__main__':
    main()
