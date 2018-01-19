---
UID : NC:d3d12umddi.PFND3D12DDI_CREATEVIDEODECODER_0032
title : PFND3D12DDI_CREATEVIDEODECODER_0032
author : windows-driver-content
description : Used to create a video decoder.
old-location : display\pfnd3d12ddi_createvideodecoder_0032.htm
old-project : display
ms.assetid : F3E8FB7A-A25B-47CE-8B14-9AE8737930D4
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3D11_1DDI_GETCAPTUREHANDLEDATA, D3D11_1DDI_GETCAPTUREHANDLEDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d12umddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PFND3D12DDI_CREATEVIDEODECODER_0032
req.alt-loc : d3d12umddi.h
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


# PFND3D12DDI_CREATEVIDEODECODER_0032 callback function
Used to create a video decoder.

## Syntax

```
PFND3D12DDI_CREATEVIDEODECODER_0032 Pfnd3d12ddiCreatevideodecoder0032;

HRESULT Pfnd3d12ddiCreatevideodecoder0032(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_CREATE_VIDEO_DECODER_0032 *pArgs,
  D3D12DDI_HVIDEODECODER_0020 hDrvVideoDecoder
)
{...}
```

## Parameters

`hDrvDevice`

The hardware device being processed.

`*pArgs`



`hDrvVideoDecoder`

The video decoder.


## Return Value

Returns STATUS_SUCCESS if completed successfully.


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