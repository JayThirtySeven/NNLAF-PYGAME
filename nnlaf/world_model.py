from rect import Rect


class Battle(Rect):
    """This class represents a single 'battle' event during the game."""
    def __init__(self):
        Rect.__init__(self)
        self.zone = None

    def draw(self, surface):
        pass


class Target(Rect):
    """This class represents a single 'target' in the game world, which is any
    non-terrain and non-enemy object that the player can interact with."""
    def __init__(self):
        Rect.__init__(self)
        self.zone = None

    def draw(self, surface):
        pass


class Terrain(Rect):
    """This class represents an arbitrary amount of 'terrain', which is all of the
    non-interactive parts of the world. Most importantly, terrain provides layout
    and collision data.

    A single ``Terrain`` instance can represent as little as a single tile or as
    much as an entire level. The main practical concern is that each ``Terrain``
    instance is treated as an indivisible unit by the engine.

    Future engine features and optimizations might dictate the optimal 'size' of each
    ``Terrain`` instance, but for now it's a design convenience so that world data can
    be organized in arbitrary ways."""
    def __init__(self):
        Rect.__init__(self)
        self.zone = None
        self.static = True
        self.images = []

    def add_image(self, image_surface):
        self.union(Rect(*image_surface.get_rect()))
        self.images.append(image_surface)

    @property
    def rect(self):
        return self

    def draw(self, surface):
        for i in self.images:
            surface.blit(i, self)