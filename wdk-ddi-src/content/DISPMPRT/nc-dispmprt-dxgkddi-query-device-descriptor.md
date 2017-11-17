---
UID: NC.dispmprt.DXGKDDI_QUERY_DEVICE_DESCRIPTOR
title: DXGKDDI_QUERY_DEVICE_DESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 2c24670b-d331-4492-b2a2-4d99f9afd410
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

# DXGKDDI_QUERY_DEVICE_DESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_QUERY_DEVICE_DESCRIPTOR DxgkddiQueryDeviceDescriptor; 

// Definition

NTSTATUS DxgkddiQueryDeviceDescriptor 
(
	IN_CONST_PVOID MiniportDeviceContext
	IN_ULONG ChildUid
	INOUT_PDXGK_DEVICE_DESCRIPTOR DeviceDescriptor
)
{...}

DXGKDDI_QUERY_DEVICE_DESCRIPTOR PDXGKDDI_QUERY_DEVICE_DESCRIPTOR


```

## -parameters

### -param MiniportDeviceContext: 
### -param ChildUid: 
### -param DeviceDescriptor: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also