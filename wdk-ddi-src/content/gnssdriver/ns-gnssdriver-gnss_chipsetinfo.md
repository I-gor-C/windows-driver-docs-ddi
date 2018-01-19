---
UID : NS:gnssdriver.GNSS_CHIPSETINFO
title : GNSS_CHIPSETINFO
author : windows-driver-content
description : This structure defines the specific data elements associated with the GNSS hardware.
old-location : sensors\gnss_chipsetinfo.htm
old-project : sensors
ms.assetid : DE45805C-09E6-44B8-A4DA-BF73EC444AA9
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : GNSS_CHIPSETINFO, *PGNSS_CHIPSETINFO, GNSS_CHIPSETINFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : gnssdriver.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : GNSS_CHIPSETINFO
req.alt-loc : gnssdriver.h
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
req.typenames : "*PGNSS_CHIPSETINFO, GNSS_CHIPSETINFO"
---

# GNSS_CHIPSETINFO structure
This structure defines the specific data elements associated with the GNSS hardware.

## Syntax
````
typedef struct {
  ULONG Size;
  ULONG Version;
  WCHAR ManufacturerID[25];
  WCHAR HardwareID[25];
  WCHAR FirmwareVersion[20];
  BYTE  Unused[512];
} GNSS_CHIPSETINFO, *PGNSS_CHIPSETINFO;
````

## Members

        
            `Size`

            Structure size.
        
            `Version`

            Version number.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | gnssdriver.h |