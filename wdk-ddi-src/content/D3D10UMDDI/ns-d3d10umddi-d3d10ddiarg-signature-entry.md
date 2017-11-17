---
UID: NS.d3d10umddi.D3D10DDIARG_SIGNATURE_ENTRY
title: D3D10DDIARG_SIGNATURE_ENTRY
author: windows-driver-content
description: The D3D10DDIARG_SIGNATURE_ENTRY structure describes an entry for a signature.
old-location: display\d3d10ddiarg_signature_entry.htm
ms.assetid: 9a7a595e-59b1-4cc2-ab09-ba22aebae9ca
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10DDIARG_SIGNATURE_ENTRY
req.alt-loc: d3d10umddi.h
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
ms.keywords: D3D10DDIARG_SIGNATURE_ENTRY, D3D10DDIARG_SIGNATURE_ENTRY
req.iface: 
---

# D3D10DDIARG_SIGNATURE_ENTRY structure



## -description
<p>The D3D10DDIARG_SIGNATURE_ENTRY structure describes an entry for a signature.</p>


## -syntax

````
typedef struct D3D10DDIARG_SIGNATURE_ENTRY {
  D3D10_SB_NAME SystemValue;
  UINT          Register;
  BYTE          Mask;
} D3D10DDIARG_SIGNATURE_ENTRY;
````


## -struct-fields
<dl>

### -field <b>SystemValue</b>

<dd>
<p>[in] The D3D10_SB_NAME-typed value that indicates the system name of the signature entry. The D3D10_SB_NAME enumeration is defined in the D3d10tokenizedprogramformat.hpp header file. One of the following values can be set.</p>
<table>
<tr>
<th>Value</th>
<th>System name</th>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_UNDEFINED (0)</p>
</td>
<td>
<p>The entry does not have a system name.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_POSITION (1)</p>
</td>
<td>
<p>Position.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_CLIP_DISTANCE (2)</p>
</td>
<td>
<p>Clip distance.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_CULL_DISTANCE (3)</p>
</td>
<td>
<p>Cull distance.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_RENDER_TARGET_ARRAY_INDEX (4)</p>
</td>
<td>
<p>Render target array index.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_VIEWPORT_ARRAY_INDEX (5)</p>
</td>
<td>
<p>Viewport array index.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_VERTEX_ID (6)</p>
</td>
<td>
<p>Vertex ID.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_PRIMITIVE_ID (7)</p>
</td>
<td>
<p>Primitive ID.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_INSTANCE_ID (8)</p>
</td>
<td>
<p>Instance ID.</p>
</td>
</tr>
<tr>
<td>
<p>D3D10_SB_NAME_IS_FRONT_FACE (9)</p>
</td>
<td>
<p>Is front face.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Register</b>

<dd>
<p>[in] The number of the register for the signature entry.</p>
</dd>

### -field <b>Mask</b>

<dd>
<p>[in] The xyzw mask for the signature entry. The four least significant bits (LSBs) of the mask represent xyzw respectively.</p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541746">D3D10DDIARG_STAGE_IO_SIGNATURES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10DDIARG_SIGNATURE_ENTRY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
