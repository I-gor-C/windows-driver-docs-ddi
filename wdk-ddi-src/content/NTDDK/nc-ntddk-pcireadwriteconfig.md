---
UID: NC.ntddk.PciReadWriteConfig
title: PciReadWriteConfig
author: windows-driver-content
description: 
ms.assetid: 8abaa185-2e25-4a12-93cb-8c6203e37f73
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

# PciReadWriteConfig callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PciReadWriteConfig Pcireadwriteconfig; 

// Definition

VOID Pcireadwriteconfig 
(
	_BUS_HANDLER *BusHandler
	PCI_SLOT_NUMBER Slot
	PVOID Buffer
	ULONG Offset
	ULONG Length
)
{...}

PciReadWriteConfig 


```

## -parameters

### -param *BusHandler: 
### -param Slot: 
### -param Buffer: 
### -param Offset: 
### -param Length: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also