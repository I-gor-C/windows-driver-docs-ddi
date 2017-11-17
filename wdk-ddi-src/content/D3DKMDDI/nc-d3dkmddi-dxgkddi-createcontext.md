---
UID: NC.d3dkmddi.DXGKDDI_CREATECONTEXT
title: DXGKDDI_CREATECONTEXT
author: windows-driver-content
description: 
ms.assetid: cabd1bd1-abac-48f3-bcdc-d06d205dac94
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

# DXGKDDI_CREATECONTEXT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_CREATECONTEXT DxgkddiCreatecontext; 

// Definition

NTSTATUS DxgkddiCreatecontext 
(
	IN_CONST_HANDLE hDevice
	INOUT_PDXGKARG_CREATECONTEXT pCreateContext
)
{...}

DXGKDDI_CREATECONTEXT PDXGKDDI_CREATECONTEXT


```

## -parameters

### -param hDevice: 
### -param pCreateContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also