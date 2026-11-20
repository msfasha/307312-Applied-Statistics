# 307312 Applied Statistics — Statistical Inference And Estimation
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- inferential-2-16 ---
# set.seed() makes this simulation reproducible; rnorm() creates the source's artificial population.
# replicate() repeats sampling with replacement; each column returns a mean and a sample-based SE.
set.seed(307312)
population <- rnorm(1000000, mean=50, sd=10)
# sample(replace=TRUE) draws independently with replacement; sqrt(30) is the SE denominator.
results <- replicate(1000, {
  x <- sample(population, size=30, replace=TRUE)
  c(sample_mean=mean(x), estimated_SE=sd(x)/sqrt(30))
})
# sd() and mean() compare simulated sampling spread and average estimated SE; agreement is illustrative.
# hist() uses 30 bins to display the 1,000 sample means; this simulation is not a mathematical proof.
c(SD_of_sample_means=sd(results[1,]), average_estimated_SE=mean(results[2,]))
hist(results[1,], breaks=30, col="#D4D4D4", main="Distribution of Sample Means", xlab="Sample Mean")

# --- inferential-2-17 ---
# qnorm(0.95) gives the upper critical z for a central 90% interval; sigma=8.63 is treated as known.
# sqrt(n) scales population SD into SE; c(-1,1) constructs the lower and upper endpoints in kg.
n <- 50; xbar <- 73.16; sigma <- 8.63
xbar + c(-1,1)*qnorm(0.95)*sigma/sqrt(n)

# --- inferential-2-19 ---
# qt(0.95,df=49) gives the central 90% t critical value when SD 8.63 is estimated from 50 observations.
# This t interval uses unknown population SD; it can differ from the original normal approximation.
73.16 + c(-1,1)*qt(0.95,df=49)*8.63/sqrt(50)

# --- inferential-2-25 ---
# qt() uses 19 degrees of freedom for n=20; the central 90% interval leaves 5% in each tail.
# The stated sample SD 8.3946 and mean 72.94 are in kg; no individual observations are invented.
72.94 + c(-1,1)*qt(0.95,df=19)*8.3946/sqrt(20)

# --- inferential-3-22 ---
# This summary-data t test uses the source's n=40, mean 3.4 days, and variance 1.887179487 days squared.
# pt() gives tail area with df=39; doubling the upper tail of abs(t) gives the two-sided p-value.
n <- 40; t_stat <- (3.4-3)/sqrt(1.887179487/n)
c(t=t_stat, df=n-1, p_value=2*pt(abs(t_stat),df=n-1,lower.tail=FALSE))

# --- inferential-3-24 ---
# Use the source summary values: n=30, mean output 520 units, and sample variance 340.0689655 units squared.
# pt(lower.tail=FALSE) tests the stated upper-tail alternative mu>500, with df=29.
t_stat <- (520-500)/sqrt(340.0689655/30)
c(t=t_stat, p_value=pt(t_stat,df=29,lower.tail=FALSE))

# --- inferential-3-27 ---
# Load the exact 30 paired observations printed in the source slide.
paired <- read.csv("data/inferential-statistics/paired_scores.csv")
head(paired)
c(n=nrow(paired), mean_change=mean(paired$score2 - paired$score1))

# --- inferential-3-28 ---
# Compare score2 minus score1 within the same students.
t.test(x=paired$score2, y=paired$score1, paired=TRUE,
       alternative="greater", conf.level=0.95)

# --- inferential-3-29 ---
# Load the exact printed salary samples; the source currency labels conflict.
salaries <- read.csv("data/inferential-statistics/graduate_salaries.csv")
c(male_mean=mean(salaries$male), female_mean=mean(salaries$female))

# --- inferential-3-30 ---
# Pooled two-sided comparison under the source equal-variance assumption.
t.test(x=salaries$male, y=salaries$female, var.equal=TRUE,
       alternative="two.sided", conf.level=0.95)

# --- inferential-3-31 ---
# Load the exact printed female-graduate salary samples.
majors <- read.csv("data/inferential-statistics/female_major_salaries.csv")
c(political_science_mean=mean(majors$political_science),
  social_science_mean=mean(majors$social_science))

