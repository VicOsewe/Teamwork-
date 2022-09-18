"""interfaces"""
from abc import abstractmethod
from typing import Generic, List, TypeVar

# Type definition for Model
M = TypeVar("M")

# Type definition for Unique Id
K = TypeVar("K")


class RepositoryMeta(Generic[M, K]):
    """Abstract class for Repository"""
    @abstractmethod
    def create(self, instance: M) -> M:
        """create a new instance of the Model"""
        pass # pylint: disable=unnecessary-pass

    @abstractmethod
    def delete(self, id: K) -> None: # pylint: disable=invalid-name,redefined-builtin
        """delete an instance of the Model"""
        pass # pylint: disable=unnecessary-pass

    @abstractmethod
    def get(self, id: K) -> M: # pylint: disable=invalid-name,redefined-builtin
        """Fetch an existing instance of the Model by it's unique Id"""
        pass # pylint: disable=unnecessary-pass

    @abstractmethod
    def list(self, limit: int, start: int) -> List[M]:
        """Lists all existing instance of the Model"""
        pass # pylint: disable=unnecessary-pass

    @abstractmethod
    def update(self, id: K, instance: M) -> M: # pylint: disable=invalid-name,redefined-builtin
        """Updates an existing instance of the Model"""
        pass # pylint: disable=unnecessary-pass
