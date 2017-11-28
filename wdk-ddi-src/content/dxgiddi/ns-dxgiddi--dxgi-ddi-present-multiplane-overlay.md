---
UID: NS.dxgiddi._DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY
title: DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY
author: windows-driver-content
description: Specifies overlay planes to display.
old-location: display\dxgi_ddi_present_multiplane_overlay.htm
old-project: display
ms.assetid: 18811f98-df57-43ab-b8f7-26301abeb823
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY, DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY
req.alt-loc: Dxgiddi.h
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

# DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY structure



## -description
<p>Specifies overlay planes to display.</p>


## -syntax

````
typedef struct _DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY {
  UINT                                   LayerIndex;
  BOOL                                   Enabled;
  DXGI_DDI_HRESOURCE                     hResource;
  UINT                                   SubResourceIndex;
  DXGI_DDI_MULTIPLANE_OVERLAY_ATTRIBUTES PlaneAttributes;
} DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY;
````


## -struct-fields
<dl>

### -field <b>LayerIndex</b>

<dd>
<p>The zero-based index of the overlay plane to display. The top plane (in the z-direction) has index zero. The planes' index values must be sequential from top to bottom.</p>
</dd>

### -field <b>Enabled</b>

<dd>
<p>Indicates whether the overlay plane specified by <b>LayerIndex</b> is enabled for display.</p>
</dd>

### -field <b>hResource</b>

<dd>
<p>A handle to the resource that is displayed by using the overlay plane.</p>
</dd>

### -field <b>SubResourceIndex</b>

<dd>
<p>The zero-based index into the resource, which is specified by the handle in the <b>hResource</b> member. This index indicates the subresource, or surface, on which an overlay plane is to be displayed.</p>
</dd>

### -field <b>PlaneAttributes</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/hh780283">DXGI_DDI_MULTIPLANE_OVERLAY_ATTRIBUTES</a>  that specifies overlay plane attributes.</p>
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
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh780283">DXGI_DDI_MULTIPLANE_OVERLAY_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_PRESENT_MULTIPLANE_OVERLAY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
