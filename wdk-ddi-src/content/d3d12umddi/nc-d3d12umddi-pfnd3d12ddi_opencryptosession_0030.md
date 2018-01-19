---
UID : NC:d3d12umddi.PFND3D12DDI_OPENCRYPTOSESSION_0030
title : PFND3D12DDI_OPENCRYPTOSESSION_0030
author : windows-driver-content
description : Used to open a crypto session.
old-location : display\pfnd3d12ddi_opencryptosession_0030.htm
old-project : display
ms.assetid : 37A4A739-019E-41E6-B7B8-8F61E915C845
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
req.alt-api : PFND3D12DDI_OPENCRYPTOSESSION_0030
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


# PFND3D12DDI_OPENCRYPTOSESSION_0030 callback function
Used to open a crypto session.

## Syntax

```
PFND3D12DDI_OPENCRYPTOSESSION_0030 Pfnd3d12ddiOpencryptosession0030;

HRESULT Pfnd3d12ddiOpencryptosession0030(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_OPEN_CRYPTO_SESSION_0030 *pArgs,
  D3D12DDI_HCRYPTOSESSION_0030 hDrvCryptoSession
)
{...}
```

## Parameters

`hDrvDevice`

The hardware device being processed.

`*pArgs`



`hDrvCryptoSession`

The crypto session.


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