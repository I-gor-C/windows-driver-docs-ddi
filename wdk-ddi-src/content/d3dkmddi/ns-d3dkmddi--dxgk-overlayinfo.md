---
UID: NS.d3dkmddi._DXGK_OVERLAYINFO
title: DXGK_OVERLAYINFO
author: windows-driver-content
description: The DXGK_OVERLAYINFO structure describes parameters that are required to create or modify an overlay.
old-location: display\dxgk_overlayinfo.htm
old-project: display
ms.assetid: 7c2a7484-452f-4801-b650-3d8221740892
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_OVERLAYINFO, DXGK_OVERLAYINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_OVERLAYINFO
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

# DXGK_OVERLAYINFO structure



## -description
<p>The DXGK_OVERLAYINFO structure describes parameters that are required to create or modify an overlay. </p>


## -syntax

````
typedef struct _DXGK_OVERLAYINFO {
  HANDLE           hAllocation;
  PHYSICAL_ADDRESS PhysicalAddress;
  UINT             SegmentId;
  RECT             DstRect;
  RECT             SrcRect;
  VOID             *pPrivateDriverData;
  UINT             PrivateDriverDataSize;
} DXGK_OVERLAYINFO;
````


## -struct-fields
<dl>

### -field <b>hAllocation</b>

<dd>
<p>[in] A handle to the allocation to be displayed on the overlay.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>[in] The physical address, within the segment that <b>SegmentId</b> specifies, of the allocation to be displayed.</p>
</dd>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment in which the allocation is currently paged-in.</p>
</dd>

### -field <b>DstRect</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that contains the overlay destination rectangle, in device coordinates.</p>
</dd>

### -field <b>SrcRect</b>

<dd>
<p>[in] A RECT structure that contains the overlay source rectangle, in device coordinates.</p>
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
<a href="display.dxgkddicreateoverlay">DxgkDdiCreateOverlay</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557572">DXGKARG_CREATEOVERLAY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559496">DXGKARG_UPDATEOVERLAY</a>
</dt>
<dt>
<a href="display.dxgkddiupdateoverlay">DxgkDdiUpdateOverlay</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_OVERLAYINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
