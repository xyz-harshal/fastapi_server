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


