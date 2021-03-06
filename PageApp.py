import calendar
import json
from datetime import datetime

import facebook
import pandas as pd


class PageApp:
    def __init__(self, json_file):
        super().__init__()

        with open(json_file, "r") as f:
            data = json.load(f)

        page_token = data["page"]["token"]
        self.page_id = data["page"]["id"]
        sdk_version = data["sdk_version"]

        self.graph = facebook.GraphAPI(access_token=page_token, version=sdk_version)

    def daily_insights_for_month(self, metric, year, month):
        """Get a daily insight for a given year/month"""
        last_day_in_month = calendar.monthrange(year, month)[1]

        return self.graph.get_connections(
            id=self.page_id,
            connection_name="insights",
            metric=metric,
            period="day",
            since=datetime(year, month, 1),
            until=datetime(year, month, last_day_in_month),
            show_description_from_api_doc=True,
        )

    # ---------------------------------- DEMOGRAPHICS ----------------------------------
    def read_daily_demographics_insights_into_df(self, year, month):
        df_page = pd.DataFrame(columns=pd.MultiIndex(levels=[[], []], codes=[[], []]))

        # The total number of people who have liked your Page. (Unique Users). Lifetime
        fans = self.daily_insights_for_month("page_fans", year, month)
        end_time, value = list(), list()

        for item in fans["data"][0]['values']:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)
            except IndexError:
                value.append(0)

        df_page["fans", "value"] = pd.Series(data=value, index=end_time, name="value")

        # The number of people who liked your Page, broken down by the most common places where people can like
        # your Page.(Unique Users). Daily
        fans_by_like_source_unique = self.daily_insights_for_month(
            "page_fans_by_like_source_unique", year, month
        )
        end_time, news_feed, other = list(), list(), list()
        page_suggestions, restored_likes, search, your_page = (
            list(),
            list(),
            list(),
            list(),
        )

        for item in fans_by_like_source_unique["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                news_feed.append(item["value"]["News Feed"])
            except KeyError:
                news_feed.append(0)
            try:
                other.append(item["value"]["Other"])
            except KeyError:
                other.append(0)
            try:
                page_suggestions.append(item["value"]["Page Suggestions"])
            except KeyError:
                page_suggestions.append(0)
            try:
                restored_likes.append(
                    item["value"]["Restored Likes from Reactivated Accounts"]
                )
            except KeyError:
                restored_likes.append(0)
            try:
                search.append(item["value"]["Search"])
            except KeyError:
                search.append(0)
            try:
                your_page.append(item["value"]["Your Page"])
            except KeyError:
                your_page.append(0)

        df_page["fans_by_like_source_unique", "news_feed"] = pd.Series(
            data=news_feed, index=end_time, name="news_feed"
        )
        df_page["fans_by_like_source_unique", "other"] = pd.Series(
            data=other, index=end_time, name="other"
        )
        df_page["fans_by_like_source_unique", "page_suggestions"] = pd.Series(
            data=page_suggestions, index=end_time, name="page_suggestions"
        )
        df_page["fans_by_like_source_unique", "restored_likes"] = pd.Series(
            data=restored_likes, index=end_time, name="restored_likes"
        )
        df_page["fans_by_like_source_unique", "search"] = pd.Series(
            data=search, index=end_time, name="search"
        )
        df_page["fans_by_like_source_unique", "your_page"] = pd.Series(
            data=your_page, index=end_time, name="your_page"
        )

        # This is a breakdown of the number of Page Followers (Fans) from different countries. Daily

        page_fans_by_country = self.daily_insights_for_month(
            'page_fans_country', year, month
        )
        end_time = list() 
        it, es, id, us, pt, de, tr, br, eg, dz, fr, gb, mx, xk, pl, au, cn, co, ro, gr, ru = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), 

        for item in page_fans_by_country["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                it.append(item["value"]["IT"])
            except KeyError:
                it.append(0)
            except IndexError:
                it.append(0)
            try:
                es.append(item["value"]["ES"])
            except KeyError:
                es.append(0)
            except IndexError:
                es.append(0)
            try:
                id.append(item["value"]["IN"])
            except KeyError:
                id.append(0)
            except IndexError:
                id.append(0)
            try:
                us.append(item["value"]["US"])
            except KeyError:
                us.append(0)
            except IndexError:
                us.append(0)
            try:
                pt.append(item["value"]["PT"])
            except KeyError:
                pt.append(0)
            except IndexError:
                pt.append(0)
            try:
                de.append(item["value"]["DE"])
            except KeyError:
                de.append(0)
            except IndexError:
                de.append(0)
            try:
                tr.append(item["value"]["TR"])
            except KeyError:
                tr.append(0)
            except IndexError:
                tr.append(0)
            try:
                br.append(item["value"]["BR"])
            except KeyError:
                br.append(0)
            except IndexError:
                br.append(0)
            try:
                eg.append(item["value"]["EG"])
            except KeyError:
                eg.append(0)
            except IndexError:
                eg.append(0)
            try:
                dz.append(item["value"]["DZ"])
            except KeyError:
                dz.append(0)
            except IndexError:
                dz.append(0)
            try:
                fr.append(item["value"]["FR"])
            except KeyError:
                fr.append(0)
            except IndexError:
                fr.append(0)
            try:
                gb.append(item["value"]["GB"])
            except KeyError:
                gb.append(0)
            except IndexError:
                gb.append(0)
            try:
                mx.append(item["value"]["MX"])
            except KeyError:
                mx.append(0)
            except IndexError:
                mx.append(0)
            try:
                xk.append(item["value"]["XK"])
            except KeyError:
                xk.append(0)
            except IndexError:
                xk.append(0)
            try:
                pl.append(item["value"]["PL"])
            except KeyError:
                pl.append(0)
            except IndexError:
                pl.append(0)
            try:
                au.append(item["value"]["AU"])
            except KeyError:
                au.append(0)
            except IndexError:
                au.append(0)
            try:
                cn.append(item["value"]["CN"])
            except KeyError:
                cn.append(0)
            except IndexError:
                cn.append(0)
            try:
                co.append(item["value"]["CO"])
            except KeyError:
                co.append(0)
            except IndexError:
                co.append(0)
            try:
                ro.append(item["value"]["RO"])
            except KeyError:
                ro.append(0)
            except IndexError:
                ro.append(0)
            try:
                gr.append(item["value"]["GR"])
            except KeyError:
                gr.append(0)
            except IndexError:
                gr.append(0)
            try:
                ru.append(item["value"]["RS"])
            except KeyError:
                ru.append(0)
            except IndexError:
                ru.append(0)

        df_page["page_fans_country", "IT"] = pd.Series(
            data=it, index=end_time, name="IT"
        )
        df_page["page_fans_country", "ES"] = pd.Series(
            data=es, index=end_time, name="ES"
        )
        df_page["page_fans_country", "IN"] = pd.Series(
            data=id, index=end_time, name="IN"
        )
        df_page["page_fans_country", "US"] = pd.Series(
            data=us, index=end_time, name="US"
        )
        df_page["page_fans_country", "PT"] = pd.Series(
            data=pt, index=end_time, name="PT"
        )
        df_page["page_fans_country", "DE"] = pd.Series(
            data=de, index=end_time, name="DE"
        )
        df_page["page_fans_country", "TR"] = pd.Series(
            data=tr, index=end_time, name="TR"
        )
        df_page["page_fans_country", "BR"] = pd.Series(
            data=br, index=end_time, name="BR"
        )
        df_page["page_fans_country", "EG"] = pd.Series(
            data=eg, index=end_time, name="EG"
        )
        df_page["page_fans_country", "DZ"] = pd.Series(
            data=dz, index=end_time, name="DZ"
        )
        df_page["page_fans_country", "FR"] = pd.Series(
            data=fr, index=end_time, name="FR"
        )
        df_page["page_fans_country", "GB"] = pd.Series(
            data=gb, index=end_time, name="GB"
        )
        df_page["page_fans_country", "MX"] = pd.Series(
            data=mx, index=end_time, name="MX"
        )
        df_page["page_fans_country", "XK"] = pd.Series(
            data=xk, index=end_time, name="XK"
        )
        df_page["page_fans_country", "PL"] = pd.Series(
            data=pl, index=end_time, name="PL"
        )
        df_page["page_fans_country", "AU"] = pd.Series(
            data=au, index=end_time, name="AU"
        )
        df_page["page_fans_country", "CN"] = pd.Series(
            data=cn, index=end_time, name="CN"
        )
        df_page["page_fans_country", "CO"] = pd.Series(
            data=co, index=end_time, name="CO"
        )
        df_page["page_fans_country", "RO"] = pd.Series(
            data=ro, index=end_time, name="RO"
        )
        df_page["page_fans_country", "GR"] = pd.Series(
            data=gr, index=end_time, name="GR"
        )
        df_page["page_fans_country", "RS"] = pd.Series(
            data=ru, index=end_time, name="RS"
        )


        # This is a breakdown of the number of Page likes from the most common places where people can like your Page.
        # (Total Count). Daily
        fans_by_like_source = self.daily_insights_for_month(
            "page_fans_by_like_source", year, month
        )
        end_time, news_feed, other = list(), list(), list()
        page_suggestions, restored_likes, search, your_page = (
            list(),
            list(),
            list(),
            list(),
        )

        for item in fans_by_like_source["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                news_feed.append(item["value"]["News Feed"])
            except KeyError:
                news_feed.append(0)
            try:
                other.append(item["value"]["Other"])
            except KeyError:
                other.append(0)
            try:
                page_suggestions.append(item["value"]["Page Suggestions"])
            except KeyError:
                page_suggestions.append(0)
            try:
                restored_likes.append(
                    item["value"]["Restored Likes from Reactivated Accounts"]
                )
            except KeyError:
                restored_likes.append(0)
            try:
                search.append(item["value"]["Search"])
            except KeyError:
                search.append(0)
            try:
                your_page.append(item["value"]["Your Page"])
            except KeyError:
                your_page.append(0)

        df_page["fans_by_like_source", "news_feed"] = pd.Series(
            data=news_feed, index=end_time, name="news_feed"
        )
        df_page["fans_by_like_source", "other"] = pd.Series(
            data=other, index=end_time, name="other"
        )
        df_page["fans_by_like_source", "page_suggestions"] = pd.Series(
            data=page_suggestions, index=end_time, name="page_suggestions"
        )
        df_page["fans_by_like_source", "restored_likes"] = pd.Series(
            data=restored_likes, index=end_time, name="restored_likes"
        )
        df_page["fans_by_like_source", "search"] = pd.Series(
            data=search, index=end_time, name="search"
        )
        df_page["fans_by_like_source", "your_page"] = pd.Series(
            data=your_page, index=end_time, name="your_page"
        )

        return df_page

    # ---------------------------------- IMPRESSIONS -----------------------------------
    def read_daily_impressions_insights_into_df(self, year, month):
        df_page = pd.DataFrame(columns=pd.MultiIndex(levels=[[], []], codes=[[], []]))

        # The number of people who had any content from your Page or about your Page enter their screen. This includes
        # posts, check-ins, ads, social information from people who interact with your Page and more. (Unique Users).
        # Daily
        unique = self.daily_insights_for_month("page_impressions_unique", year, month)
        end_time, value = list(), list()

        for item in unique["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["impressions_unique", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        # The number of times any content from your Page or about your Page entered a person's screen.
        # This includes posts, check-ins, ads, social information from people who interact with your Page and more.
        # (Total Count). Daily
        impressions = self.daily_insights_for_month("page_impressions", year, month)
        end_time, value = list(), list()

        for item in impressions["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["impressions", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        # Total number of people who saw a story about your Page by story type. (Unique Users). Daily
        by_story_unique = self.daily_insights_for_month(
            "page_impressions_by_story_type_unique", year, month
        )
        end_time, mention, other, fan, page_post, checkin = (
            list(),
            list(),
            list(),
            list(),
            list(),
            list(),
        )

        for item in by_story_unique["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                mention.append(item["value"]["mention"])
            except KeyError:
                mention.append(0)
            try:
                other.append(item["value"]["other"])
            except KeyError:
                other.append(0)
            try:
                fan.append(item["value"]["fan"])
            except KeyError:
                fan.append(0)
            try:
                page_post.append(item["value"]["page post"])
            except KeyError:
                page_post.append(0)
            try:
                checkin.append(item["value"]["checkin"])
            except KeyError:
                checkin.append(0)

        df_page["impressions_by_story_unique", "mention"] = pd.Series(
            data=mention, index=end_time, name="mention"
        )
        df_page["impressions_by_story_unique", "other"] = pd.Series(
            data=other, index=end_time, name="other"
        )
        df_page["impressions_by_story_unique", "fan"] = pd.Series(
            data=fan, index=end_time, name="fan"
        )
        df_page["impressions_by_story_unique", "page_post"] = pd.Series(
            data=page_post, index=end_time, name="page_post"
        )
        df_page["impressions_by_story_unique", "checkin"] = pd.Series(
            data=checkin, index=end_time, name="checkin"
        )

        #  Total impressions of stories published by a friend about your Page by story type. (Total Count). Daily
        by_story = self.daily_insights_for_month(
            "page_impressions_by_story_type", year, month
        )
        end_time, mention, other, fan, page_post, checkin = (
            list(),
            list(),
            list(),
            list(),
            list(),
            list(),
        )

        for item in by_story["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                mention.append(item["value"]["mention"])
            except KeyError:
                mention.append(0)
            try:
                other.append(item["value"]["other"])
            except KeyError:
                other.append(0)
            try:
                fan.append(item["value"]["fan"])
            except KeyError:
                fan.append(0)
            try:
                page_post.append(item["value"]["page post"])
            except KeyError:
                page_post.append(0)
            try:
                checkin.append(item["value"]["checkin"])
            except KeyError:
                checkin.append(0)

        df_page["impressions_by_story", "mention"] = pd.Series(
            data=mention, index=end_time, name="mention"
        )
        df_page["impressions_by_story", "other"] = pd.Series(
            data=other, index=end_time, name="other"
        )
        df_page["impressions_by_story", "fan"] = pd.Series(
            data=fan, index=end_time, name="fan"
        )
        df_page["impressions_by_story", "page_post"] = pd.Series(
            data=page_post, index=end_time, name="page_post"
        )
        df_page["impressions_by_story", "checkin"] = pd.Series(
            data=checkin, index=end_time, name="checkin"
        )

        # Total Page Reach by user country. (Unique Users). Daily
        by_country = self.daily_insights_for_month(
            "page_impressions_by_country_unique", year, month
        )
        end_time = list()
        gb, us, ru, it = list(), list(), list(), list()

        for item in by_country["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                gb.append(item["value"]["GB"])
            except KeyError:
                gb.append(0)
            except IndexError:
                gb.append(0)
            try:
                us.append(item["value"]["US"])
            except KeyError:
                us.append(0)
            except IndexError:
                us.append(0)
            try:
                ru.append(item["value"]["RU"])
            except KeyError:
                ru.append(0)
            except IndexError:
                ru.append(0)

        df_page["impressions_by_country", "GB"] = pd.Series(
            data=gb, index=end_time, name="GB"
        )
        df_page["impressions_by_country", "US"] = pd.Series(
            data=us, index=end_time, name="US"
        )
        df_page["impressions_by_country", "RU"] = pd.Series(
            data=ru, index=end_time, name="RU"
        )

        # Total Page Reach by age and gender. (Unique Users). Daily
        by_age_gender_unique = self.daily_insights_for_month(
            "page_impressions_by_age_gender_unique", year, month
        )
        end_time = list()
        f_13_17, f_18_24, f_25_34, f_35_44, f_45_54, f_55_64 = (
            list(),
            list(),
            list(),
            list(),
            list(),
            list(),
        )
        f_65_plus = list()
        m_13_17, m_18_24, m_25_34, m_35_44, m_45_54, m_55_64 = (
            list(),
            list(),
            list(),
            list(),
            list(),
            list(),
        )
        m_65_plus = list()

        for item in by_age_gender_unique["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                f_13_17.append(item["value"]["F.13-17"])
            except KeyError:
                f_13_17.append(0)
            except IndexError:
                f_13_17.append(0)
            try:
                f_18_24.append(item["value"]["F.18-24"])
            except KeyError:
                f_18_24.append(0)
            except IndexError:
                f_18_24.append(0)
            try:
                f_25_34.append(item["value"]["F.25-34"])
            except KeyError:
                f_25_34.append(0)
            except IndexError:
                f_25_34.append(0)
            try:
                f_35_44.append(item["value"]["F.35-44"])
            except KeyError:
                f_35_44.append(0)
            except IndexError:
                f_35_44.append(0)
            try:
                f_45_54.append(item["value"]["F.45-54"])
            except KeyError:
                f_45_54.append(0)
            except IndexError:
                f_45_54.append(0)
            try:
                f_55_64.append(item["value"]["F.55-64"])
            except KeyError:
                f_55_64.append(0)
            except IndexError:
                f_55_64.append(0)
            try:
                f_65_plus.append(item["value"]["F.65+"])
            except KeyError:
                f_65_plus.append(0)
            except IndexError:
                f_65_plus.append(0)
            try:
                m_13_17.append(item["value"]["M.13-17"])
            except KeyError:
                m_13_17.append(0)
            except IndexError:
                m_13_17.append(0)
            try:
                m_18_24.append(item["value"]["M.18-24"])
            except KeyError:
                m_18_24.append(0)
            except IndexError:
                m_18_24.append(0)
            try:
                m_25_34.append(item["value"]["M.25-34"])
            except KeyError:
                m_25_34.append(0)
            except IndexError:
                m_25_34.append(0)
            try:
                m_35_44.append(item["value"]["M.35-44"])
            except KeyError:
                m_35_44.append(0)
            except IndexError:
                m_35_44.append(0)
            try:
                m_45_54.append(item["value"]["M.45-54"])
            except KeyError:
                m_45_54.append(0)
            except IndexError:
                m_45_54.append(0)
            try:
                m_55_64.append(item["value"]["M.55-64"])
            except KeyError:
                m_55_64.append(0)
            except IndexError:
                m_55_64.append(0)
            try:
                m_65_plus.append(item["value"]["M.65+"])
            except KeyError:
                m_65_plus.append(0)
            except IndexError:
                m_65_plus.append(0)

        df_page["impressions_by_age_gender_unique", "F.13-17"] = pd.Series(
            data=f_13_17, index=end_time, name="F.13-17"
        )
        df_page["impressions_by_age_gender_unique", "F.18-24"] = pd.Series(
            data=f_18_24, index=end_time, name="F.18-24"
        )
        df_page["impressions_by_age_gender_unique", "F.25-34"] = pd.Series(
            data=f_25_34, index=end_time, name="F.25-34"
        )
        df_page["impressions_by_age_gender_unique", "F.35-44"] = pd.Series(
            data=f_35_44, index=end_time, name="F.35-44"
        )
        df_page["impressions_by_age_gender_unique", "F.45-54"] = pd.Series(
            data=f_45_54, index=end_time, name="F.45-54"
        )
        df_page["impressions_by_age_gender_unique", "F.55-64"] = pd.Series(
            data=f_55_64, index=end_time, name="F.55-64"
        )
        df_page["impressions_by_age_gender_unique", "F.65+"] = pd.Series(
            data=f_65_plus, index=end_time, name="F.65+"
        )
        df_page["impressions_by_age_gender_unique", "M.13-17"] = pd.Series(
            data=m_13_17, index=end_time, name="M.13-17"
        )
        df_page["impressions_by_age_gender_unique", "M.18-24"] = pd.Series(
            data=m_18_24, index=end_time, name="M.18-24"
        )
        df_page["impressions_by_age_gender_unique", "M.25-34"] = pd.Series(
            data=m_25_34, index=end_time, name="M.25-34"
        )
        df_page["impressions_by_age_gender_unique", "M.35-44"] = pd.Series(
            data=m_35_44, index=end_time, name="M.35-44"
        )
        df_page["impressions_by_age_gender_unique", "M.45-54"] = pd.Series(
            data=m_45_54, index=end_time, name="M.45-54"
        )
        df_page["impressions_by_age_gender_unique", "M.55-64"] = pd.Series(
            data=m_55_64, index=end_time, name="M.55-64"
        )
        df_page["impressions_by_age_gender_unique", "M.65+"] = pd.Series(
            data=m_65_plus, index=end_time, name="M.65+"
        )

        return df_page

    # ----------------------------------- ENGAGEMENT -----------------------------------
    def read_daily_engagement_insights_into_df(self, year, month):
        df_page = pd.DataFrame(columns=pd.MultiIndex(levels=[[], []], codes=[[], []]))

        # The number of people who engaged with your Page. Engagement includes any click or story created.
        # (Unique Users). Daily
        engaged_users = self.daily_insights_for_month("page_engaged_users", year, month)
        end_time, value = list(), list()

        for item in engaged_users["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["engaged_users", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        # The number of of people who clicked on any of your content, by type. Stories that are created without clicking
        # on Page content (ex, liking the Page from timeline) are not included. (Unique Users). Daily
        by_consumption_type_unique = self.daily_insights_for_month(
            "page_consumptions_by_consumption_type_unique", year, month
        )
        end_time, video_play, other_clicks, photo_view, link_clicks = (
            list(),
            list(),
            list(),
            list(),
            list(),
        )

        for item in by_consumption_type_unique["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                video_play.append(item["value"]["video play"])
            except KeyError:
                video_play.append(0)
            try:
                other_clicks.append(item["value"]["other clicks"])
            except KeyError:
                other_clicks.append(0)
            try:
                photo_view.append(item["value"]["photo view"])
            except KeyError:
                photo_view.append(0)
            try:
                link_clicks.append(item["value"]["link clicks"])
            except KeyError:
                link_clicks.append(0)

        df_page["consumptions_by_type_unique", "video_play"] = pd.Series(
            data=video_play, index=end_time, name="video_play"
        )
        df_page["consumptions_by_type_unique", "other_clicks"] = pd.Series(
            data=other_clicks, index=end_time, name="other_clicks"
        )
        df_page["consumptions_by_type_unique", "photo_view"] = pd.Series(
            data=photo_view, index=end_time, name="photo_view"
        )
        df_page["consumptions_by_type_unique", "link_clicks"] = pd.Series(
            data=link_clicks, index=end_time, name="link_clicks"
        )

        # The number of clicks on any of your content, by type. Stories generated without clicks on page content
        # (e.g., liking the page in Timeline) are not included. (Total Count). Daily
        by_consumption_type = self.daily_insights_for_month(
            "page_consumptions_by_consumption_type", year, month
        )
        end_time, video_play, other_clicks, photo_view, link_clicks = (
            list(),
            list(),
            list(),
            list(),
            list(),
        )

        for item in by_consumption_type["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                video_play.append(item["value"]["video play"])
            except KeyError:
                video_play.append(0)
            try:
                other_clicks.append(item["value"]["other clicks"])
            except KeyError:
                other_clicks.append(0)
            try:
                photo_view.append(item["value"]["photo view"])
            except KeyError:
                photo_view.append(0)
            try:
                link_clicks.append(item["value"]["link clicks"])
            except KeyError:
                link_clicks.append(0)

        df_page["consumptions_by_type", "video_play"] = pd.Series(
            data=video_play, index=end_time, name="video_play"
        )
        df_page["consumptions_by_type", "other_clicks"] = pd.Series(
            data=other_clicks, index=end_time, name="other_clicks"
        )
        df_page["consumptions_by_type", "photo_view"] = pd.Series(
            data=photo_view, index=end_time, name="photo_view"
        )
        df_page["consumptions_by_type", "link_clicks"] = pd.Series(
            data=link_clicks, index=end_time, name="link_clicks"
        )

        # Total check-ins at your Place (Unique Users). Daily
        places_checkin = self.daily_insights_for_month(
            "page_places_checkin_total_unique", year, month
        )
        end_time, value = list(), list()

        for item in places_checkin["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["places_checkin", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        # The number of people who have given negative feedback to your Page, by type. (Unique Users). Daily
        negative_feedback_by_type_unique = self.daily_insights_for_month(
            "page_negative_feedback_by_type_unique", year, month
        )
        end_time, hide_all_clicks, hide_clicks, unlike_page_clicks = (
            list(),
            list(),
            list(),
            list(),
        )
        report_spam_clicks = list()

        for item in negative_feedback_by_type_unique["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                hide_all_clicks.append(item["value"]["hide_all_clicks"])
            except KeyError:
                hide_all_clicks.append(0)
            try:
                hide_clicks.append(item["value"]["hide_clicks"])
            except KeyError:
                hide_clicks.append(0)
            try:
                unlike_page_clicks.append(item["value"]["unlike_page_clicks"])
            except KeyError:
                unlike_page_clicks.append(0)
            try:
                report_spam_clicks.append(item["value"]["report_spam_clicks"])
            except KeyError:
                report_spam_clicks.append(0)

        df_page["negative_feedback_by_type_unique", "hide_all_clicks"] = pd.Series(
            data=hide_all_clicks, index=end_time, name="hide_all_clicks"
        )
        df_page["negative_feedback_by_type_unique", "hide_clicks"] = pd.Series(
            data=hide_clicks, index=end_time, name="hide_clicks"
        )
        df_page["negative_feedback_by_type_unique", "unlike_page_clicks"] = pd.Series(
            data=unlike_page_clicks, index=end_time, name="unlike_page_clicks"
        )
        df_page["negative_feedback_by_type_unique", "report_spam_clicks"] = pd.Series(
            data=report_spam_clicks, index=end_time, name="report_spam_clicks"
        )

        # The number of times people have given negative feedback to your Page, by type. (Total Count). Daily
        negative_feedback_by_type = self.daily_insights_for_month(
            "page_negative_feedback_by_type", year, month
        )
        end_time, hide_all_clicks, hide_clicks, unlike_page_clicks = (
            list(),
            list(),
            list(),
            list(),
        )
        report_spam_clicks = list()

        for item in negative_feedback_by_type["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                hide_all_clicks.append(item["value"]["hide_all_clicks"])
            except KeyError:
                hide_all_clicks.append(0)
            try:
                hide_clicks.append(item["value"]["hide_clicks"])
            except KeyError:
                hide_clicks.append(0)
            try:
                unlike_page_clicks.append(item["value"]["unlike_page_clicks"])
            except KeyError:
                unlike_page_clicks.append(0)
            try:
                report_spam_clicks.append(item["value"]["report_spam_clicks"])
            except KeyError:
                report_spam_clicks.append(0)

        df_page["negative_feedback_by_type", "hide_all_clicks"] = pd.Series(
            data=hide_all_clicks, index=end_time, name="hide_all_clicks"
        )
        df_page["negative_feedback_by_type", "hide_clicks"] = pd.Series(
            data=hide_clicks, index=end_time, name="hide_clicks"
        )
        df_page["negative_feedback_by_type", "unlike_page_clicks"] = pd.Series(
            data=unlike_page_clicks, index=end_time, name="unlike_page_clicks"
        )
        df_page["negative_feedback_by_type", "report_spam_clicks"] = pd.Series(
            data=report_spam_clicks, index=end_time, name="report_spam_clicks"
        )

        # The number of times people have given positive feedback to your Page, by type. (Unique Users). Daily
        positive_feedback_by_type_unique = self.daily_insights_for_month(
            "page_positive_feedback_by_type_unique", year, month
        )
        end_time, link, like, comment, other = list(), list(), list(), list(), list()

        for item in positive_feedback_by_type_unique["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                link.append(item["value"]["link"])
            except KeyError:
                link.append(0)
            try:
                like.append(item["value"]["like"])
            except KeyError:
                like.append(0)
            try:
                comment.append(item["value"]["comment"])
            except KeyError:
                comment.append(0)
            try:
                other.append(item["value"]["other"])
            except KeyError:
                other.append(0)

        df_page["positive_feedback_by_type_unique", "link"] = pd.Series(
            data=link, index=end_time, name="link"
        )
        df_page["positive_feedback_by_type_unique", "like"] = pd.Series(
            data=like, index=end_time, name="like"
        )
        df_page["positive_feedback_by_type_unique", "comment"] = pd.Series(
            data=comment, index=end_time, name="comment"
        )
        df_page["positive_feedback_by_type_unique", "other"] = pd.Series(
            data=other, index=end_time, name="other"
        )

        # The number of times people have given positive feedback to your Page, by type. (Total Count). Daily
        positive_feedback_by_type = self.daily_insights_for_month(
            "page_positive_feedback_by_type", year, month
        )
        end_time, link, like, comment, other = list(), list(), list(), list(), list()

        for item in positive_feedback_by_type["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                link.append(item["value"]["link"])
            except KeyError:
                link.append(0)
            try:
                like.append(item["value"]["like"])
            except KeyError:
                like.append(0)
            try:
                comment.append(item["value"]["comment"])
            except KeyError:
                comment.append(0)
            try:
                other.append(item["value"]["other"])
            except KeyError:
                other.append(0)

        df_page["positive_feedback_by_type", "link"] = pd.Series(
            data=link, index=end_time, name="link"
        )
        df_page["positive_feedback_by_type", "like"] = pd.Series(
            data=like, index=end_time, name="like"
        )
        df_page["positive_feedback_by_type", "comment"] = pd.Series(
            data=comment, index=end_time, name="comment"
        )
        df_page["positive_feedback_by_type", "other"] = pd.Series(
            data=other, index=end_time, name="other"
        )

        return df_page

    # ------------------------------------ REACTIONS -----------------------------------
    def read_daily_reactions_insights_into_df(self, year, month):

        df_page = pd.DataFrame(columns=pd.MultiIndex(levels=[[], []], codes=[[], []]))

        # Total post like reactions of a page. Daily
        reactions_like_total = self.daily_insights_for_month(
            "page_actions_post_reactions_like_total", year, month
        )
        end_time, value = list(), list()

        for item in reactions_like_total["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["reactions_like", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        # Total post love reactions of a page. Daily
        reactions_love_total = self.daily_insights_for_month(
            "page_actions_post_reactions_love_total", year, month
        )
        end_time, value = list(), list()

        for item in reactions_love_total["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["reactions_love", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        # Total post wow reactions of a page. Daily
        reactions_wow_total = self.daily_insights_for_month(
            "page_actions_post_reactions_wow_total", year, month
        )
        end_time, value = list(), list()

        for item in reactions_wow_total["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["reactions_wow", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        # Total post haha reactions of a page. Daily
        reactions_haha_total = self.daily_insights_for_month(
            "page_actions_post_reactions_haha_total", year, month
        )
        end_time, value = list(), list()

        for item in reactions_haha_total["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["reactions_haha", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        # Total post sorry reactions of a page. Daily
        reactions_sorry_total = self.daily_insights_for_month(
            "page_actions_post_reactions_sorry_total", year, month
        )
        end_time, value = list(), list()

        for item in reactions_sorry_total["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["reactions_sorry", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        # Total post anger reactions of a page. Daily
        reactions_anger_total = self.daily_insights_for_month(
            "page_actions_post_reactions_anger_total", year, month
        )
        end_time, value = list(), list()

        for item in reactions_anger_total["data"][0]["values"]:
            end_time.append(item["end_time"][:10])
            try:
                value.append(item["value"])
            except KeyError:
                value.append(0)

        df_page["reactions_anger", "value"] = pd.Series(
            data=value, index=end_time, name="value"
        )

        return df_page

    # ----------------------------- JOIN ALL PAGE INSIGHTS -----------------------------
    def write_daily_page_insights_into_csv(self, year, month):
        df_demographics = self.read_daily_demographics_insights_into_df(year, month)
        df_impressions = self.read_daily_impressions_insights_into_df(year, month)
        df_engagement = self.read_daily_engagement_insights_into_df(year, month)
        df_reactions = self.read_daily_reactions_insights_into_df(year, month)

        df_page = (
            df_demographics.join(df_impressions).join(df_engagement).join(df_reactions)
        )
        df_page.to_csv(f"Daily_page_insights_{year}_{month}.csv")


def main():
    app = PageApp("facebook.json")

    # change the year and month to get insights for a specific year/month
    app.write_daily_page_insights_into_csv(2022, 6)
    
if __name__ == "__main__":
    main()
