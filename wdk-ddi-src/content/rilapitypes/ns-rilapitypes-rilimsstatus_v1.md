---
UID : NS:rilapitypes.RILIMSSTATUS_V1
title : RILIMSSTATUS_V1
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilimsstatus_v1_2.htm
old-project : netvista
ms.assetid : e2abab6d-d9c5-4342-8436-fd05a2a298ef
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILIMSSTATUS_V1 structure [Network Drivers Starting with Windows Vista], *LPRILIMSSTATUS_V1, RILIMSSTATUS_V1, netvista.rilimsstatus_v1_2, rilapitypes/RILIMSSTATUS_V1
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
req.typenames : RILIMSSTATUS_V1, *LPRILIMSSTATUS_V1
req.product : Windows 10 or later.
---

# RILIMSSTATUS_V1 structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILIMSSTATUS_V1 {
  DWORD         cbSize;
  DWORD         dwParams;
  DWORD         dwExecutor;
  HUICCAPP      hUiccApp;
  DWORD         dwAvailableServices;
  RILSMSFORMAT  dwSMSSupportedFormat;
} RILIMSSTATUS_V1, RILIMSSTATUS_V1;
````

## Members


`cbSize`



`dwAvailableServices`



`dwExecutor`



`dwParams`



`dwSMSSupportedFormat`



`hUiccApp`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |