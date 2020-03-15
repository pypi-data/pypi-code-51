import mlflow

import os

from typing import Any, Dict, List, Optional
from os.path import basename, sep


class Tracker:

    def __init__(self, experiment_name: str, artifact_root_path: str):
        self.__experiment_name: str = experiment_name
        self.__artifact_root_path: str = artifact_root_path

    def start_run(self):
        mlflow.set_experiment(self.__experiment_name)

    def track(self,
              artifact_file_paths: Optional[List[str]] = None,
              parameters: Optional[Dict[str, Any]] = None,
              metrics: Optional[Dict[str, Any]] = None,
              tags: Optional[Dict[str, str]] = None):
        if artifact_file_paths:
            for artifact_file_path in artifact_file_paths:
                artifact_path = artifact_file_path[len(self.__artifact_root_path):-len(basename(artifact_file_path))]
                artifact_path = artifact_path.strip(sep)  # remove leading and trailing / or \
                if self.__mlflow_repo_is_remote():
                    artifact_path = artifact_path.replace(sep, "/")  # replace Windows separator with S3 forward slash
                mlflow.log_artifact(local_path=artifact_file_path, artifact_path=artifact_path)
        if parameters:
            for parameter_name, parameter_value in parameters.items():
                mlflow.log_param(parameter_name, parameter_value)
        if metrics:
            for metric_name, metric_value in metrics.items():
                mlflow.log_metric(metric_name, metric_value)
        if tags:
            for tag_name, tag_value in tags.items():
                mlflow.set_tag(tag_name, tag_value)

    @staticmethod
    def end_run():
        mlflow.end_run()

    @staticmethod
    def __mlflow_repo_is_remote() -> bool:
        result: bool = False
        env_name = "MLFLOW_TRACKING_URI"
        if env_name in os.environ:
            env_value = os.environ[env_name]
            result = "localhost" not in env_value
        return result
