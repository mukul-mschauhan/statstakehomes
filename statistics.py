import pandas as pd
import numpy as np
import streamlit as st
st.set_page_config(layout="wide")
import scipy.stats as stats
import random
from statsmodels.stats import weightstats as stest
import statsmodels.api as sm

# SideBar Radio Button
sbar = st.sidebar.radio(label = "Statistics Take Homes", options = ["Day 01", "Day 02", "Day 03", "Day 04"])

header =st.container()
q1 = st.container()
q2 = st.container()
q3 = st.container()
q4 = st.container()
q5 = st.container()
q6 = st.container()
q7 = st.container()
q8 = st.container()
q9 = st.container()
q10 = st.container()
q11 = st.container()
q12 = st.container()
q13 = st.container()
q14 = st.container()
q15 = st.container()
q16 = st.container()
q17 = st.container()
q18 = st.container()
q19 = st.container()
q20 = st.container()

with header:
    st.title("Statistics Take Homes")
    st.subheader("Let's begin with some hands-on practice exercises")


############################################ D A Y 0 1 ##############################################################################
#***********************************************************************************************************************************#
#The rainfall (in mm) in the city is recorded for 10 days. Find the rainfall value under which 60% of the rainfall would lie.
with q1:
    if sbar=="Day 01":
        st.markdown("**Q.1. The rainfall (in mm) in the city is recorded for 10 days. Find the rainfall value under which 60% of the rainfall would lie.**")
        st.write("Given Data:    **rainfall(in mm) = [86, 74, 90, 108, 65,84, 75, 92, 102, 93]**")
        pressed = st.button("Q.1. Solution", True)
        if pressed:
            # compute 60th percentile using quantile()
            rainfall = [86, 74, 90, 108, 65,84, 75, 92, 102, 93]
            with st.echo():  
                rain_60 = np.quantile(rainfall,0.60)
            st.write('60% of the rainfall for 10 days would lie below' + ' ' + str(rain_60) + 'mm')
        st.markdown("---")  
        

#The performance of John and Jack in the monthly exams is given below. Identify the most consistent student.
with q2:
    if sbar=="Day 01":
        st.markdown("**Q.2. The performance of John and Jack in the monthly exams is given below. Identify the most consistent student.**")
        st.write("Given Data:    **John = [42, 38, 47, 35, 39, 46]**")
        st.write("Given Data:    **Jack = [32, 36, 46, 49, 28, 30]**")
        pressed = st.button("Q.2. Solution", True)
        if pressed:
            john = [42, 38, 47, 35, 39, 46]
            jack = [32, 36, 46, 49, 28, 30]
            # average marks of John & SD
            john_avg = np.mean(john)
            john_std = np.std(john)
            # average marks of Jack 
            jack_avg = np.mean(jack)
            jack_std = np.std(jack)
            # calculate coefficient of variation for both the students
            john_cv = (john_std/ john_avg)*100
            jack_cv = (jack_std/ jack_avg)*100
            st.write('Coefficient of Variation for John', np.round(john_cv,3))
            st.write('Coefficient of Variation for John', np.round(jack_cv,3))
            st.markdown("**Hint: Lower the CV, Higher the Consistency.**")
        st.markdown("---")  
    
# 3. The amount of Calcium, Potassium and Iron in the chocolate cookies of 5 different brands is collected. 
# Find out which mineral can be neglected while comparing the different cookie brands?
with q3:
    if sbar=="Day 01":
        st.markdown("**Q.3. The performance of John and Jack in the monthly exams is given below. Identify the most consistent student.**")
        st.write("Given Data:    Calcium (in mg) = [132, 138.56, 147.2, 145.6, 139]")
        st.write("Given Data:    Potassium (in mg) = [122.2, 116, 106.6, 119.52, 128]")
        st.write("Given Data:    Iron (in mg) = [2.96, 3.02, 3.01, 2.99, 2.93]")
        pressed = st.button("Q.3. Solution", True)
        if pressed:
            Cal = [132, 138.56, 147.2, 145.6, 139]
            Pot = [122.2, 116, 106.6, 119.52, 128]
            Iron = [2.96, 3.02, 3.01, 2.99, 2.93]
            # calculate the standard deviation of all the three minerals
            st.write('Standard deviation of Calcium', np.round(np.std(Cal),3))
            st.write('Standard deviation of Potassium', np.round(np.std(Pot),3))
            st.write('Standard deviation of Iron', np.round(np.std(Iron),3))
            result = f" **Conclusion:** The above output shows that the **standard deviation** of **Iron** is **near zero.** \
                This implies that the amount of iron in the cookies of all the brands is almost equal. \
                    Thus we can neglect the quantity of iron while comparing the different cookie brands."
            st.markdown(result)
        st.markdown("---") 

#4. On an online payment gateway, on average 9 out of 25 customers are getting an error while redeeming the gift coupon. 
# A random sample of 40 customers is selected. 
# Find the probability that at most 16 customers will get the same error.
with q4:
    if sbar=="Day 01":
        q = f"**Q.4. On an online payment gateway, on average 9 out of 25 customers are getting an error while redeeming the gift coupon.\
            A random sample of 40 customers is selected. Find the probability that at most 16 customers will get the same error.**"
        st.markdown(q)
        stmnt = f"**Approach** - Consider a discrete random variable X representing the occurrence of error while redeeming the gift coupon. \
            Here X follows a binomial distribution with sample(n) = 40, prob(p) = 9/25."
        st.write(stmnt)
        pressed = st.button("Q.4. Solution", True)
        if pressed:
            prob = stats.binom.cdf(k = 16, n = 40, p = 0.36)
            st.write('The probability that at most 16 customers will get the same error is:', prob)
        st.markdown("---")
        
