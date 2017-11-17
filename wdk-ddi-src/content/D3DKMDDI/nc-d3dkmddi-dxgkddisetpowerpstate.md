---
UID: NC.d3dkmddi.DXGKDDISETPOWERPSTATE
title: DXGKDDISETPOWERPSTATE
author: windows-driver-content
description: 
ms.assetid: 72610df6-b6f8-4654-ae67-55befb04705e
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

# DXGKDDISETPOWERPSTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDISETPOWERPSTATE Dxgkddisetpowerpstate; 

// Definition

NTSTATUS Dxgkddisetpowerpstate 
(
	IN_CONST_HANDLE DriverContext
	UINT ComponentIndex
	UINT RequestedComponentPState
)
{...}

DXGKDDISETPOWERPSTATE PDXGKDDISETPOWERPSTATE


```

## -parameters

### -param DriverContext: 
### -param ComponentIndex: 
### -param RequestedComponentPState: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also