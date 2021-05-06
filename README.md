# dsnd-i2ds

#TODO

### Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#project-motivation)
3. [File Descriptions](#file-descriptions)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing-authors-acknowledgements)


## Installation <a name="installation"></a>
There are no additional libraries outside of the standard Anaconda distribution required to run the associated code. However, it should be noted the inconsistencies are found with the Jupyter Notebook workspace provided by Udacity, especially when exploring the optimal model. The discrepancy will be noted in the Notebook and all official results will be derived from the standard Python/Anaconda environment (via .py).

## Project Motivation <a name="project-motivation"></a>
Every year there seem to be dozens of social media or general blog posts about the "Top 10 Languages to Learn in 20XX". Having been working with the StackOverflow 2017 Survey data for a little while now, I thought it might interesting to see how those developers felt about their languages - "what get's used?", "what is gaining traction or losing its lead?", "do people actually like working with the tools that are most prevalent?". The survey has been tracking current technologies respondents were using (language, O/S, web framework, supporting technologies, etc.). Knowing this, the following questions came to mind:

1. *What are the most popular languages that developers want to work with? Which ones are the most popular and which are up-and-coming? How has this changed over time?* We will be using he 2018, 2019, and 2020 data as this question and it's responses are relatively consistent.

2. *How do the languages a developer wants to utilize impact a developer's job satisfaction?* There is something to be said about how well you like your job when you are paid well for it, but what about based on what your tool bag looks like? If you get to play with your toys rather than what you're told to deal with, does that actually matter?

3. *How do developers evaluate their own competency given their years of experience and gender?* It's often said that men and women have widely different opinions of their own abilities and that younger men, specifically, tend towards over-confidence or at least, state higher levels of expertise than women would at the same age.

## File Descriptions <a name="file-descriptions"></a>
Guide others through the files in your repository. You may not talk about every file here, but you should let them know where they can find the work they might find most interesting.

The jupyter notebook can be found [here](https://github.com/michaelpartel/dsnd-i2ds/tree/main/ipynb). Within it, each question has it's own separate notebook file. Code and results:
  * question 1 can be found in *[Language Popularity Over Time According to StackOverflow.ipynb](https://github.com/michaelpartel/dsnd-i2ds/blob/main/ipynb/Language%20Popularity%20Over%20Time%20According%20to%20StackOverflow.ipynb)*
  * question 2 can be found in *[LanguageDesireAndJobSatisfaction.ipynb](https://github.com/michaelpartel/dsnd-i2ds/blob/main/ipynb/LanguageDesireAndJobSatisfaction.ipynb)*
  * question 3 can be found in *[ConfidenceByGenderYears.ipynb](https://github.com/michaelpartel/dsnd-i2ds/blob/main/ipynb/ConfidenceByGenderYears.ipynb)*

##  Results <a name="results"></a>
When your project isn't meant to be interactive or used for other projects, you should instead talk about the technical details of your project. What were your results? What did you do to improve them? What methods did you try? What worked? What didn't work?

1. For question 1, the approach was fairly straight-forward. Since the respondents could utilize a multi-select answer, the data allowed each response to be a semi-colon separated list.
    * Identify each value possible in the list of languages.
    * Loop over the dataframe and count each time a language is used.
    * Sort these values and plot them via bar chart
    * Develop a year-year comparison chart showing the delta from year A to year B.
    * Repeat for all three years of data.

We saw clearly that C, Java, JavaScript, and Python were in the top with a fairly steep reduction in popularity as the list went on. This top-4 contained the same languages for the three years, but with Python and JavaScript changing places. Also to note for anyone who uses Excel Macros, VBA was at the bottom all three years. Also worth noting, the distance between the top (C and Java) and the rest went down consistently each year with a reduction from 13.6 to 11.4% market share for C. TypeScript and Rust seemed to gain the most share over the three years, even though they have a small amount regardless.

2. For question 2, the approach relied on cleaning the data for use in ML linear regression to see just what impact language choices had on job satisfaction.
    * Reduce the data to just Satisfaction and Desired Languages.
    * Convert the satisfaction strings to numeric and placed in the correct so they can be arithmetically operated on.
    * Clear out rows with nans in the satisfaction column and dummy the language column by splitting on semi-colon.
    * Fit the model

The model did not quite result in anything useful. By that, I mean the model had R-Squared values of 0.0045 and 0.0037 for train and test data sets. This means that given the current state of the data, there is effectively no statistical impact on job satisfaction by the choice of language a developer wants to use. To further look at this, the average job satisfaction when a specific language was desired was compared to the same for when that language was not desired. While we can't say the model was of use, we can see what kind of small impact their is.
    * Group the data by language and satisfaction and take the mean.
    * Split into a dataframe of desired language scores and a dataframe of not-desired language scores.
    * Develop the same kind of delta comparison chart as question 1.

Again, we expect very small to no impact due to languages - the interesting result is that some languages seem to have a minor impact. Scala, Dart, Erlang, and Objective-C provide a negative impact when desired in the range of -0.08 to -0.1 satisfaction. Conversely, Bash/Shell/PowerShell provides a positive 0.11 satisfaction score. This suggests that while some of the languages may drive satisfaction, it is more likely to be based on work environment or what you are doing with that language rather than the language itself.

  While we cannot say a languages are a large impact on satisfaction, they may be related to other traits that are.

3. For question 3, the approach was likewise - clean and/or "dummy" the data, then plot the comparisons. In this situation, there were some data imputation decisions made to simplify it such as with the multi-select gender responses. Respondents could select: Man, Woman, non-binary, genderqueer, gender-neutral or all of the above. In order to simiplify the comparison, and in an attempt remain inclusive/non-presumptive, non-binary / genderqueer / gender-neutral were grouped as "Non-Binary". At best, one hopes this is not seen as offensive and at worst, merely a lack of tact.
    * Generate a "dummy" function to create simplified data columns for each gender.
    * Generate a "dummy" function to replace the SelfAssessed Capability as a numeric.
    * Correct the outlier "<1 year" and ">50 years" as 0 and 51 respectively
    * Fix the nans and group each gender by SelfAssessed scores X Years of experience to get the counts for each unique pairing
    * Plot the data:
      - Plot both raw and percentile within the gender (e.g., Number of men that scored X for Y years divided by total men)

Several plots were generated using Seaborn's bubble plot. In hindsight, this plot can make it difficult to see when the data is overlaid, but it worked serviceably enough. For the lower years of experience on the percentile chart, we saw a large percent of Non-binary respondents score themselves as 5 (Far Above Average) and a large percent of women score themselves as 4 (A Little Above Average). As years of experience grow, men take over all categories. When examining the non-normalized data, we see just how skewed the population is: the men outweigh women and non-binary at 78k to 7.4k. That makes the percentile assessment seem somewhat questionable simply due to population delta. That thought aside, we also saw that Men tend to score themselves higher with a range from 3-5 at the lower experience levels where women tend to only score 3-4. Non-binary seems to follow the 3-5 of the men and mirrors many of the population bubbles on the chart.

  This suggests that, yes, we can say men are more likely to score themselves higher on average, but that it is not by a large percent of the gender (just by volume in the industry).

## Licensing, Authors, and Acknowledgements <a name="licensing-authors-acknowledgements"></a>
Some functions (clean_and _plot, bar_comp, and fit_model) are heavily/almost entirely based on those utilized in the Udacity Introduction to Data Science notebooks. The general nature of these functions was greatly appreciated. Like those in the datasets, StackOverflow was a great source of "why did this break?".
