---
UID: NC.dispmprt.DXGKDDI_RESET_DEVICE
title: DXGKDDI_RESET_DEVICE
author: windows-driver-content
description: 
ms.assetid: b10c260a-23fc-4cff-903d-106cbbb26749
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

# DXGKDDI_RESET_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_RESET_DEVICE DxgkddiResetDevice; 

// Definition

VOID DxgkddiResetDevice 
(
	IN_CONST_PVOID MiniportDeviceContext
)
{...}

DXGKDDI_RESET_DEVICE PDXGKDDI_RESET_DEVICE


```

## -parameters

### -param MiniportDeviceContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also