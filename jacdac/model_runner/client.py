# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class ModelRunnerClient(Client):
    """
    Runs machine learning models.
     * 
     * Only models with a single input tensor and a single output tensor are supported at the moment.
     * Input is provided by Sensor Aggregator service on the same device.
     * Multiple instances of this service may be present, if more than one model format is supported by a device.
    Implements a client for the `Model Runner <https://microsoft.github.io/jacdac-docs/services/modelrunner>`_ service.

    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_MODEL_RUNNER, JD_MODEL_RUNNER_PACK_FORMATS, role)


    @property
    def auto_invoke_every(self) -> Optional[int]:
        """
        When register contains `N > 0`, run the model automatically every time new `N` samples are collected.
        Model may be run less often if it takes longer to run than `N * sampling_interval`.
        The `outputs` register will stream its value after each run.
        This register is not stored in flash., 
        """
        return self.register(JD_MODEL_RUNNER_REG_AUTO_INVOKE_EVERY).value()

    @auto_invoke_every.setter
    def auto_invoke_every(self, value: int) -> None:
        self.register(JD_MODEL_RUNNER_REG_AUTO_INVOKE_EVERY).set_values(value)


    @property
    def last_run_time(self) -> Optional[int]:
        """
        The time consumed in last model execution., _: us
        """
        return self.register(JD_MODEL_RUNNER_REG_LAST_RUN_TIME).value()

    @property
    def allocated_arena_size(self) -> Optional[int]:
        """
        Number of RAM bytes allocated for model execution., _: B
        """
        return self.register(JD_MODEL_RUNNER_REG_ALLOCATED_ARENA_SIZE).value()

    @property
    def model_size(self) -> Optional[int]:
        """
        The size of the model in bytes., _: B
        """
        return self.register(JD_MODEL_RUNNER_REG_MODEL_SIZE).value()

    @property
    def last_error(self) -> Optional[str]:
        """
        Textual description of last error when running or loading model (if any)., 
        """
        return self.register(JD_MODEL_RUNNER_REG_LAST_ERROR).value()

    @property
    def format(self) -> Optional[ModelRunnerModelFormat]:
        """
        The type of ML models supported by this service.
        `TFLite` is flatbuffer `.tflite` file.
        `ML4F` is compiled machine code model for Cortex-M4F.
        The format is typically present as first or second little endian word of model file., 
        """
        return self.register(JD_MODEL_RUNNER_REG_FORMAT).value()

    @property
    def format_version(self) -> Optional[int]:
        """
        A version number for the format., 
        """
        return self.register(JD_MODEL_RUNNER_REG_FORMAT_VERSION).value()

    @property
    def parallel(self) -> Optional[bool]:
        """
        (Optional) If present and true this service can run models independently of other
        instances of this service on the device., 
        """
        return self.register(JD_MODEL_RUNNER_REG_PARALLEL).bool_value()


    def set_model(self, model_size: int) -> None:
        """
        Open pipe for streaming in the model. The size of the model has to be declared upfront.
        The model is streamed over regular pipe data packets.
        The format supported by this instance of the service is specified in `format` register.
        When the pipe is closed, the model is written all into flash, and the device running the service may reset.
        """
        self.send_cmd_packed(JD_MODEL_RUNNER_CMD_SET_MODEL, model_size)
    
