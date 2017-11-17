---
UID: NC.compstui._CPSUICALLBACK
title: _CPSUICALLBACK
author: windows-driver-content
description: 
ms.assetid: e547f0ac-a256-4cd8-8fd0-c921e91a4275
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: compstui.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# _CPSUICALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

_CPSUICALLBACK Cpsuicallback; 

// Definition

LONG Cpsuicallback 
(
	PCPSUICBPARAM pCPSUICBParam
)
{...}

_CPSUICALLBACK 


```

## -parameters

### -param pCPSUICBParam: 



## -returns

Returns LONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also