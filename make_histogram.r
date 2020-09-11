library(tidyverse)

# Paths.
date_string = Sys.Date()
image_path = paste(
  "data/past_pics/hist/", date_string, ".png",
  sep = "", collapse = "")
most_recent_image_path = "data/most_recent_hist.png"

# Read.
history = read_csv("data/history.csv")

# Graph.
ggplot(data = history, aes(x = rounds)) +
  geom_histogram(bins = 30) +
  labs(title = "Length of a game of War",
       subtitle = format(date_string, format = "%B %d, %Y"),
       x = "Number of rounds",
       y = "Frequency") +
  theme(legend.position = "none")

# Save.
ggsave(image_path, height = 4, width = 6)
ggsave(most_recent_image_path, height = 4, width = 6)

