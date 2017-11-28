---
UID: NC.d3dkmddi.DXGKDDI_VIDPN_RELEASETARGETMODESET
title: DXGKDDI_VIDPN_RELEASETARGETMODESET
author: windows-driver-content
description: The pfnReleaseTargetModeSet function releases a handle to a target mode set object.
old-location: display\dxgk_vidpn_interface_pfnreleasetargetmodeset.htm
old-project: display
ms.assetid: bd369651-57d4-406f-ba51-9632362de15d
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
req.alt-api: pfnReleaseTargetModeSet
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

# DXGKDDI_VIDPN_RELEASETARGETMODESET callback



## -description
<p>The <b>pfnReleaseTargetModeSet</b> function releases a handle to a target mode set object.</p>


## -prototype

````
DXGKDDI_VIDPN_RELEASETARGETMODESET pfnReleaseTargetModeSet;

NTSTATUS APIENTRY pfnReleaseTargetModeSet(
  _In_ const D3DKMDT_HVIDPN              hVidPn,
  _In_ const D3DKMDT_HVIDPNTARGETMODESET hVidPnTargetModeSet
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPn</i> [in]

<dd>
<p>[in] A handle to a VidPN object that contains the target mode set object. The VidPN manager previously provided this handle to the display miniport driver by calling <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a>, <a href="display.dxgkddiissupportedvidpn">DxgkDdiIsSupportedVidPn</a>, or <a href="display.dxgkddirecommendfunctionalvidpn">DxgkDdiRecommendFunctionalVidPn</a>.</p>
</dd>

### -param <i>hVidPnTargetModeSet</i> [in]

<dd>
<p>[in] The handle to be released.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnReleaseTargetModeSet</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN</b></dt>
</dl><p>The handle supplied in <i>hVidPn</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN_TARGETMODESET</b></dt>
</dl><p>The handle supplied in <i>hVidPnTargetModeSet</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_RESOURCES_NOT_RELATED</b></dt>
</dl><p>The VidPN identified by <i>hVidPn</i> does not contain the target mode set identified by <i>hVidPnTargetModeSet</i>.</p>

<p> </p>

## -remarks
<p>When you have finished using a handle that you obtained by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md">pfnAcquireTargetModeSet</a>, you must release the handle by calling <b>pfnReleaseTargetModeSet</b>.</p>

<p>If you obtain a handle by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-createnewtargetmodeset.md">pfnCreateNewTargetModeSet</a> and then pass that handle to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-assigntargetmodeset.md">pfnAssignTargetModeSet</a>, you do not need to release the handle.</p>

<p>If you obtain a handle by calling <b>pfnCreateNewTargetModeSet</b> and then you decide not to assign the new source mode set to a source, you must release the newly obtained handle by calling <b>pfnReleaseTargetModeSet</b>.</p>

<p>The D3DKMDT_HVIDPN and D3DKMDT_HVIDPNTARGETMODESET data types are defined in <i>D3dkmdt.h</i>. </p>

<p>When you have finished using a handle that you obtained by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md">pfnAcquireTargetModeSet</a>, you must release the handle by calling <b>pfnReleaseTargetModeSet</b>.</p>

<p>If you obtain a handle by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-createnewtargetmodeset.md">pfnCreateNewTargetModeSet</a> and then pass that handle to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-assigntargetmodeset.md">pfnAssignTargetModeSet</a>, you do not need to release the handle.</p>

<p>If you obtain a handle by calling <b>pfnCreateNewTargetModeSet</b> and then you decide not to assign the new source mode set to a source, you must release the newly obtained handle by calling <b>pfnReleaseTargetModeSet</b>.</p>

<p>The D3DKMDT_HVIDPN and D3DKMDT_HVIDPNTARGETMODESET data types are defined in <i>D3dkmdt.h</i>. </p>

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
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md">pfnAcquireTargetModeSet</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-createnewtargetmodeset.md">pfnCreateNewTargetModeSet</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPN_RELEASETARGETMODESET callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
