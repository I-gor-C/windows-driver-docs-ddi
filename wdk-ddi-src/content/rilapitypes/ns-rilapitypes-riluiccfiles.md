---
UID : NS:rilapitypes.RILUICCFILES
title : RILUICCFILES
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluiccfiles_2.htm
old-project : netvista
ms.assetid : 282cd191-03c5-4599-9a61-e84221ef9143
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.riluiccfiles_2, RILUICCFILES structure [Network Drivers Starting with Windows Vista], *LPRILUICCFILES, rilapitypes/RILUICCFILES, RILUICCFILES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : rilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*LPRILUICCFILES, RILUICCFILES"
req.product : Windows 10 or later.
---

# RILUICCFILES structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILUICCFILES {
  DWORD               cbSize;
  DWORD               dwNumFiles;
  RILUICCFILEPATH [1] filePath;
} RILUICCFILES, RILUICCFILES;
````

## Members


`cbSize`



`dwNumFiles`



`filePath`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |