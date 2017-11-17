---
UID: NC.d3dkmddi.DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3
title: DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3
author: windows-driver-content
description: 
ms.assetid: c48d1cc7-8f37-4f2e-be68-465416186ff8
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

# DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3 DxgkddiSetvidpnsourceaddresswithmultiplaneoverlay3; 

// Definition

NTSTATUS DxgkddiSetvidpnsourceaddresswithmultiplaneoverlay3 
(
	IN_CONST_HANDLE hAdapter
	IN_OUT_PDXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3 pSetVidPnSourceAddressWithMultiPlaneOverlay
)
{...}

DXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3 PDXGKDDI_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3


```

## -parameters

### -param hAdapter: 
### -param pSetVidPnSourceAddressWithMultiPlaneOverlay: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also