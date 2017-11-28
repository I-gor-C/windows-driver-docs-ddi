---
UID: NS.d3dkmthk._D3DKMT_SETDISPLAYMODE
title: D3DKMT_SETDISPLAYMODE
author: windows-driver-content
description: The D3DKMT_SETDISPLAYMODE structure describes the primary allocation that is used for scanning out to the display.
old-location: display\d3dkmt_setdisplaymode.htm
old-project: display
ms.assetid: cb590e18-59a4-4c4d-9d97-9f60c409c2e9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_SETDISPLAYMODE, D3DKMT_SETDISPLAYMODE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_SETDISPLAYMODE
req.alt-loc: d3dkmthk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# D3DKMT_SETDISPLAYMODE structure



## -description
<p>The D3DKMT_SETDISPLAYMODE structure describes the primary allocation that is used for scanning out to the display. </p>


## -syntax

````
typedef struct _D3DKMT_SETDISPLAYMODE {
  D3DKMT_HANDLE                         hDevice;
  D3DKMT_HANDLE                         hPrimaryAllocation;
  D3DDDI_VIDEO_SIGNAL_SCANLINE_ORDERING ScanLineOrdering;
  D3DDDI_ROTATION                       DisplayOrientation;
  UINT                                  PrivateDriverFormatAttribute;
  D3DKMT_SETDISPLAYMODE_FLAGS           Flags;
} D3DKMT_SETDISPLAYMODE;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the device that requests setting of the display mode.</p>
</dd>

### -field <b>hPrimaryAllocation</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents the kernel-mode handle to the primary allocation for scanning out. </p>
</dd>

### -field <b>ScanLineOrdering</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544682">D3DDDI_VIDEO_SIGNAL_SCANLINE_ORDERING</a>-typed value that indicates how scan lines are ordered in the display mode.</p>
</dd>

### -field <b>DisplayOrientation</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544646">D3DDDI_ROTATION</a>-typed value that identifies the orientation of the display mode.</p>
</dd>

### -field <b>PrivateDriverFormatAttribute</b>

<dd>
<p>[out] A UINT value that specifies a private format attribute that the OpenGL installable client driver (ICD) should use to convert the current primary surface if a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547169">D3DKMTSetDisplayMode</a> function failed with STATUS_GRAPHICS_INCOMPATIBLE_PRIVATE_FORMAT. </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Supported in Windows 7 and later versions.</p>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff548286">D3DKMT_SETDISPLAYMODE_FLAGS</a> structure that specifies, in bit-field flags, attributes for setting the display mode. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544646">D3DDDI_ROTATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544682">D3DDDI_VIDEO_SIGNAL_SCANLINE_ORDERING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548286">D3DKMT_SETDISPLAYMODE_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547169">D3DKMTSetDisplayMode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_SETDISPLAYMODE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
