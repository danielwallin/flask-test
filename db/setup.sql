CREATE USER dbuser;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT INSERT, UPDATE, DELETE, SELECT ON TABLES
TO dbuser, postgres;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT EXECUTE ON FUNCTIONS
TO dbuser, postgres;

CREATE TABLE todos (
    id SERIAL PRIMARY KEY,    
    title VARCHAR NOT NULL,
    completed BOOLEAN,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO todos(title, completed) VALUES ('Title 1', FALSE);
INSERT INTO todos(title, completed) VALUES ('Title 2', FALSE);
INSERT INTO todos(title, completed) VALUES ('Title 3', TRUE);
INSERT INTO todos(title, completed) VALUES ('Title 4', FALSE);