#5. The survey by road safety department states that the in the Oneonta city the average speed of vehicle is 65 mph and the 
# standard deviation is 9 mph. Find the probability that a randomly selected vehicle has a speed greater than 78 mph.

with q5:
    if sbar=="Day 01":
        q = f"**Q.5. The survey by road safety department states that the in the Oneonta city the average speed of vehicle is 65 mph and the standard deviation is 9 mph.\
            Find the probability that a randomly selected vehicle has a speed greater than 78 mph..**"
        st.markdown(q)
        stmnt = f"**Approach** - Consider a continuous random variable X representing the speed of the vehicle.\
            Here X follows a normal distribution with mean = 65 and standard deviation= 9."
        st.write(stmnt)
        
        pressed = st.button("Q.5. Solution", True)
        if pressed:
            avg = 65
            sd = 9
            zscore = (78-avg)/sd
            st.write("Code for Calculating Probability")
            with st.echo(): 
                prob = stats.norm.sf(zscore)
            st.write('The probability that at most 16 customers will get the same error is:', prob)
        st.markdown("---")

#6. A wrist-watch company wants to perform a quality check before launching their next-generation k22-digital watch. 
# The production team has delivered 30 watches with number tags as 1,2,...30 on each watch for the quality check. 
# Pick 5 watches randomly to check the quality.

with q6:
    if sbar=="Day 01":
        q = f"**Q.6. A wrist-watch company wants to perform a quality check before launching their next-generation k22-digital watch. \
            The production team has delivered 30 watches with number tags as 1,2,...30 on each watch for the quality check. \
            Pick 5 watches randomly to check the quality.**"
        st.markdown(q)
        approach = f" **Approach:** Here we select 5 watches without replacement from a population of 30 watches and draw a sample from that.\
            We would use Random Package to achieve the desired results."
        st.markdown(approach)
        
        pressed = st.button("Q.6. Solution", True)
        if pressed:
            data = np.arange(1,31,1)
            with st.echo(): 
                sample_wor = random.sample(population = list(data), k = 5)
            result = f"Sample without replacement is = **{sample_wor}**"
            st.markdown(result)
        st.markdown("---")
        
#7.The fill amount in 2-liter soft drink bottles is normally distributed, with a mean of 2.0 liters and a 
# standard deviation of 0.05 liter. 
# If the bottles contain less than 95% of the listed net content (1.90 liters, in our case), 
# the manufacturer may be subject to penalty by the state office of consumer affairs. 
# Bottles that have a net content above 2.1 liters may cause excess spillage upon opening. 
# What is the proportion of bottles that will contain
#a) between 1.9 and 2.0 liters

#b) between 1.9 and 2.1 liters

#c) below 1.9 liters or above 2.1 liters

#d) At least how much soft drink(in litres) is contained in 99% of the bottles?

with q7:
    if sbar=="Day 01":
        q = f"**Q.7. The fill amount in 2-liter soft drink bottles is normally distributed, \
            with a mean of 2.0 liters and a standard deviation of 0.05 liter. \
                If the bottles contain less than 95% of the listed net content (1.90 liters, in our case),\
                    the manufacturer may be subject to penalty by the state office of consumer affairs. \
                        Bottles that have a net content above 2.1 liters may cause excess spillage upon opening. \
                            What is the proportion of bottles that will contain :-**"
        st.markdown(q)
        st.write("""
        * a) between 1.9 and 2.0 liters
        * b) between 1.9 and 2.1 liters
        * c) below 1.9 liters or above 2.1 liters
        * d) At least how much soft drink(in litres) is contained in 99% of the bottles?""")
        #approach = f" **Approach:** Here we select 5 watches without replacement from a population of 30 watches and draw a sample from that.\
         #   We would use Random Package to achieve the desired results."
        #st.markdown(approach)
        
        pressed = st.button("Q.7. Solution", True)
        if pressed:
            # Between 1.9 and 2.0 Litres
            mu = 2
            sigma = 0.05
            x1=1.9
            x2=2.0
            z1 = (x1-mu)/sigma
            z2 = (x2-mu)/sigma
            pval = stats.norm.cdf(z2)- stats.norm.cdf(z1)
            st.write('Probability of Soft Drink Bottles between 1.9 and 2.0 liters:',pval)
            # Between 1.9 and 2.1 liters
            mu = 2
            sigma = 0.05
            x1=1.9
            x2=2.1
            z1 = (x1-mu)/sigma
            z2 = (x2-mu)/sigma
            pval = stats.norm.cdf(z2)- stats.norm.cdf(z1)
            st.write('Probability of Soft Drink Bottles between 1.9 and 2.1 liters is:',pval)
            # Below 1.9 and Above 2.1 liters
            mu = 2
            sigma = 0.05
            x1=1.9
            x2=2.1
            z1 = (x1-mu)/sigma
            z2 = (x2-mu)/sigma
            pval = 1-(stats.norm.cdf(z2)- stats.norm.cdf(z1))
            st.write('Probability of Soft Drink Bottles with below 1.9 and Above 2.0 liters is:',pval)
            # d) At least how much soft drink(in litres) is contained in 99% of the bottles?
            pval = 0.99
            z = stats.norm.isf(0.99)
            x = np.round(mu+ (z*sigma),3)
            st.write('Atleast {} litres is contained in 99% of bottles'.format(x))
        st.markdown("---")

############################################ D A Y 0 2 ##############################################################################
#***********************************************************************************************************************************#

