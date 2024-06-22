# dashboard/views.py
import pandas as pd
from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from .text_df import what_app_chat_to_data_frame
from .analysis import *
import plotly.express as px
from plotly.offline import plot


def index(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        data = file.read().decode("utf-8")
        df = what_app_chat_to_data_frame(data)
        if df is not None:
            # Convert Timestamp objects to string before storing in session
            df["DateTime"] = df["DateTime"].astype(str)
            request.session["csv_data"] = json.dumps(df.to_dict())
            return redirect("stats")
        else:
            return HttpResponse("Error processing data. Please check the input format.")
    return render(request, "index.html")


def stats(request):
    csv_data = request.session.get("csv_data")
    df = pd.DataFrame.from_dict(json.loads(csv_data))

    user_lst = df["User"].unique().tolist()
    user_lst.remove("WhatApp Notification")
    user_lst.sort()
    user_lst.insert(0, "Overall")

    if request.method == "POST" and "username" in request.POST:
        username = request.POST["username"]

        if username != "Overall":
            msg = total_no_of_messages(df, username)
            word = total_no_of_word(df, username)
            media = total_no_media_file(df, username)
            link = total_no_of_msg_with_url(df, username)
            top_word = top_10_word(df, username)
            top_emoji = top_10_emoji(df, username)
            year=year_wise_analysis(df,username)
            month=month_wise_analysis(df,username)
            day=day_wise_analysis(df,username)
            word_cloud_img = word_cloud(df, username)
            print(username, msg, word, media, link)
            return render(
                request,
                "statistics.html",
                {
                    "unique_users": user_lst,
                    "username": username,
                    "msg": msg,
                    "word": word,
                    "media": media,
                    "link": link,
                    "top_word": top_word.to_html(classes="table table-striped"),
                    "top_emoji": top_emoji.to_html(classes="table table-striped"),
                    "year":year,
                    "month":month,
                    "day":day,
                    "word_cloud":word_cloud_img ,
                },
            )
        else:
            top_emoji = top_10_emoji(df, username)
            msg = total_no_of_messages(df, username)
            word = total_no_of_word(df, username)
            media = total_no_media_file(df, username)
            link = total_no_of_msg_with_url(df, username)
            top_user = top_five_user_table(df)
            top_user_bar = top_five_user_bar(df)
            top_user_pie = top_five_user_pie(df)
            top_word = top_10_word(df, username)
            year=year_wise_analysis(df,username)
            month=month_wise_analysis(df,username)
            day=day_wise_analysis(df,username)
            word_cloud_img = word_cloud(df, username)
            print(username, msg, word, media, link)
            return render(
                request,
                "statistics.html",
                {
                    "unique_users": user_lst,
                    "username": username,
                    "msg": msg,
                    "word": word,
                    "media": media,
                    "link": link,
                    "top_user": top_user.to_html(classes="table table-striped"),
                    "top_user_bar": top_user_bar,
                    "top_user_pie": top_user_pie,
                    "top_word": top_word.to_html(classes="table table-striped"),
                    "top_emoji": top_emoji.to_html(classes="table table-striped"),
                    "year":year,
                    "month":month,
                    "day":day,
                    "word_cloud":word_cloud_img ,
                },
            )

    else:
        username = "Overall"
        year=year_wise_analysis(df,username)
        top_emoji = top_10_emoji(df, username)
        msg = total_no_of_messages(df, username)
        word = total_no_of_word(df, username)
        media = total_no_media_file(df, username)
        link = total_no_of_msg_with_url(df, username)
        top_user = top_five_user_table(df)
        top_user_bar = top_five_user_bar(df)
        top_user_pie = top_five_user_pie(df)
        top_word = top_10_word(df, username)
        month=month_wise_analysis(df,username)
        day=day_wise_analysis(df,username)
        word_cloud_img = word_cloud(df, username)
        print(username, msg, word, media, link)
        return render(
            request,
            "statistics.html",
            {
                "unique_users": user_lst,
                "username": username,
                "msg": msg,
                "word": word,
                "media": media,
                "link": link,
                "top_user": top_user.to_html(classes="table table-striped"),
                "top_user_bar": top_user_bar,
                "top_user_pie": top_user_pie,
                "top_word": top_word.to_html(classes="table table-striped"),
                "top_emoji": top_emoji.to_html(classes="table table-striped"),
                "year":year,
                "month":month,
                "day":day,
                "word_cloud":word_cloud_img ,
            },
        )
