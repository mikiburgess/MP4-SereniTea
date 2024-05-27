<p align="center">
  <img src="" alt="...">
</p>

<h1 align="center">Deploying SereniTea Emporium</h1>

> A Guide to Development and Deployment

This section describes how to use the SereniTea project repository for undertaking further local development or deploying the site to Heroku.

- - -

## Local Development

#### How to Fork this Project Repo
1. Log in (or sign up) to Github.
2. Navigate to the project repository.
3. Click the Fork button at the top right of the page.

#### How to Clone this Project Repo
1. Log in (or sign up) to GitHub.
2. Navigate to the project repository.
3. Click on the Code button, and select the Local tab.
4. Select whether you would like to clone with HTTPS, SSH or GitHub CLI.
5. Copy the link shown by clicking the 'copy' button.
6. Open the  in your code editor and change the current working directory to the location you want to use for the cloned directory.
7. Type the command 'git clone' into the terminal and then paste the link you copied from GitHub. 
8. Press enter. You will now have a clone of the project repo.

- - -

## Deployment to Heroku
This project was deployed using [Heroku](https://www.heroku.com/). The instructions to achieve this are below:

On your local machine:
1. Open a command line/terminal window within the main project folder. 
2. Create a requirements.txt file by typing `pip3 freeze --local > requirements.txt` at the command line. 
3. Create a Procfile by typing `echo web: python app.py > Procfile` 
4. Add and commit these files to Github.

Go to [Heroku](https://www.heroku.com/). Log in or create an account
1. Click the 'New' button and click 'Create new app'.
2. Enter a unique name for your project with no capital letters or spaces and select the region closest to you (e.g., Europe). Click 'Create App'.
3. Inside the dashboard for your new app, go to the 'Settings' tab. 
4. Scroll down and click 'Reveal Config Vars' then enter data for the following variables:
    - `IP : 0.0.0.0`
    - `PORT : 5000`
    - `... : ...` Your MongoDB database name
    - `DATABASE : ...` Your MongoBD URI (found on MongoDB by going to Clusters > Connect > Connect to your application)
    - `SECRET_KEY : ...` Your secret key

...



<p align="center">
    <img src="" alt="Heroku config variables">
<br>
<em>Figure 1: Heroku Config Variables</em>
</p>


5. Link Github repo to Heroku by navigating to the Deploy tab. Select 'GitHub, enter the name of the repository and click connect. 

<p align="center">
    <img src="images/heroku-connect-to-github.png" alt="Connecting to GitHub">
<br>
<em>Figure 2: Connecting to GitHub</em>
</p>

6. Once connected, select the repo branch to deploy (e.g. main) then click the Enable Automatic Deployment option.

<p align="center">
    <img src="images/heroku-deploy-branch.png" alt="Deployment branch">
<br>
<em>Figure 3: Selecting the branch to deploy</em>
</p>

To deploy immediately, in the Manual Deploy section again select the branch you want to deploy and click Deploy Branch. This will retrieve the code from GitHub. Once this is complete you'll receive a message "Your app was successfully deployed." You can then click "View" to access the deployed app.

<p align="center">
    <img src="images/heroku-app-deployed.png" alt="Successful deployment">
<br>
<em>Figure 4: Successful deployment</em>
</p>

<kbd>[Return to Top](#Deploying-SereniTea-Emporium)</kbd>

- - -
