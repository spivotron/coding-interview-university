class AddMovieIdToComment < ActiveRecord::Migration[5.2]
  def change
    add_column :comments, :movieID, :integer 
  end
end
