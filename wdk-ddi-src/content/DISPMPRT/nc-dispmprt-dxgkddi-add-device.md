---
UID: NC.dispmprt.DXGKDDI_ADD_DEVICE
title: DXGKDDI_ADD_DEVICE
author: windows-driver-content
description: 
ms.assetid: 2d1f2086-0106-4295-9ad2-a04f92efc4ca
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

# DXGKDDI_ADD_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_ADD_DEVICE DxgkddiAddDevice; 

// Definition

NTSTATUS DxgkddiAddDevice 
(
	IN_CONST_PDEVICE_OBJECT PhysicalDeviceObject
	OUT_PPVOID MiniportDeviceContext
)
{...}

DXGKDDI_ADD_DEVICE PDXGKDDI_ADD_DEVICE


```

## -parameters

### -param PhysicalDeviceObject: 
### -param MiniportDeviceContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also