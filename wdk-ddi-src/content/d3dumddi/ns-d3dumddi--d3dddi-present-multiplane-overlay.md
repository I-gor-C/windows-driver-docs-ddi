---
UID: NS.d3dumddi._D3DDDI_PRESENT_MULTIPLANE_OVERLAY
title: D3DDDI_PRESENT_MULTIPLANE_OVERLAY
author: windows-driver-content
description: Specifies an overlay plane to display.
old-location: display\d3dddi_present_multiplane_overlay.htm
old-project: display
ms.assetid: 45db9dbb-d1e1-4ed3-bf4d-99b6ac7542ae
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_PRESENT_MULTIPLANE_OVERLAY, D3DDDI_PRESENT_MULTIPLANE_OVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_PRESENT_MULTIPLANE_OVERLAY
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
req.iface: 
---

# D3DDDI_PRESENT_MULTIPLANE_OVERLAY structure



## -description
<p>Specifies an overlay plane to display.</p>


## -syntax

````
typedef struct _D3DDDI_PRESENT_MULTIPLANE_OVERLAY {
  UINT                                 LayerIndex;
  BOOL                                 Enabled;
  HANDLE                               hResource;
  UINT                                 SubResourceIndex;
  D3DDDI_MULTIPLANE_OVERLAY_ATTRIBUTES PlaneAttributes;
} D3DDDI_PRESENT_MULTIPLANE_OVERLAY;
````


## -struct-fields
<dl>

### -field <b>LayerIndex</b>

<dd>
<p>The zero-based index of the overlay plane to display. The top plane (in the z-direction) has index zero. The planes' index values must be sequential from top to bottom.</p>
</dd>

### -field <b>Enabled</b>

<dd>
<p>Indicates if the overlay plane specified by <b>LayerIndex</b> is enabled for display.</p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_PRESENT_MULTIPLANE_OVERLAY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
