---
UID: NS.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_PLANE2
title: DXGK_MULTIPLANE_OVERLAY_PLANE2
author: windows-driver-content
description: DXGK_MULTIPLANE_OVERLAY_PLANE2 is used with the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to specify an overlay plane to display.
old-location: display\dxgk_multiplane_overlay_plane2.htm
old-project: display
ms.assetid: 31A1EAFB-FA48-432D-963E-EA907B43F08A
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MULTIPLANE_OVERLAY_PLANE2, DXGK_MULTIPLANE_OVERLAY_PLANE2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_PLANE2
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_MULTIPLANE_OVERLAY_PLANE2 structure



## -description
<p><b>DXGK_MULTIPLANE_OVERLAY_PLANE2</b> is used with the <a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay2">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2</a> function to specify an overlay plane to display.</p>


## -syntax

````
typedef struct _DXGK_MULTIPLANE_OVERLAY_PLANE2 {
  UINT                                LayerIndex;
  BOOL                                Enabled;
  UINT                                AllocationSegment;
  PHYSICAL_ADDRESS                    AllocationAddress;
  HANDLE                              hAllocation;
  DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2 PlaneAttributes;
} DXGK_MULTIPLANE_OVERLAY_PLANE2;
````


## -struct-fields
<dl>

### -field LayerIndex

<dd>
<p>The zero-based index of the overlay plane to display. The top plane (in the z-direction) has index zero. The planes' index values must be sequential from top to bottom.</p>
</dd>

### -field Enabled

<dd>
<p>Indicates whether the overlay plane specified by <b>LayerIndex</b> is enabled for display.</p>
</dd>

### -field AllocationSegment

<dd>
<p>The identifier of a segment that data is read from.</p>
</dd>

### -field AllocationAddress

<dd>
<p>A <b>PHYSICAL_ADDRESS</b> data type (which is defined as <b>LARGE_INTEGER</b>) that indicates the physical address within the segment that <b>AllocationSegment</b> specifies, where the data is read.</p>
</dd>

### -field hAllocation

<dd>
<p>A handle to the allocation to be displayed on the overlay plane.</p>
</dd>

### -field PlaneAttributes

<dd>
<p>A structure of type <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-attributes2.md">DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2</a> that specifies overlay plane attributes.</p>
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
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay2">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-multiplane-overlay-attributes2.md">DXGK_MULTIPLANE_OVERLAY_ATTRIBUTES2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_MULTIPLANE_OVERLAY_PLANE2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
