# Anvil Error Tracker

This project allows you to collect and track any errors in your app. It comes with a dashboard for better analyzing and monitoring your errors. It is built for [Anvil](https://anvil.works?utm_source=github:app_README), the framework for building web apps with nothing but Python.

## Features

* Group same errors, merge similar errors and maintain a timeline of any updates and occurrences for it.
* Mark any error as fixed or ignore the ones that don’t need to be fixed.
* See details for any error including the detailed traceback, users facing it, device details for users, link to session logs, etc.
* Keep a track of errors that were previously fixed but had reappeared.
* Filter, search and sort errors. You can also search by email to see errors faced by a user
* Allows multiple users to collaborate
  
## How to Use It

**Step 1:** Clone the Base App - https://anvil.works/build#clone:AFZOVYSJUBCSX5OV=I6YEGM2ZW5KHUGYJZRZS5TH3
This app has the actual app as a third-party dependency inside it (Which allows live updates from the original repository without cloning again)

**Step 2:** Add the Error Tracker Dependency to the App you want to use it for.
You can add it as a third-party dependency using the app token `TE6Q6FOVYDAFQFVB`

**Step 3:** Add the existing tables from Error Tracker Dashboard App to your main app
You need to add the following tables - 

* app_data
* errors
* timeline

## How to Add Users

The dashboard allows users to sign up, but keeps the account disabled by default. As the app owner, you can enable accounts that you want to allow access to by checking the enabled column on the Data Tables in Anvil Editor
___

**To get Announcements for this app, subscribe to the notifications for Discussions.**
You can post any queries or feature requests on the discussions - https://github.com/Divyesh06/Anvil-Error-Tracker/discussions

## How to Contribute

To contribute to this library, you can create a fork of this repository, edit it in the Anvil Editor, and submit a pull request.

## Error Tracker Dependency

The dashboard requires a minimal Error Tracker Dependency to be added to your main Anvil App for tracking errors. You can add it to your app using the App token - `TE6Q6FOVYDAFQFVB`

Clone Link - https://anvil.works/build#clone:TE6Q6FOVYDAFQFVB=ELBOEQAVEFDO3MGSENOQDUFU

Github Repo - https://github.com/Divyesh06/Error-Tracker-Dependency-anvil

Follow the guide at https://github.com/Divyesh06/Error-Tracker-Dependency-anvil/blob/master/README.md to implement error tracking
