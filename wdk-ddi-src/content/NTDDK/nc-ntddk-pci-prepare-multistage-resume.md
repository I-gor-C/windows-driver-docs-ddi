---
UID: NC.ntddk.PCI_PREPARE_MULTISTAGE_RESUME
title: PCI_PREPARE_MULTISTAGE_RESUME
author: windows-driver-content
description: 
ms.assetid: 2b05a6af-78b3-45ce-b073-43a0873c2bdc
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

# PCI_PREPARE_MULTISTAGE_RESUME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCI_PREPARE_MULTISTAGE_RESUME PciPrepareMultistageResume; 

// Definition

VOID PciPrepareMultistageResume 
(
	PVOID Context
)
{...}

PCI_PREPARE_MULTISTAGE_RESUME PPCI_PREPARE_MULTISTAGE_RESUME


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also