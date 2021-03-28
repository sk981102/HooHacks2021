# HooHacks2021
(UVA Hackathon) HooHacks for 2021, By Shaun Kim

## Inspiration
"7 Vaccine Myths Debunked"

Those eye-catching headlines drag people's attention, but what are people really concerned about? What are others discussing online about the vaccinations? 

Our goals are to educate people about vaccines and collect data about people's fear. 

### i) Educating users about vaccinations

### ii) Gathering data ad building a strong database for people's concern about the vaccine

## What it does

The web-application allows users to take the survey. The questions are derived from the most pressing concerns from the online community. Based on the users' answer, we provide truth from the reliable sources such as CDC, WHO, etc. We record individual responses in the database to provide policy makers/ healthcare providers more insights into where people's concerns are coming from.

## How we built it

Web Application: Django & sqlite3

ML Algorithms: Sentiment Analysis - TextBlob, Topic Modeling - gensim LDA

Data Collection: PRAW, from reddit

## Challenges we ran into
1. SpiCy got updated and did not support the old TextBlob sentiment analysis measure
2. Producing pretty graphics and data visualizations
3. Just web development in general. Not too experienced with it

## Accomplishments that we're proud of
We built everything from scratch, even data collection :)

## What we learned

## What's next for DebunkVax
1. Continue building analysis in different online communities to inform public and derive insights

2. We want to scrape data from various pharmacies and let people know of the availability without having to go into each pharmacy website. 

3. Collect more detailed data to build a robust database to help healthcare workers and policymakers what concerns the public the most. 

4. Censor languages better! 
5. 
