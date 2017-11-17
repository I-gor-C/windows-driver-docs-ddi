---
UID: NS.d3dumddi.D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO
title: D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO
author: windows-driver-content
description: Specifies the support attributes that the hardware provides for multiplane overlays.
old-location: display\d3dddi_check_multiplane_overlay_support_plane_info.htm
ms.assetid: dda53c24-bd3d-4476-bbb4-b00b0d8aeb3d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO
req.alt-loc: D3dumddi.h
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
ms.keywords: D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO, D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO
req.iface: 
---

# D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO structure



## -description
<p>Specifies the support attributes that the hardware provides for multiplane overlays.</p>


## -syntax

````
typedef struct D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO {
  HANDLE                               hResource;
  UINT                                 SubResourceIndex;
  D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES PlaneAttributes;
} D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>A handle to the resource. The display miniport driver must set this member to a value that it can use to refer to its private tracking structure for the resource.</p>
</dd>

### -field <b>SubResourceIndex</b>

<dd>
<p>The zero-based index into the resource, which is specified by the handle in the <b>hResource</b> member. This index indicates the subresource, or surface, on which an overlay plane is to be displayed.</p>
</dd>

### -field <b>PlaneAttributes</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh780234">D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES</a> structure that specifies overlay plane attributes.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh780234">D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
