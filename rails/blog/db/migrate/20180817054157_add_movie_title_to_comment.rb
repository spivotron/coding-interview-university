class AddMovieTitleToComment < ActiveRecord::Migration[5.2]
  def change
    add_column :comments, :movie_name, :string
  end
end
