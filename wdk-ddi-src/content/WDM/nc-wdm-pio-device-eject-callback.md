---
UID: NC.wdm.PIO_DEVICE_EJECT_CALLBACK
title: PIO_DEVICE_EJECT_CALLBACK
author: windows-driver-content
description: 
ms.assetid: d52ebd48-d89e-46e5-93c9-c18fddadb06b
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

# PIO_DEVICE_EJECT_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PIO_DEVICE_EJECT_CALLBACK PioDeviceEjectCallback; 

// Definition

VOID PioDeviceEjectCallback 
(
	NTSTATUS Status
	PVOID Context
)
{...}

PIO_DEVICE_EJECT_CALLBACK 


```

## -parameters

### -param Status: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also