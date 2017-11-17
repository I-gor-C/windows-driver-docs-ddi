---
UID: NC.wdbgexts.PWINDBG_DISASM
title: PWINDBG_DISASM
author: windows-driver-content
description: 
ms.assetid: 7fb835df-89c8-4f43-8b7a-b7b3e2c83b9d
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

# PWINDBG_DISASM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_DISASM PwindbgDisasm; 

// Definition

ULONG PwindbgDisasm 
(
	ULONG_PTR *lpOffset
	PCSTR lpBuffer
	ULONG fShowEffectiveAddress
)
{...}

PWINDBG_DISASM 


```

## -parameters

### -param *lpOffset: 
### -param lpBuffer: 
### -param fShowEffectiveAddress: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also