---
UID: NC.dispmprt.DXGKDDI_STOP_DEVICE
title: DXGKDDI_STOP_DEVICE
author: windows-driver-content
description: 
ms.assetid: 74f825c2-db55-4c02-99cc-6592a169efd1
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

# DXGKDDI_STOP_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_STOP_DEVICE DxgkddiStopDevice; 

// Definition

NTSTATUS DxgkddiStopDevice 
(
	IN_CONST_PVOID MiniportDeviceContext
)
{...}

DXGKDDI_STOP_DEVICE PDXGKDDI_STOP_DEVICE


```

## -parameters

### -param MiniportDeviceContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also