---
UID: NS.d3d10umddi.D3D11_1DDIARG_SIGNATURE_ENTRY
title: D3D11_1DDIARG_SIGNATURE_ENTRY
author: windows-driver-content
description: Describes an entry for a signature.
old-location: display\d3d11_1ddiarg_signature_entry.htm
ms.assetid: 571ed880-a4c6-4eb1-a254-c1faf2a589d2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDIARG_SIGNATURE_ENTRY
req.alt-loc: D3d10umddi.h
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
ms.keywords: D3D11_1DDIARG_SIGNATURE_ENTRY, D3D11_1DDIARG_SIGNATURE_ENTRY
req.iface: 
---

# D3D11_1DDIARG_SIGNATURE_ENTRY structure



## -description
<p>Describes an entry for a signature.</p>


## -syntax

````
typedef struct D3D11_1DDIARG_SIGNATURE_ENTRY {
  D3D10_SB_NAME                    SystemValue;
  UINT                             Register;
  BYTE                             Mask;
  D3D10_SB_REGISTER_COMPONENT_TYPE RegisterComponentType;
  D3D11_SB_OPERAND_MIN_PRECISION   MinPrecision;
} D3D11_1DDIARG_SIGNATURE_ENTRY;
````


## -struct-fields
<dl>

### -field <b>SystemValue</b>

<dd>
<p>[in] The <b>D3D10_SB_NAME</b>-typed value that indicates the system name of the signature entry. The <b>D3D10_SB_NAME</b> enumeration is defined in the D3d10tokenizedprogramformat.hpp header file. One of the following values can be set.</p>
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

### -field <b>RegisterComponentType</b>

<dd>
<p>A  <b>D3D10_SB_REGISTER_COMPONENT_TYPE</b> type that indicates the register component type.</p>
<p>The <b>D3D10_SB_REGISTER_COMPONENT_TYPE</b> enumeration is defined in the D3d10tokenizedprogramformat.hpp header file.</p>
</dd>

### -field <b>MinPrecision</b>

<dd>
<p>A <b>D3D11_SB_OPERAND_MIN_PRECISION</b> type that indicates a minimum precision of source and destination operands.</p>
<p>The <b>D3D11_SB_OPERAND_MIN_PRECISION</b> enumeration is defined in the D3d10tokenizedprogramformat.hpp header file.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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