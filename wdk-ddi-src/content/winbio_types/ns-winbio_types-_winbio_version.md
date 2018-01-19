---
UID : NS:winbio_types._WINBIO_VERSION
title : _WINBIO_VERSION
author : windows-driver-content
description : The WINBIO_VERSION structure describes major and minor version information for a WBDI driver.
old-location : biometric\winbio_version.htm
old-project : biometric
ms.assetid : 6a89a581-0af4-4a42-be81-fb7cb1f33bdd
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WINBIO_VERSION, WINBIO_VERSION, *PWINBIO_VERSION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : winbio_types.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 7 and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WINBIO_VERSION
req.alt-loc : winbio_types.h
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
req.typenames : WINBIO_VERSION, *PWINBIO_VERSION
req.product : Windows 10 or later.
---

# _WINBIO_VERSION structure
The WINBIO_VERSION structure describes major and minor version information for a WBDI driver.

## Syntax
````
typedef struct _WINBIO_VERSION {
  DWORD MajorVersion;
  DWORD MinorVersion;
} WINBIO_VERSION, *PWINBIO_VERSION;
````

## Members

        
            `MajorVersion`

            Identifies the major version of the driver.
        
            `MinorVersion`

            Identifies the minor version of the driver.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | winbio_types.h |