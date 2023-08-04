from Parse import parseFeed, downloadArticle
from Dbias.bias_classification import *
from Model import predict_politics

if __name__ == '__main__':
    feed = parseFeed("https://news.google.com/rss/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE")
    for entry in feed.entries:
        article = downloadArticle(entry.link)

        if(article != None):
            highest_spectrum, highest_confidence, spectrum = predict_politics(article.summary)

            if(highest_confidence > 0.9):
                print("-----------------------")

                print(article.title)
                print(entry.source["title"])

                print(highest_spectrum, highest_confidence, spectrum)

                bias = classifier(article.summary)
                bias_label = bias[0]["label"]
                bias_score = bias[0]["score"]
                print(bias_label, bias_score)

                print("-----------------------")
