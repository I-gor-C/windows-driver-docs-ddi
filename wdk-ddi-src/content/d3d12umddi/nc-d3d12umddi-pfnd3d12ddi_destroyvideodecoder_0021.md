---
UID : NC:d3d12umddi.PFND3D12DDI_DESTROYVIDEODECODER_0021
title : PFND3D12DDI_DESTROYVIDEODECODER_0021
author : windows-driver-content
description : Destroys the video decoder.
old-location : display\pfnd3d12ddi_destroyvideodecoder_.htm
old-project : display
ms.assetid : 97028FEB-A3C2-4C2F-B64E-07024BC3C382
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3D11_1DDI_GETCAPTUREHANDLEDATA, D3D11_1DDI_GETCAPTUREHANDLEDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d12umddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PFND3D12DDI_DESTROYVIDEODECODER_0021
req.alt-loc : D3d12umddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_DESTROYVIDEODECODER_0021 callback function
Destroys the video decoder.

## Syntax

```
PFND3D12DDI_DESTROYVIDEODECODER_0021 Pfnd3d12ddiDestroyvideodecoder0021;

void Pfnd3d12ddiDestroyvideodecoder0021(
  D3D12DDI_HDEVICE hDrvDevice,
  D3D12DDI_HVIDEODECODER_0020 hDrvVideoDecoder
)
{...}
```

## Parameters

`hDrvDevice`



`hDrvVideoDecoder`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |