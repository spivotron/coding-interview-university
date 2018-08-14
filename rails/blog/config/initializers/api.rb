require 'rest-client'

#RestClient get request to the NYT endpoint with my API Key being parsed into a JS object
data = JSON.parse( RestClient.get("https://api.themoviedb.org/3/movie/555?api_key=f816912831ec92fbe9e10762bb01c252"))
#Iterating through each result/article of the NYT
data.each do |key, value|
  #finding existing articles

  existing_article = Article.find_by(title: data["original_title"])
  #checking if the articles abstract is there and if the article doesnt exist
  if data["original_title"].length > 0
    if !existing_article
      news = Article.new do |key|
        key.title  = data['original_title']
        key.release_date = data['release_date']
        key.genre = data['genres'][0]['name']
        key.image = "https://image.tmdb.org/t/p/w300" +data['poster_path']
        # key.headline = article["title"]
        # key.news_station = "New York Times"
        # key.abstract = article["abstract"]
        # key.category = article["section"]
        # key.url = article["url"]
        # #Some of the articles didnt have pictures so I made a default one if there was no pic
        # if article["multimedia"].length === 0
        #   key.image = "http://www.nytimes.com/services/mobile/img/ios-newsreader-icon.png"
        # else
        #   key.image = article["multimedia"][0]["url"]
        # end
        # key.date = Time.now
      end
      #Saving articles
      if news.save
        puts "saved"
      else
        puts "not saved"
      end
    end
  end
end
