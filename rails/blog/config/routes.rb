Rails.application.routes.draw do
  get 'welcome/index'
  resources :articles do
    collection do
      get :sort_by_date
      get :sort_by_title
      get :sort_by_genre
    end
    resources :comments
  end
  resources :reviews
  root 'articles#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
