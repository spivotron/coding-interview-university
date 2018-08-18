class ArticlesController < ApplicationController

  def new
    @article = Article.new
  end

  def index
    @articles= Article.all
    @recent_comments = Comment.limit(4).order("created_at desc").all
  end

  def sort_by_date
    @articles = Article.all.sort_by{|m| m.release_date}
    @recent_comments = Comment.limit(4).order("created_at desc").all
    render 'index'
  end

  def sort_by_title
    @articles = Article.all.sort_by{|m| m.title}
    @recent_comments = Comment.limit(4).order("created_at desc").all
    render 'index'
  end

  def sort_by_genre
    @articles = Article.all.sort_by{|m| m.genre}
    @recent_comments = Comment.limit(4).order("created_at desc").all
    render 'index'
  end

  def edit
    @article = Article.find(params[:id])
  end


  def create
    @article = Article.new(article_params)
    if @article.save
      redirect_to @article
    else
      render 'new'
    end

  end

  def update
    @article = Article.find(params[:id])
    if @article.update(article_params)
      redirect_to @article
    else
      render 'edit'
    end
  end

  def destroy
    @article = Article.find(params[:id])
    @article.destroy
    redirect_to articles_path
  end

  def show
    @article = Article.find(params[:id])
  end

  private
    def article_params
      params.require(:article).permit(:title, :text)
    end

end
