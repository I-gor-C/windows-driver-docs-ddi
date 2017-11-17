---
UID: NC.dispmprt.DXGKDDI_REMOVE_DEVICE
title: DXGKDDI_REMOVE_DEVICE
author: windows-driver-content
description: 
ms.assetid: e3d80a3b-c583-4f55-9c2f-10f8ddc5dfcc
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

# DXGKDDI_REMOVE_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_REMOVE_DEVICE DxgkddiRemoveDevice; 

// Definition

NTSTATUS DxgkddiRemoveDevice 
(
	IN_CONST_PVOID MiniportDeviceContext
)
{...}

DXGKDDI_REMOVE_DEVICE PDXGKDDI_REMOVE_DEVICE


```

## -parameters

### -param MiniportDeviceContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also