---
UID : NC:d3d12umddi.PFND3D12DDI_CREATE_PIPELINE_STATE_0033
title : PFND3D12DDI_CREATE_PIPELINE_STATE_0033
author : windows-driver-content
description : Used to create a pipeline state.
old-location : display\pfnd3d12ddi_create_pipeline_state_0033.htm
old-project : display
ms.assetid : F8255544-D5B6-4692-BDC0-EF5A2B856153
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
req.alt-api : PFND3D12DDI_CREATE_PIPELINE_STATE_0033
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


# PFND3D12DDI_CREATE_PIPELINE_STATE_0033 callback function
Used to create a pipeline state.

## Syntax

```
PFND3D12DDI_CREATE_PIPELINE_STATE_0033 Pfnd3d12ddiCreatePipelineState0033;

HRESULT Pfnd3d12ddiCreatePipelineState0033(
   D3D12DDI_HDEVICE,
  CONST D3D12DDIARG_CREATE_PIPELINE_STATE_0033 *,
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