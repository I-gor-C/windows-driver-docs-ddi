---
UID: NC:d3d12umddi.PFND3D12DDI_CREATEVIDEODECODERHEAP_0032
title: PFND3D12DDI_CREATEVIDEODECODERHEAP_0032
author: windows-driver-content
description: Used to create a video decoder heap.
old-location: display\pfnd3d12ddi_createvideodecoderheap_0032.htm
old-project: display
ms.assetid: EC383086-CE8F-4387-8F92-BEC8215A97DA
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.pfnd3d12ddi_createvideodecoderheap_0032, PFND3D12DDI_CREATEVIDEODECODERHEAP_0032 callback function [Display Devices], PFND3D12DDI_CREATEVIDEODECODERHEAP_0032, d3d12umddi/PFND3D12DDI_CREATEVIDEODECODERHEAP_0032
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3d12umddi.h
apiname:
-	PFND3D12DDI_CREATEVIDEODECODERHEAP_0032
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_CREATEVIDEODECODERHEAP_0032 callback function
Used to create a video decoder heap.

## Syntax

```
PFND3D12DDI_CREATEVIDEODECODERHEAP_0032 Pfnd3d12ddiCreatevideodecoderheap0032;

HRESULT Pfnd3d12ddiCreatevideodecoderheap0032(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032 *,
  D3D12DDI_HVIDEODECODERHEAP_0032 hDrvVideoDecoderHeap
)
{...}
```

## Parameters

`hDrvDevice`

The hardware device being processed.

`*`



`hDrvVideoDecoderHeap`

The video decoder heap.


## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h |