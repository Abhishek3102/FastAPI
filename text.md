Yes, you can enforce the maximum number of allergies in a single line using `Field` with the `max_items` constraint. Here's the updated version of your code using **`Field(..., max_items=5)`**:

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr
    age: int = Field(gt=0, lt=120)
    github_url: AnyUrl
    weight: float = Field(gt=0)
    marital_status: bool = True
    allergies: Optional[List[str]] = Field(default=None, max_items=5)
    contact_details: Dict[str, str]
```

### ✅ What this does:

- `max_items=5` enforces that at most 5 items are allowed in the list.
- `default=None` keeps it optional with `None` as the default.

Let me know if you want to also set `min_items` or apply further constraints.
