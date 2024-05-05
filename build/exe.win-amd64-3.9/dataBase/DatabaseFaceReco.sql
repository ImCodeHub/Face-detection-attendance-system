/*
SQLyog Community v13.1.3  (32 bit)
MySQL - 8.0.28 : Database - testdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`testdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `testdb`;

/*Table structure for table `facerecognition` */

DROP TABLE IF EXISTS `facerecognition`;

CREATE TABLE `facerecognition` (
  `Department` varchar(255) DEFAULT NULL,
  `Course` varchar(255) DEFAULT NULL,
  `Year` varchar(20) DEFAULT NULL,
  `Semester` varchar(20) DEFAULT NULL,
  `StudentID` varchar(255) DEFAULT NULL,
  `StudentName` varchar(255) DEFAULT NULL,
  `Class` varchar(255) DEFAULT NULL,
  `RollNo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Gender` varchar(255) DEFAULT NULL,
  `DOB` varchar(255) DEFAULT NULL,
  `EmailID` varchar(255) DEFAULT NULL,
  `MobileNO` varchar(15) NOT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Teachar` varchar(255) DEFAULT NULL,
  `PhotoSample` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`RollNo`,`MobileNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `facerecognition` */

insert  into `facerecognition`(`Department`,`Course`,`Year`,`Semester`,`StudentID`,`StudentName`,`Class`,`RollNo`,`Gender`,`DOB`,`EmailID`,`MobileNO`,`Address`,`Teachar`,`PhotoSample`) values 
('Computer','MCA','2022-23','4th sem','1','Ankit sharma','A','0724CA201007','Male','24/11/1993','shaolin.ankit@gmail.com','8962780856','mandsaur','c.k. panday','Yes');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
