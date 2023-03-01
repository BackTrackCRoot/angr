from angr.storage.memory_mixins import MemoryMixin


class RegionCategoryMixin(MemoryMixin):
    @property
    def category(self):
        return "mem"
