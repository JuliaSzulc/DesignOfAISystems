import requests
from base64 import b64encode
from datetime import date, datetime

class TaskManager:
    def __init__(self, credentials):
        self.auth_header = None
        self.obtain_token(credentials['key'], credentials['secret'])

    def obtain_token(self, key, secret):
        credentials = b64encode('{}:{}'.format(key, secret).encode()).decode()
        header = {'Authorization': 'Basic ' + credentials,
                  'Content-Type': 'application/x-www-form-urlencoded'}
        params = {'grant_type': 'client_credentials'}

        resp = requests.post('https://api.vasttrafik.se/token',
                             headers=header,
                             params=params)

        token = resp.json()['access_token']
        self.auth_header = {'Authorization': 'Bearer ' + token}

    def send_request(self, url, params=None):
        params['format'] = 'json'
        resp = requests.get(url, headers=self.auth_header, params=params)
        return resp.json()

    def get_stop_id(self, stop):
        url = 'https://api.vasttrafik.se/bin/rest.exe/v2/location.name'
        resp = self.send_request(url, {'input': stop})

        id = resp['LocationList']['StopLocation'][0]['id']
        return id

    def get_first_trip(self, form):
        origin_id = self.get_stop_id(form['origin'])
        dest_id = self.get_stop_id(form['destination'])

        url = 'https://api.vasttrafik.se/bin/rest.exe/v2/trip'
        params = {'originId': origin_id,
                  'destId': dest_id,
                  'numTrips': 1}
        resp = self.send_request(url, params)
        trip = resp['TripList']['Trip'][0]['Leg']

        response = [
            trip['type'].lower(),
            trip['sname'],
            trip['Origin']['name'],
            trip['Destination']['name'],
            trip['direction'],
            trip['Origin']['time']
        ]
        return response

    def get_first_line(self, form):
        origin_id = self.get_stop_id(form['origin'])

        url = 'https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard'
        params = {'id': origin_id,
                  'date': date.today().strftime("%Y%m%d"),
                  'time': form['time (hh:mm)'],
                  'timeSpan': 360,  # next 6 hours
                  'maxDeparturesPerLine': 1  # only one line-direction combination
                  }
        resp = self.send_request(url, params)

        departure_board = resp['DepartureBoard']['Departure']
        line_departures = [trip for trip in departure_board
                           if trip['sname'] == form['line']]

        responses = {}

        for i, departure in zip(range(len(line_departures)), line_departures):
            response = [
                departure['type'].lower(),
                departure['sname'],
                departure['direction'],
                departure['stop'],
                departure['time'],
                ''
            ]
            responses[i] = response

        return responses

    def get_average_trip_time(self, form):
        origin_id = self.get_stop_id(form['origin'])
        dest_id = self.get_stop_id(form['destination'])

        url = 'https://api.vasttrafik.se/bin/rest.exe/v2/trip'
        params = {'originId': origin_id,
                  'destId': dest_id,
                  'numTrips': 20}

        resp = self.send_request(url, params)
        trips = resp['TripList']['Trip']

        time_sum = 0
        counter = 0

        for trip in trips:
            trip = trip['Leg']

            if isinstance(trip, list):
                for alt_trip in trip:
                    time_sum += self.get_trip_time(alt_trip)
                counter += 1
                continue

            time_sum += self.get_trip_time(trip)
            counter += 1

        avg_time = time_sum / counter / 60  # minutes

        response = [
            int(avg_time),
            trips[0]['Leg']['Origin']['name'],
            trips[0]['Leg']['Destination']['name'],
            '',
            '',
            ''
        ]

        return response

    def get_trip_time(self, trip):
        origin_time = trip['Origin']['time']
        origin_time = datetime.strptime(origin_time, "%H:%M")

        dest_time = trip['Destination']['time']
        dest_time = datetime.strptime(dest_time, "%H:%M")

        trip_time = dest_time - origin_time

        return trip_time.seconds

    def create_query(self, form):
        choice = {
            1: self.get_first_trip,
            2: self.get_first_line,
            3: self.get_average_trip_time
        }

        action = choice.get(form['id'])
        response = action(form)

        return response
