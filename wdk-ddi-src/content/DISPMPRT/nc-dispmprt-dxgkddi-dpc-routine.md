---
UID: NC.dispmprt.DXGKDDI_DPC_ROUTINE
title: DXGKDDI_DPC_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 1b575280-5aa0-452e-a4bf-eb67f701d020
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

# DXGKDDI_DPC_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_DPC_ROUTINE DxgkddiDpcRoutine; 

// Definition

VOID DxgkddiDpcRoutine 
(
	IN_CONST_PVOID MiniportDeviceContext
)
{...}

DXGKDDI_DPC_ROUTINE PDXGKDDI_DPC_ROUTINE


```

## -parameters

### -param MiniportDeviceContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also