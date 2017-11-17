---
UID: NC.dispmprt.DXGKDDI_STOP_DEVICE_AND_RELEASE_POST_DISPLAY_OWNERSHIP
title: DXGKDDI_STOP_DEVICE_AND_RELEASE_POST_DISPLAY_OWNERSHIP
author: windows-driver-content
description: 
ms.assetid: 12523e17-9681-4c64-b847-35d3c7214e89
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

# DXGKDDI_STOP_DEVICE_AND_RELEASE_POST_DISPLAY_OWNERSHIP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_STOP_DEVICE_AND_RELEASE_POST_DISPLAY_OWNERSHIP DxgkddiStopDeviceAndReleasePostDisplayOwnership; 

// Definition

NTSTATUS DxgkddiStopDeviceAndReleasePostDisplayOwnership 
(
	PVOID MiniportDeviceContext
	D3DDDI_VIDEO_PRESENT_TARGET_ID TargetId
	PDXGK_DISPLAY_INFORMATION DisplayInfo
)
{...}

DXGKDDI_STOP_DEVICE_AND_RELEASE_POST_DISPLAY_OWNERSHIP PDXGKDDI_STOP_DEVICE_AND_RELEASE_POST_DISPLAY_OWNERSHIP


```

## -parameters

### -param MiniportDeviceContext: 
### -param TargetId: 
### -param DisplayInfo: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also