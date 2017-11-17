---
UID: NC.ntddk.PCI_ROOT_BUS_CAPABILITY
title: PCI_ROOT_BUS_CAPABILITY
author: windows-driver-content
description: 
ms.assetid: 7f4aff92-bff2-42a7-8906-2aec006bf9ae
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

# PCI_ROOT_BUS_CAPABILITY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCI_ROOT_BUS_CAPABILITY PciRootBusCapability; 

// Definition

VOID PciRootBusCapability 
(
	PVOID Context
	PPCI_ROOT_BUS_HARDWARE_CAPABILITY HardwareCapability
)
{...}

PCI_ROOT_BUS_CAPABILITY PPCI_ROOT_BUS_CAPABILITY


```

## -parameters

### -param Context: 
### -param HardwareCapability: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also