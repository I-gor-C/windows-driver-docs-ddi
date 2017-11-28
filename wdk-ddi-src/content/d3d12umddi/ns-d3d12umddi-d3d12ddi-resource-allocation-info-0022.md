---
UID: NS.d3d12umddi.D3D12DDI_RESOURCE_ALLOCATION_INFO_0022
title: D3D12DDI_RESOURCE_ALLOCATION_INFO_0022
author: windows-driver-content
description: Specifies information for resource allocation.
old-location: display\d3d12ddi_resource_allocation_info_0022.htm
old-project: display
ms.assetid: 71CDBF47-B32D-4084-B2F6-9F8C037FCB79
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_RESOURCE_ALLOCATION_INFO_0022, D3D12DDI_RESOURCE_ALLOCATION_INFO_0022
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_RESOURCE_ALLOCATION_INFO_0022
req.alt-loc: D3d12umddi.h
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

# D3D12DDI_RESOURCE_ALLOCATION_INFO_0022 structure



## -description
<p>Specifies information for resource allocation.</p>


## -syntax

````
typedef struct D3D12DDI_RESOURCE_ALLOCATION_INFO_0022 {
  UINT64                   ResourceDataSize;
  AdditionalDataHeaderSize UINT64;
  UINT64                   AdditionalDataSize;
  UINT32                   ResourceDataAlignment;
  UINT32                   AdditionalDataHeaderAlignment;
  UINT32                   AdditionalDataAlignment;
  D3D12DDI_TEXTURE_LAYOUT  Layout;
  UINT8                    MipLevelSwizzleTransition[5];
  UINT8                    PlaneSliceSwizzleTransition[2];
} D3D12DDI_RESOURCE_ALLOCATION_INFO_0022;
````


## -struct-fields
<dl>

### -field <b>ResourceDataSize</b>

<dd>
<p>The data size of  the resource. </p>
</dd>

### -field <b>UINT64</b>

<dd>
<p>The additional size of the data header.</p>
</dd>

### -field <b>AdditionalDataSize</b>

<dd>
<p>The additional data size.</p>
</dd>

### -field <b>ResourceDataAlignment</b>

<dd>
<p>The data alignment of the resource.</p>
</dd>

### -field <b>AdditionalDataHeaderAlignment</b>

<dd>
<p>The data alignment of the additional header.</p>
</dd>

### -field <b>AdditionalDataAlignment</b>

<dd>
<p>The additional data alignment. </p>
</dd>

### -field <b>Layout</b>

<dd>
<p>The texture layout as a <a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi-texture-layout.md">D3D12DDI_TEXTURE_LAYOUT</a> value. </p>
</dd>

### -field <b>MipLevelSwizzleTransition</b>

<dd>
<p>The MIP level for a swizzle transition.</p>
</dd>

### -field <b>PlaneSliceSwizzleTransition</b>

<dd>
<p>The plane slice for a swizzle transition. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d12umddi\ne-d3d12umddi-d3d12ddi-texture-layout.md">D3D12DDI_TEXTURE_LAYOUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D12DDI_RESOURCE_ALLOCATION_INFO_0022 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
