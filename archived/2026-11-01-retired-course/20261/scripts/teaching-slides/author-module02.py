"""Concise teaching text in the existing Module 2 sequence, including instructor additions."""
import csv,json,re
from pathlib import Path
ROOT=Path.cwd(); BASE=ROOT/'20261/modules/02-data-and-descriptive-statistics'
BUILD=ROOT/'20261/_output/.module02-teaching-build'
FILES={i:sorted(BASE.glob(f'{i:02d}-*.qmd'))[0] for i in range(1,6)}
SOURCES={i:p.read_text() for i,p in FILES.items()}
SLIDES=[]
def section(lesson,query):
    lines=SOURCES[lesson].splitlines();heads=[];inside=False
    for i,line in enumerate(lines):
        if line.lstrip().startswith('```'):inside=not inside
        m=re.match(r'^(#{1,6}) (.+)',line)
        if m and not inside:heads.append((i,len(m[1]),m[2]))
    if query=='__intro__':return 1,heads[0][0],'\n'.join(lines[:heads[0][0]])
    start,level,_=next(h for h in heads if h[2]==query)
    end=next((h[0] for h in heads if h[0]>start and h[1]<=level),len(lines))
    return start+1,end,'\n'.join(lines[start:end])
def add(l,h,t,b='',code='',comments=(),image=None,table=None,arabic='',hint='',kind='content'):
    start,end,original=section(l,h)
    if code:
        assert len(comments)>=2,t
        code='\n'.join('# '+c for c in comments)+'\n'+code
    SLIDES.append(dict(lesson=l,title=t,body=b,code=code,image=image,table=table,arabic=arabic,hint=hint,kind=kind,plot=None,refs=[],source=FILES[l].name,heading=h,start=start,end=end,original=original))
def divider(l,t,b,h='__intro__'):add(l,h,t,b,kind='divider')
def plot(l,h,t,label,b='',hint=''):
    add(l,h,t,b,image=f'20261/_output/.module02-teaching-build/plots/lesson{l}-{label}-1.png',hint=hint)
def asset(l,h,t,name,b='',hint=''):
    add(l,h,t,b,image='20261/assets/module02/'+name,hint=hint)
def csvtable(name,cols=None,headers=None,digits=2):
    with (BUILD/'tables'/name).open() as f:
        reader=csv.DictReader(f);rows=list(reader);cols=cols or reader.fieldnames
    def fmt(v):
        try:
            n=float(v)
            return str(int(n)) if n.is_integer() else f'{n:.{digits}f}'
        except (ValueError,TypeError):return v
    return [headers or cols]+[[fmt(r[c]) for c in cols] for r in rows]

