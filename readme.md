 File "/home/harshal/code/socials/server/main.py", line 7, in <module>
    from routes import userRoute
  File "/home/harshal/code/socials/server/routes/userRoute.py", line 6, in <module>
    schema.base.metadata.create_all(bind=engine)
AttributeError: module 'schema' has no attribute 'base'

Base: <class 'sqlalchemy.orm.decl_api.Base'>
UserSchema: <class 'schema.userSchema.userSchema'>
DB: <sqlalchemy.orm.session.Session object at 0x75f223743d90>
Request: email='hakk@gmail.com' password='1234'
INFO:     127.0.0.1:33614 - "POST /login HTTP/1.1" 200 OK

File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/sqlalchemy/sql/schema.py", line 464, in _new
    raise exc.InvalidRequestError(
sqlalchemy.exc.InvalidRequestError: Table 'students' is already defined for this MetaData instance.  Specify 'extend_existing
=True' to redefine options and columns on an existing Table object.

  File "/home/harshal/code/socials/server/main.py", line 9, in <module>
    jwt_decode(encoded_data)
  File "/home/harshal/code/socials/server/auth.py", line 21, in jwt_decode
    payload=jwt.decode(token,SECRET_KEY,algorithm=[ALGORITHM])
TypeError: decode() got an unexpected keyword argument 'algorithm'

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXJzaGFsX2lzX2FuX2Fzc2hvbGUifQ.C9vREjvFR4lO5L1whsweZgSM1Q3j2yKWTSK2lLtx_YM

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXJzaGFsX2lzX2dvb2RfYm95In0.vnggYNiD9KpOA0oMbxyEJKeRGXCMekXDnrMPLCgQsAVwwg3J8
psmdFD8QBSmroqSs7tqe11HEVGwgvasJu-msl0Imzgl2KYOfIUbNLvq0b6spp0Hsh3Y4S1G2RD104slDf68w8J1noeqvoPu51NVoURnrrBu5bGUAv17Xj4VmIWA71q
cN4CX75wSt2xZhO7HHKYg0uWJhnxCXVw7xlSfPD878NfZjK9A3wxnC4s2kFnlo4GhF2qD_IgHne49GuHI5pSfPozMBFnXWeU-nPSDvIAbFpaNTIFePvFJTHFIQCnOZ
zHo0KPEUqMiTdT-i2SnpXAc7wb-Vz6XP9qzGBL0OA


sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "peoples" does not exist
LINE 2: FROM peoples 
             ^

[SQL: SELECT peoples.id AS peoples_id, peoples.email AS peoples_email, peoples.password AS peoples_password 
FROM peoples 
WHERE peoples.email = %(email_1)s 
 LIMIT %(param_1)s]
[parameters: {'email_1': 'moneoeo@gmail.com', 'param_1': 1}]
(Background on this error at: https://sqlalche.me/e/20/f405)


(trapped) error reading bcrypt version
Traceback (most recent call last):
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/passlib/handlers/bcrypt.py", line 620, in _load_bac
kend_mixin
    version = _bcrypt.__about__.__version__
AttributeError: module 'bcrypt' has no attribute '__about__'
INFO:     127.0.0.1:46292 - "POST /register HTTP/1.1" 200 OK


INFO:     127.0.0.1:47106 - "POST /login HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 399
, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 70, in _
_call__
    return await self.app(scope, receive, send)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/applications.py", line 123, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/middleware/errors.py", line 186, in __cal
l__
    raise exc
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/middleware/errors.py", line 164, in __cal
l__
    await self.app(scope, receive, _send)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/middleware/exceptions.py", line 65, in __
call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/_exception_handler.py", line 64, in wrapp
ed_app
    raise exc
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/_exception_handler.py", line 53, in wrapp
ed_app
    await app(scope, receive, sender)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/routing.py", line 776, in app
    await route.handle(scope, receive, send)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/routing.py", line 297, in handle
    await self.app(scope, receive, send)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/routing.py", line 77, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/_exception_handler.py", line 64, in wrapp
ed_app
    raise exc
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/_exception_handler.py", line 53, in wrapp
ed_app
    await app(scope, receive, sender)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/starlette/routing.py", line 72, in app
    response = await func(request)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/fastapi/routing.py", line 278, in app
    raw_response = await run_endpoint_function(
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/fastapi/routing.py", line 191, in run_endpoint_func
tion
    return await dependant.call(**values)
  File "/home/harshal/code/socials/server/routes/userRoute.py", line 16, in login
    token=jwt_encode(findUser.id)
  File "/home/harshal/code/socials/server/auth.py", line 16, in jwt_encode
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/jose/jwt.py", line 53, in encode
    return jws.sign(claims, key, headers=headers, algorithm=algorithm)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/jose/jws.py", line 42, in sign
    encoded_payload = _encode_payload(payload)
  File "/home/harshal/code/socials/server/env/lib/python3.10/site-packages/jose/jws.py", line 146, in _encode_payload
    payload = json.dumps(
  File "/usr/lib/python3.10/json/__init__.py", line 238, in dumps
    **kw).encode(obj)
  File "/usr/lib/python3.10/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/lib/python3.10/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/usr/lib/python3.10/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type UUID is not JSON serializable

