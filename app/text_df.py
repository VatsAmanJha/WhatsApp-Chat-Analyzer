import pandas as pd
import re
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")


def what_app_chat_to_data_frame(data):
    pattern = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}"
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    messages = [message.strip(" -") for message in messages]
    df = pd.DataFrame(
        {
            "DateTime": dates,
            "user_message": messages,
        }
    )
    df["DateTime"] = pd.to_datetime(df["DateTime"], format="%m/%d/%y, %H:%M")
    # df["DateTime"] = df["DateTime"].dt.strftime("%Y-%m-%d %I:%M:%S %p")

    users = []
    messages = []
    for message in df["user_message"]:
        entry = re.split("([\w\W]+?):\s", message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append("WhatApp Notification")
            messages.append(entry[0])
    df['Year'] = df['DateTime'].dt.year
    df['Month'] = df['DateTime'].dt.month_name()
    df['Day'] = df['DateTime'].dt.day
    df['Hour'] = df['DateTime'].dt.hour
    df['Minute'] = df['DateTime'].dt.minute
    df['Day_Name']=df['DateTime'].dt.day_name()
    df["User"] = users
    df["Message"] = messages
    df.drop(columns=["user_message"], inplace=True)

    return df
