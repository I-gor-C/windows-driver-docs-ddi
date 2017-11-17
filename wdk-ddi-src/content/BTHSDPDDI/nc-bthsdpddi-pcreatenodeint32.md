---
UID: NC.bthsdpddi.PCREATENODEINT32
title: PCREATENODEINT32
author: windows-driver-content
description: 
ms.assetid: 665fd14e-fb25-4dbf-ba1c-b2a3fa2c713b
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

# PCREATENODEINT32 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEINT32 Pcreatenodeint32; 

// Definition

PSDP_NODE Pcreatenodeint32 
(
	LONG lVal
	ULONG tag
)
{...}

PCREATENODEINT32 


```

## -parameters

### -param lVal: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also