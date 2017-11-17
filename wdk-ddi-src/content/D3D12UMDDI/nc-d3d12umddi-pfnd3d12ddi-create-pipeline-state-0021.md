---
UID: NC.d3d12umddi.PFND3D12DDI_CREATE_PIPELINE_STATE_0021
title: PFND3D12DDI_CREATE_PIPELINE_STATE_0021
author: windows-driver-content
description: The pfnCreatePipelineState callback function creates a pipeline state.
old-location: display\pfnd3d12ddi_create_pipeline_state_0021.htm
ms.assetid: 08C19E55-7DD7-4BDF-8C9A-A2E1B973AFEC
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnCreatePipelineState
req.alt-loc: D3d12umddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
req.iface: 
---

# PFND3D12DDI_CREATE_PIPELINE_STATE_0021 callback



## -description
<p>The <i>pfnCreatePipelineState</i> callback function creates a pipeline state.</p>


## -prototype

````
PFND3D12DDI_CREATE_PIPELINE_STATE_0021 pfnCreatePipelineState;

HRESULT APIENTRY* pfnCreatePipelineState(
             D3D12DDI_HDEVICE                       hDevice,
  _In_ const D3D12DDIARG_CREATE_PIPELINE_STATE_0010 *CreatePipelineState,
             D3D12DDI_HPIPELINESTATE                hPipelineState,
             D3D12DDI_HRTPIPELINESTATE              hRTPipelineState
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> 

<dd>
<p>The handle of a device. </p>
</dd>

### -param <i>CreatePipelineState</i> [in]

<dd>
<p>A value used to create a pipeline state.</p>
</dd>

### -param <i>hPipelineState</i> 

<dd>
<p>The handle of a pipeline state. </p>
</dd>

### -param <i>hRTPipelineState</i> 

<dd>
<p>The handle of the pipeline state for the driver to use when it calls back into the runtime.</p>
</dd>
</dl>

## -returns
<p>If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks
<p>Access this function by using the <a href="https://msdn.microsoft.com/4E4C3DB3-9C4C-4BBC-82C4-C5C41C0B818C">D3D12DDI_DEVICE_FUNCS_CORE_0021</a> structure.</p>

<p>Access this function by using the <a href="https://msdn.microsoft.com/4E4C3DB3-9C4C-4BBC-82C4-C5C41C0B818C">D3D12DDI_DEVICE_FUNCS_CORE_0021</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>