# jwt_fastapi




### **1️⃣ `main.py`**

* Entry point of the FastAPI app.
* Imports routers (`routes/auth.py`) and registers them.
* Starts the FastAPI server.
* Depends on `db.py` for DB session and `config.py` for settings.

**Flow:**
`Request → router → endpoint function → utils/db → response`

---

### **2️⃣ `routes/auth.py`**

* **Contains:** `/register` and `/login` endpoints.
* **Uses:**

  * `schemas.py` → validates input (UserCreate, UserLogin) and output (TokenResponse).
  * `utils/password.py` → hashes & verifies passwords.
  * `utils/auth.py` → generates JWT tokens.
  * `db.py` → gets DB session (`Session`).
  * `models.py` → interacts with `User` & `Token` tables.

**Flow:**
`POST /auth/register → validate via schemas → hash password → store in DB → return msg`
`POST /auth/login → validate via schemas → verify password → create JWT → return tokens`

---

### **3️⃣ `models.py`**

* **Contains:** SQLAlchemy table definitions (`User` and `Token`).
* **Used by:** `routes/auth.py`, `utils/auth.py` (optional, if storing tokens).
* **Purpose:** Defines DB structure.

---

### **4️⃣ `schemas.py`**

* **Contains:** Pydantic models: `UserCreate`, `UserLogin`, `TokenResponse`.
* **Used by:** `routes/auth.py` to enforce **input/output formats**.
* **Purpose:** Ensures **API request and response follow correct structure**.

---

### **5️⃣ `db.py`**

* **Contains:** DB engine, sessionmaker, Base.
* **Provides:** `get_db()` dependency for endpoints.
* **Used by:** `routes/auth.py`, anywhere DB access is needed.
* **Purpose:** Centralizes DB connection.

---

### **6️⃣ `config.py`**

* **Contains:** `Settings` class (database + JWT configs).
* **Used by:** `db.py`, `utils/auth.py` (for secrets, expiry, algorithm), and `main.py`.
* **Purpose:** Central config for DB and JWT.

---

### **7️⃣ `utils/password.py`**

* **Contains:** `secure_pwd()` → hash password, `verify_pwd()` → check password.
* **Used by:** `routes/auth.py`.
* **Purpose:** Encapsulates password handling.

---

### **8️⃣ `utils/auth.py`**

* **Contains:** JWT functions: `create_access_token`, `create_refresh_token`, `decodeJWT`, `JWTBearer`.
* **Used by:** `routes/auth.py` (create JWT) and **protected routes** via `JWTBearer`.
* **Purpose:** Central JWT handling, reusable anywhere.

---

### **Visual Flow: Request → DB → Response**

```
Client
  |
  v
POST /auth/register or /login
  |
  v
routes/auth.py (endpoint function)
  |---> schemas.py validates input
  |---> utils/password.py hashes/verifies password
  |---> db.py provides DB session
  |---> models.py interacts with DB tables
  |---> utils/auth.py generates JWT tokens
  |
  v
Database (Postgres)
  |
  v
Return response to Client (schemas.py ensures output format)
```

---

✅ **Key Notes for Reusability**

* `utils/auth.py` + `utils/password.py` are **standalone** → can copy to any project.
* `schemas.py` ensures all endpoints use a standard request/response format.
* `db.py` + `models.py` can be reused but may require changes per DB schema.

---


