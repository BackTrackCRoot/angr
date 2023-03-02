from typing import TYPE_CHECKING, Optional, Set, Union

from angr.analyses.analysis import AnalysesHub
from angr.knowledge_plugins.key_definitions import LiveDefinitions

from .reaching_definitions import ReachingDefinitionsAnalysis

if TYPE_CHECKING:
    from angr.knowledge_plugins.key_definitions.definition import Definition
    from angr.storage.memory_mixins import MultiValuedMemory
    from angr.storage.memory_mixins.paged_memory.pages import MVListPage
    from angr.storage.memory_object import SimMemoryObject


def get_all_definitions(region: "MultiValuedMemory") -> Set["Definition"]:
    all_defs: Set["Definition"] = set()

    # MultiValuedMemory only uses ListPage internally
    for page in region._pages.values():
        page: "MVListPage"

        for idx in page.stored_offset:
            cnt_set: Optional[Union["SimMemoryObject", Set["SimMemoryObject"]]] = page.content[idx]
            if cnt_set is None:
                continue
            elif type(cnt_set) is not set:
                cnt_set = {cnt_set}
            for cnt in cnt_set:
                for def_ in LiveDefinitions.extract_defs(cnt.object):
                    all_defs.add(def_)

    return all_defs


AnalysesHub.register_default("ReachingDefinitions", ReachingDefinitionsAnalysis)
