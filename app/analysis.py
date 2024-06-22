import pandas as pd
import re
from datetime import datetime
import warnings
import plotly.express as px
from plotly.offline import plot
from collections import Counter
import emoji
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
import io

warnings.filterwarnings("ignore")


def total_no_of_messages(df, user):
    if user == "Overall":
        return df.shape[0]

    else:
        return df[df["User"] == user].shape[0]


def total_no_of_word(df, user):
    if user == "Overall":
        words = []
        for message in df["Message"]:
            words.extend(message.split())

        return len(words)

    else:
        words = []
        temp_df = df[df["User"] == user]
        for message in temp_df["Message"]:
            words.extend(message.split())

        return len(words)


def total_no_media_file(df, user):
    media_row = df[df["Message"] == "<Media omitted>\n"]
    if user == "Overall":
        return media_row.shape[0]

    else:
        return media_row[media_row["User"] == user].shape[0]


def total_no_of_msg_with_url(df, user):
    url_regex = r"(http|https)://\S+"
    url_row = df[df["Message"].str.contains(url_regex)]
    if user == "Overall":
        return url_row.shape[0]

    else:
        return url_row[url_row["User"] == user].shape[0]


def top_five_user_table(df):
    top_df = df["User"].value_counts().reset_index().head(5)
    return top_df.rename(columns={"count": "MessageCount"})


def top_five_user_pie(df):
    top_df = df["User"].value_counts().reset_index().head(5)
    top_df = top_df.rename(columns={"count": "MessageCount"})
    pie_fig = px.pie(
        data_frame=top_df,
        names="User",
        values="MessageCount",
        title="Top 5 Users by Message Count",
    )
    return plot(pie_fig, output_type="div")


def top_five_user_bar(df):
    top_df = df["User"].value_counts().reset_index().head(5)
    top_df = top_df.rename(columns={"count": "MessageCount"})
    bar_fig = px.bar(
        data_frame=top_df,
        x="User",
        y="MessageCount",
        title="Top 5 Users by Message Count",
    )
    return plot(bar_fig, output_type="div")


def top_10_word(df, user):
    temp = df[df["User"] != "WhatApp Notification"]
    temp = temp[temp["Message"] != "<Media omitted>\n"]
    f = open("app\stop_hinglish.txt", "r")
    stop_word_hinglish = f.read()
    f = open("app\stopwords_hindi.txt", "r", encoding="utf-8")
    stop_word_hindi = f.read()
    stop_word = stop_word_hindi + stop_word_hinglish
    if user == "Overall":
        words = []
        for message in temp["Message"]:
            for word in message.lower().split():
                if word not in stop_word:
                    words.append(word)
        top_words_df = pd.DataFrame(Counter(words).most_common(10))
        return top_words_df.rename(columns={0: "Word", 1: "Frequency"})

    else:
        words = []
        temp_df = temp[temp["User"] == user]
        for message in temp_df["Message"]:
            for word in message.lower().split():
                if word not in stop_word:
                    words.append(word)

        top_words_df = pd.DataFrame(Counter(words).most_common(10))
        return top_words_df.rename(columns={0: "Word", 1: "Frequency"})


def top_10_emoji(df, user):
    if user == "Overall":
        words = []
        for message in df["Message"]:
            for c in message:
                if emoji.is_emoji(c):
                    words.append(c)
        top_emoji_df = pd.DataFrame(Counter(words).most_common(10))
        return top_emoji_df.rename(columns={0: "Emoji", 1: "Frequency"})

    else:
        temp_df = df[df["User"] == user]
        words = []
        for message in temp_df["Message"]:
            for c in message:
                if emoji.is_emoji(c):
                    words.append(c)
        top_emoji_df = pd.DataFrame(Counter(words).most_common(10))
        return top_emoji_df.rename(columns={0: "Emoji", 1: "Frequency"})


def year_wise_analysis(df, user):
    if user == "Overall":
        timeline_Year = df.groupby(["Year"]).count()["Message"].reset_index()
        bar_fig = px.bar(
            data_frame=timeline_Year,
            x="Year",
            y="Message",
            title="Year Wise Analysis",
        )
        line_fig = go.Figure()
        line_fig.add_trace(
            go.Scatter(
                x=timeline_Year["Year"],
                y=timeline_Year["Message"],
                mode="lines",
                name="Messages",
            )
        )
        bar_fig.update_traces(opacity=0.6)
        bar_fig.add_trace(line_fig.data[0])
        combined_plot = plot(bar_fig, output_type="div")

        return combined_plot
    else:
        user_df = df[df["User"] == user]
        timeline_Year = user_df.groupby(["Year"]).count()["Message"].reset_index()
        bar_fig = px.bar(
            data_frame=timeline_Year,
            x="Year",
            y="Message",
            title="Year Wise Analysis",
        )
        line_fig = go.Figure()
        line_fig.add_trace(
            go.Scatter(
                x=timeline_Year["Year"],
                y=timeline_Year["Message"],
                mode="lines",
                name="Messages",
            )
        )
        bar_fig.update_traces(opacity=0.6)
        bar_fig.add_trace(line_fig.data[0])
        combined_plot = plot(bar_fig, output_type="div")
        return combined_plot


