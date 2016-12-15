DROP TABLE IF EXISTS presentations;
DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    name        VARCHAR(255) NOT NULL UNIQUE,
    profileUrl  VARCHAR(255) NOT NULL,
    PRIMARY KEY (name)
);

CREATE TABLE presentations
(
    id          VARCHAR(24) NOT NULL UNIQUE,
    title       VARCHAR(255) NOT NULL,
    thumbnail   VARCHAR(255),
    creator     VARCHAR(255) NOT NULL,
    createdAt   DATE NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT crtr FOREIGN KEY (creator) REFERENCES users(name)
    ON DELETE CASCADE
);