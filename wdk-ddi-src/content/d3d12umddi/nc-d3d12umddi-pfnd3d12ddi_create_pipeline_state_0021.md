---
UID : NC:d3d12umddi.PFND3D12DDI_CREATE_PIPELINE_STATE_0021
title : PFND3D12DDI_CREATE_PIPELINE_STATE_0021
author : windows-driver-content
description : The pfnCreatePipelineState callback function creates a pipeline state.
old-location : display\pfnd3d12ddi_create_pipeline_state_0021.htm
old-project : display
ms.assetid : 08C19E55-7DD7-4BDF-8C9A-A2E1B973AFEC
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3D11_1DDI_GETCAPTUREHANDLEDATA, D3D11_1DDI_GETCAPTUREHANDLEDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d12umddi.h
req.include-header : D3d12umddi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnCreatePipelineState
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


# PFND3D12DDI_CREATE_PIPELINE_STATE_0021 callback function
The <i>pfnCreatePipelineState</i> callback function creates a pipeline state.

## Syntax

```
PFND3D12DDI_CREATE_PIPELINE_STATE_0021 Pfnd3d12ddiCreatePipelineState0021;

HRESULT Pfnd3d12ddiCreatePipelineState0021(
   D3D12DDI_HDEVICE,
  CONST D3D12DDIARG_CREATE_PIPELINE_STATE_0010 *,
   D3D12DDI_HPIPELINESTATE,
   D3D12DDI_HRTPIPELINESTATE
)
{...}
```

## Parameters

`D3D12DDI_HDEVICE`



`*`



`D3D12DDI_HPIPELINESTATE`



`D3D12DDI_HRTPIPELINESTATE`




## Return Value

If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.

## Remarks

Access this function by using the <a href="..\d3d12umddi\ns-d3d12umddi-d3d12ddi_device_funcs_core_0021.md">D3D12DDI_DEVICE_FUNCS_CORE_0021</a> structure.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |