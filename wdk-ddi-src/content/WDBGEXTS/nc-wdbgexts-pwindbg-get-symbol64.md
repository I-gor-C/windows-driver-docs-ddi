---
UID: NC.wdbgexts.PWINDBG_GET_SYMBOL64
title: PWINDBG_GET_SYMBOL64
author: windows-driver-content
description: 
ms.assetid: 7ae4fa44-ec24-4c74-bd6c-f9601e5d97b2
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

# PWINDBG_GET_SYMBOL64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_GET_SYMBOL64 PwindbgGetSymbol64; 

// Definition

VOID PwindbgGetSymbol64 
(
	ULONG64 offset
	PCHAR pchBuffer
	PULONG64 pDisplacement
)
{...}

PWINDBG_GET_SYMBOL64 


```

## -parameters

### -param offset: 
### -param pchBuffer: 
### -param pDisplacement: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also