---
UID: NC.d3dkmddi.DXGKDDI_CREATEPROTECTEDSESSION
title: DXGKDDI_CREATEPROTECTEDSESSION
author: windows-driver-content
description: 
ms.assetid: 968a5dcf-61de-43b1-89fa-648c7e4083e4
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

# DXGKDDI_CREATEPROTECTEDSESSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_CREATEPROTECTEDSESSION DxgkddiCreateprotectedsession; 

// Definition

NTSTATUS DxgkddiCreateprotectedsession 
(
	IN_CONST_HANDLE hAdapter
	INOUT_PDXGKARG_CREATEPROTECTEDSESSION pCreateProtectedSession
)
{...}

DXGKDDI_CREATEPROTECTEDSESSION PDXGKDDI_CREATEPROTECTEDSESSION


```

## -parameters

### -param hAdapter: 
### -param pCreateProtectedSession: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also