def day_wise_analysis(df, user):
    if user == "Overall":
        timeline_Year = df.groupby(["Day_Name"]).count()["Message"].reset_index()
        bar_fig = px.bar(
            data_frame=timeline_Year,
            x="Day_Name",
            y="Message",
            title="Day Wise Analysis",
        )
        line_fig = go.Figure()
        line_fig.add_trace(
            go.Scatter(
                x=timeline_Year["Day_Name"],
                y=timeline_Year["Message"],
                mode="lines",
                name="Messages",
            )
        )
        bar_fig.update_traces(opacity=0.6)
        bar_fig.add_trace(line_fig.data[0])
        combined_plot = plot(bar_fig, output_type="div")

        return combined_plot
    else:
        user_df = df[df["User"] == user]
        timeline_Year = user_df.groupby(["Day_Name"]).count()["Message"].reset_index()
        bar_fig = px.bar(
            data_frame=timeline_Year,
            x="Day_Name",
            y="Message",
            title="Day Wise Analysis",
        )
        line_fig = go.Figure()
        line_fig.add_trace(
            go.Scatter(
                x=timeline_Year["Day_Name"],
                y=timeline_Year["Message"],
                mode="lines",
                name="Messages",
            )
        )
        bar_fig.update_traces(opacity=0.6)
        bar_fig.add_trace(line_fig.data[0])
        combined_plot = plot(bar_fig, output_type="div")
        return combined_plot


def month_wise_analysis(df, user):
    if user == "Overall":
        timeline_Year = df.groupby(["Month"]).count()["Message"].reset_index()
        bar_fig = px.bar(
            data_frame=timeline_Year,
            x="Month",
            y="Message",
            title="Month Wise Analysis",
        )
        line_fig = go.Figure()
        line_fig.add_trace(
            go.Scatter(
                x=timeline_Year["Month"],
                y=timeline_Year["Message"],
                mode="lines",
                name="Messages",
            )
        )
        bar_fig.update_traces(opacity=0.6)
        bar_fig.add_trace(line_fig.data[0])
        combined_plot = plot(bar_fig, output_type="div")

        return combined_plot
    else:
        user_df = df[df["User"] == user]
        timeline_Year = user_df.groupby(["Month"]).count()["Message"].reset_index()
        bar_fig = px.bar(
            data_frame=timeline_Year,
            x="Month",
            y="Message",
            title="Month Wise Analysis",
        )
        line_fig = go.Figure()
        line_fig.add_trace(
            go.Scatter(
                x=timeline_Year["Month"],
                y=timeline_Year["Message"],
                mode="lines",
                name="Messages",
            )
        )
        bar_fig.update_traces(opacity=0.6)
        bar_fig.add_trace(line_fig.data[0])
        combined_plot = plot(bar_fig, output_type="div")
        return combined_plot


def word_cloud(df, user):
    temp = df[df["User"] != "WhatApp Notification"]
    temp = temp[temp["Message"] != "<Media omitted>\n"]
    f = open("app\stop_hinglish.txt", "r")
    stop_word_hinglish = f.read()
    f = open("app\stopwords_hindi.txt", "r", encoding="utf-8")
    stop_word_hindi = f.read()
    stop_word = stop_word_hindi + stop_word_hinglish
    if user == "Overall":
        words = []
        for message in temp["Message"]:
            for word in message.lower().split():
                if word not in stop_word:
                    words.append(word)
        words_freq = dict(Counter(words).items())
        try:
            wordcloud = WordCloud(
                width=570, height=400, background_color="white",max_words=20,
            ).generate_from_frequencies(words_freq)
            img_data = io.BytesIO()
            wordcloud.to_image().save(img_data, format="PNG")
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.getvalue()).decode()

            return f'<img src="data:image/png;base64,{img_base64}" alt="Word Cloud">'
        except:
            pass
    else:
        words = []
        temp_df = temp[temp["User"] == user]
        for message in temp_df["Message"]:
            for word in message.lower().split():
                if word not in stop_word:
                    words.append(word)

        words_freq = dict(Counter(words).items())
        try:
            wordcloud = WordCloud(
                width=570, height=400, background_color="white",max_words=20
            ).generate_from_frequencies(words_freq)

            img_data = io.BytesIO()
            wordcloud.to_image().save(img_data, format="PNG")
            img_data.seek(0)
            img_base64 = base64.b64encode(img_data.getvalue()).decode()

            return f'<img src="data:image/png;base64,{img_base64}" alt="Word Cloud">'
        except:
            pass
