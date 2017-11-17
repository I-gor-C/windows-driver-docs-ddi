---
UID: NC.dispmprt.DXGKDDI_QUERY_INTERFACE
title: DXGKDDI_QUERY_INTERFACE
author: windows-driver-content
description: 
ms.assetid: f853ffdd-cea0-42cd-b9f5-8fb6f07cfdad
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

# DXGKDDI_QUERY_INTERFACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_QUERY_INTERFACE DxgkddiQueryInterface; 

// Definition

NTSTATUS DxgkddiQueryInterface 
(
	IN_CONST_PVOID MiniportDeviceContext
	IN_PQUERY_INTERFACE QueryInterface
)
{...}

DXGKDDI_QUERY_INTERFACE PDXGKDDI_QUERY_INTERFACE


```

## -parameters

### -param MiniportDeviceContext: 
### -param QueryInterface: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also