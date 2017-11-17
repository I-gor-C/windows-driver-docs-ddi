---
UID: NC.wudfwdm.PO_FX_POWER_CONTROL_CALLBACK
title: PO_FX_POWER_CONTROL_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 1bd5b10b-97ad-419b-9206-c2105783ae7e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wudfwdm.h
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

# PO_FX_POWER_CONTROL_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PO_FX_POWER_CONTROL_CALLBACK PoFxPowerControlCallback; 

// Definition

NTSTATUS PoFxPowerControlCallback 
(
	PVOID DeviceContext
	LPCGUID PowerControlCode
	PVOID InBuffer
	SIZE_T InBufferSize
	PVOID OutBuffer
	SIZE_T OutBufferSize
	PSIZE_T BytesReturned
)
{...}

PO_FX_POWER_CONTROL_CALLBACK PPO_FX_POWER_CONTROL_CALLBACK


```

## -parameters

### -param DeviceContext: 
### -param PowerControlCode: 
### -param InBuffer: 
### -param InBufferSize: 
### -param OutBuffer: 
### -param OutBufferSize: 
### -param BytesReturned: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also