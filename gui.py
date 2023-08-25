import sys
import tkinter as tk
import json
import M3Search
import pandas as pd
import time


# def search():
#     print("_+_+_+_+_+_Please wait until the search engine has warmed up..._+_+_+_+_+_")
#     ioi = open('index_of_index.json', 'r')
#     index_of_index = json.load(ioi)
#     df = pd.read_csv('invertedindex.csv')
#     N = df.iloc[-1][1]
#     print("_+_+_+_+_+_!!Search Engine Ready!!_+_+_+_+_+_")
#     while True:
#         query = entry.get()
#         results_text.insert(tk.END, "Searching for: " + query + "\n")
#         results = M3Search.search_engine(query, index_of_index, N)
#         if results == "":
#             quit()
#         results_text.insert(tk.END, results + "\n")
#         results_text.delete('1.0', tk.END)
#         entry.delete('0', tk.END)
#         search_button.update()
#         window.update()
#         # time.sleep(5)
#         # query = entry.get()
#         # print(f'the query is {query}')
#         # sys.exit()
#
# window = tk.Tk()
# window.title("Search Engine")
#
# entry = tk.Entry(window, width=50)
# entry.pack(pady=10)
#
# results_text = tk.Text(window, width=50, height=10)
# results_text.pack(pady=10)
#
# search_button = tk.Button(window, text="Search", command=search)
# search_button.pack()
#
# window.mainloop()

def create_search_engine_window():
    # Create the search engine window.
    engine = tk.Tk()

    # Create the search entry box.
    search_entry = tk.Entry(engine)

    # Create the search button.
    search_button = tk.Button(engine, text="Search", command=search)

    # Create the results text box.
    results_textbox = tk.Text(engine)

    # Layout the widgets.
    search_entry.pack()
    search_button.pack()
    results_textbox.pack()

    return engine

def search(engine):
    # Get the search query from the entry box.
    query = engine.search_entry.get()

    # If the query is not equal to 'q', then search for it.
    if query != 'q':
        results = M3Search.search_engine(query)

        # Print the results to the results text box.
        for result in results:
            engine.results_textbox.insert(tk.END, result + "\n")

if __name__ == "main":
    # Create the search engine window.
    engine = create_search_engine_window()

    # Run the main loop.
    engine.mainloop()
