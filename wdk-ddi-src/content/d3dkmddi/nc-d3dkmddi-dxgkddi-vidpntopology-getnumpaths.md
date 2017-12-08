---
UID: NC.d3dkmddi.DXGKDDI_VIDPNTOPOLOGY_GETNUMPATHS
title: DXGKDDI_VIDPNTOPOLOGY_GETNUMPATHS
author: windows-driver-content
description: The pfnGetNumPaths function returns the number of video present paths in a specified VidPN topology.
old-location: display\dxgk_vidpntopology_interface_pfngetnumpaths.htm
old-project: display
ms.assetid: 60960774-3f90-4eeb-a408-fa37122f22ea
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
req.alt-api: pfnGetNumPaths
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

# DXGKDDI_VIDPNTOPOLOGY_GETNUMPATHS callback



## -description
<p>The <b>pfnGetNumPaths</b> function returns the number of video present paths in a specified VidPN topology.</p>


## -prototype

````
DXGKDDI_VIDPNTOPOLOGY_GETNUMPATHS pfnGetNumPaths;

NTSTATUS APIENTRY pfnGetNumPaths(
  _In_  const D3DKMDT_HVIDPNTOPOLOGY hVidPnTopology,
  _Out_       SIZE_T                 *pNumPaths
)
{ ... }
````


## -parameters
<dl>

### -param hVidPnTopology [in]

<dd>
<p>[in] A handle to a VidPN topology object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-gettopology.md">pfnGetTopology</a> function of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-vidpn-interface.md">DXGK_VIDPN_INTERFACE</a> interface.</p>
</dd>

### -param pNumPaths [out]

<dd>
<p>[out] A pointer to a SIZE_T-typed variable that receives the number of paths.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnGetNumPaths</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_TOPOLOGY</b></dt>
</dl><p>The handle supplied in <i>hVidPnTopology </i>was invalid.</p>

<p> </p>

## -remarks
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
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-getnumpathsfromsource.md">pfnGetNumPathsFromSource</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPNTOPOLOGY_GETNUMPATHS callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
