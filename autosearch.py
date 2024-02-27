import webbrowser 
import sys

def search_terms():
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
    else:
        query = input("Enter search query: ")

    webbrowser.open_new_tab('https://www.google.com/search?q=' + query)

if __name__ == '__main__':
    ###
    search_terms()