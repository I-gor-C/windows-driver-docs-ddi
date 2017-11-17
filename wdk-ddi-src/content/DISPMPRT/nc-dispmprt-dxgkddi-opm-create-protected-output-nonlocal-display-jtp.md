---
UID: NC.dispmprt.DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_NONLOCAL_DISPLAY_JTP
title: DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_NONLOCAL_DISPLAY_JTP
author: windows-driver-content
description: 
ms.assetid: 52189347-6017-4f17-8ec6-83e7969a1011
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

# DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_NONLOCAL_DISPLAY_JTP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_NONLOCAL_DISPLAY_JTP DxgkddiOpmCreateProtectedOutputNonlocalDisplayJtp; 

// Definition

NTSTATUS DxgkddiOpmCreateProtectedOutputNonlocalDisplayJtp 
(
	PVOID MiniportDeviceContext
	DXGKMDT_OPM_VIDEO_OUTPUT_SEMANTICS NewVideoOutputSemantics
	ULONG64 OPMEncoderContext
	DXGKMDT_OPM_ACTUAL_OUTPUT_FORMAT *pActualOutputFormat
	D3DDDI_VIDEO_PRESENT_TARGET_ID NonLocalOutputId
	PHANDLE NewProtectedOutputHandle
)
{...}

DXGKDDI_OPM_CREATE_PROTECTED_OUTPUT_NONLOCAL_DISPLAY_JTP 


```

## -parameters

### -param MiniportDeviceContext: 
### -param NewVideoOutputSemantics: 
### -param OPMEncoderContext: 
### -param *pActualOutputFormat: 
### -param NonLocalOutputId: 
### -param NewProtectedOutputHandle: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also