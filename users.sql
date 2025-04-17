CREATE SCHEMA `infs3070v2` ;

CREATE TABLE `infs3070v2`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `comments` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

INSERT INTO infs3070v2.users (name, email, comments) VALUES ('Bob', 'rcook2@uccs.edu', 'Blah Blah Blah'); 
INSERT INTO infs3070v2.users (name, email, comments) VALUES ('Mary', 'mp@uccs.edu', 'Blah Blah Blah'); 
INSERT INTO infs3070v2.users (name, email, comments) VALUES ('Jacob Jingleheimer', 'jj@uccs.edu', 'Blah Blah Blah'); 