with q1:
    if sbar=="Day 02":
        q = f"**Q.1. The meteorological department states that on average the temperature on summer days is 82 (degree F) in California. \
            For a study on climate change, a sample of data is collected for 20 summer days. Find the sampling error for the mean.**"
        st.markdown(q)
        st.write("Given Data:    **temp (in F) = [51, 68, 83, 93, 89, 58, 79, 54, 60, 77, 87, 57, 63, 85, 92, 74, 67, 88, 91, 82]**")
        pressed = st.button("Q.1. Solution", True)
        if pressed:
            temp = [51, 68, 83, 93, 89, 58, 79, 54, 60, 77, 87, 57, 63, 85, 92, 74, 67, 88, 91, 82]
            st.write("**Hint: ** Remember a sampling error occurs when the sample used in the study is not representative of the whole population.")
            # calculate the point estimate for the population mean
            samp_mean = np.mean(temp)
            # given population mean
            # calculate the sampling error for mean
            pop_mean = 82
            st.write("Sampling error for mean:", np.abs(samp_mean - pop_mean))
        st.markdown("---")

with q2:
    if sbar=="Day 02":
        q = f"**Q.2. A team of IT experts wants to estimate the average time required to a system to run a specific program. \
            The team aims to estimate the average time with 95% confidence. A technical report from last week shows that the standard deviation is 3.8 minutes.\
            The team decides that the margin of error should be 1.2 minutes. How many systems should the team choose for the estimation?.**"
        st.markdown(q)
        st.write("Given")
        st.write("sigma = 3.8")
        st.write("margin of error = 1.2")
        pressed = st.button("Q.2. Solution", True)
        if pressed:
            st.latex("Hint: "r'''Margin  of Error = z * {\frac{\sigma}{\surd n}}''')
            sigma = 3.8
            me = 1.2
            # Calculate Alpha 
            z_alpha_by_2 = np.abs(round(stats.norm.isf(q = 0.05/2), 4))
            # calculate sample size (n) 
            n = ((z_alpha_by_2)**2)*(sigma**2)/(me**2)

            st.write("Required number of systems for the time estimation study:", np.round(n))
        st.markdown("---")
        
with q3:
    if sbar=="Day 02":
        q = f"**Q.3. The production manager at the Xen Sewing Factory claims that on average the diameter of a class 14M\
            bobbin (small cylindrical yarn) is less than 18 mm. The previous study shows that the standard deviation is 1.7 mm. \
                Consider a sample of 40 class 14M bobbins from a normally distributed population with sample mean diameter as 17.5 mm. \
                    Calculate 99% confidence interval for the population mean diameter.**"
        st.markdown(q)
        approach = f"Approach: As the sample size is large (> 30), we use the Z-distribution to calculate the confidence interval."
        st.write(approach)
        pressed = st.button("Q.3. Solution", True)
        if pressed:
            st.write("**Hint:Use Mean and Standard Deviation to Calculate the Confidence Interval**")
            n = 40
            std_pop = 1.7
            samp_mean = 17.5
            
            interval = np.round(stats.norm.interval(0.99, loc = samp_mean, scale = std_pop / np.sqrt(n)),2)
            result = f"The 99% confidence interval of population mean is: **{interval}**"
            st.markdown(result)         
        st.markdown("---")
        
with q4:
    if sbar=="Day 02":
        q = f"**Q.4. A construction company wants to estimate the daily wages of contract workers. \
            In the construction business, the wages of contract workers follow the normal distribution with a standard deviation of \
                85 dollars. A sample of wages for 50 contract workers is considered for the study. \
                    Calculate the margin of error for a 95% confidence level.**"
        st.markdown(q)
        #approach = f"Approach: As the sample size is large (> 30), we use the Z-distribution to calculate the confidence interval."
        #st.write(approach)
        pressed = st.button("Q.4. Solution", True)
        if pressed:
            #st.write("**Hint:Use Mean and Standard Deviation to Calculate the Confidence Interval**")
            n = 50
            std = 85
            alpha= 0.95
            
            z_alpha_by_2 = np.abs(round(stats.norm.isf(q = 0.05/2), 4))
            error = (z_alpha_by_2*std)/ np.sqrt(n)
            result = f"The 99% confidence interval of population mean is: **{error}**"
            st.markdown(result)         
        st.markdown("---")
        
with q5:
    if sbar=="Day 02":
        q = f"**Q.5. To study the climate changes, a sample of data of temperature in California is collected for 20 summer days.\
            Calculate 95% confidence interval for the population mean temperature.**"
        st.markdown(q)
        st.write("Given Data:    **temp (in F) = [51, 68, 83, 93, 89, 58, 79, 54, 60, 77, 87, 57, 63, 85, 92, 74, 67, 88, 91, 82]**")
        pressed = st.button("Q.5. Solution", True)
        if pressed:
            approach = f"***Approach: As the sample size is small (< 30), we use the t-distribution to calculate the confidence interval.***"
            st.write(approach)
            #st.write("**Hint:Use Mean and Standard Deviation to Calculate the Confidence Interval**")
            temp = [51, 68, 83, 93, 89, 58, 79, 54, 60, 77, 87, 57, 63, 85, 92, 74, 67, 88, 91, 82]
            n = len(temp)
            sample_avg = np.mean(temp)
            sample_std = np.std(temp)
            
            interval = np.round(stats.t.interval(0.95, df = n-1, loc = sample_avg, scale = sample_std/np.sqrt(n)),2)
            result = f"The 99% confidence interval of population mean is: **{interval}**"
            st.markdown(result)         
        st.markdown("---")
        
