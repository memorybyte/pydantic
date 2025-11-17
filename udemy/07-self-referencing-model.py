from typing import List, Dict, Optional, Literal
from pydantic import BaseModel, Field, model_validator, field_validator

# When we use self referencing, we have to use model_rebuild()

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None # Self referencing

Comment.model_rebuild()

comment = Comment(
    id=1,
    content='First content',
    replies=[
        Comment(id=2, content='reply 1'),
        Comment(id=3, content='reply 2', replies=[
            Comment(id=4, content='reply 4')
        ])
    ]
)