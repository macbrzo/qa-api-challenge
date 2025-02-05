from typing import Optional

from pydantic import BaseModel


class RandomFactResponse(BaseModel):
    fact: str
    length: int

    def verify_fact_length(self, expected_length: Optional[int] = None):
        if not expected_length:
            expected_length = self.length
        assert (
            len(self.fact) == expected_length
        ), f"Length of {self.fact=} doesn't match value of 'length' field value {expected_length=}"
