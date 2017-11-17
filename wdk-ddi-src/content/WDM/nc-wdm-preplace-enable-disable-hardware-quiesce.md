---
UID: NC.wdm.PREPLACE_ENABLE_DISABLE_HARDWARE_QUIESCE
title: PREPLACE_ENABLE_DISABLE_HARDWARE_QUIESCE
author: windows-driver-content
description: 
ms.assetid: 92ec8979-927b-4b70-a0cf-2450a10ef11b
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

# PREPLACE_ENABLE_DISABLE_HARDWARE_QUIESCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREPLACE_ENABLE_DISABLE_HARDWARE_QUIESCE PreplaceEnableDisableHardwareQuiesce; 

// Definition

NTSTATUS PreplaceEnableDisableHardwareQuiesce 
(
	PVOID Context
	BOOLEAN Enable
)
{...}

PREPLACE_ENABLE_DISABLE_HARDWARE_QUIESCE 


```

## -parameters

### -param Context: 
### -param Enable: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also