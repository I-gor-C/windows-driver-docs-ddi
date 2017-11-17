---
UID: NC.wdbgexts.PWINDBG_OUTPUT_ROUTINE
title: PWINDBG_OUTPUT_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 6681233a-8e0a-4df7-a854-45ac45081af8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdbgexts.h
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

# PWINDBG_OUTPUT_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_OUTPUT_ROUTINE PwindbgOutputRoutine; 

// Definition

VOID PwindbgOutputRoutine 
(
	PCSTR lpFormat
	 ...
)
{...}

PWINDBG_OUTPUT_ROUTINE 


```

## -parameters

### -param lpFormat: 
### -param ...: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also