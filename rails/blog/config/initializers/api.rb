require 'rest-client'
data =  JSON.parse(RestClient.get("https://api.themoviedb.org/3/movie/popular?page=1&language=en-US&api_key=f816912831ec92fbe9e10762bb01c252"))

genre_ids= JSON.parse(RestClient.get("https://api.themoviedb.org/3/genre/movie/list?language=en-US&api_key=f816912831ec92fbe9e10762bb01c252"))
results = data['results']
results.each do |resultKey, value|
  #finding existing articles
  existing_article = Article.find_by(title: resultKey["original_title"])
  #checking if the articles abstract is there and if the article doesnt exist
  if resultKey["original_title"].length > 0
    if !existing_article
      movie = Article.new do |key|
        key.title  = resultKey['original_title']
        key.release_date = resultKey['release_date']
        key.genre =  genre_ids['genres'].find{|g| g['id']==resultKey['genre_ids'][0]}['name']
        key.image = "https://image.tmdb.org/t/p/w300" +resultKey['poster_path']

        # key.date = Time.now
      end
      #Saving articles
      if movie.save
        puts "saved movie"
      else
        puts "not saved"
      end
    end
  end
end
