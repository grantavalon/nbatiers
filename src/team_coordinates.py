import pandas as pd
import geocoder


def get_lat_lng(row):
	latlng = geocoder.google('{}, {}'.format(row.city, row.state)).latlng
	if not latlng:
		return get_lat_lng(row)
	return latlng


def main():
	team_data = pd.read_csv('../data/teams_original.csv', index_col=0)
	for ix, row in team_data.iterrows():
		latlng = get_lat_lng(row)
		print ix, latlng
		team_data.loc[ix, 'lat'] = latlng[0]
		team_data.loc[ix, 'long'] = latlng[1]
	team_data.to_csv('../data/teams.csv')


if __name__ == "__main__":
	main()