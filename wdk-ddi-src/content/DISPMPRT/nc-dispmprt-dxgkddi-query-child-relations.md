---
UID: NC.dispmprt.DXGKDDI_QUERY_CHILD_RELATIONS
title: DXGKDDI_QUERY_CHILD_RELATIONS
author: windows-driver-content
description: 
ms.assetid: 51e1dfd2-412d-48a4-8008-1aa85bda676b
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

# DXGKDDI_QUERY_CHILD_RELATIONS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_QUERY_CHILD_RELATIONS DxgkddiQueryChildRelations; 

// Definition

NTSTATUS DxgkddiQueryChildRelations 
(
	CONST PVOID MiniportDeviceContext
	PDXGK_CHILD_DESCRIPTOR ChildRelations
	ULONG ChildRelationsSize
)
{...}

DXGKDDI_QUERY_CHILD_RELATIONS PDXGKDDI_QUERY_CHILD_RELATIONS


```

## -parameters

### -param MiniportDeviceContext: 
### -param ChildRelations: 
### -param ChildRelationsSize: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also