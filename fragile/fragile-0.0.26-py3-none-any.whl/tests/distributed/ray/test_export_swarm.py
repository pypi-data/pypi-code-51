import sys

import numpy
import pytest

from fragile.distributed.ray.export_swarm import ExportedWalkers, ExportSwarm
from tests.distributed.ray import init_ray, ray


def create_cartpole_swarm():
    from fragile.core import DiscreteEnv, DiscreteUniform, Swarm
    from plangym.minimal import ClassicControl

    swarm = Swarm(
        model=lambda x: DiscreteUniform(env=x),
        env=lambda: DiscreteEnv(ClassicControl()),
        reward_limit=51,
        n_walkers=50,
        max_iters=100,
        reward_scale=2,
    )
    return swarm


swarm_types = [create_cartpole_swarm]


def create_distributed_export():
    return ExportSwarm.remote(create_cartpole_swarm)


swarm_dict = {"export": create_distributed_export}
swarm_names = list(swarm_dict.keys())


def kill_swarm(swarm):
    try:
        swarm.__ray_terminate__.remote()
    except AttributeError:
        pass
    ray.shutdown()


@pytest.mark.skipif(sys.version_info >= (3, 8), reason="Requires python3.7 or lower")
class TestExportInterface:
    @pytest.fixture(params=swarm_names, scope="class")
    def export_swarm(self, request):
        init_ray()
        swarm = swarm_dict.get(request.param)()
        request.addfinalizer(lambda: kill_swarm(swarm))
        return swarm

    def test_reset(self, export_swarm):
        reset = ray.get(export_swarm.reset.remote())
        assert reset is None

    def test_get_data(self, export_swarm):
        states_attr = ray.get(export_swarm.get_data.remote("cum_rewards"))
        assert isinstance(states_attr, numpy.ndarray)
        env_attr = ray.get(export_swarm.get_data.remote("observs"))
        assert isinstance(env_attr, numpy.ndarray)
        model_attr = ray.get(export_swarm.get_data.remote("actions"))
        assert isinstance(model_attr, numpy.ndarray)
        walkers_attr = ray.get(export_swarm.get_data.remote("minimize"))
        assert isinstance(walkers_attr, bool)
        swarm_attr = ray.get(export_swarm.get_data.remote("n_import"))
        assert isinstance(swarm_attr, int)

    def test_get_empty_walkers(self, export_swarm):
        walkers = ray.get(export_swarm.get_empty_export_walkers.remote())
        assert isinstance(walkers, ExportedWalkers)
        assert len(walkers) == 0

    def test_run_exchange_step(self, export_swarm):
        empty_walkers = ray.get(export_swarm.get_empty_export_walkers.remote())
        ray.get(export_swarm.run_exchange_step.remote(empty_walkers))

        walkers = ExportedWalkers(3)
        walkers.rewards = numpy.array([999, 777, 333])
        walkers.states = numpy.array(
            [[999, 999, 999, 999], [777, 777, 777, 777], [333, 333, 333, 333]]
        )
        walkers.id_walkers = numpy.array([999, 777, 333])
        walkers.observs = numpy.array(
            [[999, 999, 999, 999], [777, 777, 777, 777], [333, 333, 333, 333]]
        )
        ray.get(export_swarm.reset.remote())
        exported = ray.get(export_swarm.run_exchange_step.remote(walkers))
        best_found = ray.get(export_swarm.get_data.remote("best_reward"))
        assert len(exported) == ray.get(export_swarm.get_data.remote("n_export"))
        assert best_found == 999
