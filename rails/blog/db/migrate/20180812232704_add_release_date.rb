class AddReleaseDate < ActiveRecord::Migration[5.2]

  def change
    add_column :articles, :release_date :datetime
  end
end
