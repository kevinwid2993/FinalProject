# NBA Salary Prediction

The National Basketball Association (NBA) is a men's professional basketball league in North America, composed of 30 teams (29 in the United States and 1 in Canada). It is one of the four major professional sports leagues in the United States and Canada, and is widely considered to be the premier men's professional basketball league in the world. 

From the dataset which can be found here, https://www.kaggle.com/schmadam97/nba-regular-season-stats-20182019 . This project is going to predict the NBA player salary based on some of it's key feature:

1. Age
2. Points
3. Blocks
4. Steals
5. Assists
6. Rebounds

# Method 
I am using Random Forest Regressor model to predict the salary, because of it's score that reach 91%.
![score](https://user-images.githubusercontent.com/49969832/61688053-2f0dd200-ad4e-11e9-823e-1a78f17ee40e.png)

# How to run the program
1. Please run server.py on your terminal.
![server](https://user-images.githubusercontent.com/49969832/61688100-4c42a080-ad4e-11e9-8589-ad9f96f2154d.png)

2. Go to your web browser, than go to lhost:5000/ , it should be look like this.
![home0](https://user-images.githubusercontent.com/49969832/61687995-fec63380-ad4d-11e9-9b93-12e616a9ff1f.png)

3. Please fill the stats of your player.
![home](https://user-images.githubusercontent.com/49969832/61688112-56fd3580-ad4e-11e9-874b-b08c4bb6aa5d.png)

4. Your NBA Salary Prediction result
![result](https://user-images.githubusercontent.com/49969832/61688123-63818e00-ad4e-11e9-9546-a14d4b9fbdc0.png)

there you go! you have succesfully predict your NBA salary.

# Notes
i have put some additional information about the distribution plot of it's key feature, and the heatmap correlation for each features which can be found on the bottom of the homepage.
