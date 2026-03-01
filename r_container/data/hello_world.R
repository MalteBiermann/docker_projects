# Fancy Hello World with styled output
cat("\n", strrep("✨", 20), "\n")
cat("  🌟 WELCOME TO R 🌟\n")
cat(strrep("✨", 20), "\n\n")
cat("Hello, ", "\033[1;36m", "World", "\033[0m", "! 👋\n\n", sep = "")

# Load required libraries for fancy visualizations
library(ggplot2)
library(gridExtra)

# Set a theme for better-looking plots
theme_fancy <- function() {
  theme_minimal() +
    theme(
      plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
      plot.subtitle = element_text(size = 11, hjust = 0.5, color = "grey40"),
      panel.grid.major = element_line(color = "grey90"),
      axis.text = element_text(size = 10),
      axis.title = element_text(size = 11, face = "bold")
    )
}

# Create polynomial data for more interesting visualization
x <- seq(0, 10, length.out = 100)
y_sin <- sin(x)
y_cos <- cos(x)
y_poly <- 0.1 * (x - 5)^2 + 2

df <- data.frame(
  x = c(x, x, x),
  y = c(y_sin, y_cos, y_poly),
  Function = rep(c("sin(x)", "cos(x)", "0.1(x-5)² + 2"), each = length(x))
)

# Create main fancy plot
p1 <- ggplot(df, aes(x = x, y = y, color = Function, linetype = Function)) +
  geom_line(size = 1.2) +
  scale_color_manual(values = c("sin(x)" = "#FF6B6B", "cos(x)" = "#4ECDC4", "0.1(x-5)² + 2" = "#FFE66D")) +
  scale_linetype_manual(values = c("solid", "dashed", "dotted")) +
  labs(
    title = "Mathematical Functions",
    subtitle = "A fancier visualization with multiple functions",
    x = "x",
    y = "f(x)"
  ) +
  theme_fancy() +
  theme(legend.position = "bottom")

# Create a scatter plot with styling
set.seed(42)
scatter_df <- data.frame(
  x_scatter = rnorm(50, mean = 5, sd = 2),
  y_scatter = rnorm(50, mean = 0, sd = 1.5),
  group = sample(c("A", "B", "C"), 50, replace = TRUE)
)

p2 <- ggplot(scatter_df, aes(x = x_scatter, y = y_scatter, color = group, size = abs(y_scatter))) +
  geom_point(alpha = 0.7) +
  scale_color_manual(values = c("A" = "#FF1493", "B" = "#00CED1", "C" = "#FFD700")) +
  labs(
    title = "Random Scatter Plot",
    x = "X Values",
    y = "Y Values",
    size = "|Y|"
  ) +
  theme_fancy() +
  theme(legend.position = "bottom")

# Display both plots
print(p1)
print(p2)

cat("\n", strrep("✨", 20), "\n")
cat("✅ Fancy visualization complete!\n")
cat(strrep("✨", 20), "\n\n")
