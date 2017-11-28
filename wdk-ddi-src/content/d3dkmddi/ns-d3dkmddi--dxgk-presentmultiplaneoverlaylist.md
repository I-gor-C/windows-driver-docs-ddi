---
UID: NS.d3dkmddi._DXGK_PRESENTMULTIPLANEOVERLAYLIST
title: DXGK_PRESENTMULTIPLANEOVERLAYLIST
author: windows-driver-content
description: Specifies an overlay plane to display in a call to the DxgkDdiPresent function.
old-location: display\dxgk_presentmultiplaneoverlaylist.htm
old-project: display
ms.assetid: 970b3155-9e81-4725-90ee-079339c1d5c5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_PRESENTMULTIPLANEOVERLAYLIST, DXGK_PRESENTMULTIPLANEOVERLAYLIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_PRESENTMULTIPLANEOVERLAYLIST
req.alt-loc: D3dkmddi.h
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

# DXGK_PRESENTMULTIPLANEOVERLAYLIST structure



## -description
<p>Specifies an overlay plane to display in a call to the <a href="display.dxgkddipresent">DxgkDdiPresent</a> function.</p>


## -syntax

````
typedef struct _DXGK_PRESENTMULTIPLANEOVERLAYLIST {
  UINT             LayerIndex;
  BOOL             Enabled;
  HANDLE           hDeviceSpecificAllocation;
  struct {
    UINT SegmentId  :5;
    UINT Reserved  :27;
  };
  PHYSICAL_ADDRESS PhysicalAddress;
} DXGK_PRESENTMULTIPLANEOVERLAYLIST;
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

### -field <b>hDeviceSpecificAllocation</b>

<dd>
<p>A handle to the device-specific allocation that corresponds to the non device-specific allocation. The display miniport driver must set <b>hDeviceSpecificAllocation</b> to a handle value that it can use to refer to its private tracking structure for the allocation.</p>
</dd>

### -field <b>SegmentId</b>

<dd>
<p>[in] The identifier of a segment that data is read from.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>[in] A <b>PHYSICAL_ADDRESS</b> data type (which is defined as <b>LARGE_INTEGER</b>) that indicates the physical address, within the segment that <b>SegmentId</b> specifies, where the data is read.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddipresent">DxgkDdiPresent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_PRESENTMULTIPLANEOVERLAYLIST structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
