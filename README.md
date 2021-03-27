# application_email_tracker

![theme image](https://github.com/sumedhgodbole/portfolio/blob/master/images/email_classification.png)

### Contents

* [Motivation](#Motivation)
* [Prerequisites](#Prerequisites)
* [Installation](#Installation)        
* [Usage](#Usage)
* [Future Work](#Future-Work)
* [Acknowledgements](#Acknowledgements)

### Motivation

I am in the same boat as countless others right now. Hindered by COVID-19, we are all struggling to get hired. The number of applications one has to usually make just to get into an interview has nearly tripled due to the undeniably trying circumstances. To make sense of it all, the go-to option is to maintain a list of all the positions that you have applied to. But with us applying to hundreds of positions on several job boards every month, keeping track of it all becomes a daunting task in itself.

One thing to note however, is that no matter the number of applications or the plaftorm used, there is always an **email receipt** of the position you have submitted an application for. Email Classification is a pretty common Machine Learning Algorithm with many beginner courses using the Spam vs Not Spam Classification as a staple. So theorectically, if you could obtain enough of these job application receipt emails, label them and then do some quick supervised learning upon it, you could potentially sort all the application emails under a single label. 

As a fun little weekend project that would slightly lessen my job hunting woes, I decided to give this a shot.

### Prerequisites

To start off, you'll need to enable the Gmail API for your Gmail account.

To activate the Gmail API [Click Here](https://developers.google.com/gmail/api/quickstart/python)

Make sure you are logged in to the Gmail account you want to add the job applcation label for.
Follow the instructions, leaving the defaults untouched, and as easy as 1 2 3, you will have enabled the Gmail API.

What you wil need to do next, is to download the **CREDENTIALS** file (json) this API provides you with. It should be named `credentials.json` by default. (Hurray if that's the case). You need to put this file under the `gmail_credentials/` folder in the directory. These credentials are private and unique to your Gmail Account, so **CAREFUL** who you trust it with (don't worry too much cause there is also a gmail token creation session in place that needs you to login and assign permission to this API :P).

In case the file isn't called `credentials.json` you can either rename it to that, or choose a name of your liking and supply the labeler with that name as shown in the [Usage](#Usage) section.

We also need to create a label in Gmail [Tutorial Here](https://support.google.com/mail/answer/118708?co=GENIE.Platform%3DDesktop&hl=en). The same one we want to bundle all the application receipts under.

If you already have a label you want to use, supply its name as an argument to the `labeler.py` file as shown below in the [Usage](#Usage) section.

Now that we have the credentials for the Gmail API, the a label ready and waiting in Gmail, the environment set up with all the necessary libraries in it as well as the code we need to run (that's kinda obvious :P . . .  clone the repository if you haven't already!), we can finally begin labelling our emails.

### Installation

Now we need a Python wrapper for Gmail API, to be able to access our emails using Python Code. From the wide range wrappers available, I decided to go with a friendly little implementation called the `Simple Gmail API` and I've got to say it lives up to its name.

To read more about the `simplegmail` package [click here](https://pypi.org/project/simplegmail/)

To install :

```SCSS
pip3 install simplegmail
```
This will install all the things you need to be able to run this code provided you are using a Python 3.7 environment like I did for this example.

In case you want to get fancy and have a conda installation set up, use the `reuqirements.txt` provided in the repository to establish a conda environment identical to the one I used for this project.

This can be done by running :
```SCSS
conda create --name <env> --file requirements.txt
```

### Usage

Right then! With a terminal open in the same directory, run the following :

```SCSS
python3 labeler.py --older 1 --newer 10 --cred 'credentials.json' --label 'applications'
```
the arguments work as explained below :

- **--older** the emails you scan are older than the specified number of **days** (default value 1)
- **--newer** the emails you scan are older than the specified number of **days** (default value 100)
- **--cred** the name of your credentials file inside the `gmail_credentials/` folder (default value is 'credentials.json')
- **--label** the label from your Gmail that you want to assign to mails that are identified as job application receipts (default value is 'applications')

Only for the first time this script runs, there will be a pop-up window that asks you to autheticate the API and to assign it the right permissions. This only happens the first time you run the script to generate a `gmail_token.json` file. You might need to re-run the script (```Ctrl + C``` to terminate the current execution) once you see the **Authentication successful** text inside the terminal.

What this file does, is it loads a [Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) which has already been trained using a total of about 1600 samples. Some other models namely, `the vectorizer` and the `feature selector` to preprocess the email content to be ready for some ML Magic.  Its as easy as that! We collect a bunch of emails that match our search criteria, process the subject of the email and put it through the Classifier. If the classifier thinks its a job application receipt, we label that email accordingly, all using the Python Code! 

And its done! Go check your inbox..

### Future Work

- incorporating the body of the email (in additiion to simply the subject line) for making the predictions
- adding a function that allows all the emails under this label to be exported as a `.csv` file
- introduce a scheduler that allows`labeler.py` to run automatically at predefined intervals
- trigerring a summary email that gives you a list of all the positions you recently applied to 

### Acknowledgements

- A huge thank you to the creators of [simplegmail](https://pypi.org/project/simplegmail/) 
- Many thanks to [MahnoorJaved98](https://github.com/MahnoorJaved98) for providing awesome details on [Email-Classification](https://towardsdatascience.com/the-best-machine-learning-algorithm-for-email-classification-39888e7b1846) using `sklearn`.
- Thanks to my friends [Varun Jammula](https://github.com/varunjammula), [Sagar Shah](https://github.com/shahsagar) and [Omkar Kulkarni](https://github.com/Omkar21) for lending me access to their emails and bravely agreeging to share a part of their job-hunting struggles with me :P

[^ back to top](#Contents)
