---
UID: NC.ntddk.pHalQueryBusSlots
title: pHalQueryBusSlots
author: windows-driver-content
description: 
ms.assetid: 22b99a1f-66b4-4a1e-9e05-39babaf21efe
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

# pHalQueryBusSlots callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalQueryBusSlots Phalquerybusslots; 

// Definition

NTSTATUS Phalquerybusslots 
(
	PBUS_HANDLER BusHandler
	ULONG BufferSize
	PULONG SlotNumbers
	PULONG ReturnedLength
)
{...}

pHalQueryBusSlots 


```

## -parameters

### -param BusHandler: 
### -param BufferSize: 
### -param SlotNumbers: 
### -param ReturnedLength: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also