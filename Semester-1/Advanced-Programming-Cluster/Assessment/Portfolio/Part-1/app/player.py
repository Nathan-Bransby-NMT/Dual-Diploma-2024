class Player:

    _unique_id: str
    _name: str

    def __init__(self, unique_id: str, name: str) -> None:
        self._unique_id = unique_id
        self._name = name

    def __str__(self) -> str:
        return f'Player: uid={self.uid!r}, name={self.name!r}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.uid!r}, {self.name!r})'

    @property
    def uid(self) -> str:
        if not self._unique_id:
            raise ValueError('Error: No Unique ID provided.')
        return self._unique_id

    @property
    def name(self) -> str:
        if not self._name:
            raise ValueError('Error: No Name provided.')
        return self._name
