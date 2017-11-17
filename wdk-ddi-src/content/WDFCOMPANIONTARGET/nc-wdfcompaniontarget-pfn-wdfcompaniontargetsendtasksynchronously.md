---
UID: NC.wdfcompaniontarget.PFN_WDFCOMPANIONTARGETSENDTASKSYNCHRONOUSLY
title: PFN_WDFCOMPANIONTARGETSENDTASKSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: 0081dd69-c207-453c-9604-986795a836b9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcompaniontarget.h
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

# PFN_WDFCOMPANIONTARGETSENDTASKSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMPANIONTARGETSENDTASKSYNCHRONOUSLY PfnWdfcompaniontargetsendtasksynchronously; 

// Definition

WDFAPI PfnWdfcompaniontargetsendtasksynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOMPANIONTARGET CompanionTarget
	USHORT TaskQueueIdentifier
	ULONG TaskOperationCode
	PWDF_MEMORY_DESCRIPTOR InputBuffer
	PWDF_MEMORY_DESCRIPTOR OutputBuffer
	PWDF_TASK_SEND_OPTIONS TaskOptions
	PULONG_PTR BytesReturned
)
{...}

PFN_WDFCOMPANIONTARGETSENDTASKSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param CompanionTarget: 
### -param TaskQueueIdentifier: 
### -param TaskOperationCode: 
### -param InputBuffer: 
### -param OutputBuffer: 
### -param TaskOptions: 
### -param BytesReturned: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also