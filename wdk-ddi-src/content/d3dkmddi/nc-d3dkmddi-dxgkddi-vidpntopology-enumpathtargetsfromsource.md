---
UID: NC.d3dkmddi.DXGKDDI_VIDPNTOPOLOGY_ENUMPATHTARGETSFROMSOURCE
title: DXGKDDI_VIDPNTOPOLOGY_ENUMPATHTARGETSFROMSOURCE
author: windows-driver-content
description: The pfnEnumPathTargetsFromSource function returns the identifier of one of the video present targets associated with a specified video present source.
old-location: display\dxgk_vidpntopology_interface_pfnenumpathtargetsfromsource.htm
old-project: display
ms.assetid: ca925b3c-8141-419d-99a1-43764ec07315
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
req.alt-api: pfnEnumPathTargetsFromSource
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

# DXGKDDI_VIDPNTOPOLOGY_ENUMPATHTARGETSFROMSOURCE callback



## -description
<p>The <b>pfnEnumPathTargetsFromSource</b> function returns the identifier of one of the video present targets associated with a specified video present source.</p>


## -prototype

````
DXGKDDI_VIDPNTOPOLOGY_ENUMPATHTARGETSFROMSOURCE pfnEnumPathTargetsFromSource;

NTSTATUS APIENTRY pfnEnumPathTargetsFromSource(
  _In_  const D3DKMDT_HVIDPNTOPOLOGY           hVidPnTopology,
  _In_  const D3DDDI_VIDEO_PRESENT_SOURCE_ID   VidPnSourceId,
  _In_  const D3DKMDT_VIDPN_PRESENT_PATH_INDEX VidPnPresentPathIndex,
  _Out_       D3DDDI_VIDEO_PRESENT_TARGET_ID   *pVidPnTargetId
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPnTopology</i> [in]

<dd>
<p>[in] A handle to a VidPN topology object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-gettopology.md">pfnGetTopology</a> function of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-vidpn-interface.md">DXGK_VIDPN_INTERFACE</a> interface.</p>
</dd>

### -param <i>VidPnSourceId</i> [in]

<dd>
<p>[in] An integer that identifies a particular video present source.</p>
</dd>

### -param <i>VidPnPresentPathIndex</i> [in]

<dd>
<p>[in] A zero-based index into the set of paths that contain the source identified by <i>VidPnSourceId</i>.</p>
</dd>

### -param <i>pVidPnTargetId</i> [out]

<dd>
<p>[out] A pointer to a variable that receives the target identifier.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnEnumPathTargetsFromSource</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_TOPOLOGY</b></dt>
</dl><p>The handle supplied in <i>hVidPnTopology </i>was invalid.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The pointer supplied in <i>pVidPnTargetId</i> was in valid.</p>

<p> </p>

## -remarks
<p><i>VidPnPresentPathIndex</i> is not an index into the set of all paths in the topology identified by <i>hVidPnTopology</i>. It is an index into a subset of all the paths in the topology: specifically, the subset of all paths that contain the source identified by <i>VidPnSourceId</i>.</p>

<p>To enumerate (in a given topology) all the targets associated with a particular source, perform the following steps.</p>

<p>Call <b>pfnGetNumPathsFromSource</b> to determine the number N of paths that contain the source of interest. Think of those paths as an indexed set with indices 0, 1, ... N - 1.</p>

<p>For each index 0 though N - 1, pass the source identifier and the index to <b>pfnEnumPathTargetsFromSource</b>.</p>

<p>A topology is a collection paths, each of which contains a (source, target) pair. It is possible for a particular source to appear in more than one path. For example, one source can be paired with two distinct targets in the case of a clone view.</p>

<p>VidPN source identifiers are assigned by the operating system. <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>, implemented by the display miniport driver, returns the number N of video present sources supported by the display adapter. Then the operating system assigns identifiers 0, 1, 2, ... N - 1.</p>

<p>VidPN target identifiers are assigned by the display miniport driver. <a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>, implemented by the display miniport driver, returns an array of <a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a> structures, each of which contains an identifier.</p>

<p>The D3DKMDT_HVIDPNTOPOLOGY and D3DKMDT_VIDPN_PRESENT_PATH_INDEX data types are defined in <i>D3dkmdt.h</i>.  </p>

<p>The D3DDDI_VIDEO_PRESENT_SOURCE_ID and D3DDDI_VIDEO_PRESENT_TARGET_ID data types are defined in <i>D3dukmdt.h</i>.</p>

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
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-getpathsourcefromtarget.md">pfnGetPathSourceFromTarget</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPNTOPOLOGY_ENUMPATHTARGETSFROMSOURCE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
