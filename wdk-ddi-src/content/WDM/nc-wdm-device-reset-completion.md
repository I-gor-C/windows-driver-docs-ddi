---
UID: NC.wdm.DEVICE_RESET_COMPLETION
title: DEVICE_RESET_COMPLETION
author: windows-driver-content
description: 
ms.assetid: fb6c8bff-b2aa-4422-a3b1-bb98f6af78f8
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

# DEVICE_RESET_COMPLETION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DEVICE_RESET_COMPLETION DeviceResetCompletion; 

// Definition

VOID DeviceResetCompletion 
(
	NTSTATUS Status
	PVOID Context
)
{...}

DEVICE_RESET_COMPLETION 


```

## -parameters

### -param Status: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also