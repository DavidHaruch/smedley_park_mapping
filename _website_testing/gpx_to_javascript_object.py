import sys
import os
print(sys.argv)

import gpxpy
import gpxpy.gpx

for file in os.listdir(sys.argv[1]):
	#gpx_file = open(sys.argv[1], 'r')
	print('converting...' + sys.argv[1] + file)
	gpx_file = open(sys.argv[1] + file)
	js_file = open(sys.argv[1] + file + '.json', 'w+')

	gpx = gpxpy.parse(gpx_file)

	js_file.write('[\n')

	for track in gpx.tracks:
		for segment in track.segments:
			for point in segment.points:
				point_formatted = '{lat:' + str(point.latitude) + ',lng:' + str(point.longitude)+'},'
				# print '{'+'lat:{0},lng:{1},elv:{2}'.format(point.latitude, point.longitude, point.elevation)+'},'
				js_file.write(point_formatted + '\n')

	js_file.write(']')