divider(1,'Module 2: Descriptive statistics','Classify the variables.\nOrganize distributions.\nDescribe center and variability.\nCompare groups and relationships.')
divider(1,'Lesson 1: Data types and the toolbox','Understand what the values mean before choosing a summary.')
add(1,'What is statistics?','What is statistics?','Collect, organize, present, analyze, and interpret data.\nUse evidence to answer a question and support decisions.')
asset(1,'What is statistics?','Statistical displays','statistics-introduction.png','Conceptual illustration supplied for the lesson.')
add(1,'Our starting question','Restaurant case','How do meal prices differ across quality ratings?\nFirst understand each variable, then choose the tools.',arabic='كيف تختلف أسعار الوجبات بين فئات تقييم الجودة؟\nنفهم أولًا معنى كل متغيّر، ثم نختار أدوات التلخيص.')
asset(1,'Our starting question','One restaurant becomes one record','restaurant-data-and-price-insights-verified.png',hint='Adapted instructor illustration. The displayed values match the first checked CSV record.')
add(1,'First identify the observation and the variable','Observation, variable, and unit','Observational unit: the entity being studied.\nVariable: a characteristic recorded for that entity.\nObservation: one unit’s collection of recorded values.\nHere: one row per restaurant; one column per variable.')
add(1,'First identify the observation and the variable','A number needs a variable definition','101 could be an identifier, a count, or a price.\nIts meaning comes from the definition and units.\nNumerical appearance alone does not justify arithmetic.')
add(1,'Categorical and numerical data','Categorical and numerical data','Categorical values identify a group or ordered category.\nNumerical values measure how many or how much.\nMeasurement level determines which operations are meaningful.',table=[['Variable','Examples','Meaning'],['Payment method','Cash, card, e-wallet','Categorical'],['Quality rating','Good, Very Good, Excellent','Ordered category'],['Restaurant ID','101, 102, 103','Identifier'],['Order count','0, 1, 2, 3','Numerical'],['Waiting duration','2.4, 5.1, 8.7 minutes','Numerical'],['Meal price','18, 22, 28 USD','Numerical']])
add(1,'Categorical and numerical data','Codes remain labels','Cash = 1, Card = 2, E-wallet = 3 are category codes.\nA mean code of 2.1 is not an average payment method.\nCoding Good, Very Good, Excellent as 1,2,3 does not prove equal gaps.',hint='Discuss: would subtracting telephone numbers answer a measurement question?')
add(1,'Discrete and continuous numerical variables','Discrete values','Possible values form a finite or countably infinite set.\nCounts occur at separate points.\nA restaurant can receive 12 or 13 completed orders, not 12.6.')
add(1,'Discrete and continuous numerical variables','Continuous values','A continuous quantity is modeled as taking any value in an interval.\nWaiting time, weight, distance, and temperature are examples.\nBetween 2 and 3 minutes, 2.1, 2.14, and 2.145 are possible.')
add(1,'Discrete and continuous numerical variables','Possible values and recording precision','Decimal places do not decide whether a variable is discrete.\nRestricted 0.5, 1.0, 1.5-liter sizes are discrete possibilities.\nAudit duration is continuous underneath whole-day recording.\nMoney recorded to cents has discrete recording increments.',hint='State recording precision and any continuous-model approximation when it matters.')
asset(1,'Discrete and continuous numerical variables','Data-type summary','data-types.svg','Classify the variable’s meaning before selecting a summary.')
add(1,'Levels of measurement','Measurement levels','Measurement level asks which comparisons make sense.\nNominal, ordinal, interval, and ratio add different information.',hint='We explain the four levels before reading their overview diagram.')
add(1,'Nominal: labels without a natural ranking','Nominal: membership','Values label categories without a natural order.\nExamples: payment method and restaurant ID.\nUse counts, percentages, and category comparisons.')
add(1,'Ordinal: order without established equal gaps','Ordinal: membership and order','Good < Very Good < Excellent is a meaningful ranking.\nThe gaps between successive categories need not be equal.\nRetain the order in frequencies and charts.\nA median category can be meaningful; averaging codes adds assumptions.')
add(1,'Interval: equal differences, an arbitrary zero','Interval: meaningful differences','Celsius differences have equal-sized units.\n10°C to 20°C is the same change as 20°C to 30°C.\nA Celsius mean is meaningful.\n20°C is not twice the temperature of 10°C.')
add(1,'Ratio: equal differences and a meaningful zero','Ratio: meaningful differences and ratios','Zero waiting time means no waiting.\n20 minutes is twice 10 minutes.\nDuration, distance, weight, and order counts are examples.\nA meaningful zero still does not permit division by zero.')
add(1,'Ratio: equal differences and a meaningful zero','Two classifications, two questions','Discrete/continuous: which values are possible?\nMeasurement level: which comparisons are meaningful?',table=[['Variable','Possible values','Measurement level'],['Order count','Discrete','Ratio'],['Waiting duration','Continuous','Ratio'],['Celsius temperature','Usually continuous','Interval'],['Recorded calendar year','Discrete','Interval']],hint='R storage type is another issue: numeric storage does not prove quantitative meaning.')
asset(1,'Summary: what each measurement level adds','Your measurement-level overview','measurement-scales-reference.png',hint='Instructor-supplied diagram. Each step adds meaningful comparisons; ratio denominators must be nonzero.')
add(1,'Summary: what each measurement level adds','Reading the progression carefully','Nominal distinguishes membership; ordinal adds order.\nInterval adds equal differences; ratio adds meaningful ratios.\nThis progression concerns operations, not the value of an analysis.\nClassify “grades” or “medical scores” from their actual definitions.')
asset(1,'The descriptive statistics toolbox','The descriptive statistics toolbox','statistics-toolbox-teacher.png','Describe the observations we have.\nDescription alone does not establish generalization or causation.')
asset(1,'The descriptive statistics toolbox','Complementary tools','descriptive-toolbox.svg','Tables organize. Charts reveal patterns. Measures quantify features.')
add(1,'Tables: organize the information','Tables organize observations','Frequency tables summarize one variable.\nCrosstabs summarize combinations of two categorical variables.\nKeep counts, denominators, and units visible.')
add(1,'Frequency and relative frequency','Frequency and relative frequency','Frequency f: number of observations in a category or class.\nRelative frequency = f / n.\nPercentage = 100 × f / n.',table=csvtable('lesson1-quality_table.csv',headers=['Quality','Frequency','Relative frequency','Percent']),hint='150 of 300 restaurants (50%) are Very Good; this describes the recorded restaurants.')
add(1,'Grouped frequency tables','Audit case','An audit manager asks how long audits take and how much durations vary.\nUse 20 recorded audit durations, measured in days.',arabic='يسأل مدير التدقيق عن المدد اللازمة للتدقيق ومدى تفاوتها.\nنستخدم المدد المسجّلة لعشرين عملية تدقيق، مقيسة بالأيام.')
add(1,'Grouped frequency tables','Grouped numerical frequencies','Classes group nearby numerical values.\n[15,20) includes 15 and excludes 20.\n20 belongs to [20,25). Avoid gaps and overlaps.',table=csvtable('lesson1-audit_frequency.csv',headers=['Audit duration class (days)','Frequency']),hint='Cumulative counts answer ordered threshold questions; crosstabs count combinations.')
add(1,'Charts: choose a display for the question','The question chooses the chart','One category variable: bar chart, sometimes a pie chart.\nOne numerical distribution: histogram or dot plot.\nNumerical values across groups: aligned boxplots.\nTwo numerical variables: scatterplot.\nValues over time: a time-series line chart.',hint='Separate category bars; adjacent histogram intervals. Avoid misleading 3D decoration.')
plot(1,'Charts: choose a display for the question','An ordered categorical display','fig-quality-bar','Preserve the natural Good, Very Good, Excellent order.')
asset(1,'See the observations, then summarize their distribution','Every audit remains visible','book-fig-2-11.png','Each dot is one audit. Stacks show repeated durations.',hint='Anderson et al., 8th ed., Figure 2.11, p.52. © 2020 Cengage Learning. Attributed excerpt.')
plot(1,'See the observations, then summarize their distribution','The same audits, grouped','fig-audit-histogram','The histogram uses the grouped table’s 5-day boundaries.',hint='The 33-day audit remains in the data; investigate its context before any exclusion.')
add(1,'Numerical measures: quantify the pattern','What does a number summarize?','Center: mean, median, mode.\nVariability: range, variance, SD, IQR.\nPosition: percentiles, quartiles, z-scores.\nAssociation: covariance and Pearson correlation.\nShape and unusual values need a plot and context.')
add(1,'Location','Location summaries','Mean: add all values and divide by their count.\nMedian: middle value or middle-pair average after sorting.\nMode: most frequent value or category, possibly tied.',hint='Arbitrary category codes do not support meaningful means or standard deviations.')
add(1,'Spread and position','Spread and position summaries','Range = maximum − minimum. IQR = Q3 − Q1.\nSample variance divides squared deviations by n − 1.\nSample SD is its square root, in original units.\nCV expresses SD relative to a suitable positive ratio-scale mean.\nA z-score expresses distance from the mean in SD units.')
add(1,'Spread and position','The Audit numerical overview','These measures describe different features of the same 20 audits.',table=csvtable('lesson1-summary_table.csv'),hint='Quartiles use type = 6. Center 19.25/18 days; SD ≈ 5.44 days; Q1/Q3 = 15/22 days.')
add(1,'Spread and position','State the percentile convention','The book uses position (n + 1)p / 100 and interpolation.\nR’s type = 6 follows this convention for the interior percentiles here.\nR defaults to type = 7, so specify the method.')
plot(1,'Combine the tools to answer the business question','Return to the Restaurant question','fig-price-boxplot','Compare medians, spreads, overlap, and group sizes.',hint='Overview plot uses ggplot2 boxplot defaults. Lesson 3 aligns plots with explicit type-6 quartiles.')
add(1,'Combine the tools to answer the business question','Electronics case','Do weeks with more commercials tend to have higher sales?\nEach of ten rows pairs one week’s commercials and sales.\nSales are recorded in hundreds of USD.',arabic='هل تميل الأسابيع ذات الإعلانات الأكثر إلى تسجيل مبيعات أعلى؟\nيجمع كل صف من الصفوف العشرة عدد الإعلانات ومبيعات الأسبوع نفسه.\nسُجّلت المبيعات بمئات الدولارات الأمريكية.')
plot(1,'Combine the tools to answer the business question','Paired numerical observations','fig-advertising-sales','Describe association, then state what the data cannot establish.',hint='A near-zero linear correlation can coexist with a nonlinear relationship. Association does not establish causation.')
add(1,'Choose a tool: a short checklist','A short analytical checklist','Define the observational unit, units, and precision.\nClassify the variables and measurement levels.\nState the question, then choose matching summaries.\nInterpret the finding and its limitations.',hint='Pause for the Lesson 1 Quarto exercises.')
add(1,'Data for this lesson','Data and source scope','Use the prepared CSVs and their data guide.\nRestaurant: 300 records; Audit: 20; Electronics: 10.\nSoftDrink is developed next.\nThese historical teaching records do not describe today’s market.')
add(1,'References and provenance','Textbook checks and attribution','Main reference: Essentials of Modern Business Statistics with Microsoft Excel, 8th ed.\nAudit: all 20 printed values match. Electronics: all 10 pairs match.\nRestaurant: first 10 printed rows and all 12 crosstab cells match.\nRemaining individual Restaurant records are not printed for comparison.')

