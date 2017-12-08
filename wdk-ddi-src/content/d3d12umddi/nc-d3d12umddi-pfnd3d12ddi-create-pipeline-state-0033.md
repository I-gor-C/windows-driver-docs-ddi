---
UID: NC.d3d12umddi.PFND3D12DDI_CREATE_PIPELINE_STATE_0033
title: PFND3D12DDI_CREATE_PIPELINE_STATE_0033
author: windows-driver-content
description: Used to create a pipeline state.
old-location: display\pfnd3d12ddi_create_pipeline_state_0033.htm
old-project: display
ms.assetid: F8255544-D5B6-4692-BDC0-EF5A2B856153
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3D12DDI_CREATE_PIPELINE_STATE_0033
req.alt-loc: d3d12umddi.h
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
req.iface: 
---

# PFND3D12DDI_CREATE_PIPELINE_STATE_0033 callback



## -description
<p>Used to create a pipeline state.</p>


## -prototype

````
HRESULT APIENTRY* PFND3D12DDI_CREATE_PIPELINE_STATE_0033(
             D3D12DDI_HDEVICE                       d3d12ddi_hdevice,
  _In_ const D3D12DDIARG_CREATE_PIPELINE_STATE_0033 *d3d12ddiarg_create_pipeline_state_0033,
             D3D12DDI_HPIPELINESTATE                d3d12ddi_hpipelinestate,
             D3D12DDI_HRTPIPELINESTATE              d3d12ddi_hrtpipelinestate
);
````


## -parameters
<dl>

### -param d3d12ddi_hdevice 

<dd>
<p>The hardware device being processed.</p>
</dd>

### -param d3d12ddiarg_create_pipeline_state_0033 [in]

<dd>
<p>The arguments used to create a pipeline state.</p>
</dd>

### -param d3d12ddi_hpipelinestate 

<dd>
<p>Used to create a pipeline state.</p>
</dd>

### -param d3d12ddi_hrtpipelinestate 

<dd>
<p>Used to create a pipeline state.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if completed successfully.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>