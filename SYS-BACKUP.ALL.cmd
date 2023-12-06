@ECHO OFF
:: *************************************************************************************************************:
:: ***************************************** COPY JEB DIRECTORY SCRIPT *****************************************:
:: *************************************************************************************************************:
:: Author:  JBallard (JEB)                                                                                      :
:: Date:    2019.11.26                                                                                          :
:: Dir:     \\JBALLARD-9520\C$\0_SVN\2_DEV\0_SCRIPTS.Src\0_USEFUL.Dev\1_BACKUP.Dev                              :
:: Script:  SYS-BACKUP.ALL.cmd                                                                                  :
:: Purpose: A batch script that backs up important directories to a USB drive.                                  :
:: Version: 1.0                                                                                                 :
:: *************************************************************************************************************:
:: ******************************************** ROBOCOPY SWITCHES **********************************************:
:: *************************************************************************************************************:
:: /S:      The /S switch is used to copy all NON-EMPTY subdirectories                                          :
:: /E:      The /S switch Copies only the subdirectories including emtyp directories                            :
:: /XO:     The /XO switch excludes older files from being copied to the destination directory                  :
:: /MIR:    The /MIR switch will purge files on the destination directory if not found on the source            :
:: /NP:     The /NP switch will not display the percentage of copied filesets (No Progress)                     :
:: /ZB:     The /ZB switch uses Restartable Mode but switches to Backup Mode if permission problems are found   :
:: /B:      The /B switch overrides file & folder permission settings (ACLs)                                    :
:: /LEV<n>: The /LEV<n> switch Copies only the top <n> levels of the source directory tree                      :
:: /J:      The /J switch Copies using unbuffered I/O which is recommended for Large files                      :
:: /MT:     The /MT switch is used to specify the number of threads used by the ROBOCOPY Process                :
:: *************************************************************************************************************:
:: *************************************************************************************************************:
::
:: *************************************************:
:: DEFINE PARAMS, CONFIG PATHS, IMPORT CLASSES      :
:: *************************************************:
SET ARGs=/COPY:DATSO /S /ZB
SET SRCSVNDirD="\\JBALLARD-9520\C$\0_SVN"
SET DSTSVNDirD="\\JBALLARD-9520\D$\0_REPO\0_SVN"
SET SRCJBRDirD="\\JBALLARD-9520\C$\Users\jballard\Documents\MyJabberFiles"
SET DSTJBRDirD="\\JBALLARD-9520\D$\0_REPO\0_SVN\15_JABBER"
SET SRCLog="\\JBALLARD-9520\C$\0_SVN\7_LOGS\BACKUP\CMD-9520-BACKUP.LOG.jeb"
::
ECHO -----------------------------------------------:
ECHO - EXECUTING JBALLARD-9520 BACKUP PROCESSES     :
ECHO -----------------------------------------------:
::
ECHO -----------------------------------------------:
ECHO - 0 - 0_SVN TO D:\0_REPO\0_SVN                 :
ECHO -----------------------------------------------:
ROBOCOPY %SRCSVNDirD% %DSTSVNDirD% %ARGs% >> %SRCLog%
TIMEOUT 1 /NOBREAK
::
ECHO -----------------------------------------------:
ECHO - 1 - 1_JABBER TO D:\0_REPO\1_JABBER           :
ECHO -----------------------------------------------:
ROBOCOPY %SRCJBRDirD% %DSTJBRDirD% %ARGs% >> %SRCLog%
TIMEOUT 1 /NOBREAK
::
ECHO -----------------------------------------------:
ECHO - JBALLARD-9520 BACKUPS SUCCESSFULLY PROCESSED: >> %SRCLog%
ECHO -----------------------------------------------:
::
PAUSE
:: *************************************************:
:: END OF SCRIPT									:
:: *************************************************: