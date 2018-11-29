# On this day, Nov 29, 2018, scrape the https://punchng.com/ sections as listed below
# 1. JUST IN
# 2. TRENDING
# Return the output as a JSON in Javascript

# SOLUTION

# 1. JUST IN

let topstories = document.querySelectorAll('li > a > h3');
let response = {};

for (count = 0; count < topstories.length; count++){
    response[count] = topstories[count].textContent;
}
document.write(JSON.stringify(response))


# 2. TRENDING

let topstories = document.querySelectorAll('li > span > a >h1');
let response = {};

for (count = 0; count < topstories.length; count++){
    response[count] = topstories[count].textContent;
}
document.write(JSON.stringify(response))