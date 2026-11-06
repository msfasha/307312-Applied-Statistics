# Instructor-only worked answers; run from project root.
source('lessons/_includes/course-tools.R')
lines <- read.csv('data/business/superstore-lines.csv', colClasses = c(postal_code = 'character'))
orders <- make_orders(lines)
cola <- read.csv('data/business/cola.csv')
consumer <- read.csv('data/business/consumer.csv')
sink('instructor/business-course-answer-key.md')
cat('# Business-course answer key — 6 November 2026\n\n')
show_table <- function(title, x, digits=3) {
 cat('\n## ',title,'\n\n',sep='');cat(knitr::kable(x, digits=digits),sep='\n');cat('\n')
}
show_table('Part 1: regional category-manager briefing', lines %>% group_by(region) %>%
  summarise(total_sales=sum(sales),total_profit=sum(profit),.groups='drop') %>%
  mutate(margin_pct=100*total_profit/total_sales))
show_table('Practical 1: regional order counts',orders %>% count(region) %>% mutate(percent=100*n/sum(n)))
show_table('Practical 1: shipping-mode percentages within region',100*prop.table(xtabs(~region+ship_mode,data=orders),1))
show_table('Practical 1: dispatch within four days',orders %>% group_by(region) %>%
  summarise(orders=n(),within_four_days_pct=100*mean(ship_days<=4),.groups='drop'))
show_table('Practical 1: listed returns within segment',orders %>% group_by(segment) %>%
  summarise(orders=n(),listed_return_pct=100*mean(listed_return),.groups='drop'))
show_table('Practical 2: regional order sales',orders %>% group_by(region) %>%
  summarise(orders=n(),total_sales=sum(sales),mean_sales=mean(sales),median_sales=median(sales),
            sd_sales=sd(sales),iqr_sales=IQR(sales),.groups='drop'))
show_table('Practical 2: five largest orders',orders %>% arrange(desc(sales)) %>%
  select(order_id,sales,profit,line_count,quantity) %>% head(5))
ranked<-orders%>%arrange(desc(sales),order_id)
top_n<-ceiling(.1*nrow(orders))
show_table('Practical 2: top order revenue concentration',data.frame(
 rule='Top ceiling(10% of orders), ties ordered by order_id',selected_orders=top_n,
 percent_orders=100*top_n/nrow(orders),revenue_share_pct=100*sum(head(ranked$sales,top_n))/sum(orders$sales)))
lines<-lines%>%mutate(discount_band=cut(discount,c(-Inf,0,.2,Inf),
 labels=c('None','Above 0 to 20%','Above 20%'),ordered_result=TRUE))
subcategories<-lines%>%group_by(sub_category)%>%summarise(lines=n(),total_sales=sum(sales),
 total_profit=sum(profit),.groups='drop')%>%mutate(margin_pct=100*total_profit/total_sales)
show_table('Practical 3: subcategories ranked by profit',subcategories%>%arrange(total_profit))
show_table('Practical 3: subcategories ranked by margin',subcategories%>%arrange(margin_pct))
weak<-subcategories$sub_category[which.min(subcategories$total_profit)]
show_table(paste('Practical 3: discount bands within',weak),lines%>%filter(sub_category==weak)%>%
 group_by(discount_band)%>%summarise(lines=n(),total_sales=sum(sales),total_profit=sum(profit),
 loss_line_pct=100*mean(profit<0),.groups='drop')%>%mutate(margin_pct=100*total_profit/total_sales))
show_table(paste('Practical 3: three largest loss lines within',weak),lines%>%filter(sub_category==weak,profit<0)%>%
 arrange(profit)%>%select(row_id,order_id,product_name,sales,discount,profit)%>%head(3))
show_table('Practical 3: order losses by segment',orders%>%group_by(segment)%>%
 summarise(orders=n(),loss_order_pct=100*mean(profit<0),.groups='drop'))
set.seed(106);n<-100;N<-nrow(orders);x<-sample(orders$sales,n)
h<-qt(.975,n-1)*sd(x)/sqrt(n)*sqrt(1-n/N)
show_table('Part 3 A: an example random sampling audit',data.frame(seed=106,n=n,
 mean_sales=mean(x),lower95=mean(x)-h,upper95=mean(x)+h,frame_mean=mean(orders$sales)))
cat('\nThis n=100 t interval is approximate; the lesson demonstrates undercoverage for small samples from this skewed frame. Do not interpret one interval containing the frame mean as validation.\n')
t<-t.test(cola$weekly_cases[cola$display=='End aisle'],cola$weekly_cases[cola$display=='Normal'])
show_table('Part 3 B: end aisle minus normal',data.frame(effect=diff(rev(t$estimate)),lower95=t$conf.int[1],upper95=t$conf.int[2],p=t$p.value),6)
cat('\nRandom assignment supports the experimental contrast; representative sampling and long-term net profitability are not established. Obtain contribution per case, display costs and displaced sales.\n')
a<-lm(card_charges~household_size,data=consumer)
b<-lm(card_charges~income_thousands+household_size,data=consumer)
show_table('Part 3 C: household-size-only model',as.data.frame(coef(summary(a))))
show_table('Part 3 C: model comparison',anova(a,b))
new<-data.frame(income_thousands=40,household_size=4)
show_table('Part 3 C: mean-response interval at income 40, size 4',as.data.frame(predict(b,new,interval='confidence')))
show_table('Part 3 C: individual prediction interval at income 40, size 4',as.data.frame(predict(b,new,interval='prediction')))
cat('\nRegression interpretations are conditional associations. Compare residual patterns and consider the unverified selection design. Neither fit nor statistical significance establishes causal or out-of-sample business performance.\n')
cat('\n## Briefing assessment\n\nAward credit for a correct unit/denominator, labelled units, reproducible code, an evidence-based finding and a defensible limitation. Do not require an identical random sample or wording. Graphs should answer the question without clipping or misleading scales. Never accept a causal discount claim from the observational Superstore comparisons.\n')
sink()