with q6:
    if sbar=="Day 02":
        q = f"**Q.6. A botanical garden in Manchester city planted 350 plant seeds of white, pink and blue lily in the last summer. \
            After 3 months a sample of 125 plants was selected, out of which 80 plants were found to be of pink lilies. \
            Find a 90% confidence interval for the population proportion of pink lily plants.**"
        st.markdown(q)
        #st.write("Given Data:    **temp (in F) = [51, 68, 83, 93, 89, 58, 79, 54, 60, 77, 87, 57, 63, 85, 92, 74, 67, 88, 91, 82]**")
        pressed = st.button("Q.6. Solution", True)
        if pressed:
            #approach = f"***Approach: As the sample size is small (< 30), we use the t-distribution to calculate the confidence interval.***"
            #st.write(approach)
            #st.write("**Hint:Use Mean and Standard Deviation to Calculate the Confidence Interval**")
            N = 350
            n = 125
            x = 80
            p_samp = x/n
            
            interval = np.round(stats.norm.interval(0.90, loc = p_samp, scale = np.sqrt((p_samp*(1-p_samp))/n)),2)
            result = f"90% confidence interval for population proportion of pink lily plants: **{interval}**"
            st.markdown(result)         
        st.markdown("---")

with q7:
    if sbar=="Day 02":
        q = f"**Q.7. The quality assurance department claims that on average the non-fat yogurt contains less than 148 mg of \
            potassium per 100 g pack. To check this claim 35 packs of yogurt are collected and the content of potassium is recorded. \
            Can we use the Z-test to test the claim of the quality assurance department?**"
        st.markdown(q)
        
        st.write("Given Data:    **pot_mg = [151, 159, 168, 146, 129, 147, 149, 141, 150, 158, 119, 125, 139, 154, 163, 156, 132, 137, 126, 152, 127, 135, 138, 145, 128, 148, 153, 124, 170, 134, 157, 164, 144, 160, 161]**")
        approach = f"Approach: The given random sample is the quantity of potassium in a 100g pack of non-fat yogurt which is continuous \
            in nature. **To apply the Z-test for the population mean we need to test whether the sample is taken from a normally distributed population**.\
            Use the Shapiro-Wilk test to check the normality of the data."
        st.write(approach)
        
        pressed = st.button("Q.7. Solution", True)
        if pressed:
            st.write("**Hint:** Use stats.shapiro to find if the data is normal or not..")
            #approach = f"***Approach: As the sample size is small (< 30), we use the t-distribution to calculate the confidence interval.***"
            #st.write(approach)
            #st.write("**Hint:Use Mean and Standard Deviation to Calculate the Confidence Interval**")
            pot_mg = [151, 159, 168, 146, 129, 147, 149, 141, 150, 158, 119, 125, 139, 154, 163, 156, 132, 137, 126, 152, 127, 135, 138, 145, 128, 148, 153, 124, 170, 134, 157, 164, 144, 160, 161]
            stat, p_value = stats.shapiro(pot_mg)
            
            #interval = np.round(stats.norm.interval(0.90, loc = p_samp, scale = np.sqrt((p_samp*(1-p_samp))/n)),2)
            result = f"PValue: **{p_value}**"
            st.markdown(result)
            st.write("From the above result, we can see that the p-value is greater than 0.05, thus we can say that the data is normally distributed.")         
        st.markdown("---")

with q8:
    if sbar=="Day 02":
        q = f"**Q.8. The quality assurance department claims that on average the non-fat yogurt contains less than 148 mg of potassium per 100 g pack. To check this claim 35 packs of yogurt are collected and the content of potassium is recorded. \
            Use 0.05 as a level of significance to test the claim using p-value technique.**"
        st.markdown(q)
        st.write("Given Data:    ** pot_mg = [151, 159, 168, 146, 129, 147, 149, 141, 150, 158, 119, 125, 139, 154, 163, 156, 132, 137, 126, 152, 127, 135, 138, 145, 128, 148, 153, 124, 170, 134, 157, 164, 144, 160, 161]**")
        approach = f"The Null and Alternative Hypothesis  is:"
        st.markdown(approach)
        st.latex(r''' Ho:\mu \geq 148 ''')
        st.latex(r''' H1:\mu < 148 ''')
        pressed = st.button("Q.8. Solution", True)
        if pressed:
            pot_mg = [151, 159, 168, 146, 129, 147, 149, 141, 150, 158, 119, 125, 139, 154, 163, 156, 132, 137, 126, 152,127, 135, 138, 145, 128, 148, 153, 124, 170, 134, 157, 164, 144, 160, 161]
            z_score, pval = stest.ztest(x1 = pot_mg, value = 148, alternative = 'smaller')
            
            result = f"PValue: **{pval}**"
            st.markdown(result) 
            st.write("Here the p-value is greater than 0.05, thus we fail to reject (i.e. accept) the null hypothesis. Thus, there is no enough evidence to conclude that on average the non-fat yogurt contains less than 148 mg of potassium per 100 g pack.")       
        st.markdown("---")
        
with q9:
    if sbar=="Day 02":
        q = f"**Q.9. The production manager at the Xen Sewing Factory claims that on average the diameter of a class 14M bobbin is less than 18 mm. The previous study shows that the standard deviation is 1.7 mm. Consider a sample of 40 class 14M bobbins from a normally distributed population with sample mean diameter as 17.5 mm. \
            Test the claim of the production manager with 99% confidence.**"
        st.markdown(q)
        approach = f"The Null and Alternative Hypothesis  is:"
        st.markdown(approach)
        st.latex(r''' Ho:\mu \geq 18 ''')
        st.latex(r''' H1:\mu < 18 ''')
        pressed = st.button("Q.9. Solution", True)
        if pressed:
            def z_test(pop_mean, pop_std, n, samp_mean):
       
                # calculate the test statistic
                z_score = (samp_mean - pop_mean) / (pop_std / np.sqrt(n))
                return z_score
            # given data
            n = 40
            pop_mean = 18
            pop_std = 1.7
            samp_mean = 17.5
            # calculate the test statistic using the function 'z_test'
            crit = stats.norm.isf(0.99)
            z_score = z_test(pop_mean, pop_std, n, samp_mean)
            st.write("**Critical Value:**", crit)
            st.write("**Z Test Stat:** ", z_score)
        st.markdown("---")
            
