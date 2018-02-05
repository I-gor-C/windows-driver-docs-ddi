---
UID : NS:ntddrilapitypes.RILSETPREFERREDOPERATORLISTPARAMS
title : RILSETPREFERREDOPERATORLISTPARAMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsetpreferredoperatorlistparams.htm
old-project : netvista
ms.assetid : cec1db47-640c-467a-ba7d-270659ebbba2
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : "*LPRILSETPREFERREDOPERATORLISTPARAMS, ntddrilapitypes/RILSETPREFERREDOPERATORLISTPARAMS, RILSETPREFERREDOPERATORLISTPARAMS structure [Network Drivers Starting with Windows Vista], RILSETPREFERREDOPERATORLISTPARAMS, netvista.rilsetpreferredoperatorlistparams"
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
req.typenames : RILSETPREFERREDOPERATORLISTPARAMS, *LPRILSETPREFERREDOPERATORLISTPARAMS
---

# RILSETPREFERREDOPERATORLISTPARAMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILSETPREFERREDOPERATORLISTPARAMS {
  HUICCAPP             hUiccApp;
  DWORD                dwPreferredListSize;
  RILOPERATORNAMES [1] PreferredList;
} RILSETPREFERREDOPERATORLISTPARAMS, RILSETPREFERREDOPERATORLISTPARAMS;
````

## Members


`dwPreferredListSize`



`hUiccApp`



`PreferredList`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |