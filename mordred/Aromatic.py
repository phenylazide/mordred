from ._base import Descriptor

__all__ = (
    'AromaticAtomsCount', 'AromaticBondsCount',
)


class AromaticBase(Descriptor):
    __slots__ = ()

    @classmethod
    def preset(cls):
        yield cls()

    def __str__(self):
        return self._name

    def parameters(self):
        return ()

    rtype = int


class AromaticAtomsCount(AromaticBase):
    r"""aromatic atoms count descriptor."""
    __slots__ = ()
    _name = 'nAromAtom'

    def calculate(self):
        return sum(
            1
            for a in self.mol.GetAtoms()
            if a.GetIsAromatic()
        )


class AromaticBondsCount(AromaticBase):
    r"""aromatic bonds count descriptor."""
    __slots__ = ()
    _name = 'nAromBond'

    def calculate(self):
        return sum(
            1
            for b in self.mol.GetBonds()
            if b.GetIsAromatic()
        )
