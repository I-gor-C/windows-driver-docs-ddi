---
UID: NC.d3dkmddi.DXGKDDI_PREEMPTCOMMAND
title: DXGKDDI_PREEMPTCOMMAND
author: windows-driver-content
description: 
ms.assetid: ab21de26-99a8-4c9f-b2d5-05473e16882e
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

# DXGKDDI_PREEMPTCOMMAND callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_PREEMPTCOMMAND DxgkddiPreemptcommand; 

// Definition

NTSTATUS DxgkddiPreemptcommand 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_PDXGKARG_PREEMPTCOMMAND pPreemptCommand
)
{...}

DXGKDDI_PREEMPTCOMMAND PDXGKDDI_PREEMPTCOMMAND


```

## -parameters

### -param hAdapter: 
### -param pPreemptCommand: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also