# --- inferential-3-32 ---
# Welch comparison for the stated one-sided question at alpha 0.01.
t.test(x=majors$political_science, y=majors$social_science,
       alternative="greater", var.equal=FALSE, conf.level=0.99)

# --- inferential-3-36 ---
# prop.test() tests the source's 140 satisfied customers out of 200 against p=0.75.
# correct=FALSE omits continuity correction to match the source normal-approximation calculation.
prop.test(140,200,p=0.75,alternative="two.sided",correct=FALSE)

# --- inferential-3-38 ---
# prop.test() compares 65/100 in the new-treatment group with 50/100 in the standard-treatment group.
# greater sets the source's one-sided alternative; correct=FALSE matches its uncorrected pooled z test.
prop.test(c(65,50),c(100,100),alternative="greater",correct=FALSE)

# --- inferential-3-44 ---
# Enter the original observed counts, with age groups as rows.
beverages <- matrix(c(30,40,50,30,20,30), nrow=3, byrow=TRUE,
  dimnames=list(c("Under 30","30 to 50","Over 50"),
                c("Product A","Product B")))
beverages

# --- inferential-3-46 ---
# Expected counts under independence: row total times column total / grand total.
expected <- outer(X=rowSums(beverages), Y=colSums(beverages), FUN="*") /
            sum(beverages)
expected

# --- inferential-3-48 ---
# Compare the observed and expected counts with the chi-square test.
chi <- chisq.test(x=beverages, correct=FALSE)
chi

# --- inferential-3-49 ---
# Review each contribution before adding the chi-square statistic.
contributions <- (beverages - expected)^2 / expected
contributions
c(chi_square=sum(contributions), df=unname(chi$parameter),
  p_value=chi$p.value)

# --- inferential-3-53 ---
# read.csv() loads the exact 15 scores printed for the three teaching methods.
# aov(score~group) fits one-way ANOVA; summary() reports its F test under independent normal errors and equal variances.
# Open the course folder in Positron; paths start in that folder.
methods <- read.csv("data/inferential-statistics/teaching_methods.csv")
summary(aov(score~group,data=methods))

# --- inferential-3-56 ---
# factor() treats gender and method as categories in the exact eight printed observations.
# gender*method includes both main effects and their interaction; aov() assumes independent, equal-variance normal errors.
# Open the course folder in Positron; paths start in that folder.
teaching <- read.csv("data/inferential-statistics/teaching_gender.csv")
teaching$gender <- factor(teaching$gender)
teaching$method <- factor(teaching$method)
summary(aov(score~gender*method,data=teaching))

# --- inferential-4-9 ---
# read.csv() imports the ten houses printed in the source; price is in thousands of dollars and size in square feet.
# lm(price~size) fits least squares with an intercept; summary() reports coefficients, R-squared, and inference.
# Open the course folder in Positron; paths start in that folder.
houses <- read.csv("data/inferential-statistics/houses.csv")
simple <- lm(price~size,data=houses)
summary(simple)

# --- inferential-4-11 ---
# anova() partitions the fitted model's variability into regression and residual components.
# The F test assumes the source's independent, constant-variance normal-error linear model.
anova(simple)

# --- inferential-4-14 ---
# factor(location) treats the source location codes 1,2,3 as categories rather than equal-spaced numerical scores.
# lm() adds size, bedrooms, age, and location effects; ten rows provide very limited residual degrees of freedom.
houses$location <- factor(houses$location)
multiple <- lm(price~size+bedrooms+age+location,data=houses)
summary(multiple)

# --- inferential-4-16 ---
# fitted() returns predicted prices and resid() returns observed minus fitted prices in thousands of dollars.
# abline(h=0) adds a horizontal reference: patterns may reveal model problems, not prove an assumption.
plot(fitted(simple),resid(simple),pch=16,col="#595959",xlab="Fitted price (thousands of dollars)",ylab="Residual")
abline(h=0,lty=2)

# --- inferential-4-20 ---
# qqnorm() compares residual quantiles with a normal distribution; qqline() adds a reference line.
# This plot examines the error-normality assumption; it does not require normally distributed predictors.
qqnorm(resid(simple),pch=16,col="#595959")
qqline(resid(simple))
