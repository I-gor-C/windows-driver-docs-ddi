---
UID: NC.scutil.POWER_CALLBACK
title: POWER_CALLBACK
author: windows-driver-content
description: 
ms.assetid: ea621f65-23af-4003-99c0-3e7523416635
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: scutil.h
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

# POWER_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

POWER_CALLBACK PowerCallback; 

// Definition

NTSTATUS PowerCallback 
(
	PDEVICE_OBJECT DeviceObject
	DEVICE_POWER_STATE DeviceState
	PBOOLEAN PostWaitWake
)
{...}

POWER_CALLBACK 


```

## -parameters

### -param DeviceObject: 
### -param DeviceState: 
### -param PostWaitWake: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also