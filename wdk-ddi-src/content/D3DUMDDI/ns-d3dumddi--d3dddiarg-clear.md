---
UID: NS.d3dumddi._D3DDDIARG_CLEAR
title: D3DDDIARG_CLEAR
author: windows-driver-content
description: The D3DDDIARG_CLEAR structure describes the parameters of a hardware-assisted clearing operation.
old-location: display\d3dddiarg_clear.htm
ms.assetid: f437f94c-075e-43e6-bf28-0e7c7bd78c5a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_CLEAR
req.alt-loc: d3dumddi.h
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
ms.keywords: D3DDDIARG_CLEAR, D3DDDIARG_CLEAR
req.iface: 
---

# D3DDDIARG_CLEAR structure



## -description
<p>The D3DDDIARG_CLEAR structure describes the parameters of a hardware-assisted clearing operation. </p>


## -syntax

````
typedef struct _D3DDDIARG_CLEAR {
  UINT  Flags;
  UINT  FillColor;
  FLOAT FillDepth;
  UINT  FillStencil;
} D3DDDIARG_CLEAR;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>[in] A UINT value that specifies which buffers the driver should clear and how the clear operation should be performed. This member can be a bitwise OR of the following values. For more information, see the Remarks section in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406339">Clear</a> reference page.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DCLEAR_TARGET (0x00000001l)</p>
</td>
<td>
<p>The driver should clear the context's render target to the color that is specified by the <b>FillColor</b> member. This value is defined in <i>D3d8types.h</i>.</p>
</td>
</tr>
<tr>
<td>
<p>D3DCLEAR_STENCIL (0x00000004l)</p>
</td>
<td>
<p>The driver should clear the context's stencil buffer to the value that is specified by the <b>FillStencil</b> member. This value is defined in <i>D3d8types.h</i>.</p>
</td>
</tr>
<tr>
<td>
<p>D3DCLEAR_ZBUFFER (0x00000002l)</p>
</td>
<td>
<p>The driver should clear the context's depth buffer to the depth that is specified by the <b>FillDepth</b> member. This value is defined in <i>D3d8types.h</i>.</p>
</td>
</tr>
<tr>
<td>
<p>D3DCLEAR_COMPUTERECTS (0x00000008l)</p>
</td>
<td>
<p>If rectangles are specified for clearing, the driver should clip them against the current viewport. If no rectangles are specified, the driver should clear the entire viewport. This value is defined in <i>D3dhal.h</i>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>FillColor</b>

<dd>
<p>[in] The color value that the driver should clear the context's render target to.</p>
</dd>

### -field <b>FillDepth</b>

<dd>
<p>[in] The value that the driver should use to set the depth in the context's depth buffer. This member can be a value in the range from 0.0 through 1.0. </p>
</dd>

### -field <b>FillStencil</b>

<dd>
<p>[in] The value that the driver should clear the context's stencil buffer to. This member can be an integer in the range from 0 through 2ⁿ-1, where <i>n</i> is the number of bits in the stencil buffer.</p>
</dd>
</dl>

## -remarks
<p>In a call to the user-mode display driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh406339">Clear</a> function, a pointer to a D3DDDIARG_CLEAR structure is passed in the <i>pData</i> parameter. The Microsoft Direct3D runtime passes information to the <i>NumRect</i> and <i>pRect</i> parameters in a call to the user-mode display driver's <b>Clear</b> function to specify the rectangular areas of the buffer that the driver should clear.</p>

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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406339">Clear</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_CLEAR structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
