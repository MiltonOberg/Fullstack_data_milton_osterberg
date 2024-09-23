from frontend.graphs import ViewsTrend, CountryViews, Top5MostWatchedVideos, Top5ClickExposure


graph_options= {
    "Views over time": ViewsTrend(),
    "Views per country": CountryViews(),
    "Top 5 most watched videos": Top5MostWatchedVideos(),
    "Top 5 click percentage of exposure": Top5ClickExposure()
}
