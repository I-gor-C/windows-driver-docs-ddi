---
UID: NC.wlanihv.DOT11EXT_ONEX_START
title: DOT11EXT_ONEX_START
author: windows-driver-content
description: 
ms.assetid: 44227d5b-7688-4b06-bbc1-1e0c5cd36247
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

# DOT11EXT_ONEX_START callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_ONEX_START Dot11extOnexStart; 

// Definition

DWORD Dot11extOnexStart 
(
	HANDLE hDot11SvcHandle
	EAP_ATTRIBUTES *pEapAttributes
)
{...}

DOT11EXT_ONEX_START 


```

## -parameters

### -param hDot11SvcHandle: 
### -param *pEapAttributes: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also