---
UID: NF.d3dkmthk.D3DKMTEscape
title: D3DKMTEscape
author: windows-driver-content
description: The D3DKMTEscape function exchanges information with the display miniport driver.
old-location: display\d3dkmtescape.htm
old-project: display
ms.assetid: 60b105df-2085-40bc-9d95-0f6b317a565e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTEscape
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
req.alt-api: D3DKMTEscape
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

# D3DKMTEscape function



## -description
<p>The <b>D3DKMTEscape</b> function exchanges information with the display miniport driver.</p>


## -syntax

````
NTSTATUS D3DKMTEscape(
  _In_ const D3DKMT_ESCAPE *pData
);
````


## -parameters
<dl>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-escape.md">D3DKMT_ESCAPE</a> structure that describes the exchanged information.</p>
</dd>
</dl>

## -returns
<p><b>D3DKMTEscape</b> returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Information was successfully shared.</p><dl>
<dt><b>STATUS_DEVICE_REMOVED</b></dt>
</dl><p>The graphics adapter was stopped or the display device was reset.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtescape.md">D3DKMTEscape</a> could not complete because of insufficient memory.</p><dl>
<dt><b>STATUS_PRIVILEGED_INSTRUCTION</b></dt>
</dl><p>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtescape.md">D3DKMTEscape</a> detected nonprivileged instructions (that is, instructions that access memory beyond the privilege of the current CPU process).</p><dl>
<dt><b>STATUS_ILLEGAL_INSTRUCTION</b></dt>
</dl><p>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtescape.md">D3DKMTEscape</a> detected instructions that cannot be supported by graphics hardware.</p>

<p> </p>

<p>This function might also return other <b>NTSTATUS</b> values.</p>

## -remarks
<p>The OpenGL ICD calls <b>D3DKMTEscape</b> to exchange data directly with the display miniport driver. For testing purposes, the OpenGL ICD can also call <b>D3DKMTEscape</b> to control the video memory manager and graphics processing unit (GPU) scheduler (which are part of <i>Dxgkrnl.sys</i>) and the behavior of the operating system's Timeout Detection and Recovery (TDR) process. </p>

<p>Hardware vendors can use <b>D3DKMTEscape</b> in their OpenGL ICDs as an extension mechanism. However, vendors should report necessary extensions to Microsoft so the extensions can be natively supported by the operating system.</p>

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
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-escape.md">D3DKMT_ESCAPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTEscape function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
