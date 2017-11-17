---
UID: NC.bthsdpddi.PCREATENODEINT16
title: PCREATENODEINT16
author: windows-driver-content
description: 
ms.assetid: 30c17563-351c-47e8-a2b0-f8524c00fc49
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: bthsdpddi.h
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

# PCREATENODEINT16 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEINT16 Pcreatenodeint16; 

// Definition

PSDP_NODE Pcreatenodeint16 
(
	SHORT sVal
	ULONG tag
)
{...}

PCREATENODEINT16 


```

## -parameters

### -param sVal: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also