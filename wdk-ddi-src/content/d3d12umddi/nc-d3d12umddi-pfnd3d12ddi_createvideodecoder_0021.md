---
UID : NC:d3d12umddi.PFND3D12DDI_CREATEVIDEODECODER_0021
title : PFND3D12DDI_CREATEVIDEODECODER_0021
author : windows-driver-content
description : The pfnCreateVideoDecoder callback function creates a video decoder.
old-location : display\pfnd3d12ddi_createvideodecoder.htm
old-project : display
ms.assetid : 5E0B6A5A-FA6E-4722-B442-FE74437224B3
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
req.alt-api : pfnCreateVideoDecoder
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


# PFND3D12DDI_CREATEVIDEODECODER_0021 callback function
The <i>pfnCreateVideoDecoder</i> callback function creates a video decoder.

## Syntax

```
PFND3D12DDI_CREATEVIDEODECODER_0021 Pfnd3d12ddiCreatevideodecoder0021;

HRESULT Pfnd3d12ddiCreatevideodecoder0021(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_CREATE_VIDEO_DECODER_0021 *pArgs,
  D3D12DDI_HVIDEODECODER_0020 hDrvVideoDecoder
)
{...}
```

## Parameters

`hDrvDevice`



`*pArgs`



`hDrvVideoDecoder`

The handle of a driver video decoder.


## Return Value

If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


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