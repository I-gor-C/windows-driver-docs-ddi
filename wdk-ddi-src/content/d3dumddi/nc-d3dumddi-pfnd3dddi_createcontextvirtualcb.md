---
UID : NC:d3dumddi.PFND3DDDI_CREATECONTEXTVIRTUALCB
title : PFND3DDDI_CREATECONTEXTVIRTUALCB
author : windows-driver-content
description : pfnCreateContextVirtualCb should be used with contexts that support virtual addressing.
old-location : display\pfncreatecontextvirtualcb.htm
old-project : display
ms.assetid : 7787FEDF-E18C-4120-A073-A13933856F57
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DXGK_PTE, DXGK_PTE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnCreateContextVirtualCb
req.alt-loc : d3dumddi.h
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
req.typenames : DXGK_PTE
---


# PFND3DDDI_CREATECONTEXTVIRTUALCB callback function
<b>pfnCreateContextVirtualCb</b> should be used with contexts that support virtual addressing.

## Syntax

```
PFND3DDDI_CREATECONTEXTVIRTUALCB Pfnd3dddiCreatecontextvirtualcb;

HRESULT Pfnd3dddiCreatecontextvirtualcb(
  HANDLE hDevice,
  D3DDDICB_CREATECONTEXTVIRTUAL *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device.

`*`




## Return Value

<dl>
<dt><b>S_OK</b></dt>
</dl>The context was successfully created.
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
        Could not allocate memory that was required for the operation to complete.
<dl>
<dt><b>E_INVALIDARG</b></dt>
</dl>Parameters were validated and determined to be incorrect.

 

This function might also return other <b>HRESULT</b> values.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |