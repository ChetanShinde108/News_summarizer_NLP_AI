import tkinter as tk
# # pip install nltk
import nltk
# # pip install textblob
from textblob import TextBlob
# # pip install newspaper3k
from newspaper import Article

# nltk.download('punkt')

# url="https://timesofindia.indiatimes.com/city/pune/250-political-workers-booked-for-vandalism-and-rioting-latest-news/articleshow/107595898.cms"

def summarize():

    url= utext.get('1.0', "end").strip()

    article= Article(url)

    article.download()
    article.parse()

    article.nlp()

    #print(f"Title: {article.title}")
    #print(f"Authors: {article.authors}")
    #print(f"Publication Date: {article.publish_date}")
    #print(f"Summary: {article.summary}")

    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete("1.0", "end")
    title.insert('1.0',article.title)

    author.delete("1.0", "end")
    author.insert('1.0',article.authors)

    publication.delete("1.0", "end")
    publication.insert('1.0',article.publish_date)

    summary.delete("1.0", "end")
    summary.insert('1.0',article.summary)

    analysis=TextBlob(article.text)
    #print(analysis.polarity)

    #print(analysis.sentiment)

    #print(f"Sentiment:",end="")
    sentiment.delete("1.0", "end")
    sentiment.insert('1.0',f"Polarity: {analysis.polarity}")

    if analysis.polarity > 0:
        print("positive")
    elif  analysis.polarity<0:
        print("negative")
    else:
        print("neutral")

    title.config(state="disabled")
    author.config(state="disabled")
    publication.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")

    



# # print(f"Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity<0 else "neutral"}")

# # print("analysis test")
# # analysis test
# # analysis1=TextBlob("Today I am ill")
# # print(analysis1.polarity)

# # print(analysis1.sentiment)

# # print(f"Sentiment:",end="")

# # if analysis1.polarity > 0:
# #     print("positive")
# # elif  analysis1.polarity<0:
# #     print("negative")
# # else:
# #     print("neutral")


# # visual interface
    
root=tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

ulable=tk.Label(root, text="URL")
ulable.pack()
utext=tk.Text(root, height=1, width=140)
utext.pack()

btn=tk.Button(root,text="Summarize", command= summarize)
btn.pack()

tlable=tk.Label(root, text="Title")
tlable.pack()
title=tk.Text(root, height=1, width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()

alable=tk.Label(root, text="Author")
alable.pack()
author=tk.Text(root, height=1, width=140)
author.config(state='disabled',bg='#dddddd')
author.pack()

plable=tk.Label(root, text="Publishing Date")
plable.pack()
publication=tk.Text(root, height=1, width=140)
publication.config(state='disabled',bg='#dddddd')
publication.pack()

slable=tk.Label(root, text="Summary")
slable.pack()
summary=tk.Text(root, height=20, width=140)
summary.config(state='disabled',bg='#dddddd')
summary.pack()

selable=tk.Label(root, text="Sentiment Analysis")
selable.pack()
sentiment=tk.Text(root, height=1, width=140)
sentiment.config(state='disabled',bg='#dddddd')
sentiment.pack()


root.mainloop()

