# Maintainer only: export pinned source workbooks without changing them.
# Students use the CSVs and do not need readxl.
suppressPackageStartupMessages(library(readxl))
superstore_path <- 'books/tableau/sample_-_superstore.xls'
d <- as.data.frame(read_excel(superstore_path, sheet = 'Orders'))
names(d) <- c('row_id','order_id','order_date','ship_date','ship_mode','customer_id',
 'customer_name','segment','country','city','state','postal_code','region','product_id',
 'category','sub_category','product_name','sales','quantity','discount','profit')
d$order_date <- as.Date(d$order_date)
d$ship_date <- as.Date(d$ship_date)
# Pin completed fictional order years; do not silently change dates to match older tutorials.
d <- d[d$country == 'United States' & d$order_date >= as.Date('2023-01-01') &
       d$order_date < as.Date('2026-01-01'), ]
r <- as.data.frame(read_excel(superstore_path, sheet = 'Returns'))
stopifnot(!anyDuplicated(r[['Order ID']]), all(r$Returned == 'Yes'))
d$return_status <- ifelse(d$order_id %in% r[['Order ID']], 'Listed return', 'Not listed')
# Postal codes include Canadian letters; keep source text, never coerce to numbers.
d$postal_code <- as.character(d$postal_code)
write.csv(d, 'data/business/superstore-lines.csv', row.names = FALSE, na = '')
cola_path <- 'books/2-Basic business statistics  concepts and applications/Data-9th e/browse/Data_Files/Excel/COLA.XLS'
c <- as.data.frame(read_excel(cola_path, sheet = 'Data'))
c <- data.frame(store_id = c(paste0('N',1:10),paste0('E',1:10)),
 display = rep(c('Normal','End aisle'), each = 10),
 weekly_cases = c(c$Normal,c$EndAisle))
write.csv(c,'data/business/cola.csv',row.names=FALSE)
consumer_path <- 'books/1-Modern Business Statistics-Organized-Data/7th-Data - Modern Business Statistics with Microsoft Excel Anderson Sweeney Williams/Chapter 15 Multiple Regression/Consumer.xls'
u <- as.data.frame(read_excel(consumer_path))
names(u) <- c('income_thousands','household_size','card_charges')
write.csv(u,'data/business/consumer.csv',row.names=FALSE)
cat('Exported Superstore lines:',nrow(d),'orders:',length(unique(d$order_id)), '\n')
cat('Order date range:',as.character(range(d$order_date)),'\n')
cat('Missing cells by variable:\n'); print(colSums(is.na(d)))
