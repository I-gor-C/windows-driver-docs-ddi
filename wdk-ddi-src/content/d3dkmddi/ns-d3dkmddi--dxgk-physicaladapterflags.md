---
UID: NS.d3dkmddi._DXGK_PHYSICALADAPTERFLAGS
title: DXGK_PHYSICALADAPTERFLAGS
author: windows-driver-content
description: DXGK_PHYSICALADAPTERFLAGS defines a set of flags that used to indicate the type of memory management model that is supported by a device.
old-location: display\dxgk_physicaladapterflags.htm
old-project: display
ms.assetid: AACF0C99-D6E2-4C7C-BAE6-BF558FDAFDE0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_PHYSICALADAPTERFLAGS, DXGK_PHYSICALADAPTERFLAGS
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
req.alt-api: DXGK_PHYSICALADAPTERFLAGS
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

# DXGK_PHYSICALADAPTERFLAGS structure



## -description
<p><b>DXGK_PHYSICALADAPTERFLAGS</b> defines a set of flags that used to indicate the type of memory management model that is supported by a device.</p>


## -syntax

````
typedef struct _DXGK_PHYSICALADAPTERFLAGS {
  union {
    struct {
      UINT IoMmuSupported  :1;
      UINT GpuMmuSupported  :1;
      UINT MovingPagingSupported  :1;
      UINT VPRPagingContextRequired  :1;
      UINT Reserved  :28;
    };
    UINT   Value;
  };
} DXGK_PHYSICALADAPTERFLAGS;
````


## -struct-fields
<dl>

### -field IoMmuSupported

<dd>
<p>Indicates that the CPU and GPU share a common address space and common page tables.</p>
</dd>

### -field GpuMmuSupported

<dd>
<p>Indicates that the video memory manager manages the GPU memory management unit and underlying page tables to expose services to the user mode driver.</p>
</dd>

### -field MovingPagingSupported

<dd>
<p>Indicates that the device driver is capable of moving content to a new destination on the same memory segment.</p>
</dd>

### -field VPRPagingContextRequired

<dd>
<p>Indicates that the device driver requires that move paging operations done within a Video Protected Region occur on a different paging context than standard paging operations.</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field Value

<dd>
<p>The consolidated  value of the bitfield members in this structure.</p>
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