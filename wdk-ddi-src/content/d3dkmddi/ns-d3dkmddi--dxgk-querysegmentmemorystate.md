---
UID: NS.d3dkmddi._DXGK_QUERYSEGMENTMEMORYSTATE
title: DXGK_QUERYSEGMENTMEMORYSTATE
author: windows-driver-content
description: DXGK_QUERYSEGMENTMEMORYSTATE is used with DxgkDdiQueryAdapterInfo to query invalid graphics processing unit (GPU) memory ranges.
old-location: display\dxgk_querysegmentmemorystate.htm
old-project: display
ms.assetid: 565D8D8D-6EBB-4303-8F7E-E2A4B1DAE4EA
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_QUERYSEGMENTMEMORYSTATE, DXGK_QUERYSEGMENTMEMORYSTATE, DXGK_SEGMENTMEMORYSTATE
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
req.alt-api: DXGK_QUERYSEGMENTMEMORYSTATE
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

# DXGK_QUERYSEGMENTMEMORYSTATE structure



## -description
<p><b>DXGK_QUERYSEGMENTMEMORYSTATE</b> is used with <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> to query invalid graphics processing unit (GPU) memory ranges.</p>


## -syntax

````
typedef struct _DXGK_QUERYSEGMENTMEMORYSTATE {
  WORD             DriverSegmentId;
  WORD             PhysicalAdapterIndex;
  UINT             NumInvalidMemoryRanges;
  DXGK_MEMORYRANGE *pMemoryRanges;
} DXGK_QUERYSEGMENTMEMORYSTATE;
````


## -struct-fields
<dl>

### -field <b>DriverSegmentId</b>

<dd>
<p>A  1-based segment identifier of a local GPU memory segment.</p>
</dd>

### -field <b>PhysicalAdapterIndex</b>

<dd>
<p>Physical adapter index in a linked display adapter link.</p>
</dd>

### -field <b>NumInvalidMemoryRanges</b>

<dd>
<p>The number of entries in the <b>pMemoryRanges</b> array. This is the value returned by the kernel mode driver in <a href="https://msdn.microsoft.com/library/windows/hardware/dn906842">DXGK_SEGMENTDESCRIPTOR4</a>.</p>
</dd>

### -field <b>pMemoryRanges</b>

<dd>
<p>Array of <a href="https://msdn.microsoft.com/library/windows/hardware/dn906829">DXGK_MEMORYRANGE</a> structures for the invalid memory ranges.</p>
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
<a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906842">DXGK_SEGMENTDESCRIPTOR4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906829">DXGK_MEMORYRANGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_QUERYSEGMENTMEMORYSTATE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
