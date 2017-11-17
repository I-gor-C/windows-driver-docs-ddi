---
UID: NC.d3dkmddi.DXGKDDI_RESTARTFROMTIMEOUT
title: DXGKDDI_RESTARTFROMTIMEOUT
author: windows-driver-content
description: 
ms.assetid: 720015cb-9567-4ffa-9ce0-d16025c55361
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

# DXGKDDI_RESTARTFROMTIMEOUT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_RESTARTFROMTIMEOUT DxgkddiRestartfromtimeout; 

// Definition

NTSTATUS DxgkddiRestartfromtimeout 
(
	IN_CONST_HANDLE hAdapter
)
{...}

DXGKDDI_RESTARTFROMTIMEOUT PDXGKDDI_RESTARTFROMTIMEOUT


```

## -parameters

### -param hAdapter: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also