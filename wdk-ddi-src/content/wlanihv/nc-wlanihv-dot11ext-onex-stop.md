---
UID: NC.wlanihv.DOT11EXT_ONEX_STOP
title: DOT11EXT_ONEX_STOP
author: windows-driver-content
description: 
ms.assetid: ccc9bc9e-0c94-4188-bd54-38f1fc52c732
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wlanihv.h
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

# DOT11EXT_ONEX_STOP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_ONEX_STOP Dot11extOnexStop; 

// Definition

DWORD Dot11extOnexStop 
(
	HANDLE hDot11SvcHandle
)
{...}

DOT11EXT_ONEX_STOP 


```

## -parameters

### -param hDot11SvcHandle: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also