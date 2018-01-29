---
UID : NS:ntddrilapitypes.RILGPPCAUSE
title : RILGPPCAUSE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilgppcause.htm
old-project : netvista
ms.assetid : 4072183a-36b5-4a77-a1a5-95b97950b01a
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilgppcause, RILGPPCAUSE structure [Network Drivers Starting with Windows Vista], *LPRILGPPCAUSE, ntddrilapitypes/RILGPPCAUSE, RILGPPCAUSE
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
req.typenames : "*LPRILGPPCAUSE, RILGPPCAUSE"
---

# RILGPPCAUSE structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILGPPCAUSE {
  DWORD  dwLocation;
  DWORD  dwCauseValue;
} RILGPPCAUSE, RILGPPCAUSE;
````

## Members


`dwCauseValue`



`dwLocation`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |