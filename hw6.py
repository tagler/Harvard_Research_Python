grouped_birds = birddata.groupby("bird_name")
mean_speeds = grouped_birds.speed_2d.mean()
grouped_birds.head()

mean_altitudes = grouped_birds.altitude.mean()

birddata.date_time = pd.to_datetime(birddata.date_time)
birddata["date"] = birddata.date_time.dt.date
birddata.date.head()

grouped_bydates = birddata.groupby("date")
mean_altitudes_perday = grouped_bydates.altitude.mean()

grouped_birdday = birddata.groupby(["bird_name","date"])
mean_altitudes_perday = grouped_birdday.altitude.mean()
mean_altitudes_perday.head()

data = birddata.groupby(["bird_name","date"]).speed_2d.mean()
eric_daily_speed  = birddata[birddata.bird_name == "Eric"].groupby("date").speed_2d.mean()
sanne_daily_speed = birddata[birddata.bird_name == "Sanne"].groupby("date").speed_2d.mean()
nico_daily_speed  = birddata[birddata.bird_name == "Nico"].groupby("date").speed_2d.mean()

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()

birddata[birddata.bird_name == "Eric"]