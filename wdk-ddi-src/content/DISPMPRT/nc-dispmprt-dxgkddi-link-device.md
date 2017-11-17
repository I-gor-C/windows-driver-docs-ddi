---
UID: NC.dispmprt.DXGKDDI_LINK_DEVICE
title: DXGKDDI_LINK_DEVICE
author: windows-driver-content
description: 
ms.assetid: 4ec1060a-1b66-4db3-ad26-6554310c9766
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

# DXGKDDI_LINK_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_LINK_DEVICE DxgkddiLinkDevice; 

// Definition

NTSTATUS DxgkddiLinkDevice 
(
	IN_CONST_PDEVICE_OBJECT PhysicalDeviceObject
	IN_CONST_PVOID MiniportDeviceContext
	INOUT_PLINKED_DEVICE LinkedDevice
)
{...}

DXGKDDI_LINK_DEVICE PDXGKDDI_LINK_DEVICE


```

## -parameters

### -param PhysicalDeviceObject: 
### -param MiniportDeviceContext: 
### -param LinkedDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also