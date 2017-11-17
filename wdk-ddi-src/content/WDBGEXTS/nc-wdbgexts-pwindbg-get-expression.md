---
UID: NC.wdbgexts.PWINDBG_GET_EXPRESSION
title: PWINDBG_GET_EXPRESSION
author: windows-driver-content
description: 
ms.assetid: 7cac32da-c640-4a18-857d-e5e65447f4b7
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

# PWINDBG_GET_EXPRESSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_GET_EXPRESSION PwindbgGetExpression; 

// Definition

ULONG_PTR PwindbgGetExpression 
(
	PCSTR lpExpression
)
{...}

PWINDBG_GET_EXPRESSION 


```

## -parameters

### -param lpExpression: 



## -returns

Returns ULONG_PTR that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also