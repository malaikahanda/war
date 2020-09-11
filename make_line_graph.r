library(tidyverse)

# Paths.
date_string = Sys.Date()
image_path = paste(
  "data/past_pics/line/", date_string, ".png",
  sep = "", collapse = "")
most_recent_image_path = "data/most_recent_line.png"

# Read.
game = read_csv("data/most_recent_game.csv")

# Graph.
ggplot(data = game, aes(x = round, y = cards, group = player)) +
  geom_line(aes(color = player)) +
  labs(title = "Cards during a game of War",
       subtitle = format(date_string, format = "%B %d, %Y"),
       x = "Round",
       y = "Number of cards") +
  theme(legend.position = "none")

# Save.
ggsave(image_path, height = 4, width = 6)
ggsave(most_recent_image_path, height = 4, width = 6)

