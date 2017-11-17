---
UID: NC.ntddk.PciPin2Line
title: PciPin2Line
author: windows-driver-content
description: 
ms.assetid: 224eec2c-dd3a-47aa-b07f-58e258270b62
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

# PciPin2Line callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PciPin2Line Pcipin2line; 

// Definition

VOID Pcipin2line 
(
	_BUS_HANDLER *BusHandler
	_BUS_HANDLER *RootHandler
	PCI_SLOT_NUMBER SlotNumber
	PPCI_COMMON_CONFIG PciData
)
{...}

PciPin2Line 


```

## -parameters

### -param *BusHandler: 
### -param *RootHandler: 
### -param SlotNumber: 
### -param PciData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also