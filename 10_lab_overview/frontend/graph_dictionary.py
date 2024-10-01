from frontend.graphs import ViewsTrend, Top5MostWatchedVideos, Top5ClickExposure



graph_options= {
    "Visningar över tid": ViewsTrend(),
    "Top 5 videos med flest visningar": Top5MostWatchedVideos(),
    "Top 5 klick procent av exponeringar": Top5ClickExposure()
}