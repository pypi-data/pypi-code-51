from .module import Module


class LightSensor(Module):
    possible_events = {'changed', 'filter_changed'}
    threshold = 10

    def __init__(self, id, alias, robot):
        Module.__init__(self, 'LightSensor', id, alias, robot)
        self._value = 0.0

    @property
    def lux(self):
        """ Light in lux. """
        return self._value

    def _update(self, new_state):
        Module._update(self, new_state)
        if 'lux' in new_state:
            new_light = new_state['lux']
            if new_light != self._value:
                self._pub_event('changed', self._value, new_light)

                if abs(new_light - self._value) > self.threshold:
                    self._pub_event('filter_changed',
                                    self._value, new_light)

                self._value = new_light
