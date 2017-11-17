---
UID: NS.d3dkmddi._DXGK_SEGMENTDESCRIPTOR4
title: DXGK_SEGMENTDESCRIPTOR4
author: windows-driver-content
description: The DXGK_SEGMENTDESCRIPTOR4 structure describes a programmable CPU host aperture.
old-location: display\dxgk_segmentdescriptor4.htm
ms.assetid: 0958443F-1554-47B0-83B9-283D98D927CE
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_SEGMENTDESCRIPTOR4
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
ms.keywords: DXGK_SEGMENTDESCRIPTOR4, DXGK_SEGMENTDESCRIPTOR4
req.iface: 
---

# DXGK_SEGMENTDESCRIPTOR4 structure



## -description
<p>The <b>DXGK_SEGMENTDESCRIPTOR4</b> structure describes a programmable CPU host aperture.</p>


## -syntax

````
typedef struct _DXGK_SEGMENTDESCRIPTOR4 {
  DXGK_SEGMENTFLAGS Flags;
  PHYSICAL_ADDRESS  BaseAddress;
  SIZE_T            Size;
  SIZE_T            CommitLimit;
  SIZE_T            SystemMemoryEndAddress;
  union {
    PHYSICAL_ADDRESS     CpuTranslatedAddress;
    DXGK_CPUHOSTAPERTURE CpuHostAperture;
  };
  UINT              NumInvalidMemoryRanges;
} DXGK_SEGMENTDESCRIPTOR4;
````


## -struct-fields
<dl>

### -field <b>Flags</b>

<dd>
<p>Segment bit field flags</p>
</dd>

### -field <b>BaseAddress</b>

<dd>
<p>The physical base address for the segment in the GPU.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of the segment in bytes.</p>
</dd>

### -field <b>CommitLimit</b>

<dd>
<p>The maximum number of bytes that can be committed to this segment. </p>
<div class="alert"><b>Note</b>  This applies to the aperture segment only.</div>
<div> </div>
</dd>

### -field <b>SystemMemoryEndAddress</b>

<dd>
<p>For segments that are partially composed of system memory, all allocations ending after this address are purged during hibernate.</p>
</dd>

### -field <b>CpuTranslatedAddress</b>

<dd>
<p>If <b>Flags.SupportsCpuHostAperture</b>==<b>FALSE</b> and the segment is CPU visible, this will be the CPU physical base address of the segment.</p>
</dd>

### -field <b>CpuHostAperture</b>

<dd>
<p>If <b>Flags.SupportsCpuHostAperture</b>==<b>TRUE</b>, this will have the CPU address and size of the <b>CPUHostAperture</b>.</p>
</dd>

### -field <b>NumInvalidMemoryRanges</b>

<dd>
<p>The number of invalid memory ranges in the segment. If this value is not zero, the kernel mode driver will be called with DdiQueryAdapterInfo(DXGKQAITYPE_SEGMENTMEMORYSTATE) to get information about invalid memory ranges.</p>
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