# MODULE02_LESSON2
divider(2,'Lesson 2: Frequency tables and charts','Turn observations into a distribution, then explain the display.','What we will learn')
add(2,'What we will learn','From observations to interpretation','Count categories and construct numerical classes.\nChoose and read the corresponding displays.\nExplain shape, center, spread, and unusual features.\nKeep denominators and units explicit.')
add(2,'Business case: which soft drinks were purchased?','SoftDrink case','Which brands were selected in 50 recorded purchases?\nOne observation is one purchase, not necessarily one distinct customer.',arabic='ما العلامات التجارية المختارة في خمسين عملية شراء مسجّلة؟\nتمثّل كل مشاهدة عملية شراء واحدة، وليس بالضرورة عميلًا مختلفًا.',hint='Use brand_book_label. Documented name mapping preserves the original purchase counts.')
add(2,'From observations to a frequency table','A valid frequency distribution','Each observation belongs to exactly one category.\nUse consistent labels and handle missing values explicitly.\nDo not count a record twice. Relevant zero-count categories may remain.')
add(2,'From observations to a frequency table','Count, proportion, and percentage','Relative frequency = f / n. Percentage = 100f / n.\n0.38 is 38%, not 0.38%.\nThe totals here are 50, 1, and 100%.',table=csvtable('lesson2-brand_table.csv',headers=['Brand','Frequency','Relative frequency','Percent']),hint='Coca-Cola: 19/50 = 38%. Compute Pepsi’s share from 13 purchases before checking Quarto.')
add(2,'From observations to a frequency table','Frequency calculations in R','Counts become proportions only after choosing the denominator.',hint='Calculate from unrounded values; round the display only.')
plot(2,'Bar charts: compare categories','Bar charts compare categories','fig-soft-drink-bars','Descending frequency aids comparison of these nominal brands.',hint='Start the quantity axis at zero. Retain meaningful order for ordinal categories.')
add(2,'Bar charts: compare categories','Ordering and interpretation','Alphabetical order helps lookup; descending counts help comparison.\nCounts and percentages from one sample are rescalings of the same finding.\nObserved purchase shares do not establish market share or profit.')
plot(2,'Pie charts: show shares of one whole','Pie charts describe one whole','fig-soft-drink-pie','Categories must be nonoverlapping parts of a named total.',hint='Coca-Cola’s 38% is 136.8°. Discuss the tied shares and long labels; bars often make them easier to compare.')
add(2,'Percentages need a denominator','Percentages need a denominator','Name the whole: 50 recorded purchases.\nDifferent sample sizes and sampling coverage matter in comparisons.\nNominal categories have no natural cumulative order.\nThe top three shares total 80%; “top three” is an analytical choice.')
add(2,'Business case: how long do audits take?','Audit-duration case','Describe 20 year-end audit completion times, recorded in days.\nWhich ranges are common, and how many finish before a threshold?\nOne observation is one audit.',arabic='نصف مدد إنجاز عشرين عملية تدقيق لنهاية السنة، والمسجّلة بالأيام.\nما فئات المدة الأكثر شيوعًا، وكم عملية انتهت قبل حد محدد؟\nتمثّل كل مشاهدة عملية تدقيق واحدة.',hint='These observations do not promise a future client’s completion date.')
add(2,'Group numerical values into classes','Numerical classes','The observed minimum and maximum are 12 and 33 days.\nFive classes suggest width (33 − 12)/5 = 4.2 days.\nUse convenient 5-day classes starting at 10.\nGrouping reveals patterns but loses individual detail.')
add(2,'Group numerical values into classes','Boundary rules','Use [10,15), [15,20), [20,25), [25,30), [30,35).\nInclude lower endpoints and exclude upper endpoints.\n15 belongs to the second class; 20 belongs to the third.\nEvery value must enter exactly one class, including the maximum.')
add(2,'Group numerical values into classes','Audit grouped frequencies','The modal class is 15–<20 days: 8 audits, or 40%.\nA modal class does not identify an exact modal duration.',table=csvtable('lesson2-audit_table.csv',headers=['Days','Frequency','Relative frequency','Percent']),hint='For whole-day records, these reproduce the book’s 10–14, 15–19, and subsequent classes.')
add(2,'Group numerical values into classes','Class construction in R','Choose boundaries deliberately before counting.')
plot(2,'Histograms: reveal the numerical distribution','Audit histogram','fig-audit-frequency-histogram','Equal-width rectangles count observations in neighboring numerical intervals.',hint='Most audits lie below 25 days. A longer observation warrants context, not automatic deletion.')
add(2,'What does a distribution tell us?','What does a distribution describe?','Where observations concentrate, spread out, or leave gaps.\nThe x-axis shows measured values. The y-axis shows its labeled quantity.\nA histogram is not a time trend unless time itself is the measured variable.')
add(2,'What does a distribution tell us?','Four questions for a histogram','Shape: balance, tail direction, and prominent peaks?\nCenter: where is a typical region?\nSpread: how far do values extend and concentrate?\nUnusual features: gaps, isolated values, or small separated groups?',hint='Read horizontal units and scale before comparing apparent widths.')
plot(2,'Skewness: name the direction of the longer tail','Skewness follows the tail','fig-histogram-shapes','Symmetric: similar sides. Right-skewed: longer right tail. Left-skewed: longer left tail.',hint='Constructed teaching illustrations, not observed Audit data or evidence of normality.')
add(2,'Skewness: name the direction of the longer tail','Shape needs careful language','Name skewness from the tail, not the tallest bar.\nIn many familiar one-peaked distributions, extremes pull the mean toward the tail.\nThat is not a universal mean/median ordering rule.\nA symmetric histogram alone does not establish a normal distribution.')
plot(2,'Modality: count prominent peaks, not every uneven bar','Prominent peaks and modality','fig-histogram-modality','Unimodal: one prominent peak. Bimodal: two. Multimodal: several.',hint='Artificial teaching patterns. Small uneven bars are not automatically distinct modes.')
add(2,'Modality: count prominent peaks, not every uneven bar','Possible peaks need checking','Several peaks can suggest mixed groups worth investigating.\nThey do not prove that those groups exist.\nSampling variation, rounding, bin width, and starting points affect the display.')
add(2,'Additional comparison: recorded student ages and heights','The supplementary measurement file','The local file contains 8,239 age/height records.\nIt omits names and identifiers.\nPopulation, collection method, real/simulated status, and units are undocumented.\nUse recorded units and keep this separate from the textbook cases.')
plot(2,'Additional comparison: recorded student ages and heights','Your age-and-height comparison','fig-student-histogram-comparison','Age has a long right tail; height has a more balanced central concentration.',hint='All 8,239 records remain. Different scales and bin widths prevent direct width/count comparisons.')
add(2,'Additional comparison: recorded student ages and heights','Limits of the supplementary comparison','Small bumps do not establish subpopulations or exact normality.\nUncommon ages or heights are not automatically errors.\nDo not treat this as a verified university survey or infer missing units.')
plot(2,'Unusual observations and the effect of bins','Same audits, different bins','fig-audit-bin-sensitivity','The same 20 values appear with 1-, 5-, and 10-day bins.',hint='The dashed line marks 33 days, not an outlier threshold. Taller combined bins do not mean more audits overall.')
add(2,'Unusual observations and the effect of bins','A display choice can create a feature','Check several sensible widths and starting points.\nReturn to the raw values before naming a small peak or isolated group.\nA histogram alone provides no universal outlier cutoff.\nLesson 3 introduces an explicit IQR screening rule.')
add(2,'Read the Audit histogram in four sentences','Audit interpretation in four sentences','Shape: a longer upper tail and one prominent peak in 5-day bins.\nCenter: high teens; exact mean 19.25 and median 18 days.\nSpread: observed durations run from 12 to 33 days.\nUnusual features: investigate the sparse upper end and 33-day audit.')
asset(2,'Keep the individual values in view','The dot plot preserves individual values','book-fig-2-11.png','One dot per audit; stacks preserve repeated durations.',hint='Anderson et al., 8th ed., Figure 2.11, p.52. © 2020 Cengage Learning.')
add(2,'Bar chart or histogram?','Bar chart or histogram?',table=[['Feature','Bar chart','Histogram'],['Horizontal meaning','Distinct categories','Numerical intervals'],['Order','Useful order; retain ordinal order','Numerical order'],['Separation','Gaps distinguish categories','Neighboring rectangles'],['Width','Consistent display choice','Represents interval width'],['Question','How common is each category?','How are values distributed?']])
add(2,'Bar chart or histogram?','Unequal class widths need density','With unequal widths, count heights can mislead.\nHistogram area must represent frequency.\nDensity height = frequency / class width,\nor relative frequency / class width.\nOur equal-width examples can use count heights directly.')
add(2,'Cumulative frequencies: answer a threshold question','Cumulative frequencies','Add counts through successive ordered classes.\nThe denominator remains the same 20 audits.',table=csvtable('lesson2-cumulative.csv',headers=['Duration threshold','Cumulative audits','Cumulative percent']),hint='17/20 = 85% took less than 25 days; 3/20 = 15% took at least 25 days.')
add(2,'Cumulative frequencies: answer a threshold question','A threshold inside a class','Grouped counts cannot identify exactly how many are below 18 days.\nReturn to the CSV for a threshold inside a class.\n“Less than 20” and “20 or less” differ when a 20-day value is present.')
asset(2,'Summary: choose and explain the display','Frequency workflow summary','frequency-workflow.svg',hint='Pause for the matching Quarto practice; keep meaning, construction, display, and interpretation aligned.')
add(2,'Data and references','Data checks and limits','SoftDrink totals match after the documented name mapping; order is not asserted.\nAll 20 printed Audit observations match.\nShape/modality examples are artificial; student measurements have metadata limits.\nThe attributed dot plot remains distinct from original course R graphics.')

