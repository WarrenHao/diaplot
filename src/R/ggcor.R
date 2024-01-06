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