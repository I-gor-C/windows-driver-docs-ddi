---
UID: NF.d3dkmthk.D3DKMTInvalidateActiveVidPn
title: D3DKMTInvalidateActiveVidPn
author: windows-driver-content
description: The D3DKMTInvalidateActiveVidPn function invalidates the active video present network (VidPN) currently in use.Note   This function is obsolete in Windows 7 and later versions of the Windows operating systems.
old-location: display\d3dkmtinvalidateactivevidpn.htm
ms.assetid: a7cac46d-b64d-4362-99ab-179aa6525ba2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems for display miniport drivers with version < DXGKDDI_INTERFACE_VERSION_WIN7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTInvalidateActiveVidPn
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
ms.keywords: D3DKMTInvalidateActiveVidPn
req.iface: 
---

# D3DKMTInvalidateActiveVidPn function



## -description
<p>The <b>D3DKMTInvalidateActiveVidPn</b> function invalidates the active video present network (VidPN) currently in use.</p>
<p>
<div class="alert"><b>Note</b>    This function is obsolete in Windows 7 and later versions of the Windows operating systems.</div>
<div> </div>
</p>


## -syntax

````
NTSTATUS D3DKMTInvalidateActiveVidPn(
  _In_ const D3DKMT_INVALIDATEACTIVEVIDPN *pData
);
````


## -parameters
<dl>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548082">D3DKMT_INVALIDATEACTIVEVIDPN</a> structure that describes parameters that invalidate the active VidPN currently in use.</p>
</dd>
</dl>

## -returns
<p><b>D3DKMTInvalidateActiveVidPn</b> returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The VidPN currently in use was successfully invalidated.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_DISPLAY_ADAPTER</b></dt>
</dl><p>No graphics adapter was specified in the <b>hAdapter</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548082">D3DKMT_INVALIDATEACTIVEVIDPN</a> to invalidate the VidPN for.</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547023">D3DKMTInvalidateActiveVidPn</a> could not complete because of insufficient memory.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The display mode that is requested by the OpenGL installable client driver (ICD) in the buffer pointed to by the <b>pPrivateDriverData</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548082">D3DKMT_INVALIDATEACTIVEVIDPN</a> is not supported by the display miniport driver.</p>

<p>This status value will also be returned if this function is called on a computer running Windows 7 and later by a display miniport driver with DXGKDDI_INTERFACE_VERSION &gt;= DXGKDDI_INTERFACE_VERSION_WIN7.</p><dl>
<dt><b>STATUS_DEVICE_REMOVED</b></dt>
</dl><p>The graphics adapter was stopped.</p><dl>
<dt><b>STATUS_GRAPHICS_NO_RECOMMENDED_FUNCTIONAL_VIDPN</b></dt>
</dl><p>The display miniport driver did not recommend a VidPN to replace the VidPN currently in use.</p>

<p> </p>

<p>This function might also return other NTSTATUS values.</p>

## -remarks
<p>When the <b>D3DKMTInvalidateActiveVidPn</b> function is called to invalidate the VidPN currently in use, the current VidPN is replaced with a new VidPN that the display miniport driver recommends. Because the display miniport driver must recommend a new VidPN, the display miniport driver must be able to determine the display mode that the OpenGL ICD requires from the buffer pointed to by the <b>pPrivateDriverData</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548082">D3DKMT_INVALIDATEACTIVEVIDPN</a>.</p>

<p>The OpenGL ICD can call <b>D3DKMTInvalidateActiveVidPn</b> for display modes (for example, clone-view mode) that are not supported by using the more general call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547169">D3DKMTSetDisplayMode</a> function. </p>

<p>When the <b>D3DKMTInvalidateActiveVidPn</b> function is called to invalidate the VidPN currently in use, the current VidPN is replaced with a new VidPN that the display miniport driver recommends. Because the display miniport driver must recommend a new VidPN, the display miniport driver must be able to determine the display mode that the OpenGL ICD requires from the buffer pointed to by the <b>pPrivateDriverData</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548082">D3DKMT_INVALIDATEACTIVEVIDPN</a>.</p>

<p>The OpenGL ICD can call <b>D3DKMTInvalidateActiveVidPn</b> for display modes (for example, clone-view mode) that are not supported by using the more general call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547169">D3DKMTSetDisplayMode</a> function. </p>

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
<p>Available in Windows Vista and later versions of the Windows operating systems for display miniport drivers with version &lt; DXGKDDI_INTERFACE_VERSION_WIN7.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548082">D3DKMT_INVALIDATEACTIVEVIDPN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547169">D3DKMTSetDisplayMode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTInvalidateActiveVidPn function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