# MODULE02_LESSON3
divider(3,'Lesson 3: Numerical measures','Connect each measure to the distribution and the question.','What we will learn')
add(3,'What we will learn','Center, variability, and position','Interpret mean, median, and mode.\nExplain what mean and range preserve and conceal.\nUse variance, SD, quartiles, IQR, CV, and z-scores appropriately.\nCompare distributions with consistent units and conventions.')
add(3,'Business case: describe a typical audit and its variability','A typical audit and its variability','Describe the same 20 year-end audit durations, in days.\nWhat duration is typical, and how much do durations differ?',arabic='نصف المدد نفسها لعشرين عملية تدقيق لنهاية السنة، مقيسة بالأيام.\nما المدة المعتادة، وإلى أي حد تختلف مدد التدقيق؟',hint='An observed sample describes these audits; it does not guarantee a future completion time.')
add(3,'Mean, median, and mode: three meanings of typical','Three meanings of typical','Mean balances all numerical values.\nMedian locates the middle after sorting.\nMode identifies the most frequent value or category.\nChoose according to the question; the measures are not interchangeable.')
add(3,'Mean: balance all the numerical values','The arithmetic mean','x̄ = (Σ xᵢ) / n\nAdd all observations, then divide by their number.\nFor Audit: total 385 days / 20 audits = 19.25 days.')
add(3,'Mean: balance all the numerical values','Why the mean is useful','It compresses many observations into one summary of their level.\nIt keeps the original units.\nMean × number of observations = total.\nEvery value contributes, which matters for total workload.')
add(3,'Mean: balance all the numerical values','What the mean leaves out','It does not show how values are distributed.\nAn extreme value can pull it away from most observations.\nSensitivity can matter for totals while weakening a typical-value description.\nA mean needs a spread measure and a plot.')
add(3,'Median: locate the middle after sorting','Median: the middle by rank','Sort the values before finding the middle.\nWith an even n, average the two middle numerical observations.\nFor 20 audits, positions 10 and 11 are both 18 days.\nMedian = (18 + 18) / 2 = 18 days.',hint='With ties, “half below and half above” need not mean strictly below and strictly above.')
add(3,'Mode: identify the most frequent value','Mode: frequency rather than rank','The most frequent exact audit duration is 18 days.\nA mode can be tied; report all equally most frequent values.\nFor categorical data, a modal category remains meaningful.\nR’s mode() reports a storage mode, not the statistical mode.',table=csvtable('lesson3-center.csv',headers=['Measure','Days']))
plot(3,'Mode: identify the most frequent value','Two centers in the Audit data','fig-audit-center','The mean is 19.25 days; the median is 18 days.',hint='Longer durations pull the mean upward here. This ordering alone is not a universal skewness test.')
add(3,'When the mean conceals the typical value','Your seven-dollar example','Amounts: USD 1, 2, 3, 3, 3, 1, 100.\nTotal = USD 113. Mean = 113/7 ≈ USD 16.14.\nThe mean lies above six of the seven observations.\nMedian and mode are both USD 3.',hint='Original instructor slide 38 / reference PDF p.51. No business setting is specified in the source.')
asset(3,'When the mean conceals the typical value','Your original mean example','teaching-slides/instructor-reference-p51.png',hint='Instructor-provided reference, original slide 38 (PDF p.51). The preceding slide gives the reduced explanation.')
add(3,'When the mean conceals the typical value','What this example does and does not show','The mean correctly relates the total to seven observations.\nUSD 3 better describes the middle or most frequent amount here.\nMedian and mode do not supply the total or describe spread.\nRetain a valid USD 100 observation even when it makes the mean untypical.')
add(3,'Variability: how different are the durations?','Why center needs variability','A representative mean still tells us nothing by itself about separation.\nYour five sets all have mean 200, despite different internal variation.',table=[['Set','Original values','Mean','Range'],['S1','100, 200, 300','200','200'],['S2','200, 200, 200','200','0'],['S3','0, 600, 0','200','600'],['S4','−600, 600, 600','200','1200'],['S5','−2000, 2500, 100','200','4500']],hint='Instructor slides 44–45 / PDF pp.60–61. Conceptual values in arbitrary units, not audit days.')
add(3,'Variability: how different are the durations?','The same mean can conceal different data','S2 has no variation: every observation is 200.\nS5 runs from −2000 to 2500.\n“Mean = 200” correctly summarizes a shared average.\nIt compresses away their differences. Describe center and dispersion together.')
add(3,'Range: the full observed span','Range: the observed endpoints','Range = maximum − minimum.\nFor Audit: 33 − 12 = 21 days.\nFor S1–S5: 200, 0, 600, 1200, and 4500 units.\nUseful for the full observed span, but it uses only two observations.')
add(3,'The range is sensitive to an extreme value','The USD 99 range','Return to USD 1, 2, 3, 3, 3, 1, 100.\nRange = 100 − 1 = USD 99.\nSix of seven observations occupy only USD 1 to USD 3.\nBoth the wide full span and tight main cluster are real features.')
add(3,'The range is sensitive to an extreme value','A hypothetical endpoint change','If USD 100 were USD 1000, the range would be USD 999.\nThe other six observations would remain exactly the same.\nAn endpoint change can dominate the range.',hint='This is a labeled hypothetical sensitivity illustration. The CSV still contains USD 100.')
add(3,'The range misses the values between the endpoints','Range misses internal differences','Original course illustration, arbitrary units:\nA = 0, 5, 5, 5, 10.\nB = 0, 0, 5, 10, 10.\nBoth have mean 5 and range 10. Their internal patterns differ.')
plot(3,'The range misses the values between the endpoints','Equal range, different internal spread','fig-same-range-different-spread','A concentrates at the center; B concentrates at the endpoints.',hint='Original course illustration. Stacks preserve repeated observations; the dashed line is the shared mean.')
add(3,'Mean absolute deviation: every distance contributes','Why use every deviation?','To describe internal spread, consider each distance from the mean.\nSigned deviations sum to zero, so they cancel.\nAbsolute values prevent this cancellation.\nMean absolute deviation = Σ|xᵢ − x̄| / n.')
add(3,'Mean absolute deviation: every distance contributes','Mean absolute deviation for A and B','A’s distances: 5, 0, 0, 0, 5. Average = 2 units.\nB’s distances: 5, 5, 0, 5, 5. Average = 4 units.\nEvery observation contributes, so the measure distinguishes internal spread.',hint='R’s mad() defaults to a scaled median absolute deviation, a different measure.')
add(3,'Mean absolute deviation: every distance contributes','Absolute and squared distances','Absolute contributions grow linearly with distance.\nSquared contributions emphasize larger distances more strongly.\nThis choice serves different purposes.\nNeither approach is automatically resistant to extremes or universally better.')
asset(3,'Sample variance: average squared variation, with an adjustment','Your variance illustrations','teaching-slides/instructor-variance-diagrams.png','Conceptual illustrations from your supplied variance/SD slide.',hint='Original slide 47 / PDF p.63. The displayed 1/n formula is a population-style average; sample variance uses n − 1.')
add(3,'Sample variance: average squared variation, with an adjustment','Sample variance','s² = Σ(xᵢ − x̄)² / (n − 1), for n > 1.\nSquaring prevents positive and negative deviations from cancelling.\nVariance uses squared measurement units.\nEstimating the mean uses one degree of freedom.')
add(3,'Sample variance: average squared variation, with an adjustment','Sample or complete population?','A complete population variance uses its population mean and denominator N.\nFor these 20 audits, we use the sample denominator n − 1.\n“All rows available” does not itself make the file a population.\nThe designation depends on the question.')
add(3,'Sample variance: average squared variation, with an adjustment','Why the n − 1 adjustment?','Under independent sampling from a common population with finite variance,\nthe n − 1 adjustment makes sample variance an unbiased estimator.\nThis justification does not turn any convenience dataset into an independent sample.')
add(3,'Standard deviation: spread in the original units','Standard deviation','s = √s².\nAudit sample variance ≈ 29.57 days². Sample SD ≈ 5.44 days.\nSD summarizes spread around the mean in the original units.\nNormality is not required merely to calculate it.')
add(3,'Standard deviation: spread in the original units','What SD does not mean','SD is not the standard error.\nIt is not the maximum possible deviation.\nIt does not guarantee that every observation lies within one SD of the mean.',table=[(['Set']+r if i==0 else [['A','B'][i-1]]+r) for i,r in enumerate(csvtable('lesson3-spread_comparison.csv',headers=['n','Mean','Range','Mean abs. deviation','Sample SD']))],hint='A and B share n, mean, and range. Mean absolute deviation and SD distinguish their internal spread.')
add(3,'Standard deviation: spread in the original units','What improved, and what remains?','Using all values addresses the internal spread that range misses.\nMean absolute deviation and SD still respond to extreme values.\nNext, quartiles and IQR describe the distribution’s central portion.')
add(3,'Percentiles and quartiles: locate values by rank','Percentiles and quartiles','Percentiles locate values in an ordered distribution.\nQ1, Q2, Q3 correspond to the 25th, 50th, 75th percentiles.\nQ2 is the median. Ties and interpolation matter in small samples.\nState the convention used to compute sample percentiles.')
add(3,'Percentiles and quartiles: locate values by rank','The book’s percentile positions','Lp = (n + 1)p / 100, with interpolation between adjacent values.\nFor n = 20: L25 = 5.25, L50 = 10.5, L75 = 15.75.\nThe adjacent Audit values give Q1 = 15, Q2 = 18, Q3 = 22 days.')
add(3,'Percentiles and quartiles: locate values by rank','Consistent software conventions','R’s IQR() and ordinary ggplot2 boxplots have their own defaults.\nCalculate IQR from the stated quartiles.\nUse explicitly supplied boxplot statistics when matching type 6.\nAgreement for Audit does not make methods interchangeable in every dataset.',hint='Do not extrapolate the book’s interior-position rule beyond the available ordered values.')
add(3,'Interquartile range: the width of the middle half','Interquartile range','IQR = Q3 − Q1 = 22 − 15 = 7 days.\nIt describes the width of the central portion.\nWith ties, an inclusive Q1–Q3 interval need not contain exactly half the records.\nIQR is less sensitive to extremes, while leaving tail detail out.')
add(3,'Five-number summaries and boxplots','Five-number summary','Minimum, Q1, median, Q3, maximum.\nFor Audit: 12, 15, 18, 22, 33 days.')
add(3,'Five-number summaries and boxplots','Boxplot screening rules','The box extends from Q1 to Q3 and marks the median.\nLower fence = Q1 − 1.5IQR. Upper fence = Q3 + 1.5IQR.\nWhiskers stop at observed values inside the fences.\nBeyond-fence observations remain part of the data.')
asset(3,'Five-number summaries and boxplots','Your boxplot anatomy diagram','boxplot-anatomy-reference.png',hint='Supplied schematic. Its “Minimum” and “Maximum” formulas label fences, not generally observed endpoints.')
add(3,'Five-number summaries and boxplots','Fences and whiskers are different','Audit fences: 4.5 and 32.5 days.\nObserved whisker endpoints: 12 and 28 days.\nThe 33-day audit is flagged but remains in the dataset.\nAn outlier flag prompts investigation, not automatic deletion.')
plot(3,'Five-number summaries and boxplots','Audit boxplot with the stated convention','fig-audit-book-boxplot','Explicit type-6 quartiles align the plot and numerical summary.',hint='The five-number summary still includes the maximum 33, even though the upper whisker ends at 28.')
add(3,'How much does a long observation change the summary?','A sensitivity comparison','Hypothetically replace the longest audit, 33 days, with 60 days.\nCompare measures without changing the source data.',table=csvtable('lesson3-sensitivity.csv',headers=['Dataset','Mean (days)','Median (days)','SD (days)','IQR (days)']),hint='Mean and SD change strongly; median and IQR remain unchanged in this illustration.')
add(3,'Coefficient of variation','Coefficient of variation','CV = 100s / x̄, expressed as a percentage.\nCompare relative spread for suitable ratio-scale variables.\nRequire a meaningful zero and a positive, nonzero mean.\nA Celsius-temperature CV is not meaningful.',hint='Audit CV ≈ 28.25%; a mean near zero makes the ratio unstable.')
add(3,'Z-score','Z-scores','z = (x − x̄) / s, with s > 0.\nSign indicates which side of the mean; magnitude gives distance in SD units.\nFor the 33-day audit, z ≈ 2.53.\nThis calculation does not establish normality or an automatic outlier rule.')
add(3,'Two additional measures: CV and z-scores','Relative spread and standardized position','CV describes spread relative to a suitable mean.\nA z-score locates one value relative to the mean and SD.\nThey answer different questions and both need context.')
add(3,'Business case: compare restaurant price distributions','Compare Restaurant price distributions','Compare typical meal prices and variability across the 300 restaurants.\nRatings are ordered Good, Very Good, Excellent; prices are in USD.\nOne observation remains one restaurant.',arabic='نقارن أسعار الوجبات المعتادة ومدى تفاوتها في بيانات ثلاثمئة مطعم.\nفئات الجودة مرتبة: جيد، وجيد جدًا، وممتاز؛ والأسعار بالدولار الأمريكي.\nتظل كل مشاهدة ممثّلة لمطعم واحد.',hint='These observational group comparisons describe association rather than a causal quality effect.')
add(3,'Business case: compare restaurant price distributions','Group center and spread','Retain each group’s size alongside its summaries.',table=csvtable('lesson3-group_summary.csv',cols=['Quality','N','Mean','Median','SD'],headers=['Quality','n','Mean (USD)','Median (USD)','SD (USD)']))
add(3,'Business case: compare restaurant price distributions','Group quartiles and IQR','Use the same type-6 convention across every group.',table=csvtable('lesson3-group_summary.csv',cols=['Quality','Q1','Q3','IQR'],headers=['Quality','Q1 (USD)','Q3 (USD)','IQR (USD)']),hint='Good has IQR USD 10; Very Good has the largest IQR, USD 12.')
plot(3,'Business case: compare restaurant price distributions','Compare distributions together','fig-restaurant-consistent-boxplots','Medians increase from USD 19.50 to 25.00 to 34.50, with overlap.',hint='Higher typical price and greater variability are different questions. A category does not determine an individual price.')
asset(3,'Summary: match the measure to the question','Numerical measures summary','numerical-measures-summary.svg',hint='Describe center, variability, and position with units, conventions, and a plot.')
add(3,'Summary: match the measure to the question','A limitation suggests a companion','Mean pulled by extremes: add median and a distribution plot.\nCenter hides variation: add a spread measure.\nRange misses internal values: add absolute deviation or SD.\nSD responds to extremes: add IQR and the median.\nEvery companion still leaves some information out.',hint='Pause for Lesson 3 practice. Preserve valid observations and explain the business meaning.')
add(3,'Sources and data','Your examples and their provenance','Seven dollar amounts: instructor slide 38 / reference PDF p.51.\nFive equal-mean sets: slides 44–45 / PDF pp.60–61.\nAbsolute and squared deviation reasoning: slides 46–47.\nThe A/B equal-range comparison is an original course illustration.\nThe CSV and source notes preserve values, units, and origins.')

