library(tidyverse)

# Paths.
date_string = Sys.Date()
image_path = paste(
  "data/past_pics/pct/", date_string, ".png",
  sep = "", collapse = "")
most_recent_image_path = "data/most_recent_pct.png"

# Calculate.
history = read_csv("data/history.csv")
n = nrow(history)
pct = cumsum(history$winner == "Player 1") / 1:n
df = data.frame("player" = c(rep("Player 1", n), rep("Player 2", n)),
                "pct" = c(pct, 1 - pct),
                "order" = c(1:n, 1:n))
axis_label_breaks = c(1, round(n / 2), n)
axis_labels = format(history$date[axis_label_breaks], format = "%m/%d")

# Graph.
ggplot(data = df, aes(x = order, y = pct, fill = player)) +
  geom_area(size = 0.5, color = "grey40") +
  ylim(0, 1) +
  labs(title = "Percentage of wins over time",
       subtitle = format(date_string, format = "%B %d, %Y")) +
  scale_x_continuous(breaks = axis_label_breaks, labels = axis_labels) +
  theme(axis.title.x = element_blank(),
        axis.title.y = element_blank(),
        axis.text.y = element_blank(),
        axis.ticks.y = element_blank(),
        legend.position = "none")

# Save.
ggsave(image_path, height = 4, width = 6)
ggsave(most_recent_image_path, height = 4, width = 6)



