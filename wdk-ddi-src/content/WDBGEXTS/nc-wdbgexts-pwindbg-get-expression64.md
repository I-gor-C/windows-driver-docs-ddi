---
UID: NC.wdbgexts.PWINDBG_GET_EXPRESSION64
title: PWINDBG_GET_EXPRESSION64
author: windows-driver-content
description: 
ms.assetid: b06cd3b0-f61e-4bbe-84fa-771f6c6f923e
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

# PWINDBG_GET_EXPRESSION64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_GET_EXPRESSION64 PwindbgGetExpression64; 

// Definition

ULONG64 PwindbgGetExpression64 
(
	PCSTR lpExpression
)
{...}

PWINDBG_GET_EXPRESSION64 


```

## -parameters

### -param lpExpression: 



## -returns

Returns ULONG64 that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also