# MODULE02_LESSON4
divider(4,'Lesson 4: Relationships between variables','Choose tools for the variable pair.\nState the comparison and its denominator.')
add(4,'What we will learn','From one variable to relationships','Compare category combinations, group distributions, and paired numbers.\nUse a plot and numerical summaries together.\nDescribe association with its observational limits.')
add(4,'Choose tools for the variable pair','Match the pair to the question',table=[['Variable pair','Tools','Question'],['Categorical + categorical','Crosstab, percentages, bars','Which combinations occur?'],['Categorical + numerical','Group summaries, boxplots','How do distributions differ?'],['Numerical + numerical','Scatterplot, covariance, correlation','How do paired values move?']])
add(4,'Business case: quality ratings and meal-price bands','Restaurant: quality and price bands','Use 300 historical Los Angeles restaurant records.\nQuality is ordered; meal price is measured in USD.\nAsk how price bands differ within quality, and quality within price.',arabic='نستخدم ثلاثمئة سجل تاريخي لمطاعم في لوس أنجلوس.\nفئات الجودة مرتبة، وسعر الوجبة مقيس بالدولار الأمريكي.\nنسأل كيف تتوزع فئات السعر داخل كل مستوى جودة، وكيف تتوزع الجودة داخل كل فئة سعر.')
add(4,'Crosstabs: count combinations','Build a crosstab','Each cell counts one combination of quality and price band.\nBands are [10,20), [20,30), [30,40), [40,50) USD.\nUSD 20 belongs to the second band.',table=csvtable('lesson4-counts.csv'),hint='Row and column margins sum to 300. Each restaurant appears in one interior cell.')
add(4,'Joint, marginal, and conditional percentages','Ask “among whom?” first','64 restaurants are Very Good and priced USD 20–<30.\nJoint: 64 / 300 = 21.33% of all restaurants.\nMarginal: 150 / 300 = 50% are Very Good.\nWithin Very Good: 64 / 150 = 42.67%.\nWithin USD 20–<30: 64 / 118 = 54.24%.',hint='Same numerator, different denominator: these percentages answer different questions.')
add(4,'Row percentages: price distribution within quality','Within a quality group','Divide each cell by its row total; each row sums to 100%.',table=csvtable('lesson4-row-percentages.csv'),hint='Half of Good restaurants are in USD 10–<20. Retain group sizes: 84, 150, and 66.')
plot(4,'Row percentages: price distribution within quality','Compare price distributions within quality','fig-restaurant-conditional-bars','Use a common 100% scale for groups of different sizes.',hint='Compare precise values using the table; middle stacked segments have different baselines.')
add(4,'Row percentages: price distribution within quality','A threshold comparison','Among Excellent restaurants, 50 / 66 = 75.8% cost at least USD 30.\nAmong Good restaurants, 2 / 84 = 2.4% cost at least USD 30.\nState the quality group in each denominator.\nCalculate using counts, then round the displayed result.',hint='Describe these records. Group differences alone do not show a causal quality effect.')
add(4,'Column percentages: quality distribution within price','Within a price band','Divide each cell by its column total; each column sums to 100%.',table=csvtable('lesson4-column-percentages.csv'),hint='Among USD 40–<50 restaurants, 22 / 28 = 78.6% are Excellent.')
add(4,'Column percentages: quality distribution within price','Reversing the condition changes the answer','Excellent among USD 40–<50: 22 / 28 = 78.6%.\nUSD 40–<50 among Excellent: 22 / 66 = 33.3%.\nA crosstab reveals association, not causation.\nBand choices and omitted subgroup structure can hide patterns.',hint='These data do not establish that one variable causes the other.')
add(4,'Business case: commercials and weekly electronics sales','Electronics: advertising and sales','Ten weekly pairs record television commercials and sales.\nSales are in hundreds of USD: 50 means USD 5,000.\nAsk whether weeks with more commercials tend to have higher sales.',arabic='تسجّل عشرة أزواج أسبوعية عدد الإعلانات التلفزيونية والمبيعات.\nالمبيعات مقيسة بمئات الدولارات الأمريكية؛ فالقيمة 50 تعني 5000 دولار.\nنسأل هل تميل الأسابيع ذات الإعلانات الأكثر إلى تسجيل مبيعات أعلى.',hint='Checked against the local Stereo workbook. The proposed explanatory variable does not establish a cause.')
add(4,'Business case: commercials and weekly electronics sales','The ten observed weekly pairs','One row pairs one week; sales are in hundreds of USD.',table=csvtable('lesson4-electronics.csv',headers=['Week','Commercials','Sales (hundreds of USD)']))
add(4,'Scatterplots: inspect the paired pattern','Keep each week’s pair together','Place commercials on x and sales on y.\nSorting the columns independently destroys the pairs.\nDo not connect points as a time path when describing this relationship.')
plot(4,'Scatterplots: inspect the paired pattern','Read the paired pattern','fig-electronics-scatterplot','Positive direction; approximately linear form; fairly close clustering.',hint='Describe variation and unusual observations as well as the overall direction.')
add(4,'Covariance: do deviations move together?','Covariance starts with deviations','Compare each value with its own variable’s mean.\nSame-sign deviations give a positive product.\nOpposite-sign deviations give a negative product.\nSample covariance = Σ[(x − x̄)(y − ȳ)] / (n − 1).')
add(4,'Covariance: do deviations move together?','Covariance for Electronics','x̄ = 3 commercials; ȳ = 51 hundreds of USD.\nSum of deviation products = 99.\nSample covariance = 99 / 9 = 11.\nUnits: commercials × hundreds of USD.\nIts magnitude depends on units, so it is not a standardized strength score.')
add(4,'Correlation: standardize the linear association','Pearson correlation','r = sample covariance / (sₓsᵧ).\nBoth variables must have nonzero variation.\nUnitless, from −1 to +1; sign gives linear direction.\nMagnitude describes linear association, not every possible pattern.')
add(4,'Correlation: standardize the linear association','Interpret the Electronics correlation','r ≈ 0.9305: a strong positive linear association in these ten weeks.\nIt is not a sales slope or “93% of sales.”\nRead the scatterplot before describing the coefficient.\nCalculation alone does not require normally distributed variables.',hint='Inference and prediction need additional assumptions, addressed later in the course.')
add(4,'Changing units: covariance changes, correlation stays','Change sales units','Convert hundreds of USD to USD by multiplying by 100.',table=csvtable('lesson4-units.csv',headers=['Sales unit','Sample covariance','Correlation'],digits=4),hint='Positive unit rescaling changes covariance and SD proportionally; correlation stays the same.')
plot(4,'Why a correlation coefficient needs its plot','The coefficient needs its plot','fig-correlation-patterns','Artificial examples: increasing line, decreasing line, and a curved pattern.',hint='The symmetric quadratic pattern has r = 0 despite a clear numerical relationship.')
add(4,'Why a correlation coefficient needs its plot','Limits of a single correlation','A near-zero r does not rule out a curved relationship.\nUnusual points, restricted ranges, or mixed groups can change r.\nA valid unusual observation is not automatically an error.\nOther factors could affect advertising and sales.\nTen observed weeks do not guarantee the same future relationship.')
add(4,'Summary: a defensible relationship description','A defensible relationship description','Name the variables, units, observational unit, and comparison.\nChoose tools for the pair and report the denominator.\nDescribe form, direction, variation, and unusual observations.\nUse summaries with the plot and state observational limits.',hint='Pause for Lesson 4 practice: calculate, interpret, and qualify the result.')
add(4,'Sources and data','Relationship sources','Essentials of Modern Business Statistics with Microsoft Excel, 8th ed.\nRestaurant and Electronics/Stereo use the checked teaching CSVs.\nFigures and calculations retain the extended lesson’s data and conventions.\nSee its Sources and data section for the scope of each workbook match.')