with q10:
    if sbar=="Day 02":
        q = f"**Q.10. The NY university has opened the post of Astrophysics professor. \
            The total number of applications was 36. To check the authenticity of the applicants a sample of 10 applications was collected,\
                out of which 3 applicants were found to be a fraud. \
            Estimate the number of fraud applicants from all the applications.**"
        st.markdown(q)
        pressed = st.button("Q.10. Solution", True)
        if pressed:
            # total number of applications 
            N = 36
            # number of applications in a sample
            n = 10
            # number of fraud applicants in a sample
            x = 3
            # sample proportion fraud applicants
            p_samp = x/n
            # estimate the number of fraud applicants
            num_fraud = p_samp*N
            # round the number to get an integer value
            st.write('The number of fraud applicants:', round(num_fraud))
        st.markdown("---")
        
with q11:
    if sbar=="Day 02":
        q = f"**Q.11. The physical trainer at a university wants to estimate the average height of students at the university. \
            The trainer collects the data of 100 students and found that the average height is 168 cm with a standard deviation of 12 cm. \
                Find the 95% confidence interval for the population average height.**"
        st.markdown(q)
        pressed = st.button("Q.11. Solution", True)
        if pressed:
            st.write("**Approach: As the sample size is large (> 30), we use the Z-distribution to calculate the confidence interval.**")
            n = 100
            sample_avg = 168
            sample_std = 12
            interval = stats.norm.interval(0.95, loc = sample_avg, scale = sample_std/np.sqrt(n))
            st.write('95% confidence interval for population average height is', interval)
        st.markdown("---")
        
with q12:
    if sbar=="Day 02":
        q = f"**Q.12. The health magazine in Los Angeles states that a person should drink 1.8 L water every day.\
            To study this statement, the physician collects the data of 15 people and found that the average water \
                intake for these people is 1.6 L with a standard deviation of 0.5 L. \
            Calculate the 90% confidence interval for the population average water intake.**"
        st.markdown(q)
        pressed = st.button("Q.12. Solution", True)
        if pressed:
            st.write("**Approach: As the sample size is small (< 30), we use the t-distribution to calculate the confidence interval.**")
            n = 15
            sample_avg = 1.6
            sample_std = 0.5
            interval = stats.t.interval(0.90, df = n-1, loc = sample_avg, scale = sample_std/np.sqrt(n))
            st.write('90% confidence interval for population mean is', interval)
        st.markdown("---")
        
with q13:
    if sbar=="Day 02":
        q = f"**Q.13. The production manager at the automobile company states that all the steel rods are produced with an average length of 26 cm and a standard deviation of 2.4 cm. The length of 60 rods is collected as a sample and the average length of these rods is found to be 24.8 cm. \
            Test whether the length of the rod is different than 26 cm with a 95% confidence interval.**"
        st.markdown(q)
        approach = f"The Null and Alternative Hypothesis  is:"
        st.markdown(approach)
        st.latex(r''' Ho:\mu = 26 ''')
        st.latex(r''' H1:\mu \not= 26 ''')
        pressed = st.button("Q.13. Solution", True)
        if pressed:
            st.write("**Approach: As the Population SD is given, we use the Z-distribution to calculate the confidence interval.**")
            n = 60
            samp_avg = 24.8
            pop_std = 2.4
            interval = stats.norm.interval(0.95, loc = samp_avg, scale = pop_std / np.sqrt(n))
            st.write('95% confidence interval for population mean:', interval)
            st.write("Here the confidence interval do not contain the value in the null hypothesis (i.e. 26), thus we reject the null hypothesis and conclude that the average length of rod is not 26 cm.")
        st.markdown("---")
        
def z_test(pop_mean, pop_std, n, samp_mean):
    z_score = (samp_mean - pop_mean) / (pop_std / np.sqrt(n))
    return z_score

def t_test(pop_mean, samp_std, n, samp_mean):
    t_score = (samp_mean - pop_mean) / (samp_std / np.sqrt(n))
    return t_score

with q14:
    if sbar=="Day 02":
        q = f"**Q.14. The production manager at tea emporium claims that the weight of a green tea bag is less than 3.5 g. To test the manager's claim consider a sample of 50 tea bags. The sample average weight is found to be 3.28 g with a standard deviation of 0.6 g. \
            Use the p-value technique to test the claim at a 10% level of significance.**"
        st.markdown(q)
        approach = f"The Null and Alternative Hypothesis  is:"
        st.markdown(approach)
        st.latex(r''' Ho:\mu \geq 3.5 ''')
        st.latex(r''' H1:\mu < 3.5 ''')
        pressed = st.button("Q.14. Solution", True)
        if pressed:
            #st.write("**Approach: As the Population SD is given, we use the Z-distribution to calculate the confidence interval.**")
            n = 50
            pop_mean = 3.5
            samp_std = 0.6
            samp_mean = 3.28
            t_score = t_test(pop_mean, samp_std, n, samp_mean)
            st.write('T Test Statistic:', t_score)
            p_value = stats.t.cdf(t_score, n-1)
            st.write('P-Value:', p_value)
            st.write("Here the p-value is less than 0.1, thus we **reject the null hypothesis** and conclude that the **average weight of a green tea bag is less than 3.5 gm.**")
        st.markdown("---")
        
