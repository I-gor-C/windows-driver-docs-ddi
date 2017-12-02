---
UID: NC.d3dkmddi.DXGKDDI_VIDPNTOPOLOGY_ADDPATH
title: DXGKDDI_VIDPNTOPOLOGY_ADDPATH
author: windows-driver-content
description: The pfnAddPath function adds a video present path to a specified VidPN topology object.
old-location: display\dxgk_vidpntopology_interface_pfnaddpath.htm
old-project: display
ms.assetid: 893e0be1-aa29-429a-a3ca-a9f19053fd92
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
req.alt-api: pfnAddPath
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

# DXGKDDI_VIDPNTOPOLOGY_ADDPATH callback



## -description
<p>The <b>pfnAddPath</b> function adds a video present path to a specified VidPN topology object.</p>


## -prototype

````
DXGKDDI_VIDPNTOPOLOGY_ADDPATH pfnAddPath;

NTSTATUS APIENTRY pfnAddPath(
  _In_ D3DKMDT_HVIDPNTOPOLOGY           hVidPnTopology,
  _In_ D3DKMDT_VIDPN_PRESENT_PATH CONST *pVidPnPresentPath
)
{ ... }
````


## -parameters
<dl>

### -param hVidPnTopology [in]

<dd>
<p>[in] A handle to a VidPN topology object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-gettopology.md">pfnGetTopology</a> function of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-vidpn-interface.md">DXGK_VIDPN_INTERFACE</a> interface.</p>
</dd>

### -param pVidPnPresentPath [in]

<dd>
<p>[in] A pointer to a D3DKMDT_VIDPN_PRESENT_PATH structure that describes the path. The display miniport driver previously obtained this pointer by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-createnewpathinfo.md">pfnCreateNewPathInfo</a>.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnAddPath</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_TOPOLOGY</b></dt>
</dl><p>The handle supplied in <i>hVidPnTopology </i>was invalid.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The path cannot be removed in the context of the current DDI call.</p>

<p> </p>

## -remarks
<p>To add a path to a topology, the display miniport driver performs the following steps.</p>

<p>Call <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-createnewpathinfo.md">pfnCreateNewPathInfo</a> to obtain a pointer to a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path.md">D3DKMDT_VIDPN_PRESENT_PATH</a> structure allocated by the VidPN manager.</p>

<p>Populate the D3DKMDT_VIDPN_PRESENT_PATH structure with information about the path, including video present source and target identifiers.</p>

<p>Call <b>pfnAddPath</b> to add the path to a topology. </p>

<p>The VidPN manager allocates a D3DKMDT_VIDPN_PRESENT_PATH structure when you call <b>pfnCreateNewPathInfo</b>. If you add the path described by that structure to a topology, then you do not need to explicitly release the structure; <b>pfnAddPath</b> releases it.</p>

<p>If you obtain a D3DKMDT_VIDPN_PRESENT_PATH structure by calling <b>pfnCreateNewPathInfo</b> and then decide not to add that path to a topology, then you must explicity release the structure by calling <b>pfnReleasePathInfo</b>.</p>

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

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-createnewpathinfo.md">pfnCreateNewPathInfo</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-releasepathinfo.md">pfnReleasePathInfo</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path.md">D3DKMDT_VIDPN_PRESENT_PATH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPNTOPOLOGY_ADDPATH callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