divider(5,'Lesson 5: Integrated review','Use the same sequence to produce a short reproducible report.')
add(5,'Purpose and submission','Your review report','Create one concise Quarto section per task.\nKeep readable tables, plots, and business interpretations together.\nState units and quartile conventions; preserve the source data.\nUse the extended review for the complete submission instructions.')
add(5,'1. Define the variables and choose tools','1. Define before summarizing','Identify the observational unit, variable meanings, and units.\nClassify type and measurement level.\nDistinguish counts from measured quantities.\nExplain why averaging an ID or brand code is not meaningful.')
add(5,'2. Summarize one categorical distribution','2. SoftDrink frequencies','Build counts, relative frequencies, percentages, and a bar chart.\nIdentify the most frequent brand and interpret the denominator.\nOne recorded purchase does not represent every consumer’s preference.')
add(5,'3. Describe a numerical distribution','3. Audit durations','Show the distribution and describe shape, center, spread, and unusual values.\nReport n, mean, median, range, SD, and type-6 quartiles/IQR.\nApply fences as screening flags, retaining valid observations.\nChoose a useful center/spread pair and explain its limitations.')
add(5,'4. Compare groups and percentages','4. Restaurant comparisons','Compare group n, medians, IQRs, and aligned boxplots.\nConstruct the four-band price crosstab.\nCompare “at least USD 30” within quality using the correct denominators.\nSeparate an observed association from a causal claim.')
add(5,'5. Describe numerical association','5. Electronics association','Inspect the scatterplot, then calculate covariance and correlation.\nExplain the units and the effect of changing sales units.\nDescribe linear direction and strength with the plot.\nState what these ten weekly pairs cannot establish.')
add(5,'Review checklist','Before submitting','Meaning: are variables, units, and denominators clear?\nTools: do the displays and measures answer the question?\nReproducibility: are data paths and conventions stated?\nInterpretation: does each number have a contextual explanation?\nLimitations: what does the summary leave out?',hint='The extended Quarto lessons remain the working material for code, practice, and full explanations.')


