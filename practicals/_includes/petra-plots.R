# Shared Petra grayscale styling; blue/orange distinguish analytical groups.
suppressPackageStartupMessages(library(ggplot2))
petra_ink <- "#4B4B4B"
petra_accent <- "#D4D4D4"
petra_groups <- c(Growth = "#3B6B8A", Value = "#B56A3A")
petra_risk <- c("very low" = "#EFF3F6", "low" = "#CBDCE8",
                "average" = "#91B3CC", "high" = "#557F9D", "very high" = "#244860")
petra_charge <- c(No = "#777777", Yes = "#3B6B8A")
theme_set(theme_minimal(base_size = 12) +
            theme(panel.grid.minor = element_blank(),
                  plot.title = element_text(colour = "#262626", face = "bold"),
                  axis.title = element_text(colour = "#303030"),
                  legend.position = "bottom"))
