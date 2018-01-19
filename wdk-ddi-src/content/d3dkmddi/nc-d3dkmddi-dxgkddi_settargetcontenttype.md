---
UID : NC:d3dkmddi.DXGKDDI_SETTARGETCONTENTTYPE
title : DXGKDDI_SETTARGETCONTENTTYPE
author : windows-driver-content
description : Passes the content type for which the driver should optimize on the specified target.
old-location : display\dxgkddi_settargetcontenttype.htm
old-project : display
ms.assetid : 7639BF7B-6219-4490-953F-80E76CDFBAAA
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dkmddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGKDDI_SETTARGETCONTENTTYPE
req.alt-loc : d3dkmddi.h
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
req.typenames : DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_SETTARGETCONTENTTYPE function
Passes the content type for which the driver should optimize on the specified target.  <div class="alert"><b>Note</b>  This is functionally equivalent to the DxgkDdi_UpdateActiveVidPnPresentPath in previous WDDM versions if only the D3DKMDT_VIDPN_PRESENT_PATH_CONTENT field is changed.</div>
<div> </div>

## Syntax

```
DXGKDDI_SETTARGETCONTENTTYPE DxgkddiSettargetcontenttype;

NTSTATUS DxgkddiSettargetcontenttype(
  IN_CONST_HANDLE hAdapter,
  IN_CONST_PDXGKARG_SETTARGETCONTENTTYPE pSetTargetContentTypeArg
)
{...}
```

## Parameters

`hAdapter`

A handle that identifies the adapter.

`pSetTargetContentTypeArg`

A pointer to a <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_settargetcontenttype.md">DXGKARG_SETTARGETCONTENTTYPE</a> structure that provides the target to be modified and the new type of content being displayed on it.


## Return Value

If this routine succeeds, it returns STATUS_SUCCESS.

## Remarks

This is an optional DDI, so the function pointer in DRIVER_INITIALIZATION_DATA should be set to null if the DDI is not implemented for every adapter supported by the driver.
This function is always called at PASSIVE level so the supporting code should be made pageable.
</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |