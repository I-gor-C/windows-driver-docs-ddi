---
UID: NC.dispmprt.DXGKDDI_SET_POWER_STATE
title: DXGKDDI_SET_POWER_STATE
author: windows-driver-content
description: 
ms.assetid: b05be17c-6d2b-4059-bebe-35d072cf9ab2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dispmprt.h
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

# DXGKDDI_SET_POWER_STATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SET_POWER_STATE DxgkddiSetPowerState; 

// Definition

NTSTATUS DxgkddiSetPowerState 
(
	IN_CONST_PVOID MiniportDeviceContext
	IN_ULONG DeviceUid
	IN_DEVICE_POWER_STATE DevicePowerState
	IN_POWER_ACTION ActionType
)
{...}

DXGKDDI_SET_POWER_STATE PDXGKDDI_SET_POWER_STATE


```

## -parameters

### -param MiniportDeviceContext: 
### -param DeviceUid: 
### -param DevicePowerState: 
### -param ActionType: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also