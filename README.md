# application_email_tracker

### Motivation

I am in the same boat as countless others right now. Hindered by COVID-19, we are all struggling to get hired. The number of applications one has to usually make just to get into an interview has nearly doubled tripled to the undeniably trying circumstances. To make sense of it all, the go-to option is maintain a list of all the positions that you have applied to. But with us applying to hundreds of positions on several job boards every month, keeping track of it all becomes a daunting task in itself.

One thing to note however, is that no matter the number of applications or the plaftorm used, there is always an **email receipt** of the position you have submitted an application for. Email Classification is a pretty common Machine Learning Algorithm with many beginner courses using the Spam vs Not Spam Classification as a staple. So theorectically, if you could obtain enough of these job application receipt emails, label them and then do some quick supervised learning upon it, you could potentially sort all the application emails under a single label. 

As a fun little weekend project that would slightly lessen my job hunting woes, I decided to give this a shot.

### Prerequisites

To start off, you'll need to enable the Gmail API for your Gmail account.
To activate the Gmail API [Click Here](https://developers.google.com/gmail/api/quickstart/python)
Make sure you are logged in to the Gmail account you want to add the job applcation label for.
Follow the instructions, leaving the defaults untouched, and as easy as 1 2 3, you will have enabled the Gmail API.

What you wil need to do next, is to download the ** CREDENTIALS** file (json) this API provides you with. It should be named `credentials.json` by default. (Hurray if that's the case). You need to put this file under the `gmail_credentials/` folder in the directory. These credentials are private and unique to your Gmail Account (don't worry there is also token creation session in place), so *CAREFUL* who you trust it with.

In case the file isn't called `credentials.json` you can either rename it to that or choose a name of your liking and supply the labeler with that name as shown in the [Instructions Section](#Using-the-labeler).

### Installation

We need the Gmail API to access our emails using Python Code. There is a stock Python wrapper from Google in stead of which I chose the more friendlier Simple Gmail API and I've got to say it lives up to its name.

For details on the `simplegmail` package [click here](https://pypi.org/project/simplegmail/)

```SCSS
pip3 install simplegmail
```
```SCSS
conda create --name <env> --file requirements.txt
```
### Using the labeler

#### Create a Label in Gmail

### Future Work

### Acknowledgements
