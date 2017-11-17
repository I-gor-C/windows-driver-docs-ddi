---
UID: NC.ntddk.PCI_LINE_TO_PIN
title: PCI_LINE_TO_PIN
author: windows-driver-content
description: 
ms.assetid: f782c129-f1e6-4dbf-81c4-e02e5669c7ff
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

# PCI_LINE_TO_PIN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCI_LINE_TO_PIN PciLineToPin; 

// Definition

VOID PciLineToPin 
(
	PVOID Context
	PPCI_COMMON_CONFIG PciNewData
	PPCI_COMMON_CONFIG PciOldData
)
{...}

PCI_LINE_TO_PIN PPCI_LINE_TO_PIN


```

## -parameters

### -param Context: 
### -param PciNewData: 
### -param PciOldData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also