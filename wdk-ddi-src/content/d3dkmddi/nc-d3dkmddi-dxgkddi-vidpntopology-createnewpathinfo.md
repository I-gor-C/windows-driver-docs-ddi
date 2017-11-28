---
UID: NC.d3dkmddi.DXGKDDI_VIDPNTOPOLOGY_CREATENEWPATHINFO
title: DXGKDDI_VIDPNTOPOLOGY_CREATENEWPATHINFO
author: windows-driver-content
description: The pfnCreateNewPathInfo function returns a pointer to a D3DKMDT_VIDPN_PRESENT_PATH structure that the display miniport driver populates before calling pfnAddPath.
old-location: display\dxgk_vidpntopology_interface_pfncreatenewpathinfo.htm
old-project: display
ms.assetid: 2d9a4e10-514d-4ea9-9d60-0bbb7cdca29d
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnCreateNewPathInfo
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

# DXGKDDI_VIDPNTOPOLOGY_CREATENEWPATHINFO callback



## -description
<p>The <b>pfnCreateNewPathInfo</b> function returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a> structure that the display miniport driver populates before calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-addpath.md">pfnAddPath</a>.</p>


## -prototype

````
DXGKDDI_VIDPNTOPOLOGY_CREATENEWPATHINFO pfnCreateNewPathInfo;

NTSTATUS APIENTRY pfnCreateNewPathInfo(
  _In_  const D3DKMDT_HVIDPNSOURCEMODESET hVidPnTopology,
  _Out_       D3DKMDT_VIDPN_PRESENT_PATH  **ppNewVidPnPresentPathInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPnTopology</i> [in]

<dd>
<p>[in] A handle to a VidPN topology object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-gettopology.md">pfnGetTopology</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562108">DXGK_VIDPN_INTERFACE</a> interface.</p>
</dd>

### -param <i>ppNewVidPnPresentPathInfo</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a D3DKMDT_VIDPN_PRESENT_PATH structure allocated by the VidPN manager.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnCreateNewPathInfo</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_TOPOLOGY</b></dt>
</dl><p>The handle supplied in <i>hVidPnTopology </i>was invalid.</p>

<p> </p>

## -remarks
<p>After you call <b>pfnCreateNewPathInfo</b> to obtain a D3DKMDT_VIDPN_PRESENT_PATH structure, you must do one, but not both, of the following:</p>

<p>Populate the structure and pass it to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-addpath.md">pfnAddPath</a>.</p>

<p>Release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-releasepathinfo.md">pfnReleasePathInfo</a>.</p>

<p>The D3DKMDT_HVIDPNTOPOLOGY data type is defined in <i>D3dkmdt.h</i>.</p>

<p>After you call <b>pfnCreateNewPathInfo</b> to obtain a D3DKMDT_VIDPN_PRESENT_PATH structure, you must do one, but not both, of the following:</p>

<p>Populate the structure and pass it to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-addpath.md">pfnAddPath</a>.</p>

<p>Release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-releasepathinfo.md">pfnReleasePathInfo</a>.</p>

<p>The D3DKMDT_HVIDPNTOPOLOGY data type is defined in <i>D3dkmdt.h</i>.</p>

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
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-addpath.md">pfnAddPath</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-releasepathinfo.md">pfnReleasePathInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPNTOPOLOGY_CREATENEWPATHINFO callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
