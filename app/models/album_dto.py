

class AlbumDto:
    id: int
    title: str
    artistName: str

    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title