---
UID: NF.d3dkmthk.D3DKMTSetVidPnSourceOwner
title: D3DKMTSetVidPnSourceOwner
author: windows-driver-content
description: The D3DKMTSetVidPnSourceOwner function sets and releases the video present source in the path of a video present network (VidPN) topology that owns the VidPN.
old-location: display\d3dkmtsetvidpnsourceowner.htm
old-project: display
ms.assetid: e75020cf-39b4-434c-b071-dc75de6cc81b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTSetVidPnSourceOwner
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTSetVidPnSourceOwner
req.alt-loc: Gdi32.dll,API-MS-Win-dx-d3dkmt-l1-1-0.dll,API-MS-Win-dx-d3dkmt-l1-1-1.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Gdi32.lib
req.dll: Gdi32.dll
req.irql: 
req.iface: 
---

# D3DKMTSetVidPnSourceOwner function



## -description
<p>The <b>D3DKMTSetVidPnSourceOwner</b> function sets and releases the video present source in the path of a video present network (VidPN) topology that owns the VidPN.</p>


## -syntax

````
NTSTATUS APIENTRY D3DKMTSetVidPnSourceOwner(
  _In_ const D3DKMT_SETVIDPNSOURCEOWNER *pData
);
````


## -parameters
<dl>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-setvidpnsourceowner.md">D3DKMT_SETVIDPNSOURCEOWNER</a> structure that describes the parameters for setting or releasing.</p>
</dd>
</dl>

## -returns
<p><b>D3DKMTSetVidPnSourceOwner</b> returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The video present source was successfully set or released.</p><dl>
<dt><b>STATUS_DEVICE_REMOVED</b></dt>
</dl><p>The graphics adapter was stopped or the display device was reset.</p><dl>
<dt><b>STATUS_GRAPHICS_VIDPN_SOURCE_IN_USE</b></dt>
</dl><p>The video present source that is specified by an element in the array that the  <b>pVidPnSourceId</b> member of <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-setvidpnsourceowner.md">D3DKMT_SETVIDPNSOURCEOWNER</a> specifies is already owned by a display mode manager (DMM) client and cannot be used until the client releases the video present source.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_SOURCE</b></dt>
</dl><p>The video present source that is specified by an element in the array that the  <b>pVidPnSourceId</b> member of <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-setvidpnsourceowner.md">D3DKMT_SETVIDPNSOURCEOWNER</a> specifies is invalid. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other NTSTATUS values.</p>

## -remarks
<p>To set ownership of video present sources, the OpenGL installable client driver (ICD) sets values in the array that the <b>pType</b> member of the <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-setvidpnsourceowner.md">D3DKMT_SETVIDPNSOURCEOWNER</a> structure specifies, identifiers of the video present sources in the array that the <b>pVidPnSourceId</b> member of D3DKMT_SETVIDPNSOURCEOWNER specifies, and the number of video present sources in the <b>VidPnSourceCount</b> member of D3DKMT_SETVIDPNSOURCEOWNER. </p>

<p>To release ownership of any video present sources, the ICD sets <b>pType</b> and <b>pVidPnSourceId</b> to <b>NULL</b> and <b>VidPnSourceCount</b> to zero in D3DKMT_SETVIDPNSOURCEOWNER.</p>

<p>The ICD passes a pointer to <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-setvidpnsourceowner.md">D3DKMT_SETVIDPNSOURCEOWNER</a> in the <i>pData</i> parameter in a call to <b>D3DKMTSetVidPnSourceOwner</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Gdi32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Gdi32.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-setvidpnsourceowner.md">D3DKMT_SETVIDPNSOURCEOWNER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTSetVidPnSourceOwner function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