with q15:
    if sbar=="Day 02":
        q = f"**Q.15. The physician at university claims that the average height of male students in the university hostel is more than \
            175 cm with a standard deviation of 8 cm. \
                To test the claim the physical trainer at a university collects the data of 75 male students in the hostel and \
                    calculate the average height of those 75 students as 176.3 cm. \
            Test the physician's claim at 95% confidence.**"
        st.markdown(q)
        approach = f"The Null and Alternative Hypothesis  is:"
        st.markdown(approach)
        st.latex(r''' Ho:\mu \leq 175 ''')
        st.latex(r''' H1:\mu > 175 ''')
        pressed = st.button("Q.15. Solution", True)
        if pressed:
            n = 75
            pop_mean = 175
            pop_std = 8
            samp_mean = 176.3
            z_score = z_test(pop_mean, pop_std, n, samp_mean)
            st.write('Z Test Statistic:', z_score)
            p_value = stats.norm.cdf(z_score)
            st.write('P-Value:', p_value)
            st.write("Here the p-value is greater than 0.05, thus we ** fail to reject the null hypothesis** meaning avg height is 175 or less")
        st.markdown("---")
        
with q16:
    if sbar=="Day 02":
        q = f"**Q.16. The quality control department at a soap company states that their herbal soap contains 28 ml of palm oil with a standard deviation of 3.5 ml. A sample of 120 soaps is considered. The average amount of palm oil in the sample is 27.6 ml.\
            Test whether the amount of palm oil is different than 28 ml using the 90% confidence interval.**"
        st.markdown(q)
        approach = f"The Null and Alternative Hypothesis  is:"
        st.markdown(approach)
        st.latex(r''' Ho:\mu = 28 ''')
        st.latex(r''' H1:\mu \not= 28 ''')
        pressed = st.button("Q.16. Solution", True)
        if pressed:
            n = 120
            #pop_mean = 175
            pop_std = 3.5
            samp_mean = 27.6
            interval = stats.norm.interval(0.90, loc = samp_mean, scale = pop_std / np.sqrt(n))
            st.write('90% confidence interval for population mean:', interval)
            st.write("Here the confidence interval contains the value in the null hypothesis (i.e. 28), \
                thus we fail to reject (i.e. accept) the null hypothesis and conclude that the amount of palm oil in the herbal soap is 28 ml.")
        st.markdown("---")
        
############################################ D A Y 0 3 ##############################################################################
#***********************************************************************************************************************************#
# 1. A financial firm AlpaMoney has recently started their online payment gateway and claims that the level of customer satisfaction 
# about the transactions is the same as that of their competitor firm PayEarly. Consider the equality of an average level of satisfaction 
# as the null hypothesis and test the claim using a critical value method with 90% confidence.
with q1:
    if sbar=="Day 03":
        q = f"**Q.1. A financial firm AlpaMoney has recently started their online payment gateway and claims that the level of customer \
            satisfaction about the transactions is the same as that of their competitor firm PayEarly. \
                Consider the equality of an average level of satisfaction as the null hypothesis and test the claim using a critical value \
                    method with 90% confidence. Statistics given for Alpha Money and Pay Early are sample_mean1 = 4.23, \
                        sample_mean2 = 3.56, samplesd1 = 1.6, samplesd2 = 0.72, sample1count = 527, sample2count = 652**"
        st.markdown(q)
        pressed = st.button("Q.1. Solution", True)
        if pressed:
            z_val = np.abs(round(stats.norm.isf(q = 0.1/2), 2))
            st.write('Critical value for two-tailed Z-test:', z_val)
            def TwoSampZTest(samp_mean_1, samp_mean_2, samp_std_1, samp_std_2, value, n1, n2):   
                # calculate the test statistic
                denominator = np.sqrt((samp_std_1**2 / n1) + (samp_std_2**2 / n2))
                zscore = ((samp_mean_1 - samp_mean_2) - (value)) / denominator
                # return the z-score
                return zscore
            sm_1 = 4.23
            sm_2 = 3.56
            sstd_1 = 1.6
            sstd_2 = 0.72
            null_val = 0
            n_1 = 527
            n_2 = 652
            zscore = TwoSampZTest(samp_mean_1 = sm_1, samp_mean_2 = sm_2, samp_std_1 = sstd_1, samp_std_2 = sstd_2, value = null_val, 
                      n1 = n_1, n2 = n_2)
            st.write("Z Test Statistic", zscore)
            st.write("**Here the z-score is greater than 1.64. Thus, we reject the null hypothesis and conclude that the customer level of satisfaction for both the companies is not the same.**")
        st.markdown("---")

# 2. The economic journal claims that the students who graduated from tier 1 universities get more salary than the average salary of 35000$. A random sample of 20 graduated students is selected to test the claim. Use p-value criteria to test the claim with 0.1 as a level of significance.

