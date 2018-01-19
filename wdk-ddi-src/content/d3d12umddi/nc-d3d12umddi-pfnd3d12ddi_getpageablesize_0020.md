---
UID : NC:d3d12umddi.PFND3D12DDI_GETPAGEABLESIZE_0020
title : PFND3D12DDI_GETPAGEABLESIZE_0020
author : windows-driver-content
description : The pfnGetPageableSize callback function gets the pageable size.
old-location : display\pfnd3d12ddi_getpageablesize.htm
old-project : display
ms.assetid : DC215186-A216-4C34-AE9A-A487178B34C0
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
req.alt-api : pfnGetPageableSize
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


# PFND3D12DDI_GETPAGEABLESIZE_0020 callback function
The <i>pfnGetPageableSize</i> callback function gets the pageable size.

## Syntax

```
PFND3D12DDI_GETPAGEABLESIZE_0020 Pfnd3d12ddiGetpageablesize0020;

UINT64 Pfnd3d12ddiGetpageablesize0020(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_GET_PAGEABLE_SIZE_0020 *pArgs
)
{...}
```

## Parameters

`hDrvDevice`



`*pArgs`




## Return Value

None


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