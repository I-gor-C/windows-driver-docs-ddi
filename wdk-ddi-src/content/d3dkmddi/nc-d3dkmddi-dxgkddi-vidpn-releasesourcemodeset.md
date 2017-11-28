---
UID: NC.d3dkmddi.DXGKDDI_VIDPN_RELEASESOURCEMODESET
title: DXGKDDI_VIDPN_RELEASESOURCEMODESET
author: windows-driver-content
description: The pfnReleaseSourceModeSet function releases a handle to a source mode set object.
old-location: display\dxgk_vidpn_interface_pfnreleasesourcemodeset.htm
old-project: display
ms.assetid: f1ee8761-f36e-4a39-a78e-95975442f7d3
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
req.alt-api: pfnReleaseSourceModeSet
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

# DXGKDDI_VIDPN_RELEASESOURCEMODESET callback



## -description
<p>The <b>pfnReleaseSourceModeSet</b> function releases a handle to a source mode set object.</p>


## -prototype

````
DXGKDDI_VIDPN_RELEASESOURCEMODESET pfnReleaseSourceModeSet;

NTSTATUS APIENTRY pfnReleaseSourceModeSet(
  _In_ const D3DKMDT_HVIDPN              hVidPn,
  _In_ const D3DKMDT_HVIDPNSOURCEMODESET hVidPnSourceModeSet
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPn</i> [in]

<dd>
<p>[in] A handle to the VidPN object that contains the source mode set object. The VidPN manager previously provided this handle to the display miniport driver by calling <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a>, <a href="display.dxgkddiissupportedvidpn">DxgkDdiIsSupportedVidPn</a>, or <a href="display.dxgkddirecommendfunctionalvidpn">DxgkDdiRecommendFunctionalVidPn</a>.</p>
</dd>

### -param <i>hVidPnSourceModeSet</i> [in]

<dd>
<p>[in] The handle to be released.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnReleaseSourceModeSet</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN</b></dt>
</dl><p>The handle supplied in <i>hVidPn</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_SOURCEMODESET</b></dt>
</dl><p>The handle supplied in <i>hVidPnSourceModeSet</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_RESOURCES_NOT_RELATED</b></dt>
</dl><p>The VidPN identified by <i>hVidPn</i> does not contain the source mode set identified by <i>hVidPnSourceModeSet</i>.</p>

<p> </p>

## -remarks
<p>When you have finished using a handle that you obtained by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiresourcemodeset.md">pfnAcquireSourceModeSet</a>, you must release the handle by calling <b>pfnReleaseSourceModeSet</b>.</p>

<p>If you obtain a handle by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-createnewsourcemodeset.md">pfnCreateNewSourceModeSet</a> and then pass that handle to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-assignsourcemodeset.md">pfnAssignSourceModeSet</a>, you do not need to release the handle.</p>

<p>If you obtain a handle by calling <b>pfnCreateNewSourceModeSet</b> and then you decide not to assign the new source mode set to a source, you must release the newly obtained handle by calling <b>pfnReleaseSourceModeSet</b>.</p>

<p>The D3DKMDT_HVIDPN and D3DKMDT_HVIDPNSOURCEMODESET data types are defined in <i>D3dkmdt.h</i>. </p>

<p>When you have finished using a handle that you obtained by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiresourcemodeset.md">pfnAcquireSourceModeSet</a>, you must release the handle by calling <b>pfnReleaseSourceModeSet</b>.</p>

<p>If you obtain a handle by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-createnewsourcemodeset.md">pfnCreateNewSourceModeSet</a> and then pass that handle to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-assignsourcemodeset.md">pfnAssignSourceModeSet</a>, you do not need to release the handle.</p>

<p>If you obtain a handle by calling <b>pfnCreateNewSourceModeSet</b> and then you decide not to assign the new source mode set to a source, you must release the newly obtained handle by calling <b>pfnReleaseSourceModeSet</b>.</p>

<p>The D3DKMDT_HVIDPN and D3DKMDT_HVIDPNSOURCEMODESET data types are defined in <i>D3dkmdt.h</i>. </p>

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
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiresourcemodeset.md">pfnAcquireSourceModeSet</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-createnewsourcemodeset.md">pfnCreateNewSourceModeSet</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPN_RELEASESOURCEMODESET callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
