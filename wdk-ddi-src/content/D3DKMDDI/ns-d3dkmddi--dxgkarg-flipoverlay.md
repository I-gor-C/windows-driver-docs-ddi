---
UID: NS.d3dkmddi._DXGKARG_FLIPOVERLAY
title: DXGKARG_FLIPOVERLAY
author: windows-driver-content
description: The DXGKARG_FLIPOVERLAY structure describes a new allocation to display for the overlay.
old-location: display\dxgkarg_flipoverlay.htm
ms.assetid: c5396581-e9f2-47eb-bb82-1e54f5def4d0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_FLIPOVERLAY
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
ms.keywords: DXGKARG_FLIPOVERLAY, DXGKARG_FLIPOVERLAY
req.iface: 
---

# DXGKARG_FLIPOVERLAY structure



## -description
<p>The DXGKARG_FLIPOVERLAY structure describes a new allocation to display for the overlay. </p>


## -syntax

````
typedef struct _DXGKARG_FLIPOVERLAY {
  HANDLE           hSource;
  PHYSICAL_ADDRESS SrcPhysicalAddress;
  UINT             SrcSegmentId;
  VOID             *pPrivateDriverData;
  UINT             PrivateDriverDataSize;
} DXGKARG_FLIPOVERLAY;
````


## -struct-fields
<dl>

### -field <b>hSource</b>

<dd>
<p>[in] A handle to the source allocation to be displayed.</p>
</dd>

### -field <b>SrcPhysicalAddress</b>

<dd>
<p>[in] The physical address, within the segment that <b>SrcSegmentId</b> specifies, of the allocation to be displayed.</p>
</dd>

### -field <b>SrcSegmentId</b>

<dd>
<p>[in] The identifier of a segment in which the allocation is currently paged.</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>[in] A pointer to a block of private data that is passed from the user-mode display driver to the display miniport driver. </p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>[in] The size, in bytes, of the block of private data that <b>pPrivateDriverData</b> points to.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/9e35a48b-1741-4ee2-8e15-6ce51ad4c0ad">DxgkDdiFlipOverlay</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_FLIPOVERLAY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
