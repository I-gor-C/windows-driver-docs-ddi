---
UID: NF.d3dkmthk.D3DKMTCheckOcclusion
title: D3DKMTCheckOcclusion
author: windows-driver-content
description: The D3DKMTCheckOcclusion function verifies whether the client area of a window is occluded.
old-location: display\d3dkmtcheckocclusion.htm
old-project: display
ms.assetid: ce889a72-5f42-4bcf-aa15-6ec9b0423781
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTCheckOcclusion
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
req.alt-api: D3DKMTCheckOcclusion
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

# D3DKMTCheckOcclusion function



## -description
<p>The <b>D3DKMTCheckOcclusion</b> function verifies whether the client area of a window is occluded.</p>


## -syntax

````
NTSTATUS APIENTRY D3DKMTCheckOcclusion(
  _In_ const D3DKMT_CHECKOCCLUSION *pData
);
````


## -parameters
<dl>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-checkocclusion.md">D3DKMT_CHECKOCCLUSION</a> structure that describes parameters for checking occlusion.</p>
</dd>
</dl>

## -returns
<p><b>D3DKMTCheckOcclusion</b> returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The client area of the window is not occluded.</p><dl>
<dt><b>STATUS_GRAPHICS_PRESENT_OCCLUDED</b></dt>
</dl><p>The client area of the window is occluded.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other <b>NTSTATUS</b> values.</p>

## -remarks
<p>The handle to the window that is checked for occlusion must be valid. A window is not occluded if a part of its client area lies on a unowned video present network (VidPn) source, if its client area is an empty rectangular area (RECT), or if desktop composition is running.</p>

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
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-checkocclusion.md">D3DKMT_CHECKOCCLUSION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTCheckOcclusion function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
