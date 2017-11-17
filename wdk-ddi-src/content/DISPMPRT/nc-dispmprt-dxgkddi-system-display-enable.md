---
UID: NC.dispmprt.DXGKDDI_SYSTEM_DISPLAY_ENABLE
title: DXGKDDI_SYSTEM_DISPLAY_ENABLE
author: windows-driver-content
description: 
ms.assetid: cd39f94d-e719-4b11-ab04-521f41a1df7a
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

# DXGKDDI_SYSTEM_DISPLAY_ENABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SYSTEM_DISPLAY_ENABLE DxgkddiSystemDisplayEnable; 

// Definition

NTSTATUS DxgkddiSystemDisplayEnable 
(
	PVOID MiniportDeviceContext
	D3DDDI_VIDEO_PRESENT_TARGET_ID TargetId
	PDXGKARG_SYSTEM_DISPLAY_ENABLE_FLAGS Flags
	UINT * Width
	UINT * Height
	D3DDDIFORMAT * ColorFormat
)
{...}

DXGKDDI_SYSTEM_DISPLAY_ENABLE PDXGKDDI_SYSTEM_DISPLAY_ENABLE


```

## -parameters

### -param MiniportDeviceContext: 
### -param TargetId: 
### -param Flags: 
### -param Width: 
### -param Height: 
### -param ColorFormat: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also