---
UID : NS:rilapitypes.RILUICCRESPONSE
title : RILUICCRESPONSE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluiccresponse_2.htm
old-project : netvista
ms.assetid : c3d3481e-a0db-492d-8fc3-6bdcfa26f4c4
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : "*LPRILUICCRESPONSE, rilapitypes/RILUICCRESPONSE, netvista.riluiccresponse_2, RILUICCRESPONSE, RILUICCRESPONSE structure [Network Drivers Starting with Windows Vista]"
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
req.typenames : "*LPRILUICCRESPONSE, RILUICCRESPONSE"
req.product : Windows 10 or later.
---

# RILUICCRESPONSE structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILUICCRESPONSE {
  DWORD    cbSize;
  DWORD    dwParams;
  DWORD    dwStatusWord1;
  DWORD    dwStatusWord2;
  DWORD    dwResponseSize;
  BYTE [1] pbResponse;
} RILUICCRESPONSE, RILUICCRESPONSE;
````

## Members


`cbSize`



`dwParams`



`dwResponseSize`



`dwStatusWord1`



`dwStatusWord2`



`pbResponse`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |