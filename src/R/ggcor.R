install.packages("devtools") 

install.packages("stringi")

install.packages("stringr")

# 此处从github安装，如果github被墙，可以从gitee安装，新建一个repo，import已有的ggcor，需确保权限

devtools::install_github("WarrenHao/ggcor") 
# devtools::install_git("https://gitee.com/houyunhuang/ggcor.git") 


library(ggplot2)
library(ggcor)
set_scale()
quickcor(mtcars) + geom_square()


quickcor(mtcars, type = "upper") + geom_circle2()

# mantel test
install.packages('vegan')
install.packages('dplyr')
library(vegan)  
library(dplyr)
#> Warning: package 'dplyr' was built under R version 3.6.2
data("varechem", package = "vegan")
data("varespec", package = "vegan")

mantel <- mantel_test(varespec, varechem,
                      spec.select = list(Spec01 = 1:7,
                                         Spec02 = 8:18,
                                         Spec03 = 19:37,
                                         Spec04 = 38:44)) %>% 
  mutate(rd = cut(r, breaks = c(-Inf, 0.2, 0.4, Inf),
                  labels = c("< 0.2", "0.2 - 0.4", ">= 0.4")),
         pd = cut(p.value, breaks = c(-Inf, 0.01, 0.05, Inf),
                  labels = c("< 0.01", "0.01 - 0.05", ">= 0.05")))

quickcor(varechem, type = "upper") +
  geom_square() +
  anno_link(aes(colour = pd, size = rd), data = mantel) +
  scale_size_manual(values = c(0.5, 1, 2)) +
  scale_colour_manual(values = c("#D95F02", "#1B9E77", "#A2A2A288")) +
  guides(size = guide_legend(title = "Mantel's r",
                             override.aes = list(colour = "grey35"), 
                             order = 2),
         colour = guide_legend(title = "Mantel's p", 
                               override.aes = list(size = 3), 
                               order = 1),
         fill = guide_colorbar(title = "Pearson's r", order = 3))



# 环形图
rand_correlate(100, 8) %>% ## require ambient packages
  quickcor(circular = TRUE, cluster = TRUE, open = 45) +
  geom_colour(colour = "white", size = 0.125) +
  anno_row_tree() +
  anno_col_tree() +
  set_p_xaxis() +
  set_p_yaxis()
#> Warning: Removed 8 rows containing missing values (geom_text).


# 一般热力图
d1 <- rand_dataset(20, 30) %>% 
  gcor_tbl(cluster = TRUE)
p <- matrix(sample(LETTERS[1:4], 90, replace = TRUE), nrow = 30,
             dimnames = list(paste0("sample", 1:30), paste0("Type", 1:3))) %>% 
  gcor_tbl(name = "Type", row.order = d1) %>% 
  qheatmap(aes(fill = Type)) + coord_fixed() + remove_y_axis()
d2 <- data.frame(x = sample(paste0("var", 1:20), 200, replace = TRUE))

set_scale()
quickcor(d1) +
  geom_colour(aes(fill = value)) +
  anno_hc_bar(width = 1) +
  anno_row_custom(p) +
  anno_row_tree() +
  anno_hc_bar(pos = "top") +
  anno_bar(d2, aes(x = x), height = 0.12) +
  anno_col_tree(height = 0.12)