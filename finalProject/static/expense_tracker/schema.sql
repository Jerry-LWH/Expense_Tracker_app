-- MySQL dump 10.13  Distrib 8.0.12, for Linux (x86_64)
--
-- Host: localhost    Database: finalProject
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add user profile info',6,'add_userprofileinfo'),(22,'Can change user profile info',6,'change_userprofileinfo'),(23,'Can delete user profile info',6,'delete_userprofileinfo'),(24,'Can view user profile info',6,'view_userprofileinfo'),(25,'Can add session',7,'add_session'),(26,'Can change session',7,'change_session'),(27,'Can delete session',7,'delete_session'),(28,'Can view session',7,'view_session'),(29,'Can add transactions',8,'add_transactions'),(30,'Can change transactions',8,'change_transactions'),(31,'Can delete transactions',8,'delete_transactions'),(32,'Can view transactions',8,'view_transactions');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$PFOlw10MlU1G$Mo3kdLbqv1vKrtYtuuU42a7tNwkqnMuqzNMk8OXBnXs=','2018-12-11 01:35:50.469419',1,'administrator','','','wl87617@uga.edu',1,1,'2018-12-05 02:03:29.047876'),(21,'pbkdf2_sha256$120000$uSjPCaf4UGqX$LH1mhKbJ/UYTtEJM/GAsy1IH9vJ2DQxWJ7mRt+btRfU=','2018-12-11 04:17:53.087357',0,'Sleepy_Insomniac','Hayley','Nguyen','myhanh.nguyen2015@gmail.com',0,1,'2018-12-07 02:10:05.665878'),(36,'pbkdf2_sha256$120000$ir2hhKXZQgc5$i34Wenh854JRiS32qbkOAxQ3734OF/O8m7rqyR4Z8NA=','2018-12-11 03:33:36.839978',0,'1111','Wenhao','Lin','jerry.1224@yahoo.com',0,1,'2018-12-11 01:36:22.411211');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (9,'2018-12-05 15:12:32.138978','10','admin',3,'',4,1),(10,'2018-12-05 15:12:32.157339','11','adminaasasas',3,'',4,1),(11,'2018-12-05 15:12:32.170809','12','sssaa',3,'',4,1),(12,'2018-12-05 15:25:33.149113','13','admin',3,'',4,1),(13,'2018-12-05 15:25:33.180554','14','admindsd',3,'',4,1),(14,'2018-12-07 02:09:46.972847','20','AnthonyNguyen',3,'',4,1),(15,'2018-12-07 02:09:47.031955','19','Sleepy_Insomniac',3,'',4,1),(16,'2018-12-07 03:57:57.159159','17','111222',3,'',4,1),(17,'2018-12-07 03:57:57.181003','18','1234',3,'',4,1),(18,'2018-12-07 03:57:57.193205','16','adminsss',3,'',4,1),(19,'2018-12-07 03:57:57.202416','15','wwww',3,'',4,1),(20,'2018-12-07 16:58:30.121595','24','1111',3,'',4,1),(21,'2018-12-07 16:58:30.141657','22','1234',3,'',4,1),(22,'2018-12-07 16:58:30.149446','23','kjkjkjk',3,'',4,1),(23,'2018-12-10 03:23:33.988289','27','0000',3,'',4,1),(24,'2018-12-10 03:23:34.011888','25','1111111s',3,'',4,1),(25,'2018-12-10 03:23:34.020357','26','1234',3,'',4,1),(26,'2018-12-10 11:40:55.473840','31','0000',3,'',4,1),(27,'2018-12-10 11:40:55.533469','30','1234',3,'',4,1),(28,'2018-12-10 11:40:55.543011','29','2222',3,'',4,1),(29,'2018-12-10 11:40:55.555259','28','3366',3,'',4,1),(30,'2018-12-11 01:36:08.447042','32','0000',3,'',4,1),(31,'2018-12-11 01:36:08.521991','33','1234',3,'',4,1),(32,'2018-12-11 01:36:08.530301','34','9999',3,'',4,1),(33,'2018-12-11 01:36:08.540205','35','qqqq',3,'',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'expense_tracker','transactions'),(6,'expense_tracker','userprofileinfo'),(7,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-12-05 01:59:24.997371'),(2,'auth','0001_initial','2018-12-05 01:59:26.562916'),(3,'admin','0001_initial','2018-12-05 01:59:26.953846'),(4,'admin','0002_logentry_remove_auto_add','2018-12-05 01:59:26.981586'),(5,'admin','0003_logentry_add_action_flag_choices','2018-12-05 01:59:27.010599'),(6,'contenttypes','0002_remove_content_type_name','2018-12-05 01:59:27.324196'),(7,'auth','0002_alter_permission_name_max_length','2018-12-05 01:59:27.490525'),(8,'auth','0003_alter_user_email_max_length','2018-12-05 01:59:27.575172'),(9,'auth','0004_alter_user_username_opts','2018-12-05 01:59:27.600964'),(10,'auth','0005_alter_user_last_login_null','2018-12-05 01:59:27.760445'),(11,'auth','0006_require_contenttypes_0002','2018-12-05 01:59:27.771841'),(12,'auth','0007_alter_validators_add_error_messages','2018-12-05 01:59:27.795478'),(13,'auth','0008_alter_user_username_max_length','2018-12-05 01:59:27.969381'),(14,'auth','0009_alter_user_last_name_max_length','2018-12-05 01:59:28.164481'),(20,'sessions','0001_initial','2018-12-05 14:07:09.949604');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('islujhzvqznildmotgrotbthy26cp0mj','NDI4ODNlNjNiZTU2NDJjYmFlMzlkYTY5M2Q0ZjgwMWNhNzUwMzVlNTp7Il9hdXRoX3VzZXJfaWQiOiIzNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWNiNjYwODExMDJkZDVmOTY4YTA0MWI2ODNhNDU2OTM3OTZkNjZhYSJ9','2018-12-25 03:33:36.856151'),('pl6jf9t9qn7gj931bh9nvlr9qj2ncbgz','MDRmMTBlYTczNDJmM2UwYTJlNDk2ZWQ5ZDc0OWEyNjQ3OWJhZDA0ODp7Il9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTVjYmQxYWY5ZWYyZjZkNDFjMDVhYTZhZWQwMDg4MzI1ZTM5NTViZSJ9','2018-12-25 03:49:25.535079'),('wgm5z2il1loierg81yr6150fkclz992g','MDRmMTBlYTczNDJmM2UwYTJlNDk2ZWQ5ZDc0OWEyNjQ3OWJhZDA0ODp7Il9hdXRoX3VzZXJfaWQiOiIyMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTVjYmQxYWY5ZWYyZjZkNDFjMDVhYTZhZWQwMDg4MzI1ZTM5NTViZSJ9','2018-12-25 04:17:53.109293'),('xnx87ooj5yojfeqq01t5gt43pk9j1f1d','NzEzYTExOGU3NjFkNTI2ZTgwMzkyYmYzMmRmYTVjZjY3NTJmZGRmMzp7Il9wYXNzd29yZF9yZXNldF90b2tlbiI6IjUxdy1kZGY0MDU2M2RmNGVjYmE1ZmY3NiJ9','2018-12-20 16:44:16.714338');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expense_tracker_envelop`
--

DROP TABLE IF EXISTS `expense_tracker_envelop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `expense_tracker_envelop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_day` int(11) NOT NULL,
  `category` varchar(200) NOT NULL,
  `amounts` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expense_tracker_envelop`
--

LOCK TABLES `expense_tracker_envelop` WRITE;
/*!40000 ALTER TABLE `expense_tracker_envelop` DISABLE KEYS */;
INSERT INTO `expense_tracker_envelop` VALUES (93,1,'gas',0,36),(94,1,'grocery',0,36),(95,1,'dinning',0,36),(96,1,'housing_utility',0,36),(97,1,'health_care',0,36),(98,1,'entertainment',0,36),(99,1,'other',0,36);
/*!40000 ALTER TABLE `expense_tracker_envelop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expense_tracker_transactions`
--

DROP TABLE IF EXISTS `expense_tracker_transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `expense_tracker_transactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `category` varchar(200) NOT NULL,
  `payee` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `amounts` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expense_tracker_transactions`
--

LOCK TABLES `expense_tracker_transactions` WRITE;
/*!40000 ALTER TABLE `expense_tracker_transactions` DISABLE KEYS */;
INSERT INTO `expense_tracker_transactions` VALUES (45,'2018-12-21','gas','Jerry','',200,36),(47,'2018-12-06','gas','Wenhao Lin','',1000,36);
/*!40000 ALTER TABLE `expense_tracker_transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expense_tracker_userprofileinfo`
--

DROP TABLE IF EXISTS `expense_tracker_userprofileinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `expense_tracker_userprofileinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `portfolio_site` varchar(200) NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `activation_key` varchar(40) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `expense_tracker_userprofileinfo_user_id_342b99a2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expense_tracker_userprofileinfo`
--

LOCK TABLES `expense_tracker_userprofileinfo` WRITE;
/*!40000 ALTER TABLE `expense_tracker_userprofileinfo` DISABLE KEYS */;
INSERT INTO `expense_tracker_userprofileinfo` VALUES (12,'','',21,''),(26,'','',36,'0');
/*!40000 ALTER TABLE `expense_tracker_userprofileinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-11  0:25:34
