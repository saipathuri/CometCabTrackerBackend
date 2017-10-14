# this file is not used anymore, it was used for the bs4 scraper, didn't want to delete it
class Cab():
    def __init__(self):
        self.name = 'Cab'
        self.id = '1234567'
        self.heading = 0
        self.ignition = False
        self.latitude = '32.9859896'
        self.longitude = '-96.7517943'
        self.moved = '2017-01-01T00:00:00'
        self.updated = '2017-01-01T00:00:00'
        self.velocity = '0'

    def __init__(self, name, id, heading, ignition, latitude, longitude, moved, updated, velocity):
        self.name = name
        self.id = id
        self.heading = heading
        self.ignition = ignition
        self.latitude = latitude
        self.longitude = longitude
        self.moved = moved
        self.updated = updated
        self.velocity = velocity

    def __str__(self):
        out = ''
        out += 'Cab: %s\n' % self.name
        out += 'Info: \n'
        out += '\tId: %s\n' % self.id
        out += '\tHeading: %s\n' % self.heading
        out += '\tIgnition: %s\n' % self.ignition
        out += '\tLatitude: %s\n' % self.latitude
        out += '\tLongitude: %s\n' % self.longitude
        out += '\tMoved: %s\n' % self.moved
        out += '\tUpdated: %s\n' % self.updated
        out += '\tVelocity: %s\n' % self.velocity

        return out
