---
UID: NS.D3DUMDDI.D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO
title: D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO
author: windows-driver-content
description: Specifies the support attributes that the hardware provides for multiplane overlays.
old-location: display\d3dddi_check_multiplane_overlay_support_plane_info.htm
old-project: display
ms.assetid: dda53c24-bd3d-4476-bbb4-b00b0d8aeb3d
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO, D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO structure



## -description
Specifies the support attributes that the hardware provides for multiplane overlays.


## -syntax

````
typedef struct D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO {
  HANDLE                               hResource;
  UINT                                 SubResourceIndex;
  D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES PlaneAttributes;
} D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO;
````


## -struct-fields

### -field hResource

A handle to the resource. The display miniport driver must set this member to a value that it can use to refer to its private tracking structure for the resource.

### -field SubResourceIndex

The zero-based index into the resource, which is specified by the handle in the <b>hResource</b> member. This index indicates the subresource, or surface, on which an overlay plane is to be displayed.

### -field PlaneAttributes

A <a href="display.d3dddi_multiplane_overlay_attributes">D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES</a> structure that specifies overlay plane attributes.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="display.d3dddi_multiplane_overlay_attributes">D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
