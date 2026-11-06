# Business-course answer key — 6 November 2026


## Part 1: regional category-manager briefing

|region  | total_sales| total_profit| margin_pct|
|:-------|-----------:|------------:|----------:|
|Central |    354141.8|     32155.52|      9.080|
|East    |    465698.3|     58292.22|     12.517|
|South   |    268816.0|     37900.52|     14.099|
|West    |    475329.5|     64609.49|     13.593|


## Practical 1: regional order counts

|region  |    n| percent|
|:-------|----:|-------:|
|Central |  769|  23.149|
|East    |  931|  28.025|
|South   |  549|  16.526|
|West    | 1073|  32.300|


## Practical 1: shipping-mode percentages within region

|        | First Class| Same Day| Second Class| Standard Class|
|:-------|-----------:|--------:|------------:|--------------:|
|Central |      13.654|    4.811|       20.026|         61.508|
|East    |      16.649|    5.478|       18.904|         58.969|
|South   |      14.390|    5.282|       19.672|         60.656|
|West    |      15.284|    5.405|       18.826|         60.485|


## Practical 1: dispatch within four days

|region  | orders| within_four_days_pct|
|:-------|------:|--------------------:|
|Central |    769|               60.208|
|East    |    931|               61.117|
|South   |    549|               58.652|
|West    |   1073|               59.180|


## Practical 1: listed returns within segment

|segment     | orders| listed_return_pct|
|:-----------|------:|-----------------:|
|Consumer    |   1710|             5.789|
|Corporate   |   1021|             5.975|
|Home Office |    591|             5.245|


## Practical 2: regional order sales

|region  | orders| total_sales| mean_sales| median_sales| sd_sales| iqr_sales|
|:-------|------:|-----------:|----------:|------------:|--------:|---------:|
|Central |    769|    354141.8|    460.522|      141.372| 1089.918|   490.396|
|East    |    931|    465698.3|    500.213|      158.610|  943.312|   525.536|
|South   |    549|    268816.0|    489.647|      170.352| 1274.906|   480.902|
|West    |   1073|    475329.5|    442.991|      155.160|  733.260|   471.468|


## Practical 2: five largest orders

|order_id       |    sales|    profit| line_count| quantity|
|:--------------|--------:|---------:|----------:|--------:|
|US-2023-145317 | 23661.23| -1789.733|          7|       25|
|US-2025-118689 | 18336.74|  8762.389|          5|       18|
|US-2023-139892 | 10539.90| -1878.789|          7|       37|
|US-2023-116904 |  9900.19|  4668.693|          4|       17|
|US-2025-117121 |  9892.74|  4946.370|          1|       13|


## Practical 2: top order revenue concentration

|rule                                                 | selected_orders| percent_orders| revenue_share_pct|
|:----------------------------------------------------|---------------:|--------------:|-----------------:|
|Top ceiling(10% of orders), ties ordered by order_id |             333|         10.024|            52.704|


## Practical 3: subcategories ranked by profit

|sub_category | lines| total_sales| total_profit| margin_pct|
|:------------|-----:|-----------:|------------:|----------:|
|Tables       |   215|  146071.990|    -9584.786|     -6.562|
|Bookcases    |   152|   84855.717|    -2888.930|     -3.405|
|Supplies     |   131|   30624.128|     -233.787|     -0.763|
|Fasteners    |   153|    2166.686|      644.569|     29.749|
|Labels       |   250|    8625.096|     3801.645|     44.077|
|Art          |   514|   18255.724|     4305.824|     23.586|
|Envelopes    |   183|   13097.828|     5522.418|     42.163|
|Machines     |    82|  145693.956|     6253.972|      4.293|
|Furnishings  |   641|   62790.070|     8959.981|     14.270|
|Appliances   |   301|   64605.229|    10272.737|     15.901|
|Storage      |   558|  154165.990|    13876.026|      9.001|
|Chairs       |   427|  232894.750|    18946.617|      8.135|
|Paper        |   911|   50784.488|    22012.726|     43.345|
|Binders      |  1023|  130624.688|    22552.021|     17.265|
|Accessories  |   500|  107434.086|    26264.279|     24.447|
|Copiers      |    46|   86628.642|    30586.035|     35.307|
|Phones       |   595|  224666.538|    31666.406|     14.095|


## Practical 3: subcategories ranked by margin

