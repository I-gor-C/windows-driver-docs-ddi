---
UID: NC.d3dkmthk.PDXGK_SET_SHARED_POWER_COMPONENT_STATE
title: PDXGK_SET_SHARED_POWER_COMPONENT_STATE
author: windows-driver-content
description: 
ms.assetid: e55059bd-45be-4496-ad65-733854849805
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmthk.h
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

# PDXGK_SET_SHARED_POWER_COMPONENT_STATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDXGK_SET_SHARED_POWER_COMPONENT_STATE PdxgkSetSharedPowerComponentState; 

// Definition

NTSTATUS PdxgkSetSharedPowerComponentState 
(
	PVOID DeviceHandle
	PVOID PrivateHandle
	ULONG ComponentIndex
	BOOLEAN Active
)
{...}

PDXGK_SET_SHARED_POWER_COMPONENT_STATE 


```

## -parameters

### -param DeviceHandle: 
### -param PrivateHandle: 
### -param ComponentIndex: 
### -param Active: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also