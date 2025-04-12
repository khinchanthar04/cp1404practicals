import warnings

import wikipedia
from bs4 import GuessedAtParserWarning

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)
def main():
    """Prompt the user to input Wikipedia page titles and display the page's title, summary, and URL."""

    title = input("Input the page title: ")
    while title:
        if not title:
            print("Thank you.")
            break

        try:
            searched_page = wikipedia.page(title)
            print(f"Title: {searched_page.title}")
            print(f"Summary: {searched_page.summary}")
            print(f"URL: {searched_page.url}")
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"Page '{title}' does not match any pages. Try another id!")
        except Exception as unknown_error:
            print(f"An unexpected error occurred: {unknown_error}")
        title = input("Input the page title: ")


if __name__ == '__main__':
    main()