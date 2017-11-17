---
UID: NC.wdbgexts.PWINDBG_GET_EXPRESSION32
title: PWINDBG_GET_EXPRESSION32
author: windows-driver-content
description: 
ms.assetid: 0402344f-3bbe-4cd1-93ea-333d2b55f293
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

# PWINDBG_GET_EXPRESSION32 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_GET_EXPRESSION32 PwindbgGetExpression32; 

// Definition

ULONG PwindbgGetExpression32 
(
	PCSTR lpExpression
)
{...}

PWINDBG_GET_EXPRESSION32 


```

## -parameters

### -param lpExpression: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also