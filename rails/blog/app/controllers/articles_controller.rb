class ArticlesController < ApplicationController

  # http_basic_authenticate_with name: "dhh", password: "secret", except: [:index, :show]

  def new
    @article = Article.new
  end

  def index
    @articles= Article.all
  end

  def sort_by_date
    @articles = Article.all.sort_by{|m| m.release_date}
    render 'index'
  end

  def sort_by_title
    @articles = Article.all.sort_by{|m| m.title}
    render 'index'
  end

  def sort_by_genre
    @articles = Article.all.sort_by{|m| m.genre}
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

    # render plain: params[:article].inspect
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


  def pleaseWork
    puts "hello"
  end


  def show
    @article = Article.find(params[:id])
  end

  private
    def article_params
      params.require(:article).permit(:title, :text)
    end

    # def blank_stars
    #   @comments = Article.find(params[:id]).comments
    #   5 - rating.to_i
    # end

end
