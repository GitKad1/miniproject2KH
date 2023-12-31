# INF601 - Advanced Programming in Python
# Kadmiel Herbert
# Mini Project 2

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.

#(5/5 points) Proper import of packages used.

#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve such as:
#"How many homes in the US have access to 100Mbps Internet or more?"
#"How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
#Here are some other great datasets: https://www.kaggle.com/datasets

#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.

#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.

#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.

#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!

#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.

#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.


def createCharts(amounts):

    for amount in amounts:
        #create sorted dataframe
        data = pd.read_csv('gdp_per_capita.csv')
        country2020 = data[(data['2020'] < amount)]
        country2020 = country2020.sort_values('2020', ascending=False).head(5)

        #get country and 2020 columns
        countryArray = country2020['Country Name']
        country2020 = country2020['2020']

        #create numpy arrays
        countryY = np.array(country2020)
        countryX = np.array(range(len(countryArray)))

        #plot chart and create lables and title
        plt.plot(countryX, countryY)
        plt.xlabel("Countries")
        plt.ylabel("GDP per Capita")
        plt.title("Countries with the highest GDP per capita under {amount}")
        plt.xticks(countryX, list(countryArray))

        #Save charts as PNG files to Chart directory
        saveFile = f"Charts/Countriesunder{amount}.png"
        plt.savefig(saveFile)

        #show charts
        plt.show()


def getAmounts():
    #Get 5 amounts from the user from the user

    amounts = []
    print("Please enter 5 amounts.")
    for i in range(1, 6):

        #Test if the amount is valid
        while True:
            print("Enter amount " + str(i))
            number = input()
            try:
                amounts.append(float(number))
                break
            except:
                print("That is not a valid amount.")

    return amounts


#Start of program
#Create Charts folder
try:
    Path("Charts").mkdir()
except FileExistsError:
    pass

amounts = getAmounts()
createCharts(amounts)

