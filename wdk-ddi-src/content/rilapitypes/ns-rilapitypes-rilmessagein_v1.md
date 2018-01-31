---
UID : NS:rilapitypes.RILMESSAGEIN_V1
title : RILMESSAGEIN_V1
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmessagein_v1_2.htm
old-project : netvista
ms.assetid : 2b47523f-6938-4071-a0aa-91cdf05faed7
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RILMESSAGEIN_V1, RILMESSAGEIN_V1, RILMESSAGEIN_V1 structure [Network Drivers Starting with Windows Vista], netvista.rilmessagein_v1_2
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
req.typenames : RILMESSAGEIN_V1
req.product : Windows 10 or later.
---

# RILMESSAGEIN_V1 structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILMESSAGEIN_V1 {
  DWORD       cbSize;
  DWORD       dwExecutor;
  HUICCAPP    hUiccApp;
  DWORD       dwAckID;
  RILMESSAGE  rm;
} RILMESSAGEIN_V1, RILMESSAGEIN_V1;
````

## Members


`cbSize`



`dwAckID`



`dwExecutor`



`hUiccApp`



`rm`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |