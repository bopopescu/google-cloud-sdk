@echo off
rem Copyright 2011 Google Inc. All Rights Reserved.

rem Google Cloud SQL command line tool.
rem Example:
rem   %0 <instance> [database]

java -Dhttp.agent="Cloud SDK Command Line Tool" -jar "%~dp0\..\lib\impl\google_sql.jar" %*
