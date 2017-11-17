---
UID: NC.ntddk.PciLine2Pin
title: PciLine2Pin
author: windows-driver-content
description: 
ms.assetid: d64417e4-f2ee-4ff7-91b0-9cd8ce431354
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

# PciLine2Pin callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PciLine2Pin Pciline2pin; 

// Definition

VOID Pciline2pin 
(
	_BUS_HANDLER *BusHandler
	_BUS_HANDLER *RootHandler
	PCI_SLOT_NUMBER SlotNumber
	PPCI_COMMON_CONFIG PciNewData
	PPCI_COMMON_CONFIG PciOldData
)
{...}

PciLine2Pin 


```

## -parameters

### -param *BusHandler: 
### -param *RootHandler: 
### -param SlotNumber: 
### -param PciNewData: 
### -param PciOldData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also