with q2:
    if sbar=="Day 03":
        q = f"**Q.2. The economic journal claims that the students who graduated from tier 1 universities get more salary than the \
            average salary of 35000$. A random sample of 20 graduated students is selected to test the claim. \
            Use p-value criteria to test the claim with 0.1 as a level of significance.**"
        st.markdown(q)
        
        s = f"salary = [29560, 26534, 31020, 44300, 52335, 69190, 71100, 80100, 90000, 41002, 46118, 88129, 79713, 95881, 47989, 15188, 91631, 96189, 77819, 79590])"
        st.markdown(s)        
        pressed = st.button("Q.2. Solution", True)
        if pressed:
            st.markdown("The null and alternative hypothesis is:")
            st.latex(r'''H0: \mu \leq 35000 dollars''')
            st.latex(r'''H1: \mu > 35000 dollars ''')
            
            salary = [29560, 26534, 31020, 44300, 52335, 69190, 71100, 80100, 90000, 41002, 46118, 88129, 79713, 95881, 47989, 15188,
          91631, 96189, 77819, 79590]
            # calculate sample mean
            sample_avg = np.mean(salary)
            st.write("Sample Mean", sample_avg)
            # calculate sample standard deviation
            sample_std = np.std(salary)
            st.write("Sample Standard Deviation", sample_std)
            # sample size
            n = len(salary)
            # degrees of freedom for 1 sample t-test
            st.write('Degrees of freedom:', n - 1)
            st.caption("Lets Check the Normality of the Data")
            with st.echo():
                teststatistic, pvalue = stats.shapiro(salary)
                # use 'ttest_1samp()' to calculate the test statistic and corresponding p-value for 2-tailed test
                # pass the sample data to the parameter, 'a'
                # pass the average value in the null hypothesis to the parameter, 'popmean'
                t_stat, p_val = stats.ttest_1samp(a = salary, popmean = 35000)
            st.write("Test Statistic_Shapiro:", teststatistic)
            st.write("Pvalue_Shapiro:", pvalue)
            st.write("From the above result, we can see that the p-value is greater than 0.05, thus we can say that the data is normally distributed.")
            req_p_val = p_val/2
            st.write("Test Statistic:", t_stat)
            st.caption("Note - In our example, the hypothesis test is one-tailed. Thus, we divide the two-tailed probability by 2 to obtain the one-tailed probability.")
            st.write("Pvalue:", req_p_val)
            st.write("**We can see that the p-value is less than 0.1. \
                Thus, we reject the null hypothesis and there is enough evidence to conclude that the students who graduated from tier 1 universities get more salary than 35000$.**")
        st.markdown("---")
                
# 3. Amy and Susan are national level swimmers. Their coach conducts five rounds each of 400 m and records the time taken by the individuals. Perform a two sample t-test to test whether there is any difference between the average time taken by Amy and Susan. Use 0.05 as a level of significance.

with q3:
    if sbar=="Day 03":
        q = f"**Q.3. Amy and Susan are national level swimmers. \
            Their coach conducts five rounds each of 400 m and records the time taken by the individuals. \
                Perform a two sample t-test to test whether there is any difference between the average time taken by Amy and Susan. Use 0.05 as a level of significance.**"
        st.markdown(q)
        st.write("""
                **Use the timing (in minutes) given below:**
                * Amy_time = [4.2, 3, 3.8, 5, 4.6]
                * Susan_time = [5.2, 4.6, 3.9, 4.4, 5]""")
        pressed = st.button("Q.3. Solution", True)
        if pressed:
            
            Amy_time = [4.2, 3, 3.8, 5, 4.6]
            Susan_time = [5.2, 4.6, 3.9, 4.4, 5]

            # time taken by both the swimmers
            time = [4.2, 3, 3.8, 5, 4.6, 5.2, 4.6, 3.9, 4.4, 5]
            st.caption("Checking the Normality of the Data")
            tstats, pval = stats.shapiro(time)
            st.write("Test Stats_Shapiro: ", tstats)
            st.write("Pvalue_Shapiro: ", pval)
            st.write("**Conclusion:** From the above result, we can see that the p-value is greater than 0.05, thus we can say that the time taken by both the swimmers is normally distributed.")
            # perform Levene's test
            # levene() returns a tuple having the values of test statistics and the corresponding p-value
            st.caption("Performing Levene's Test")
            stat, p_value = stats.levene(Amy_time, Susan_time)
            st.write("Test Stats_Levene: ", stat)
            st.write("Pvalue_Levene: ", p_value)
            st.write("**Conclusion:**From the above result, we can see that the p-value is greater than 0.05, thus we can say that the population variances are equal.")
            st.markdown("**The null and alternative hypothesis is:**")
            st.write('''**H0: There is no difference between the average time taken by Amy and Susan ( 𝜇1−𝜇2=0 )**''')
            st.write('''**H1: There is difference between the average time taken by Amy and Susan ( 𝜇1−𝜇2≠0 )**''')
            # size of first sample
            n_1 = len(Amy_time)

            # size of second sample
            n_2 = len(Susan_time)

            # degrees of freedom for 2 sample t-test
            st.write('Degrees of freedom:', n_1 + n_2 - 2)
            t_stat, p_val = stats.ttest_ind(a = Amy_time, b = Susan_time)
            st.write("Test Statistic:", t_stat)
            st.write("P Value:", p_val)
            st.caption("Now Draw the Conclusions...")
        st.markdown("---")
            
# 4. A multinational company had organized a presentation activity to test the soft skills of their 6 sales executives and then offered them a skill development course. After the completion of the course, the executives again appeared for the presentation and the scores before and after the course are recorded. Test the company's claim that the course was effective in developing soft skills with 90% confidence using the p-value technique

df_score = pd.read_excel("data/paired_data.xlsx")
with q4:
    if sbar=="Day 03":
        q = f"**Q.4. A multinational company had organized a presentation activity to test the soft skills of their 6 sales executives and then offered them a skill development course. After the completion of the course, the executives again appeared for the presentation and the scores before and after the course are recorded. Test the company's claim that the course was effective in developing soft skills with 90% confidence using the p-value technique.**"
        st.markdown(q)
        pressed = st.button("Q.4. Solution", True)
        if pressed:
            st.write(df_score.head(2))
            stat, p_value = stats.shapiro(df_score['before_score'])
            st.write('Test statistic:', stat)
            st.write('P-Value:', p_value)
            st.write("**Inference:** From the above result, we can see that the p-value is greater than 0.05, thus we can say that the scores before the skill development course are normally distributed.")
            stat, p_value = stats.shapiro(df_score['after_score'])
            st.write('Test statistic:', stat)
            st.write('P-Value:', p_value)
            st.write("**Inference:** From the above result, we can see that the p-value is greater than 0.05, thus we can say that the scores after the skill development course are normally distributed.")
            st.write('''
                     The null and alternative hypothesis is:
                     H0: The skill development course was not effective in developing the soft skills (mew<=0)
                     H1: The skill development course was effective in developing the soft skills (mew>0)   
                     ''')
            t_stat, p_val = stats.ttest_rel(df_score['after_score'], df_score['before_score'])
            st.write("Pvalue", pval)
            st.write("We can see that the p-value is less than 0.1. Thus, we reject the null hypothesis and conclude that the skill development course was effective in developing soft skills of sales executives.")
    st.markdown("---")
    
