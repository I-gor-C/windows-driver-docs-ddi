---
UID: NC.dispmprt.DXGKDDI_SETGPUPARTITIONCOUNT
title: DXGKDDI_SETGPUPARTITIONCOUNT
author: windows-driver-content
description: 
ms.assetid: 312c52d2-d6f8-441a-b11d-5eecb1ab2a10
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

# DXGKDDI_SETGPUPARTITIONCOUNT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SETGPUPARTITIONCOUNT DxgkddiSetgpupartitioncount; 

// Definition

NTSTATUS DxgkddiSetgpupartitioncount 
(
	HANDLE Context
	DXGKARG_SETGPUPARTITIONCOUNT * pArgs
)
{...}

DXGKDDI_SETGPUPARTITIONCOUNT PDXGKDDI_SETGPUPARTITIONCOUNT


```

## -parameters

### -param Context: 
### -param pArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also