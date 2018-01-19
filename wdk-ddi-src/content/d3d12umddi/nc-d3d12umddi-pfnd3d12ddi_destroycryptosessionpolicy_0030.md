---
UID : NC:d3d12umddi.PFND3D12DDI_DESTROYCRYPTOSESSIONPOLICY_0030
title : PFND3D12DDI_DESTROYCRYPTOSESSIONPOLICY_0030
author : windows-driver-content
description : Used to destroy a crypto session.
old-location : display\pfnd3d12ddi_destroycryptosessionpolicy_0030.htm
old-project : display
ms.assetid : D02ED6F5-1976-4EAE-A648-0F8ED32B77C6
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
req.alt-api : PFND3D12DDI_DESTROYCRYPTOSESSIONPOLICY_0030
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


# PFND3D12DDI_DESTROYCRYPTOSESSIONPOLICY_0030 callback function
Used to destroy a crypto session.

## Syntax

```
PFND3D12DDI_DESTROYCRYPTOSESSIONPOLICY_0030 Pfnd3d12ddiDestroycryptosessionpolicy0030;

void Pfnd3d12ddiDestroycryptosessionpolicy0030(
  D3D12DDI_HDEVICE hDrvDevice,
  D3D12DDI_HCRYPTOSESSIONPOLICY_0030 hDrvCryptoSessionPolicy
)
{...}
```

## Parameters

`hDrvDevice`

The hardware device being processed.

`hDrvCryptoSessionPolicy`

The crypto session policy.


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