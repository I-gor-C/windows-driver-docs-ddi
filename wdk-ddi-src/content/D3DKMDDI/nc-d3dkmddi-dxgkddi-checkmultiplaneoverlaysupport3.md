---
UID: NC.d3dkmddi.DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3
title: DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3
author: windows-driver-content
description: 
ms.assetid: 18ae7521-4f58-41bf-83d1-8acc807f7edb
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

# DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 DxgkddiCheckmultiplaneoverlaysupport3; 

// Definition

NTSTATUS DxgkddiCheckmultiplaneoverlaysupport3 
(
	IN_CONST_HANDLE hAdapter
	IN_OUT_PDXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3 pCheckMultiPlaneOverlaySupport
)
{...}

DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 PDXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3


```

## -parameters

### -param hAdapter: 
### -param pCheckMultiPlaneOverlaySupport: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also