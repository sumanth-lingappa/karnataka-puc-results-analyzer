# karnataka-puc-results-analyzer
Analyzing Karnataka (India) PUC Results of 2020

> This mini project is for educational purpose only.

# Inspiration
I took the project's inspiration from my friend [Ravi](github.com/ravisutrave)'s [parse-sslc-results](github.com/ravisutrave/parse-sslc-results) repository

# Analysis
There can be many analysis made from the data collected - 
- percentage of student passed/failed
- subject wise pass/fail ratio
- Impact of COVID-19 on students
- - In 2020, due to COVID-19, `English` exam was conducted after almost 4 months of lockdown. 
- etc


# Misc
`students_results.zip` has a full set of more than 85k student database
`student_results` folder contains a sample database

# Few unix commands to try
- `awk '{print $1,$4}' * | grep GRAND | sed 's/\[//g' | sed 's/\]//g' | sed "s/'//g" | awk '{print $2}' |sort -nk 1`