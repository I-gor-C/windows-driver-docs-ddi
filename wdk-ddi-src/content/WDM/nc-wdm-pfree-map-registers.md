---
UID: NC.wdm.PFREE_MAP_REGISTERS
title: PFREE_MAP_REGISTERS
author: windows-driver-content
description: 
ms.assetid: 28d06ee7-b1ca-4374-b5d5-b41cb480b643
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

# PFREE_MAP_REGISTERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFREE_MAP_REGISTERS PfreeMapRegisters; 

// Definition

VOID PfreeMapRegisters 
(
	PDMA_ADAPTER DmaAdapter
	PVOID MapRegisterBase
	ULONG NumberOfMapRegisters
)
{...}

PFREE_MAP_REGISTERS 


```

## -parameters

### -param DmaAdapter: 
### -param MapRegisterBase: 
### -param NumberOfMapRegisters: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also