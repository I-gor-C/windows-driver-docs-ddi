---
UID : NS:wiadef._WIA_MICR_INFO
title : _WIA_MICR_INFO
author : windows-driver-content
description : The WIA_MICR_INFO structure stores information for one decoded MICR code.
old-location : image\wia_micr_info.htm
old-project : image
ms.assetid : E91F5D6F-40F9-4CE2-8C51-4CA7FB27F2C3
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : _WIA_MICR_INFO, WIA_MICR_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : wiadef.h
req.include-header : Wiadef.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WIA_MICR_INFO
req.alt-loc : wiadef.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : See Remarks section.
req.typenames : WIA_MICR_INFO
req.product : Windows 10 or later.
---

# _WIA_MICR_INFO structure
The <b>WIA_MICR_INFO</b> structure stores information for one decoded MICR code.

## Syntax
````
typedef struct _WIA_MICR_INFO {
  DWORD Size;
  DWORD Page;
  DWORD Length;
  WCHAR Text[1];
} WIA_MICR_INFO;
````

## Members

        
            `Length`

            Length of the MICR text, in characters, excluding the length of the NULL terminator.
        
            `Page`

            The page number where the MICR code was detected. A zero-based index referring to the current scan job.
        
            `Size`

            The total size of this structure, in bytes.
        
            `Text`

            Placeholder for a NULL terminated character string containing the MICR text.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wiadef.h (include Wiadef.h) |