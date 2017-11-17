---
UID: NC.ntddk.PCI_EXPRESS_WAKE_CONTROL
title: PCI_EXPRESS_WAKE_CONTROL
author: windows-driver-content
description: 
ms.assetid: 8959d070-b0aa-499e-bd01-546a1e2a1467
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

# PCI_EXPRESS_WAKE_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCI_EXPRESS_WAKE_CONTROL PciExpressWakeControl; 

// Definition

VOID PciExpressWakeControl 
(
	PVOID Context
	BOOLEAN EnableWake
)
{...}

PCI_EXPRESS_WAKE_CONTROL PPCI_EXPRESS_WAKE_CONTROL


```

## -parameters

### -param Context: 
### -param EnableWake: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also