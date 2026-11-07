# Instructor-only reference results. Run from the course root; not packaged for students.
source('lessons/_includes/course-tools.R')
d <- 'data/business'
get_case <- function(name) read.csv(file.path(d, paste0('extended-', name, '.csv')))
cat('\nCASE 1: Springville\n')
calls <- get_case('herald-calls')
x <- get_case('herald-marketing')
s <- get_case('herald-subscriptions')
print(summary(calls$calls)); print(sd(calls$calls)); print(IQR(calls$calls))
print(boxplot.stats(calls$calls)$out)
m <- lm(new_subscriptions ~ hours, data=x)
print(coef(m)); print(range(x$hours)); print(summary(m)$r.squared)
for (hours in c(1200,2000)) {
  print(predict(m, data.frame(hours=hours), interval='confidence'))
  print(predict(m, data.frame(hours=hours), interval='prediction'))
}
t <- lm(subscriptions ~ month, data=s)
print(coef(t)); print(predict(t,data.frame(month=25:28),interval='prediction'))
print(c(absolute_growth=tail(s$subscriptions,1)-s$subscriptions[1],
        pct_growth=100*(tail(s$subscriptions,1)/s$subscriptions[1]-1)))
print(acf(residuals(t),plot=FALSE)$acf[2])
cat('\nCASE 2: Oxford\n')
for (xbar in c(372.5,375)) {
  z <- (xbar-368)/3
  print(data.frame(mean=xbar,z=z,p=2*pnorm(-abs(z)),
                   lower=xbar-qnorm(.975)*3, upper=xbar+qnorm(.975)*3))
}
print(data.frame(n=c(25,100),se=15/sqrt(c(25,100))))
cat('\nCASE 3: BLK\n')
c <- read.csv(file.path(d,'cola.csv'))
a <- c$weekly_cases[c$display=='End aisle']; b <- c$weekly_cases[c$display=='Normal']
w <- t.test(a,b); print(w); print(t.test(a,b,var.equal=TRUE))
print(wilcox.test(a,b,exact=FALSE))
margin <- c(4,6,8)
print(data.frame(margin=margin, net=(mean(a)-mean(b))*margin-80,
                 lower=w$conf.int[1]*margin-80,upper=w$conf.int[2]*margin-80,
                 break_even_cases=80/margin))
cat('\nCASE 4: Parachute\n')
p <- get_case('parachute'); p$supplier <- factor(p$supplier)
f <- aov(strength~supplier,data=p)
print(summary(f)); print(TukeyHSD(f)); print(oneway.test(strength~supplier,data=p))
stopifnot(abs(summary(f)[[1]][['F value']][1]-3.461628925)<1e-7)
cat('\nCASE 5: Potato\n')
p <- get_case('potato')
print(c(mean=mean(p$solids), below12=sum(p$solids<12), at_or_below12=sum(p$solids<=12), n=nrow(p)))
print(cor(p))
f <- lm(solids~.,data=p); r <- lm(solids~ph+cake_thickness+drum_speed,data=p)
print(summary(f)); print(AIC(f,r)); print(summary(r))
print(head(sort(cooks.distance(f),decreasing=TRUE)))
cat('\nCASE 6: Harnswell\n')
h <- get_case('harnswell'); print(table(h$diameter))
g <- h %>% group_by(batch) %>% summarise(xbar=mean(diameter), R=diff(range(diameter)), .groups='drop')
limits <- function(g) {
  mu <- mean(g$xbar); rb <- mean(g$R)
  c(mu=mu, Rbar=rb, xlower=mu-.577*rb, xupper=mu+.577*rb, Rlower=0,Rupper=2.114*rb)
}
l <- limits(g); print(l)
flags <- g$batch[g$xbar<l['xlower'] | g$xbar>l['xupper'] | g$R>l['Rupper']]
print(flags)
stopifnot(sum(h$diameter>.5075)==56, sum(h$diameter<.5072)==0, identical(flags,17L) || identical(flags,17))
print(limits(g[g$batch!=17,]))
# Diagnostic numerical values only: the initial process is unstable.
sigma_within <- l['Rbar']/2.326
print(c(Cp_diagnostic=(.5075-.5072)/(6*sigma_within),
        Cpk_diagnostic=min((.5075-l['mu'])/(3*sigma_within),(l['mu']-.5072)/(3*sigma_within))))
