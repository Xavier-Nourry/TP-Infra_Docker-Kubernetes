CREATE DATABASE TP1_INFRA;
USE TP1_INFRA;

CREATE TABLE Activities (
    id INT NOT NULL AUTO_INCREMENT,
    description VARCHAR(250) NOT NULL,
    nbOccurrences INT NOT NULL,
    PRIMARY KEY (id)
    );