# Practical code comes from the evaluated Quarto source, never a second handwritten copy.
def chunk_code(lesson,label):
    matches=[]
    for m in re.finditer(r'```\{r[^\n]*\}\n(.*?)\n```',SOURCES[lesson],re.S):
        if re.search(r'^#\| label: '+re.escape(label)+r'\s*$',m[1],re.M):matches.append(m[1])
    assert len(matches)==1,(lesson,label,len(matches))
    value='\n'.join(line for line in matches[0].splitlines() if not line.startswith('#|')).strip()
    assert len([line for line in value.splitlines() if line.startswith('# ')])>=2,(lesson,label)
    assert not re.search(r'#\| (include|eval): false',matches[0]),(lesson,label,'hidden or unevaluated example')
    return value

def chunk_heading(lesson,label):
    inside=False;heading=None
    for line in SOURCES[lesson].splitlines():
        if line.lstrip().startswith('```'):inside=not inside
        if line.strip()=='#| label: '+label:return heading
        if not inside and re.match(r'^#{1,6} ',line):heading=re.sub(r'^#+ ','',line)
    raise ValueError((lesson,label))

def rslide(lesson,anchor,title,label,body,hint='',after=False):
    target=next(s for s in SLIDES if s['lesson']==lesson and s['title']==anchor)
    add(lesson,chunk_heading(lesson,label),title,body,hint=hint)
    slide=SLIDES.pop();slide['code']=chunk_code(lesson,label);slide['code_chunk']=label
    index=SLIDES.index(target)+(1 if after else 0)
    SLIDES.insert(index,slide)

# Keep the existing frequency/class slides, now using the exact Quarto examples.
for title,label in [('Frequency calculations in R','r-example-softdrink-frequency'),('Class construction in R','r-example-audit-classes')]:
    slide=next(s for s in SLIDES if s['title']==title)
    slide['code']=chunk_code(slide['lesson'],label);slide['code_chunk']=label

rslide(1,'One restaurant becomes one record','R example: load Restaurant data','r-example-restaurant-import',
       'Restaurant CSV: 300 restaurants; meal price in USD.',
       'Download the CSV from the Module 2 overview. Run inside the course RStudio project.')
rslide(1,'An ordered categorical display','R example: count quality ratings','quality-frequency',
       'Count the ordered categories before drawing the bars.',
       'Result: Good 84, Very Good 150, Excellent 66; percentages use all 300 restaurants.')
rslide(1,'An ordered categorical display','R example: Restaurant bar chart','fig-quality-bar',
       'Use the quality_table counts from the preceding example.',
       'geom_col() plots existing counts; the next slide shows this exact chart.')
rslide(1,'Grouped numerical frequencies','R example: load Audit data','r-example-audit-import',
       'Audit, book Table 2.4: 20 recorded durations in days.',
       'x names the raw audit-day vector used for numerical summaries.')
rslide(1,'The same audits, grouped','R example: Audit histogram','fig-audit-histogram',
       'Count raw durations using 5-day bins.',
       'Counts: 4, 8, 5, 2, 1. The next slide is the chart produced by this code.')
rslide(1,'State the percentile convention','R example: Audit quartiles','r-example-overview-quartiles',
       'x contains the 20 Audit durations in days.',
       'R output: 15, 18, 22 days. These are Q1, the median, and Q3.',after=True)
rslide(1,'Paired numerical observations','R example: load Electronics data','r-example-electronics-import',
       'Ten weekly pairs; sales are in hundreds of USD.',
       'Read the paired pattern now; Lesson 4 develops the plotting and association code.')

rslide(2,'A valid frequency distribution','R example: load SoftDrink data','soft-drink-import-example',
       'SoftDrink: 50 purchases; use the documented textbook labels.',
       'Run inside the course project. The preview shows the first six purchases.')
