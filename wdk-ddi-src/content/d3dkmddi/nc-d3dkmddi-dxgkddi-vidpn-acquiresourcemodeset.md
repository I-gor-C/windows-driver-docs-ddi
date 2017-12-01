---
UID: NC.d3dkmddi.DXGKDDI_VIDPN_ACQUIRESOURCEMODESET
title: DXGKDDI_VIDPN_ACQUIRESOURCEMODESET
author: windows-driver-content
description: The pfnAcquireSourceModeSet function returns a handle to a particular source mode set object that is contained by a specified VidPN object.
old-location: display\dxgk_vidpn_interface_pfnacquiresourcemodeset.htm
old-project: display
ms.assetid: cf19f468-86c1-4cc9-8945-e23f73a85c91
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
req.alt-api: pfnAcquireSourceModeSet
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

# DXGKDDI_VIDPN_ACQUIRESOURCEMODESET callback



## -description
<p>The <b>pfnAcquireSourceModeSet</b> function returns a handle to a particular source mode set object that is contained by a specified VidPN object.</p>


## -prototype

````
DXGKDDI_VIDPN_ACQUIRESOURCEMODESET pfnAcquireSourceModeSet;

NTSTATUS APIENTRY pfnAcquireSourceModeSet(
  _In_  const D3DKMDT_HVIDPN                    hVidPn,
  _In_  const D3DDDI_VIDEO_PRESENT_SOURCE_ID    VidPnSourceId,
  _Out_       D3DKMDT_HVIDPNSOURCEMODESET       *phVidPnSourceModeSet,
  _Out_ const DXGK_VIDPNSOURCEMODESET_INTERFACE **ppVidPnSourceModeSetInterface
)
{ ... }
````


## -parameters
<dl>

### -param <i>hVidPn</i> [in]

<dd>
<p>[in] A handle to a VidPN object. The VidPN manager previously provided this handle to the display miniport driver by calling <a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a>, <a href="display.dxgkddiissupportedvidpn">DxgkDdiIsSupportedVidPn</a>, or <a href="display.dxgkddirecommendfunctionalvidpn">DxgkDdiRecommendFunctionalVidPn</a>.</p>
</dd>

### -param <i>VidPnSourceId</i> [in]

<dd>
<p>[in] An integer that identifies one of the video present sources associated with the VidPN object.</p>
</dd>

### -param <i>phVidPnSourceModeSet</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a handle to the requested source mode set object.</p>
</dd>

### -param <i>ppVidPnSourceModeSetInterface</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-vidpnsourcemodeset-interface.md">DXGK_VIDPNSOURCEMODESET_INTERFACE</a> structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter the source mode set object.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnAcquireSourceModeSet</b> function returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDPN</b></dt>
</dl><p>The handle supplied in <i>hVidPn</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_SOURCE</b></dt>
</dl><p>The identifier supplied in <i>VidPnSourceId</i> was invalid.</p>

<p> </p>

## -remarks
<p>VidPN source identifiers are assigned by the operating system. <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a>, implemented by the display miniport driver, returns the number N of video present sources supported by the display adapter. Then the operating system assigns identifiers 0, 1, 2, ... N - 1.</p>

<p>When you have finished using the source mode set object handle, you must release the handle by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-releasesourcemodeset.md">pfnReleaseSourceModeSet</a>. Source mode set objects are reference counted, so if you acquire a handle several times, you must release it that same number of times.</p>

<p>The lifetime of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-vidpnsourcemodeset-interface.md">DXGK_VIDPNSOURCEMODESET_INTERFACE</a> structure returned in <i>ppVidPnSourceModeSetInterface</i> is owned by the operating system. Using this ownership scheme, the operating system can switch to newer implementations at run time without breaking clients of the interface.</p>

<p>The D3DDDI_VIDEO_PRESENT_SOURCE_ID data type is defined in <i>D3dukmdt.h</i>.</p>

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
<a href="display.vidpn_source_mode_set_interface">VidPN Source Mode Set Interface</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-releasetargetmodeset.md">pfnReleaseTargetModeSet</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-createnewsourcemodeset.md">pfnCreateNewSourceModeSet</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-assigntargetmodeset.md">pfnAssignTargetModeSet</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_VIDPN_ACQUIRESOURCEMODESET callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
