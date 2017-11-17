---
UID: NC.bthsdpddi.PCREATENODEINT128
title: PCREATENODEINT128
author: windows-driver-content
description: 
ms.assetid: 12368ba8-abca-4ff7-9889-24eefd9c0069
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

# PCREATENODEINT128 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEINT128 Pcreatenodeint128; 

// Definition

PSDP_NODE Pcreatenodeint128 
(
	PSDP_LARGE_INTEGER_16 pul16Val
	ULONG tag
)
{...}

PCREATENODEINT128 


```

## -parameters

### -param pul16Val: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also