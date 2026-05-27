from typing import Any, Dict, List
from charm.core.storage import BaseMemoryStore
from charm.core.logger import logger

class HelloWorldMemoryStore(BaseMemoryStore):
    """
    A template for building custom Memory & State providers for Charm.
    
    This example uses an in-memory dictionary.
    Replace it with your actual database client (Redis, MongoDB, Pinecone, etc.).
    """
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.connection_string = config.get("url", "default_connection_string")
        self._mock_db: Dict[str, List[Dict[str, Any]]] = {}
        logger.info(f"HelloWorldMemoryStore initialized with config: {config}")

    def load_messages(self, thread_id: str) -> List[Dict[str, Any]]:
        """Load message history for a specific thread."""
        return self._mock_db.get(thread_id, [])

    def save_messages(self, thread_id: str, messages: List[Dict[str, Any]]) -> None:
        """Save message history for a specific thread."""
        self._mock_db[thread_id] = messages
        logger.debug(f"Saved {len(messages)} messages for thread {thread_id}")

    def get_langgraph_checkpointer(self) -> Any:
        """
        Return a LangGraph checkpointer instance if you want to support
        stateful workflow graphs. Return None if not supported.
        """
        return None
