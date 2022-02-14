# Anime Watchlist App

[View the live project here.](https://anime1watchlist.herokuapp.com/)

This app was created to help keep track of all the diffrent titles you've seen,
speaking from experience this is a very useful app when you've seen over 100 different ones.

**User Goals:**

- To keep track of all the different titles you've seen.
- To make sure the title you want to add to the list is not already there.

**Site Owner Goals:**

- To help the user easily add titles to the list.
- Double check the users inputs to make sure the titles are not the same.

![how the website looks on diffrent devices](/images/am-i-responsive.png)

## How to Use

Its pretty simple you type in the title you wish to add to or edit in the list to get started
and then get follow up questions based on user inputs and just to make sure the list is normal 
you have to type in specified words for the program to take you to the next step, so you don't have to
worry about making some kind of mistake.

## Data Flow Model

This is an updated version based on my mentors suggestions and feedback, the original one
was a lot more simple.

![Data Flow Model](/images/data_flow_model.png)

## Features

1. **Anime Title Input**

![Anime Title Input](/images/anime-title.png)

- Input asking for the title the user wants to add.

2. **Anime Title In List**

![Anime Title In List](/images/title-exist.png)

- Comes up if the title exists in the list asking if you've seen the title or not.

3. **Anime title Not In List**

![Anime Title Not In List](/images/title-not-in-list.png)

- Comes up if the title is not in the list asking if you've seen the title or not.

4. **Add Another Title**

![Add Another Title](/images/add-another-title.png)

- Comes up at the end asking if you want to add another title or to finish up and shut down the program.

5. **Current Watchlist**

![Current Watchlist](/images/current_watchlist.png)

- This feature was created for the accessors as a user would have access to the spreadsheet and see everything happening in there.
- This is only useful until the watchlist is small as later on the Watchlist would have over 300 diffrent titles.

## Future Features

1. Add a data base with all anime titles to make sure the user did not make any spelling mistakes and to make sure the title exists.
2. Sort the watchlist in alphabetical order.

## Bugs

- No bugs have been found.

## Testing

- Passed the code through PEP8 linter and confirmed there are no problems.
- Manually entered both a title in and not in the list to make sure evrything works.
- Purposefully used incorrect or empty input data to make sure the program would be prepared for them.

## Validation Testing

- PEP8 - no errors were found.

## Deployment

- Fork or clone this repository.
- Create a new Heroku app.
- Set the buildbacks to **Python** and **NodeJS** in that order.
- Link the Heroku app to repository.
- Click on **Deploy**.

## Credits
- Code Institute Tutor Support - The best help anyone could ask for.
- My Mentor.