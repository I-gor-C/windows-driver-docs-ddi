---
UID: NC.ntddk.pKdGetPciDataByOffset
title: pKdGetPciDataByOffset
author: windows-driver-content
description: 
ms.assetid: 754bec40-b2a5-46d4-ae00-90cdf0a3e291
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# pKdGetPciDataByOffset callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pKdGetPciDataByOffset Pkdgetpcidatabyoffset; 

// Definition

ULONG Pkdgetpcidatabyoffset 
(
	ULONG BusNumber
	ULONG SlotNumber
	PVOID Buffer
	ULONG Offset
	ULONG Length
)
{...}

pKdGetPciDataByOffset 


```

## -parameters

### -param BusNumber: 
### -param SlotNumber: 
### -param Buffer: 
### -param Offset: 
### -param Length: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also