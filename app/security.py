from typing import ByteString

import bcrypt


async def password_hash(password: str) -> ByteString:
    return bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt())
