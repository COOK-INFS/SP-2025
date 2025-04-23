CREATE SCHEMA `infs3070` ;

CREATE TABLE `infs3070`.`rcook2` (
  `studentid` INT NOT NULL AUTO_INCREMENT,
  `lastName` VARCHAR(45) NULL,
  `firstName` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`studentid`));

INSERT INTO `infs3070`.`rcook2` (lastName, firstName, email) VALUES ('Cook', 'Bob', 'rcook2@uccs.edu');
INSERT INTO `infs3070`.`rcook2` (lastName, firstName, email) VALUES ('Jingleheimer', 'Jacob', 'jj@email.com');