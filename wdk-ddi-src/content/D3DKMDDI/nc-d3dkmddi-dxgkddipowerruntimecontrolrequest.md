---
UID: NC.d3dkmddi.DXGKDDIPOWERRUNTIMECONTROLREQUEST
title: DXGKDDIPOWERRUNTIMECONTROLREQUEST
author: windows-driver-content
description: 
ms.assetid: aa97b7bc-c013-4fc7-bea0-70a7aef8c55a
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

# DXGKDDIPOWERRUNTIMECONTROLREQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDIPOWERRUNTIMECONTROLREQUEST Dxgkddipowerruntimecontrolrequest; 

// Definition

NTSTATUS Dxgkddipowerruntimecontrolrequest 
(
	IN_CONST_HANDLE DriverContext
	IN LPCGUID PowerControlCode
	IN OPTIONAL PVOID InBuffer
	IN SIZE_T InBufferSize
	OUT OPTIONAL PVOID OutBuffer
	IN SIZE_T OutBufferSize
	OUT OPTIONAL PSIZE_T BytesReturned
)
{...}

DXGKDDIPOWERRUNTIMECONTROLREQUEST PDXGKDDIPOWERRUNTIMECONTROLREQUEST


```

## -parameters

### -param DriverContext: 
### -param PowerControlCode: 
### -param InBuffer: 
### -param InBufferSize: 
### -param OutBuffer: 
### -param OutBufferSize: 
### -param BytesReturned: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also