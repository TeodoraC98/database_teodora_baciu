from sqlalchemy import create_engine
import os
# postgresql://project_teodora:54qKvCbQ2mBy5UKIQeSXL8X775agHdBl@dpg-d0tcsh6mcj7s73dfdm7g-a.oregon-postgres.render.com/database_project_teodora
class Conf:
   SECRET_KEY =os.getenv('SECRET_KEY','non-set')
   SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL','postgresql://postgres:postgres@127.0.0.1:5432/projectDatabase')
   # SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL','postgresql://project_teodora:54qKvCbQ2mBy5UKIQeSXL8X775agHdBl@dpg-d0tcsh6mcj7s73dfdm7g-a.oregon-postgres.render.com/database_project_teodora')