---
UID: NC.d3dkmddi.DXGKDDI_VIDPNTOPOLOGY_REMOVEPATH
title: DXGKDDI_VIDPNTOPOLOGY_REMOVEPATH
author: windows-driver-content
description: The pfnRemovePath function removes a video present path to a specified VidPN topology object.
old-location: display\dxgk_vidpntopology_interface_pfnremovepath.htm
old-project: display
ms.assetid: 463973e0-c443-417a-86ff-0b78773d40cc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnRemovePath
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGKDDI_VIDPNTOPOLOGY_REMOVEPATH callback



## -description
<p>The <b>pfnRemovePath</b> function removes a video present path to a specified VidPN topology object.</p>


## -prototype

````
DXGKDDI_VIDPNTOPOLOGY_REMOVEPATH pfnRemovePath;

NTSTATUS APIENTRY pfnRemovePath(
  _In_ const D3DKMDT_HVIDPNTOPOLOGY         hVidPnTopology,
  _In_ const D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId,
  _In_ const D3DDDI_VIDEO_PRESENT_TARGET_ID VidPnTargetId
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPnTopology</i> [in]

<dd>
<p>[in] A handle to a VidPN topology object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-gettopology.md">pfnGetTopology</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562108">DXGK_VIDPN_INTERFACE</a> interface.</p>
</dd>

### -param <i>VidPnSourceId</i> [in]

<dd>
<p>[in] An integer that identifies a VidPN source path.</p>
</dd>

### -param <i>VidPnTargetId</i> [in]

<dd>
<p>[in] An integer that identifies a VidPN target path.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnRemovePath</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The specified video present path has been successfully removed from this VidPN topology object.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_SOURCE</b></dt>
</dl><p>The VidPN source identifier supplied in <i>VidPnSourceId </i>is invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET</b></dt>
</dl><p>The VidPN target identifier supplied in <i>VidPnTargetId </i>is invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_TOPOLOGY</b></dt>
</dl><p>The handle supplied in <i>hVidPnTopology </i>is invalid.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The path cannot be removed in the context of the current DDI call.</p>

<p> </p>

## -remarks
<p>The D3DKMDT_HVIDPNTOPOLOGY data type is defined in<i> D3dkmdt.h</i>.</p>

<p>The D3DKMDT_HVIDPNTOPOLOGY data type is defined in<i> D3dkmdt.h</i>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>