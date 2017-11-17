---
UID: NF.d3dkmthk.D3DKMTSetDisplayMode
title: D3DKMTSetDisplayMode
author: windows-driver-content
description: The D3DKMTSetDisplayMode function sets the allocation that is used to scan out to the display.
old-location: display\d3dkmtsetdisplaymode.htm
ms.assetid: bf51b8dc-82e8-420e-bc3d-7cb9e8d72b9f
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
req.alt-api: D3DKMTSetDisplayMode
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
ms.keywords: D3DKMTSetDisplayMode
req.iface: 
---

# D3DKMTSetDisplayMode function



## -description
<p>The <i>D3DKMTSetDisplayMode</i> function sets the allocation that is used to scan out to the display.</p>


## -syntax

````
NTSTATUS APIENTRY D3DKMTSetDisplayMode(
  _Inout_ const D3DKMT_SETDISPLAYMODE *pData
);
````


## -parameters
<dl>

### -param <i>pData</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548275">D3DKMT_SETDISPLAYMODE</a> structure that describes the allocation that is used to scan out.</p>
</dd>
</dl>

## -returns
<p><i>D3DKMTSetDisplayMode</i> returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The display mode was successfully set.</p><dl>
<dt><b>STATUS_DEVICE_REMOVED</b></dt>
</dl><p>The graphics adapter was stopped or the display device was reset.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p><dl>
<dt><b>STATUS_GRAPHICS_NOT_EXCLUSIVE_MODE_OWNER</b></dt>
</dl><p>
        Before the call to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547169">D3DKMTSetDisplayMode</a>, the device did not acquire exclusive ownership of the view; therefore, the device could not set the display mode.
       </p><dl>
<dt><b>D3DDDIERR_INCOMPATIBLEPRIVATEFORMAT</b></dt>
</dl><p>The OpenGL installable client driver (ICD) must convert the format of the surface that is associated with the allocation that the <b>hPrimaryAllocation</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548275">D3DKMT_SETDISPLAYMODE</a> specifies into the format attribute that the <b>PrivateDriverFormatAttribute</b> member of D3DKMT_SETDISPLAYMODE specifies. The ICD should then call 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547169">D3DKMTSetDisplayMode</a> again. The ICD could allocate a new allocation, perform a conversion bit-block transfer (bitblt) from the old primary to the new, and then destroy the old primary as long as the ICD uses the new allocation handle for this allocation for all subsequent operations. The ICD should repeat this process until 
      <i>D3DKMTSetDisplayMode</i> returns a different return value. </p>

<p> </p>

<p>This function might also return other NTSTATUS values.</p>

## -remarks
<p>Before the OpenGL ICD calls 
      <i>D3DKMTSetDisplayMode</i> to set a new display mode that uses an extended format, a multiple-sampling method, or both, the ICD must ensure that the current GDI display mode has the same resolution as the new display mode; otherwise, 
      <i>D3DKMTSetDisplayMode</i> returns <b>STATUS_INVALID_PARAMETER</b>.</p>

<p>Before the OpenGL ICD calls 
      <i>D3DKMTSetDisplayMode</i> to set a new display mode that uses an extended format, a multiple-sampling method, or both, the ICD must ensure that the current GDI display mode has the same resolution as the new display mode; otherwise, 
      <i>D3DKMTSetDisplayMode</i> returns <b>STATUS_INVALID_PARAMETER</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548275">D3DKMT_SETDISPLAYMODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTSetDisplayMode function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
