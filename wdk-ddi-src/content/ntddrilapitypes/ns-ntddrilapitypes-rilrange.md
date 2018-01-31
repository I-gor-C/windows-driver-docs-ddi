---
UID : NS:ntddrilapitypes.RILRANGE
title : RILRANGE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilrange.htm
old-project : netvista
ms.assetid : 2f704899-eb5e-4632-a76d-eb474f3273f9
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILRANGE, RILRANGE structure [Network Drivers Starting with Windows Vista], *LPRILRANGE, ntddrilapitypes/RILRANGE, netvista.rilrange
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
req.typenames : "*LPRILRANGE, RILRANGE"
---

# RILRANGE structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILRANGE {
  DWORD  dwMinValue;
  DWORD  dwMaxValue;
} RILRANGE, RILRANGE;
````

## Members


`dwMaxValue`



`dwMinValue`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |