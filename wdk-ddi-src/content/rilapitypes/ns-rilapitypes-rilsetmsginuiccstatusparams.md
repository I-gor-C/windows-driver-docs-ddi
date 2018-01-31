---
UID : NS:rilapitypes.RILSETMSGINUICCSTATUSPARAMS
title : RILSETMSGINUICCSTATUSPARAMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsetmsginuiccstatusparams_2.htm
old-project : netvista
ms.assetid : 12181c9d-c0bd-48ee-8eaf-64cc66c272f4
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilsetmsginuiccstatusparams_2, RILSETMSGINUICCSTATUSPARAMS structure [Network Drivers Starting with Windows Vista], *LPRILSETMSGINUICCSTATUSPARAMS, RILSETMSGINUICCSTATUSPARAMS, rilapitypes/RILSETMSGINUICCSTATUSPARAMS
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
req.typenames : "*LPRILSETMSGINUICCSTATUSPARAMS, RILSETMSGINUICCSTATUSPARAMS"
req.product : Windows 10 or later.
---

# RILSETMSGINUICCSTATUSPARAMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILSETMSGINUICCSTATUSPARAMS {
  HUICCAPP          hUiccApp;
  DWORD             dwIndex;
  RILMESSAGESTATUS  dwStatus;
} RILSETMSGINUICCSTATUSPARAMS, RILSETMSGINUICCSTATUSPARAMS;
````

## Members


`dwIndex`



`dwStatus`



`hUiccApp`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |