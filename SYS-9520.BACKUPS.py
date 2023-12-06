#--
#-- ************************************************************************************************************:
#-- ******************************************* JBALLARD-9520 TO USBs ******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBallard (JEB)                                                                                    :
#-- Date:     2023.9.14                                                                                         :
#-- Script:   SYS-9520.BACKUPS.py                                                                               :
#-- Dir:      \\JBALLARD-9520\C$\0_SVN\2_DEV\0_SCRIPTS.Src\0_USEFUL.Dev\1_BACKUP.Dev\                           :
#-- Purpose:  A Python script that replicates the (\\JBALLARD-9520\C$\0_SVN\) repo to an external USB Disk.     :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import os
import shutil
import datetime
import multiprocessing
#--
#-- START THE REPLICATION PROCESS WHILE PRESERVING METADATA:
def COPYFile(SRCPath, DESTPath):
    try:
        shutil.copy2(SRCPath, DESTPath)
        print(f' {TIMEStamp}: NOTE - COPIED: {SRCPath} TO {DESTPath} & {DESTPath2}')
        print(f' {TIMEStamp}: NOTE - COPIED: {SRCPath} TO {DESTPath}')
    except Exception as e:
        print(f' {TIMEStamp}: ERROR - REPLICATION FAILED TO COPY {SRCPath}: {e}')
#--
#-- REPLICATE SOURCE FILES TO 2 DIFFERENT DESTINATIONS:
def COPYFiles(src_dir, dest_dir, new_dest_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            SRCPath   = os.path.join(root, file)
            DESTPath  = os.path.join(dest_dir, os.path.relpath(SRCPath, src_dir))
            DESTPath2 = os.path.join(new_dest_dir, os.path.relpath(SRCPath, src_dir))
            if not os.path.exists(DESTPath) or os.path.getmtime(SRCPath) > os.path.getmtime(DESTPath):
                os.makedirs(os.path.dirname(DESTPath), exist_ok=True)
                COPYFile(SRCPath, DESTPath)
            if not os.path.exists(DESTPath2) or os.path.getmtime(SRCPath) > os.path.getmtime(DESTPath2):
                os.makedirs(os.path.dirname(DESTPath2), exist_ok=True)
                COPYFile(SRCPath, DESTPath2)
#--
#-- MAIN:
if __name__ == "__main__":
    #--
    #-- DEFINE SRC & 2 DEST PATHS:
    SRCDir   = r'//JBALLARD-9520/C$/0_SVN'
    DESTDir  = r'//JBALLARD-9520/D$/0_REPO/0_SVN'
    DESTDir2 = r'//JBALLARD-9520/E$/0_REPO/0_SVN'
    #--
    TIMEStamp = datetime.datetime.now().strftime('%Y-%m-%d:%H-%M-%S')
    try:
        #-- VERIFY THE EXISTANCE OF THE 2 DEST DIRS & CREATE THEM IF PATH = FALSE:
        if not os.path.exists(DESTDir):
            os.makedirs(DESTDir)
        if not os.path.exists(DESTDir2):
            os.makedirs(DESTDir2)
        #--
        print(f' {TIMEStamp}: NOTE - REPLICATION PROCESS STARTED:')
        #--
        #-- CREATE MULTI-PROCESSING POOL:
        MPPool = multiprocessing.Pool()
        #--
        #-- SCAN SOURCE REPOSITORY & ALL SUBDIRECTORIES:
        for root, _, files in os.walk(SRCDir):
            for file in files:
                SRCPath = os.path.join(root, file)
                DESTPath = os.path.join(DESTDir, os.path.relpath(SRCPath, SRCDir))
                DESTPath2 = os.path.join(DESTDir2, os.path.relpath(SRCPath, SRCDir))
                print(f' {TIMEStamp}: NOTE - REPLICATING {file}:')
                #--
                #-- USE MULTI-PROCESSING POOL THAT COPIES FILES TO 2 DIRS IN PARALLEL:
                if not os.path.exists(DESTPath) or os.path.getmtime(SRCPath) > os.path.getmtime(DESTPath):
                    os.makedirs(os.path.dirname(DESTPath), exist_ok=True)
                    MPPool.apply_async(COPYFile, (SRCPath, DESTPath))
                if not os.path.exists(DESTPath2) or os.path.getmtime(SRCPath) > os.path.getmtime(DESTPath2):
                    os.makedirs(os.path.dirname(DESTPath2), exist_ok=True)
                    MPPool.apply_async(COPYFile, (SRCPath, DESTPath2))
        #--
        #-- CLOSE MULTI-PROCESSING POOL:
        MPPool.close()
        MPPool.join()
        #--
        print(f' {TIMEStamp}: SUCCESS - REPLICATION PROCESS TO {DESTDir} & {DESTDir2} WAS SUCCESSFULL:')
        print(f' {TIMEStamp}: SUCCESS - REPLICATION PROCESS TO {DESTDir} WAS SUCCESSFULL:')
    except Exception as e:
        print(f' {TIMEStamp}: FAILURE - ERROR PROCESSING BACKUPS - {e}')
#--
#-- ********************************************************:
#-- END OF SCRIPT                                           :
#-- ********************************************************:
