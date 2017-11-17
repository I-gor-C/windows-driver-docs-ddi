---
UID: NC.d3dkmddi.DXGKDDI_DESTROYPROTECTEDSESSION
title: DXGKDDI_DESTROYPROTECTEDSESSION
author: windows-driver-content
description: 
ms.assetid: 90a770f9-700d-4774-8597-d2f03a106010
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

# DXGKDDI_DESTROYPROTECTEDSESSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_DESTROYPROTECTEDSESSION DxgkddiDestroyprotectedsession; 

// Definition

NTSTATUS DxgkddiDestroyprotectedsession 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_HANDLE hProtectedSession
)
{...}

DXGKDDI_DESTROYPROTECTEDSESSION PDXGKDDI_DESTROYPROTECTEDSESSION


```

## -parameters

### -param hAdapter: 
### -param hProtectedSession: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also