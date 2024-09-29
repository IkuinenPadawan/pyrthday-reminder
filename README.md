# Pyrthday Reminder

A simple application that reminds you of birthdays via email. Python script running on a cronjob in a Docker container and checking a PostgreSQL database for today's birthdays and sending an email accordingly.

## Features

* Automated birthday reminders via email
    * Gmail supported
* Python script runs in a Docker container on a cron schedule
* Utilizes PostgreSQL to store and check birthdays
* Easy deployment using Docker Compose

## Requirements

* Docker Engine installed on your system
* A Gmail account with an app password (see setup instructions below)

## Setup

### Pre-Setup

1. Install Docker Engine:
	* Follow the installation guide at [Docker Documentation](https://docs.docker.com/engine/install/)
2. Create a free Gmail account
3. Create a Google App Password:
	* See the "How to Create a Google App Password" section below for steps

#### How to Create a Google App Password

To use the Birthday Reminder project, you'll need a Google App Password to send emails via Gmail.

1. Enable 2-Step Verification:
	* Go to [Google Account Security](https://myaccount.google.com/security)
	* Click on "2-Step Verification"
	* Follow the prompts to set up 2-Step Verification if you haven't done so already
2. Generate an App Password:
	* Go back to the [Google Account Security page](https://myaccount.google.com/security)
	* Click on "App passwords"
	* You may be prompted to sign in again for security purposes
	* Under "Select the app and device you want to generate the app password for", choose "Other (Custom name)"
	* Enter a name for your app (e.g., "Birthday Reminder") and click "Generate"
3. Copy the App Password:
	* A 16-character password will be generated
	* Copy this password—this will be used in place of your Google account password in the `.env` file of the Birthday Reminder project

**Note**: Store the App Password securely, as it allows access to your Google account for that specific app.

### Running the Application

1. Clone the repository:
   ```sh
   git clone https://github.com/IkuinenPadawan/birthday-reminder.git
   cd birthday-reminder
2. Create a `.env` file in the `src/` folder:
   ```sh
   touch src/.env
3. Set up your email and database credentials in the `.env` file:
   ```sh
   EMAIL_FROM_ADDRESS=<email address sent from>
   EMAIL_TO_ADDRESS=<email address sent to>
   EMAIL_PASSWORD=<email from address app password>
   DB_ENGINE_URL=postgresql+psycopg2://postgres:postgres@db:5432/birthdays
4. Modify the `src/daily_birthday_check.cron` file to set your desired schedule
5. Populate the `create_birthdays.sql` script with birthdays you want to remember:
   ```sh
   INSERT INTO Persons (first_name, birthday)
   VALUES
   ('Teddy', TO_DATE('1858-01-06', 'YYYY-MM-DD')),
   -- Add your rows here following the above format (omit comma from the end if only line):
   ('<name>', TO_DATE('<birthday>', 'YYYY-MM-DD'))
7. Run and build the application in the project root folder:
   ```sh
   docker-compose up --build -d
8. Enjoy not forgetting anymore birthdays
