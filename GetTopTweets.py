import twint # https://github.com/twintproject/twint

class topTweetsFetcher: 
    
    def __init__(self):
        self.sinceBullDates = ["2021-04-01"]
        self.untilBullDates = ["2021-12-01"]

    def fetchTweets(self):
        if len(self.sinceBullDates) != len(self.untilBullDates): 
            return
    
        for i in range(0,len(self.sinceBullDates)):
            c = twint.Config() 

            c.Search = "bitcoin"
            c.Lang = "en"
            c.Limit = 100000
            c.Since = self.sinceBullDates[i]
            c.Until = self.untilBullDates[i]
            c.Min_likes = 1
            c.Min_retweets = 1
            c.Store_csv = True
            c.Output = "topTweets" + str(self.sinceBullDates[i]) + "-to-" + str(self.untilBullDates[i]) + ".csv"

            twint.run.Search(c)

    

if __name__ == "__main__":
    fetcher = topTweetsFetcher()
    fetcher.fetchTweets()