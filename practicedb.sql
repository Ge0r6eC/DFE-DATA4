-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: practicedb
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `basketball`
--

DROP TABLE IF EXISTS `basketball`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `basketball` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Team_Name` varchar(100) NOT NULL,
  `Franchise_Name` varchar(100) NOT NULL,
  `Venue` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `Region` varchar(100) NOT NULL,
  `Conference` enum('East','West') DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basketball`
--

LOCK TABLES `basketball` WRITE;
/*!40000 ALTER TABLE `basketball` DISABLE KEYS */;
INSERT INTO `basketball` VALUES (1,'Los Angeles Clippers','Clippers','Staples Centre','Los Angeles','California','West'),(2,'Golden State Warriors','Golden State','Chase Centre','San Francisco','California','West'),(3,'Atlanta Hawks','Hawks','State Farm Arena','Atlanta','Georgia','East'),(4,'Portland Trailblazers','Trailblazers','Moda Center','Portland','Oregon','West'),(5,'New York Knicks','Knicks','Madison Square Gardens','Manhattan','New York','East'),(6,'Brooklyn Nets','Nets','Barclays Center','Brooklyn','New York','East');
/*!40000 ALTER TABLE `basketball` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_stats`
--

DROP TABLE IF EXISTS `player_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_stats` (
  `PlayerID` int NOT NULL,
  `Height` int NOT NULL,
  `Age` int NOT NULL,
  `ShoeSize` int NOT NULL,
  `Weight` int DEFAULT NULL,
  PRIMARY KEY (`PlayerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_stats`
--

LOCK TABLES `player_stats` WRITE;
/*!40000 ALTER TABLE `player_stats` DISABLE KEYS */;
INSERT INTO `player_stats` VALUES (1,203,31,16,115),(2,197,29,14,120),(3,217,33,18,169),(4,205,32,16,107),(5,198,30,18,113),(6,198,32,15,142),(7,202,29,14,97),(8,189,26,15,142),(9,197,35,16,111),(10,220,31,14,157);
/*!40000 ALTER TABLE `player_stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `PlayerID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(100) DEFAULT NULL,
  `LastName` varchar(100) DEFAULT NULL,
  `TeamID` int NOT NULL,
  PRIMARY KEY (`PlayerID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,'Paul','George',1),(2,'Damian','Lillard',4),(3,'Kevin','Durant',6),(4,'James','Harden',6),(5,'Kyrie','Irving',6),(6,'Steph','Curry',2),(7,'Klay','Thompson',2),(8,'Trae','Young',3),(9,'Derrick','Rose',5),(10,'Kemba','Walker',5);
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-10 16:54:21
