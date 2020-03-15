import warnings

from hypothesis import given
from hypothesis.errors import HypothesisDeprecationWarning
from hypothesis.extra.numpy import arrays
import numpy
import pytest

from fragile.core.functions import relativize
from fragile.core.states import StatesEnv, StatesModel, StatesWalkers
from fragile.core.utils import NUMPY_IGNORE_WARNINGS_PARAMS
from fragile.core.walkers import Walkers


warnings.filterwarnings("ignore", category=HypothesisDeprecationWarning)


@pytest.fixture()
def states_walkers():
    return StatesWalkers(10)


N_WALKERS = 13


def get_walkers_discrete_gym():
    env_params = {
        "states": {"size": (128,), "dtype": numpy.int64},
        "observs": {"size": (64, 64, 3), "dtype": numpy.float32},
        "rewards": {"dtype": numpy.float32},
        "ends": {"dtype": numpy.bool_},
    }
    model_params = {
        "actions": {"size": (10,), "dtype": numpy.int64},
        "dt": {"size": None, "dtype": numpy.float32},
    }
    return Walkers(
        n_walkers=N_WALKERS, env_state_params=env_params, model_state_params=model_params
    )


def get_function_walkers():
    env_params = {
        "states": {"size": (3,), "dtype": numpy.int64},
        "observs": {"size": (3,), "dtype": numpy.float32},
        "rewards": {"dtype": numpy.float32},
        "ends": {"dtype": numpy.bool_},
    }
    model_params = {
        "actions": {"size": (3,), "dtype": numpy.int64},
        "dt": {"size": None, "dtype": numpy.float32},
    }
    return Walkers(
        n_walkers=N_WALKERS,
        env_state_params=env_params,
        model_state_params=model_params,
        minimize=True,
    )


walkers_config = {"discrete-gym": get_walkers_discrete_gym, "function": get_function_walkers}
walkers_fixture_params = ["discrete-gym", "function"]


class TestStatesWalkers:
    def test_reset(self, states_walkers):
        for name in states_walkers.keys():
            assert states_walkers[name] is not None, name
            assert len(states_walkers[name]) == states_walkers.n, name

        states_walkers.reset()
        for name in states_walkers.keys():
            assert states_walkers[name] is not None, name
            assert len(states_walkers[name]) == states_walkers.n, name

    def test_update(self, states_walkers):
        states_walkers = StatesWalkers(10)
        states_walkers.reset()
        test_vals = numpy.arange(states_walkers.n)
        states_walkers.update(virtual_rewards=test_vals, distances=test_vals)
        assert (states_walkers.virtual_rewards == test_vals).all()
        assert (states_walkers.distances == test_vals).all()


class TestWalkers:
    @pytest.fixture(params=walkers_fixture_params)
    def walkers(self, request):
        return walkers_config.get(request.param, get_walkers_discrete_gym)()

    def test_init(self, walkers):
        pass

    def test_repr_not_crashes(self, walkers):
        assert isinstance(walkers.__repr__(), str)

    def test_getattr(self, walkers):
        assert isinstance(walkers.states.will_clone, numpy.ndarray)
        assert isinstance(walkers.env_states.observs, numpy.ndarray)
        assert isinstance(walkers.env_states, StatesEnv)
        assert isinstance(walkers.model_states, StatesModel)
        with pytest.raises(AttributeError):
            assert isinstance(walkers.moco, numpy.ndarray)

    def test_calculate_end_condition(self, walkers):
        walkers.reset()
        walkers.states.update(end_condition=numpy.ones(walkers.n))
        assert walkers.calculate_end_condition()
        walkers.states.update(end_condition=numpy.zeros(walkers.n))
        assert not walkers.calculate_end_condition()
        walkers.max_iters = 10
        walkers.n_iters = 8
        assert not walkers.calculate_end_condition()
        walkers.n_iters = 11
        assert walkers.calculate_end_condition()

    def test_alive_compas(self, walkers):
        end_cond = numpy.ones_like(walkers.states.end_condition).astype(bool).copy()
        end_cond[3] = 0
        walkers.states.end_condition = end_cond
        compas = walkers.get_alive_compas()
        assert numpy.all(compas == 3), "Type of end_cond: {} end_cond: {}: alive ix: {}".format(
            type(end_cond), end_cond, walkers.states.alive_mask
        )
        assert len(compas.shape) == 1

    def test_update_clone_probs(self, walkers):
        walkers.reset()
        walkers.states.update(virtual_rewards=relativize(numpy.arange(walkers.n)))
        walkers.update_clone_probs()
        assert 0 < numpy.sum(walkers.states.clone_probs == walkers.states.clone_probs[0]), (
            walkers.states.virtual_rewards,
            walkers.states.clone_probs,
        )
        walkers.reset()
        walkers.update_clone_probs()
        assert numpy.sum(walkers.states.clone_probs == walkers.states.clone_probs[0]) == walkers.n
        assert walkers.states.clone_probs.shape[0] == walkers.n
        assert len(walkers.states.clone_probs.shape) == 1

    def test_balance_not_crashes(self, walkers):
        walkers.reset()
        walkers.balance()
        assert walkers.states.will_clone.sum() == 0

    def test_accumulate_rewards(self, walkers):
        walkers.reset()
        walkers._accumulate_rewards = True
        walkers.states.update(cum_rewards={None, 3})  # Override array of Floats and set to None
        walkers.states.update(cum_rewards=None)
        rewards = numpy.arange(len(walkers))
        walkers._accumulate_and_update_rewards(rewards)
        assert (walkers.states.cum_rewards == rewards).all()
        walkers._accumulate_rewards = False
        walkers.states.update(cum_rewards=numpy.zeros(len(walkers)))
        rewards = numpy.arange(len(walkers))
        walkers._accumulate_and_update_rewards(rewards)
        assert (walkers.states.cum_rewards == rewards).all()
        walkers._accumulate_rewards = True
        walkers.states.update(cum_rewards=numpy.ones(len(walkers)))
        rewards = numpy.arange(len(walkers))
        walkers._accumulate_and_update_rewards(rewards)
        assert (walkers.states.cum_rewards == rewards + 1).all()

    @given(observs=arrays(numpy.float32, shape=(N_WALKERS, 64, 64, 3)))
    def test_distances_not_crashes(self, walkers, observs):
        with numpy.errstate(**NUMPY_IGNORE_WARNINGS_PARAMS):
            walkers.env_states.update(observs=observs)
            walkers.calculate_distances()
            assert isinstance(walkers.states.distances[0], numpy.float32)
            assert len(walkers.states.distances.shape) == 1
            assert walkers.states.distances.shape[0] == walkers.n