rslide(2,'Bar charts compare categories','R example: order the bars','r-example-order-brands',
       'Prepare the already counted brand_table.',
       'Descending counts put frequent brands first; the alphabetical rule resolves ties.')
rslide(2,'Bar charts compare categories','R example: SoftDrink bar chart','fig-soft-drink-bars',
       'Plot existing frequencies from the ranked table.',
       'The next slide shows the resulting chart of the 50 recorded purchases.')
rslide(2,'Numerical classes','R example: load Audit data','r-example-audit-import',
       'Audit: 20 recorded durations in days.',
       'The CSV contains raw observations; cut() and the histogram will use the same boundaries.')
rslide(2,'Audit histogram','R example: histogram boundaries','fig-audit-frequency-histogram',
       'Use the boundaries created with seq(10, 35, 5).',
       'A 20-day duration enters [20,25), matching the grouped table. The next slide shows the result.')

rslide(3,'Three meanings of typical','R example: load the audit durations','r-example-audit-import',
       'Book Table 2.4: 20 durations, recorded in days.',
       'Use this x throughout the numerical examples. The full CSV link is in the Quarto case introduction.')
rslide(3,'What the mean leaves out','R example: arithmetic mean','r-example-audit-mean',
       'Audit: x contains the 20 raw durations in days.',
       'R output: 19.25 days. Multiplying by 20 recovers the 385-day total.')
rslide(3,'Median: the middle by rank','R example: median','r-example-audit-median',
       'Use the same raw Audit durations.',
       'R output: 18 days, agreeing with the two middle ordered observations.',after=True)
rslide(3,'Two centers in the Audit data','R example: statistical mode','r-example-audit-mode',
       'Find the most frequent exact duration rather than using mode().',
       'R output: 18 days. The code retains all labels tied for the largest count.')
rslide(3,'Range: the observed endpoints','R example: endpoints and range','r-example-audit-range',
       'The range() function returns endpoints; the measure needs their difference.',
       'R output: 12 and 33 days, then 21 days. Internal positions do not enter this difference.',after=True)
rslide(3,'Absolute and squared distances','R example: mean absolute deviation','r-example-audit-absolute-deviation',
       'Apply the same distance idea to the textbook Audit data.',
       'R output: 4.2 days. Every absolute distance contributes; this is different from mad().')
rslide(3,'Standard deviation','R example: sample variance','r-example-audit-variance',
       'Audit: all 20 durations contribute squared deviations.',
       'R output: 29.56579 days squared, or 29.57 after rounding.')
rslide(3,'Standard deviation','R example: sample standard deviation','r-example-audit-sd',
       'Return the variability measure to the original unit.',
       'R output: 5.437443 days, or 5.44 after rounding.',after=True)
rslide(3,'Consistent software conventions','R example: type-6 quartiles','r-example-audit-quartiles',
       'Use raw Audit durations and state the book convention.',
       'R output: Q1 = 15, Q2 = 18, Q3 = 22 days.')
rslide(3,'Interquartile range','R example: IQR from our quartiles','r-example-audit-iqr',
       'Reuse the type-6 quartiles stored by the preceding example.',
       'R output: 7 days. This keeps the percentile convention consistent.',after=True)
rslide(3,'Coefficient of variation','R example: coefficient of variation','r-example-audit-cv',
       'Audit: compare sample SD with the positive mean duration.',
       'R output: 28.24646%, or 28.25%. This describes relative spread.',after=True)
rslide(3,'Z-scores','R example: the 33-day audit','r-example-audit-z',
       'Express the longest duration as distance from the mean in SD units.',
       'R output: 2.528762. The duration is about 2.53 sample SDs above the mean.',after=True)

rslide(4,'Build a crosstab','R example: load Restaurant data','r-example-restaurant-import',
       'Restaurant: quality is ordered; meal price is in USD.',
       'Run inside the course project; the CSV link is beside the case introduction in Quarto.')
rslide(4,'Build a crosstab','R example: count category pairs','r-example-restaurant-crosstab',
       'Create four 10-USD price bands and count each quality/band combination.',
       'The next table shows the 12 checked cell counts and their marginal totals.')
rslide(4,'Within a quality group','R example: row percentages','r-example-restaurant-row-percent',
       'Among restaurants in each quality row, how are price bands distributed?',
       'Each row sums to 100%. The next slide shows the calculated percentages.')
rslide(4,'Within a price band','R example: column percentages','r-example-restaurant-column-percent',
       'Among restaurants in each price band, how is quality distributed?',
       'Each column sums to 100%. Changing the margin changes the question.')
rslide(4,'The ten observed weekly pairs','R example: load Electronics data','r-example-electronics-import',
       'Ten weekly pairs; sales are in hundreds of USD.',
       'The next table displays the observations from this CSV.')
rslide(4,'Read the paired pattern','R example: Electronics scatterplot','fig-electronics-scatterplot',
       'Map commercials and sales from the same week; label each week.',
       'The next slide shows this exact chart; sales remain in hundreds of USD.')
rslide(4,'Pearson correlation','R example: sample covariance','r-example-electronics-covariance',
       'Define x and y from the two columns of the weekly table.',
       'R output: 11, in commercials × hundreds of USD. Its magnitude depends on units.')
rslide(4,'Interpret the Electronics correlation','R example: Pearson correlation','r-example-electronics-correlation',
       'Use the x and y vectors defined in the covariance example.',
       'R output: 0.9304906. Interpret the positive linear association with the scatterplot.')

# Put the parent overview before its two measures.
i=next(i for i,s in enumerate(SLIDES) if s['title']=='Relative spread and standardized position')
s=SLIDES.pop(i);j=next(i for i,s in enumerate(SLIDES) if s['title']=='Coefficient of variation');SLIDES.insert(j,s)
for i,s in enumerate(SLIDES,1):s['number']=i
starts={s['lesson']:s['number'] for s in SLIDES if s['kind']=='divider' and s['title'].startswith('Lesson ')}
SLIDES[0]['body']='\n'.join(f"Lesson {l}: {name}  (slide {starts[l]})" for l,name in enumerate(['Data types and toolbox','Frequency tables and charts','Numerical measures','Relationships between variables','Integrated review'],1))
rows=[]
for l,source in SOURCES.items():
    inside=False
    for n,line in enumerate(source.splitlines(),1):
        if line.lstrip().startswith('```'):inside=not inside
        if inside or not re.match(r'^#{1,6} ',line):continue
        heading=re.sub(r'^#+ ','',line)
        mapped=[s['number'] for s in SLIDES if s['lesson']==l and s['start']<=n<=s['end']]
        rows.append(dict(lesson=l,line=n,heading=heading,slides=mapped))
missing=[r for r in rows if not r['slides']]
assert not missing,missing
BUILD.mkdir(parents=True,exist_ok=True)
(BUILD/'r-code-coverage.json').write_text(json.dumps([dict(lesson=s['lesson'],slide=s['number'],title=s['title'],source=s['source'],chunk=s['code_chunk']) for s in SLIDES if s.get('code_chunk')],ensure_ascii=False,indent=2))
(BUILD/'slides.json').write_text(json.dumps(SLIDES,ensure_ascii=False,indent=2))
(BUILD/'coverage.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
manifest=dict(slide_count=len(SLIDES),lesson_counts={l:sum(s['lesson']==l for s in SLIDES) for l in FILES},headings_checked=len(rows),unmapped_headings=missing,r_code_slides=sum(bool(s['code']) for s in SLIDES))
(BUILD/'content-manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest))
