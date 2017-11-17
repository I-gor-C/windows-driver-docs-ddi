---
UID: NF.d3dkmthk.D3DKMTGetDisplayModeList
title: D3DKMTGetDisplayModeList
author: windows-driver-content
description: The D3DKMTGetDisplayModeList function retrieves a list of available display modes, including modes with extended format.
old-location: display\d3dkmtgetdisplaymodelist.htm
ms.assetid: f813171d-1c7d-4f75-850f-225ea166ff5c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTGetDisplayModeList
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
ms.keywords: D3DKMTGetDisplayModeList
req.iface: 
---

# D3DKMTGetDisplayModeList function



## -description
<p>The <b>D3DKMTGetDisplayModeList</b> function retrieves a list of available display modes, including modes with extended format.</p>


## -syntax

````
NTSTATUS D3DKMTGetDisplayModeList(
  _Inout_ D3DKMT_GETDISPLAYMODELIST *pData
);
````


## -parameters
<dl>

### -param <i>pData</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548036">D3DKMT_GETDISPLAYMODELIST</a> structure that describes a list of available display modes.</p>
</dd>
</dl>

## -returns
<p><b>D3DKMTGetDisplayModeList</b> returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The list of available display modes was successfully retrieved.</p><dl>
<dt><b>STATUS_DEVICE_REMOVED</b></dt>
</dl><p>The graphics adapter was stopped.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The buffer that the OpenGL ICD supplied in the <b>pModeList</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548036">D3DKMT_GETDISPLAYMODELIST</a> that the <i>pData</i> parameter points to is not large enough to contain the requested display mode list. </p><dl>
<dt><b>STATUS_GRAPHICS_NO_AVAILABLE_VIDPN_TARGET</b></dt>
</dl><p>No video present target is available for use with the video present source that is identified by the <b>VidPnSourceId</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548036">D3DKMT_GETDISPLAYMODELIST</a> that the <i>pData</i> parameter points to. Therefore, no display modes are available for this source. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other <b>NTSTATUS</b> values.</p>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548036">D3DKMT_GETDISPLAYMODELIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTGetDisplayModeList function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
