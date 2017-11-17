---
UID: NC.dsm.DSM_DEVICE_NOT_USED
title: DSM_DEVICE_NOT_USED
author: windows-driver-content
description: 
ms.assetid: a411b142-3c79-4253-b31b-d372094da05c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_DEVICE_NOT_USED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_DEVICE_NOT_USED DsmDeviceNotUsed; 

// Definition

NTSTATUS DsmDeviceNotUsed 
(
	IN PVOID DsmContext
	IN PVOID DsmId
)
{...}

DSM_DEVICE_NOT_USED 


```

## -parameters

### -param DsmContext: 
### -param DsmId: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also