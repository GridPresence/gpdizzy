class CliTool ():
    '''
    Abstract base class for CLI Tool apps
    '''
    def __init__(self) -> None:
        self._configure()
        self._process()

    def _configure (self) -> None:
        raise NotImplementedError("Abstract base CliTool has no implementation of the _configure() method")

    def _process (self) -> None:
        raise NotImplementedError("Abstract base CliTool has no implementation of the _process() method")