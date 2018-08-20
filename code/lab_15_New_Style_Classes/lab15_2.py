#!/usr/bin/env python
"""
lab15_2.py (Optional) A Veggie class hierarchy, with a class method
and a staticmethod.
"""

class Veggie:
    """Instantiate: in subclass.
    """

    weather = "good"
    weather_d = {'bad': 4, 'ok': 7, 'good': 10}

    def PredictHarvest(self):
        """Returns a sentence predicting the harvest for the 
		Veggie.
        """
        harvest_index = self.weather_d[self.weather] - self.bug_index
        say = "%s will be %%s this year." % self
        if harvest_index > 8:
            return say % "great"
        if harvest_index > 5:
            return say % "ok"
        if harvest_index > 3:
            return say % "disappointing"
        return say % "zilch"

    @classmethod
    def UpdateBugIndex(cls, bug_index):
        """Changes the bug_index in the appropriate class.
        """
        if cls == Veggie:
            raise RuntimeError, "Veggie must in instantiated in a subclass."
        cls.bug_index = bug_index

    @staticmethod
    def UpdateWeather(weather):
        """Changes the weather in this class.
        """
        if weather not in Veggie.weather_d:
            raise ValueError, "weather must %s" % (
                ', '.join(possible_weather)
        Veggie.weather = weather

    def __str__(self):
        return self.__class__.__name__

class Asparagus(Veggie):
    bug_index = 2

class Corn(Veggie):
    bug_index = 1

class Squash(Veggie):
    bug_index = 3

def main():
    veggies = Asparagus(), Corn(), Squash()
    for veggie in veggies:
        print veggie.PredictHarvest()
    asparagus, corn, squash = veggies
    print "No bugs for asparagus."
    asparagus.UpdateBugIndex(0)
    for veggie in veggies:
        print veggie.PredictHarvest()
    print "Weather degraded to 'ok'."
    asparagus.UpdateWeather('ok')
    for veggie in veggies:
        print veggie.PredictHarvest()

if __name__ == '__main__':
    main()

