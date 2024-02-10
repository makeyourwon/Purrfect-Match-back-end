CREATE DATABASE purrfect_match;

CREATE USER purr_admin WITH PASSWORD 'purrfect';

GRANT ALL PRIVILEGES ON DATABASE purrfect_match TO purr_admin;

ALTER DATABASE purrfect_match OWNER TO purr_admin;