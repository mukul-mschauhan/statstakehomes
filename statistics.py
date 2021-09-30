from types import CodeType
import pandas as pd
import numpy as np
import streamlit as st
st.set_page_config(layout="wide")
import scipy.stats as stats
import random

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

with header:
    st.title("Statistics Take Homes")
    st.subheader("Let's begin with some hands-on practice exercises")


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