|sub_category | lines| total_sales| total_profit| margin_pct|
|:------------|-----:|-----------:|------------:|----------:|
|Tables       |   215|  146071.990|    -9584.786|     -6.562|
|Bookcases    |   152|   84855.717|    -2888.930|     -3.405|
|Supplies     |   131|   30624.128|     -233.787|     -0.763|
|Machines     |    82|  145693.956|     6253.972|      4.293|
|Chairs       |   427|  232894.750|    18946.617|      8.135|
|Storage      |   558|  154165.990|    13876.026|      9.001|
|Phones       |   595|  224666.538|    31666.406|     14.095|
|Furnishings  |   641|   62790.070|     8959.981|     14.270|
|Appliances   |   301|   64605.229|    10272.737|     15.901|
|Binders      |  1023|  130624.688|    22552.021|     17.265|
|Art          |   514|   18255.724|     4305.824|     23.586|
|Accessories  |   500|  107434.086|    26264.279|     24.447|
|Fasteners    |   153|    2166.686|      644.569|     29.749|
|Copiers      |    46|   86628.642|    30586.035|     35.307|
|Envelopes    |   183|   13097.828|     5522.418|     42.163|
|Paper        |   911|   50784.488|    22012.726|     43.345|
|Labels       |   250|    8625.096|     3801.645|     44.077|


## Practical 3: discount bands within Tables

|discount_band  | lines| total_sales| total_profit| loss_line_pct| margin_pct|
|:--------------|-----:|-----------:|------------:|-------------:|----------:|
|None           |    50|    55250.72|     10723.03|         0.000|     19.408|
|Above 0 to 20% |    47|    33044.07|      -299.70|        44.681|     -0.907|
|Above 20%      |   118|    57777.20|    -20008.12|        96.610|    -34.630|


## Practical 3: three largest loss lines within Tables

| row_id|order_id       |product_name                                             |    sales| discount|    profit|
|------:|:--------------|:--------------------------------------------------------|--------:|--------:|---------:|
|   2109|US-2024-116638 |Chromcraft Bull-Nose Wood Oval Conference Tables & Bases | 4297.644|      0.4| -1862.312|
|   4665|US-2025-109869 |Bush Advantage Collection Racetrack Conference Table     | 1272.630|      0.5|  -814.483|
|   1421|US-2023-108609 |Hon 94000 Series Round Tables                            | 1421.664|      0.4|  -734.526|


## Practical 3: order losses by segment

|segment     | orders| loss_order_pct|
|:-----------|------:|--------------:|
|Consumer    |   1710|         21.462|
|Corporate   |   1021|         19.491|
|Home Office |    591|         17.766|


## Part 3 A: an example random sampling audit

| seed|   n| mean_sales| lower95| upper95| frame_mean|
|----:|---:|----------:|-------:|-------:|----------:|
|  106| 100|    611.662| 242.432| 980.891|    470.796|


This n=100 t interval is approximate; the lesson demonstrates undercoverage for small samples from this skewed frame. Do not interpret one interval containing the frame mean as validation.

## Part 3 B: end aisle minus normal

|          | effect|  lower95| upper95|        p|
|:---------|------:|--------:|-------:|--------:|
|mean of x |   21.7| 6.568701| 36.8313| 0.007849|


Random assignment supports the experimental contrast; representative sampling and long-term net profitability are not established. Obtain contribution per case, display costs and displaced sales.

## Part 3 C: household-size-only model

|               | Estimate| Std. Error| t value| Pr(>&#124;t&#124;)|
|:--------------|--------:|----------:|-------:|------------------:|
|(Intercept)    | 2581.941|    195.263|  13.223|                  0|
|household_size |  404.128|     50.998|   7.924|                  0|


## Part 3 C: model comparison

| Res.Df|      RSS| Df| Sum of Sq|      F| Pr(>F)|
|------:|--------:|--:|---------:|------:|------:|
|     48| 18498431| NA|        NA|     NA|     NA|
|     47|  7448393|  1|  11050038| 69.727|      0|


## Part 3 C: mean-response interval at income 40, size 4

|      fit|      lwr|      upr|
|--------:|--------:|--------:|
| 4055.409| 3931.026| 4179.792|


## Part 3 C: individual prediction interval at income 40, size 4

|      fit|      lwr|      upr|
|--------:|--------:|--------:|
| 4055.409| 3244.951| 4865.866|


Regression interpretations are conditional associations. Compare residual patterns and consider the unverified selection design. Neither fit nor statistical significance establishes causal or out-of-sample business performance.

## Briefing assessment

Award credit for a correct unit/denominator, labelled units, reproducible code, an evidence-based finding and a defensible limitation. Do not require an identical random sample or wording. Graphs should answer the question without clipping or misleading scales. Never accept a causal discount claim from the observational Superstore comparisons.
