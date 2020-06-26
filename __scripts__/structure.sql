SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema thedb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `thedb` DEFAULT CHARACTER SET utf8 ;
USE `thedb` ;

-- -----------------------------------------------------
-- Table `thedb`.`ReferencePeriode`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `thedb`.`ReferencePeriod` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `in_date` DATE NOT NULL,
  `until_date` DATE NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `thedb`.`DataType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `thedb`.`DataType` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `datatype` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `thedb`.`Information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `thedb`.`Information` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `shortname` VARCHAR(100) NOT NULL,
  `nickname` VARCHAR(15) NOT NULL,
  `longName` VARCHAR(256) NOT NULL,
  `definition` TEXT(2048) NOT NULL,
  `id_datatype` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `id_datatype`),
  INDEX `fk_information_datatype_idx` (`id_datatype` ASC),
  CONSTRAINT `fk_information_datatype`
    FOREIGN KEY (`id_datatype`)
    REFERENCES `thedb`.`DataType` (`id`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `thedb`.`Granularity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `thedb`.`Granularity` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `granularity` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `thedb`.`Location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `thedb`.`Location`;
CREATE TABLE `Location` (
  `id_ibge` INT UNSIGNED NOT NULL DEFAULT '0',
  `id_ibge_memberof` INT UNSIGNED NOT NULL DEFAULT '0',
  `name` VARCHAR(45) NOT NULL DEFAULT '',
  `nickname` VARCHAR(10) NOT NULL DEFAULT '',
  `location_type` VARCHAR(45) NOT NULL DEFAULT '',
  `geo_latitude` DOUBLE NOT NULL DEFAULT '0',
  `geo_longitude` DOUBLE NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_ibge`)
) ENGINE=InnoDB;

-- -----------------------------------------------------
-- Table `thedb`.`Data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `thedb`.`Data` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `data` FLOAT NOT NULL,
  `id_information` INT UNSIGNED NOT NULL,
  `id_information_datatype` INT UNSIGNED NOT NULL,
  `id_reference_period` INT UNSIGNED NOT NULL,
  `id_location` INT UNSIGNED NOT NULL DEFAULT '0',
  `id_granularity` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `id_information`, `id_information_datatype`, `id_reference_period`, `id_location`, `id_granularity`),
  INDEX `fk_data_information_idx` (`id_information` ASC, `id_information_datatype` ASC),
  INDEX `fk_data_reference_period_idx` (`id_reference_period` ASC),
  INDEX `fk_data_location_idx` (`id_location` ASC),
  INDEX `fk_data_granularity_idx` (`id_granularity` ASC),
  CONSTRAINT `fk_data_information`
    FOREIGN KEY (`id_information`, `id_information_datatype`)
    REFERENCES `thedb`.`Information` (`id`, `id_datatype`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_data_reference_period`
    FOREIGN KEY (`id_reference_period`)
    REFERENCES `thedb`.`ReferencePeriod` (`id`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_data_location`
    FOREIGN KEY (`id_location`)
    REFERENCES `thedb`.`Location` (`id_ibge`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `fk_data_granularity`
    FOREIGN KEY (`id_granularity`)
    REFERENCES `thedb`.`Granularity` (`id`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE
) ENGINE = InnoDB;
