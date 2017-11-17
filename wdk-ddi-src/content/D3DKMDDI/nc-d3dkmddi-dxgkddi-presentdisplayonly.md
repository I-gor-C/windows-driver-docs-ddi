---
UID: NC.d3dkmddi.DXGKDDI_PRESENTDISPLAYONLY
title: DXGKDDI_PRESENTDISPLAYONLY
author: windows-driver-content
description: 
ms.assetid: 631e7044-9b80-47e8-afbd-0d1fc4eec2b2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
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

# DXGKDDI_PRESENTDISPLAYONLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_PRESENTDISPLAYONLY DxgkddiPresentdisplayonly; 

// Definition

NTSTATUS DxgkddiPresentdisplayonly 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_PDXGKARG_PRESENT_DISPLAYONLY pPresentDisplayOnly
)
{...}

DXGKDDI_PRESENTDISPLAYONLY PDXGKDDI_PRESENTDISPLAYONLY


```

## -parameters

### -param hAdapter: 
### -param pPresentDisplayOnly: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also