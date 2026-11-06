# Shared Petra chart styling for the three Part 2 practicals.
suppressPackageStartupMessages(library(ggplot2))
petra_purple <- "#A83296"
petra_accent <- "#C8ABC3"
petra_groups <- c(Growth = "#A83296", Value = "#6D526A")
petra_risk <- c("very low" = "#F0E6EF", "low" = "#DCC5D8",
                "average" = "#C199BA", "high" = "#A83296", "very high" = "#63305B")
petra_charge <- c(No = "#C8ABC3", Yes = "#79386E")
theme_set(theme_minimal(base_size = 12) +
            theme(panel.grid.minor = element_blank(),
                  plot.title = element_text(colour = "#493347", face = "bold"),
                  axis.title = element_text(colour = "#2F343B"),
                  legend.position = "bottom"))
