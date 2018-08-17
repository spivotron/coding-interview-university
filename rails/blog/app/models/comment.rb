class Comment < ActiveRecord::Base
  belongs_to :article
  def addMovieID(id)
    self.movieID = :article
  end
end
