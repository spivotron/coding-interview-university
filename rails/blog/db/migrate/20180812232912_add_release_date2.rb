class AddReleaseDate2 < ActiveRecord::Migration[5.2]

  def change
    add_column :articles, :release_date, :string
  end
end
