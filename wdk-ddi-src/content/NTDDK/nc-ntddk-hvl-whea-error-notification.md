---
UID: NC.ntddk.HVL_WHEA_ERROR_NOTIFICATION
title: HVL_WHEA_ERROR_NOTIFICATION
author: windows-driver-content
description: 
ms.assetid: 93ca2024-87e6-49f8-ba70-044904de0dec
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

# HVL_WHEA_ERROR_NOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

HVL_WHEA_ERROR_NOTIFICATION HvlWheaErrorNotification; 

// Definition

NTSTATUS HvlWheaErrorNotification 
(
	PWHEA_RECOVERY_CONTEXT RecoveryContext
	BOOLEAN PlatformDirected
	BOOLEAN Poisoned
)
{...}

HVL_WHEA_ERROR_NOTIFICATION 


```

## -parameters

### -param RecoveryContext: 
### -param PlatformDirected: 
### -param Poisoned: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also