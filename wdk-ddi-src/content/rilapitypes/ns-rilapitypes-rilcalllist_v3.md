---
UID : NS:rilapitypes.RILCALLLIST_V3
title : RILCALLLIST_V3
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcalllist_v3_2.htm
old-project : netvista
ms.assetid : 6ddeb8ab-076e-44a2-9705-8d5d527a9fd7
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilcalllist_v3_2, RILCALLLIST_V3 structure [Network Drivers Starting with Windows Vista], RILCALLLIST_V3, rilapitypes/RILCALLLIST_V3, *LPRILCALLLIST_V3, RILCALLLIST, *LPRILCALLLIST
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
req.typenames : "*LPRILCALLLIST_V3, RILCALLLIST_V3, RILCALLLIST, *LPRILCALLLIST"
req.product : Windows 10 or later.
---

# RILCALLLIST_V3 structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCALLLIST_V3 {
  DWORD              dwNumberOfCalls;
  RILCALLINFO_V3 [1] rciCallInfo;
} RILCALLLIST_V3, RILCALLLIST_V3;
````

## Members


`dwNumberOfCalls`



`rciCallInfo`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |