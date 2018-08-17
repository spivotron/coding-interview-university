class ReviewsController < ApplicationController
  def index
    @reviews = Comment.order("created_at desc").all
  end
end
