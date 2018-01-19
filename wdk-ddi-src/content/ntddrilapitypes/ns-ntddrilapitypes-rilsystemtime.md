---
UID : NS:ntddrilapitypes.RILSYSTEMTIME
title : RILSYSTEMTIME
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsystemtime.htm
old-project : netvista
ms.assetid : da01963f-a0eb-4222-b0c7-20b924f65f66
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILSYSTEMTIME, RILSYSTEMTIME, *LPRILSYSTEMTIME
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddrilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILSYSTEMTIME
req.alt-loc : ntddrilapitypes.h
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
req.typenames : RILSYSTEMTIME, *LPRILSYSTEMTIME
---

# RILSYSTEMTIME structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILSYSTEMTIME {
  WORD  wYear;
  WORD  wMonth;
  WORD  wDayOfWeek;
  WORD  wDay;
  WORD  wHour;
  WORD  wMinute;
  WORD  wSecond;
  WORD  wMilliseconds;
} RILSYSTEMTIME, RILSYSTEMTIME;
````

## Members

        
            `wDay`

            
        
            `wDayOfWeek`

            
        
            `wHour`

            
        
            `wMilliseconds`

            
        
            `wMinute`

            
        
            `wMonth`

            
        
            `wSecond`

            
        
            `wYear`

            


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |