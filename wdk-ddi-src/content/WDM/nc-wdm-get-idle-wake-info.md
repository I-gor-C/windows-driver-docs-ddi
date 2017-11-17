---
UID: NC.wdm.GET_IDLE_WAKE_INFO
title: GET_IDLE_WAKE_INFO
author: windows-driver-content
description: 
ms.assetid: a3b85110-fd79-485f-9d25-915375b8f816
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

# GET_IDLE_WAKE_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GET_IDLE_WAKE_INFO GetIdleWakeInfo; 

// Definition

NTSTATUS GetIdleWakeInfo 
(
	PVOID Context
	SYSTEM_POWER_STATE SystemPowerState
	PDEVICE_WAKE_DEPTH DeepestWakeableDstate
)
{...}

GET_IDLE_WAKE_INFO PGET_IDLE_WAKE_INFO


```

## -parameters

### -param Context: 
### -param SystemPowerState: 
### -param DeepestWakeableDstate: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also