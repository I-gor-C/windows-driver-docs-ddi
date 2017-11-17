---
UID: NC.dispmprt.DXGKDDI_INTERRUPT_ROUTINE
title: DXGKDDI_INTERRUPT_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 7291a531-0c17-4af6-abeb-13f6dc5d41d3
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

# DXGKDDI_INTERRUPT_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_INTERRUPT_ROUTINE DxgkddiInterruptRoutine; 

// Definition

BOOLEAN DxgkddiInterruptRoutine 
(
	IN_CONST_PVOID MiniportDeviceContext
	IN_ULONG MessageNumber
)
{...}

DXGKDDI_INTERRUPT_ROUTINE PDXGKDDI_INTERRUPT_ROUTINE


```

## -parameters

### -param MiniportDeviceContext: 
### -param MessageNumber: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also