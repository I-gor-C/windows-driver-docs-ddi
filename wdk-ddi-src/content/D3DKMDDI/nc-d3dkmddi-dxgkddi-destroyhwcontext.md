---
UID: NC.d3dkmddi.DXGKDDI_DESTROYHWCONTEXT
title: DXGKDDI_DESTROYHWCONTEXT
author: windows-driver-content
description: 
ms.assetid: 40210321-d672-42a9-8f2d-0a1e2f866d5c
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

# DXGKDDI_DESTROYHWCONTEXT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_DESTROYHWCONTEXT DxgkddiDestroyhwcontext; 

// Definition

NTSTATUS DxgkddiDestroyhwcontext 
(
	IN_CONST_HANDLE hHwContext
)
{...}

DXGKDDI_DESTROYHWCONTEXT PDXGKDDI_DESTROYHWCONTEXT


```

## -parameters

### -param hHwContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also