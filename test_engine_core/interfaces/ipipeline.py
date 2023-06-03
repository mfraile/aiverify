from abc import abstractmethod
from typing import Any, Tuple

from test_engine_core.interfaces.iplugin import IPlugin
from test_engine_core.plugins.enums.pipeline_plugin_type import PipelinePluginType


class IPipeline(IPlugin):
    """
    The IPipeline interface specifies methods for different supported pipeline formats
    """

    @staticmethod
    @abstractmethod
    def get_pipeline_plugin_type() -> PipelinePluginType:
        pass

    @abstractmethod
    def __init__(self, pipeline: Any) -> None:
        pass

    @abstractmethod
    def cleanup(self) -> None:
        pass

    @abstractmethod
    def setup(self) -> Tuple[bool, str]:
        pass

    @abstractmethod
    def get_pipeline(self) -> Any:
        pass

    @abstractmethod
    def get_pipeline_algorithm(self) -> str:
        pass

    @abstractmethod
    def set_pipeline(self, pipeline: Any) -> None:
        pass

    @abstractmethod
    def is_supported(self) -> bool:
        pass

    @abstractmethod
    def predict(self, data: Any, *args) -> Any:
        pass

    @abstractmethod
    def predict_proba(self, data: Any, *args) -> Any:
        pass

    @abstractmethod
    def score(self, data: Any, y_true: Any) -> Any:
        pass
