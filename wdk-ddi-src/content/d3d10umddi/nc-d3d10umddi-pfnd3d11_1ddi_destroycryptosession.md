---
UID : NC:d3d10umddi.PFND3D11_1DDI_DESTROYCRYPTOSESSION
title : PFND3D11_1DDI_DESTROYCRYPTOSESSION
author : windows-driver-content
description : Releases resources for the cryptographic session that were created through a call to the CreateCryptoSession function.
old-location : display\destroycryptosession1.htm
old-project : display
ms.assetid : 067eeba4-2914-4616-98c8-f163cbe5fae2
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SETRESULT_INFO, *PSETRESULT_INFO, SETRESULT_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnDestroyCryptoSession
req.alt-loc : D3d10umddi.h
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
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_DESTROYCRYPTOSESSION callback function
Releases resources for the cryptographic session that were created through a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createcryptosession.md">CreateCryptoSession</a> function.

## Syntax

```
PFND3D11_1DDI_DESTROYCRYPTOSESSION Pfnd3d111DdiDestroycryptosession;

void Pfnd3d111DdiDestroycryptosession(
  D3D10DDI_HDEVICE hDevice,
  D3D11_1DDI_HCRYPTOSESSION hCryptoSession
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`hCryptoSession`

A handle to the driver's private data for the cryptographic session. This handle was created by the Direct3D runtime and passed to the driver in the call to <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createcryptosession.md">CreateCryptoSession</a>.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |