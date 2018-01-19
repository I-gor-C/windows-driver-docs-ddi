---
UID : NS:scsiscan._SCSISCAN_INFO
title : _SCSISCAN_INFO
author : windows-driver-content
description : The SCSISCAN_INFO structure is used as a parameter to DeviceIoControl (described in the Microsoft Windows SDK documentation), when the specified I/O control code is IOCTL_SCSISCAN_GET_INFO.
old-location : image\scsiscan_info.htm
old-project : image
ms.assetid : 5fd9b381-c0e3-45bf-9061-da816da5e29f
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : _SCSISCAN_INFO, *PSCSISCAN_INFO, SCSISCAN_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : scsiscan.h
req.include-header : Scsiscan.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SCSISCAN_INFO
req.alt-loc : scsiscan.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSCSISCAN_INFO, SCSISCAN_INFO"
req.product : Windows 10 or later.
---

# _SCSISCAN_INFO structure
The SCSISCAN_INFO structure is used as a parameter to <a href="https://msdn.microsoft.com/1d35c087-6672-4fc6-baa1-a886dd9d3878">DeviceIoControl</a> (described in the Microsoft Windows SDK documentation), when the specified I/O control code is <a href="..\scsiscan\ni-scsiscan-ioctl_scsiscan_get_info.md">IOCTL_SCSISCAN_GET_INFO</a>.

## Syntax
````
typedef struct _SCSISCAN_INFO {
  ULONG Size;
  ULONG Flags;
  UCHAR PortNumber;
  UCHAR PathId;
  UCHAR TargetId;
  UCHAR Lun;
  UCHAR AdapterName[MAX_STRING];
  ULONG Reserved;
} SCSISCAN_INFO, *PSCSISCAN_INFO;
````

## Members

        
            `AdapterName`

            <i>For internal use only.</i>
        
            `Flags`

            Not used, must be zero.
        
            `Lun`

            Target logical unit number (LUN).
        
            `PathId`

            Host SCSI ID.
        
            `PortNumber`

            SCSI adapter number.
        
            `Reserved`

            <i>For internal use only.</i>
        
            `Size`

            Size, in bytes, of the SCSISCAN_INFO structure.
        
            `TargetId`

            Target SCSI ID.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | scsiscan.h (include Scsiscan.h) |