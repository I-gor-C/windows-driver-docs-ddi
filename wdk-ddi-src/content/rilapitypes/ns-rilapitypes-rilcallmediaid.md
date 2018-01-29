---
UID : NS:rilapitypes.RILCALLMEDIAID
title : RILCALLMEDIAID
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallmediaid_2.htm
old-project : netvista
ms.assetid : ad367969-217c-4b9a-b9b1-1b6d1bf04f2e
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILCALLMEDIAID, rilapitypes/RILCALLMEDIAID, *LPRILCALLMEDIAID, RILCALLMEDIAID structure [Network Drivers Starting with Windows Vista], netvista.rilcallmediaid_2
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
req.typenames : RILCALLMEDIAID, *LPRILCALLMEDIAID
req.product : Windows 10 or later.
---

# RILCALLMEDIAID structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCALLMEDIAID {
  RILCALLMEDIATYPE  dwType;
  DWORD             dwID;
} RILCALLMEDIAID, RILCALLMEDIAID;
````

## Members


`dwID`



`dwType`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |