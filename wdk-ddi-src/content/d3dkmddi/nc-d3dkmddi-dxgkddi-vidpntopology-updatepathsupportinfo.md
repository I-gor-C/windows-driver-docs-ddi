---
UID: NC.d3dkmddi.DXGKDDI_VIDPNTOPOLOGY_UPDATEPATHSUPPORTINFO
title: DXGKDDI_VIDPNTOPOLOGY_UPDATEPATHSUPPORTINFO
author: windows-driver-content
description: The pfnUpdatePathSupportInfo function updates the transformation and copy protection support of a particular path in a specified VidPN topology.
old-location: display\dxgk_vidpntopology_interface_pfnupdatepathsupportinfo.htm
old-project: display
ms.assetid: affe9ab2-49ef-4284-b441-49c311158827
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
req.alt-api: pfnUpdatePathSupportInfo
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

# DXGKDDI_VIDPNTOPOLOGY_UPDATEPATHSUPPORTINFO callback



## -description
<p>The <b>pfnUpdatePathSupportInfo</b> function updates the transformation and copy protection support of a particular path in a specified VidPN topology.</p>


## -prototype

````
DXGKDDI_VIDPNTOPOLOGY_UPDATEPATHSUPPORTINFO pfnUpdatePathSupportInfo;

NTSTATUS APIENTRY pfnUpdatePathSupportInfo(
  _In_ const D3DKMDT_HVIDPNTOPOLOGY     i_hVidPnTopology,
  _In_ const D3DKMDT_VIDPN_PRESENT_PATH *i_pVidPnPresentPathInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>i_hVidPnTopology</i> [in]

<dd>
<p>[in] A handle to a VidPN topology object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-gettopology.md">pfnGetTopology</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562108">DXGK_VIDPN_INTERFACE</a> interface.</p>
</dd>

### -param <i>i_pVidPnPresentPathInfo</i> [in]

<dd>
<p>[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a> structure. The <b>VidPnSourceId</b> and <b>VidPnTargetId</b> members (taken as a pair) identify the path that is to have its transformation and copy protection support updated. The <b>ContentTransformation</b> and <b>CopyProtection</b> members supply the updated transformation and copy protection support.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnUpdatePathSupportInfo</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_TOPOLOGY</b></dt>
</dl><p>The handle supplied in <i>i_hVidPnTopology</i> was invalid.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was supplied.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The path cannot be removed in the context of the current DDI call.</p>

<p> </p>

## -remarks
<p>The display miniport driver's <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a> function calls <b>pnfUpdatePathSupportInfo</b> to report rotation, scaling, and copy protection support for each of the paths in a topology.</p>

<p>The display miniport driver's <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a> function calls <b>pnfUpdatePathSupportInfo</b> to report rotation, scaling, and copy protection support for each of the paths in a topology.</p>

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