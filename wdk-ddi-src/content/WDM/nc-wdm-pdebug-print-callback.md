---
UID: NC.wdm.PDEBUG_PRINT_CALLBACK
title: PDEBUG_PRINT_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 4fd294a9-5037-40ed-8311-5bb5c39a84ff
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PDEBUG_PRINT_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_PRINT_CALLBACK PdebugPrintCallback; 

// Definition

VOID PdebugPrintCallback 
(
	PSTRING Output
	ULONG ComponentId
	ULONG Level
)
{...}

PDEBUG_PRINT_CALLBACK 


```

## -parameters

### -param Output: 
### -param ComponentId: 
### -param Level: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also