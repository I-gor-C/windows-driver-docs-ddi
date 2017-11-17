---
UID: NC.d3dkmddi.DXGKDDI_FLIPOVERLAY
title: DXGKDDI_FLIPOVERLAY
author: windows-driver-content
description: 
ms.assetid: ef3a89ec-d08d-446c-a75f-9e5042db1513
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

# DXGKDDI_FLIPOVERLAY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_FLIPOVERLAY DxgkddiFlipoverlay; 

// Definition

NTSTATUS DxgkddiFlipoverlay 
(
	IN_CONST_HANDLE hOverlay
	IN_CONST_PDXGKARG_FLIPOVERLAY pFlipOverlay
)
{...}

DXGKDDI_FLIPOVERLAY PDXGKDDI_FLIPOVERLAY


```

## -parameters

### -param hOverlay: 
### -param pFlipOverlay: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also