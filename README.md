# Activity App
A django REST repository for user and his activities. 

This repository contains 1 API
- User list containing respective activities

### Technology 

* Python (Django)
* SQLite 

## Code base contains 
* Db model
* APIs 

## Setup for development
* Create and activate `.env`
* Install packages using`pip install -r requirements/local.txt`
* Create `db.sqlite3` DB and run `./manage.py migrate --settings=activityapp.settings.local`
* In same folder conatining, `.env.example`, replicate into `.env` and replace dummy values with actual crednetials
* Run local server using `./mangae.py runserver --settings=activityapp.settings.local`

## Test local
- In postman/ any other equivalent tool: hit
   * GET  http://127.0.0.1:8000/user/activity/
   
## Project design
* Has 2 apps: `activity` and `utils`.
* `activity` has 2 models `User` and `ActivityPeriod`, and `utils` app has various general tools for API development.
* `activity` has custom command `create_users` for prepopulating the data using command `./manage.py create_users --settings=activityapp.settings.local` from `sample.json`.
* sample local development output
```{
    "ok": true,
    "members": [
        {
            "id": "8567153BD",
            "real_name": "Glinda Southgood",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "Aug 12 2020  04:15AM",
                    "end_time": "Aug 12 2020  05:15AM"
                },
                {
                    "start_time": "Sep 12 2020  04:15AM",
                    "end_time": "Sep 12 2020  05:15AM"
                },
                {
                    "start_time": "Oct 12 2020  04:15AM",
                    "end_time": "Oct 12 2020  05:15AM"
                }
            ]
        },
        {
            "id": "0F538ACD4",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity_periods": [
                {
                    "start_time": "Aug 12 2020  04:15AM",
                    "end_time": "Aug 12 2020  05:15AM"
                },
                {
                    "start_time": "Sep 12 2020  04:15AM",
                    "end_time": "Sep 12 2020  05:15AM"
                },
                {
                    "start_time": "Oct 12 2020  04:15AM",
                    "end_time": "Oct 12 2020  05:15AM"
                }
            ]
        },
        {
            "id": "BA728E3EC",
            "real_name": "Glinda Southgood",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "Aug 12 2020  04:15AM",
                    "end_time": "Aug 12 2020  05:15AM"
                },
                {
                    "start_time": "Sep 12 2020  04:15AM",
                    "end_time": "Sep 12 2020  05:15AM"
                },
                {
                    "start_time": "Oct 12 2020  04:15AM",
                    "end_time": "Oct 12 2020  05:15AM"
                }
            ]
        },
        {
            "id": "743D577A9",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity_periods": [
                {
                    "start_time": "Aug 12 2020  04:15AM",
                    "end_time": "Aug 12 2020  05:15AM"
                },
                {
                    "start_time": "Sep 12 2020  04:15AM",
                    "end_time": "Sep 12 2020  05:15AM"
                },
                {
                    "start_time": "Oct 12 2020  04:15AM",
                    "end_time": "Oct 12 2020  05:15AM"
                }
            ]
        },
        {
            "id": "38707E668",
            "real_name": "Admin",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "Aug 12 2020  04:15AM",
                    "end_time": "Aug 12 2020  04:15AM"
                }
            ]
        }
    ]
}```