#5. A survey conducted by the department of education states that the proportion of students who quit education due to financial crisis is more than 38%. To test this claim a group of 450 students is selected out of which 205 are found to be dropped out from school due to financial crisis. Test the claim using a critical value method with 95% confidence.

with q5:
    if sbar=="Day 03":
        q = f"**Q.5. A survey conducted by the department of education states that the proportion of students who quit education due to financial crisis is more than 38%. To test this claim a group of 450 students is selected out of which 205 are found to be dropped out from school due to financial crisis. Test the claim using a critical value method with 95% confidence.**"
        st.markdown(q)
        pressed = st.button("Q.5. Solution", True)
        if pressed:
            st.markdown("**The null and alternative hypothesis is:**")
            st.latex(r'''H0: P \leq 0.38''')
            st.latex(r'''H1: P > 0.38 ''')
            z_val = np.abs(round(stats.norm.isf(q = 0.05), 2))
            st.write('Critical value for one-tailed Z-test:', z_val)
            # sample size
            n = 450
            # number of children who quit the school
            x = 205
            # sample proportion
            p_samp = x / n
            # hypothesized proportion
            hypo_p = 0.38
            # calculate test statistic value for 1 sample proportion test
            z_prop = (p_samp - hypo_p) / np.sqrt((hypo_p * (1 - hypo_p)) / n)
            st.write('Test statistic:', z_prop)
            st.write("Here the test statistic is greater than the critical value (= 1.64). Thus, we reject the null hypothesis and conclude that there is enough evidence to state that the proportion of students who quit education due to financial crisis is more than 38%.")
            
        st.markdown("---")

#6. Two leading medical institutes CureOn and MedFirst have produced new vaccines on ebola. The vaccine produced by CureOn is given to 252 people in the UK out of which 78 had severe side-effects also the vaccine produced by MedFirst is given to 425 people in the UK out of which 92 had severe side-effects. Can we conclude that the vaccine produced by MedFirst is more reliable? Test the claim using p-value technique with 99% confidence.
with q6:
    if sbar=="Day 03":
        q = f"**Q.6. Two leading medical institutes CureOn and MedFirst have produced new vaccines on ebola. \
            The vaccine produced by CureOn is given to 252 people in the UK out of which 78 had severe side-effects also the vaccine produced by MedFirst is given to 425 people in the UK out of which 92 had severe side-effects. Can we conclude that the vaccine produced by MedFirst is more reliable? Test the claim using p-value technique with 99% confidence.**"
        st.markdown(q)
        pressed = st.button("Q.6. Solution", True)
        if pressed:
            st.markdown("**The null and alternative hypothesis is:**")
            st.latex(r'''H0: P1 \leq P2''')
            st.latex(r'''H1: P1 > P2 ''')
            with st.echo():
                
                CureOn_size = 252
                Med_size = 425
                CureOn_eff = 78
                Med_eff = 92
                z_prop, p_val = sm.stats.proportions_ztest(count = np.array([CureOn_eff, Med_eff]), 
                                                nobs = np.array([CureOn_size, Med_size]),  
                                                alternative = 'larger')
                st.write('p-value:', p_val)
            st.write("Here the p-value is less than 0.01. Thus, we reject the null hypothesis and conclude that the vaccine produced by MedFirst is more reliable.")
            
        st.markdown("---")

# 7. A research paper in the medical journal claims that the average height of females in Nebraska is less than 168 cm. A group of physicians conducted a survey and collected the heights of 95 females from Nebraska, and recorded the average height as 163 cm with a standard deviation of 7 cm. Assume that the sample is drawn from a normally distributed population. Test the claim in the research paper using the 95% confidence interval for the population mean.

with q7:
    if sbar=="Day 03":
        q = f"**Q.7. A research paper in the medical journal claims that the average height of females in Nebraska is less than 168 cm. A group of physicians conducted a survey and collected the heights of 95 females from Nebraska, and recorded the average height as 163 cm with a standard deviation of 7 cm. Assume that the sample is drawn from a normally distributed population. Test the claim in the research paper using the 95% confidence interval for the population mean.**"
        st.markdown(q)
        pressed = st.button("Q.7. Solution", True)
        if pressed:
            st.markdown("**The null and alternative hypothesis is:**")
            st.latex(r'''H0:\mu \geq 168''')
            st.latex(r'''H1:\mu < 168 ''')
            with st.echo():
                n = 95
                # sample mean 
                samp_mean = 163
                
                # sample standard deviation
                samp_std = 7
               
                # Creating Confidence Interval
                interval = stats.norm.interval(0.95, loc = samp_mean, scale = samp_std / np.sqrt(n))
                
                st.write('Confidence interval for population mean:', interval)
                
            st.write("Here the confidence interval does not contain the value in the null hypothesis (i.e. 168), thus we reject the null hypothesis and thus, we have enough evidence to conclude that the average height of females in Nebraska is less than 168 cm.")