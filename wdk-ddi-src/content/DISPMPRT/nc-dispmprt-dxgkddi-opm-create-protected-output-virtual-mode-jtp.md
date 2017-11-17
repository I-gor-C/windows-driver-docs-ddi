---
UID: NC.dispmprt.DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_VIRTUAL_MODE_JTP
title: DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_VIRTUAL_MODE_JTP
author: windows-driver-content
description: 
ms.assetid: e1167f58-f02a-4132-974e-50ed888516f4
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

# DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_VIRTUAL_MODE_JTP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_VIRTUAL_MODE_JTP DxgkddiOpmCreateProtectedOutputVirtualModeJtp; 

// Definition

NTSTATUS DxgkddiOpmCreateProtectedOutputVirtualModeJtp 
(
	PVOID MiniportDeviceContext
	D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId
	DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS NewVideoOutputSemantics
	DXGKMDT_OPM_ACTUAL_OUTPUT_FORMAT *pActualOutputFormat
	PHANDLE NewProtectedOutputHandle
)
{...}

DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_VIRTUAL_MODE_JTP 


```

## -parameters

### -param MiniportDeviceContext: 
### -param VidPnTargetId: 
### -param NewVideoOutputSemantics: 
### -param *pActualOutputFormat: 
### -param NewProtectedOutputHandle: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also