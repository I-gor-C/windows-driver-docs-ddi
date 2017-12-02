---
UID: NS.d3dukmdt.D3DDDI_UPDATEALLOCPROPERTY
title: D3DDDI_UPDATEALLOCPROPERTY
author: windows-driver-content
description: D3DDDI_UPDATEALLOCPROPERTY describes the parameters needed to update an allocation.
old-location: display\d3dddi_updateallocproperty.htm
old-project: display
ms.assetid: 4A8EBF10-23A3-4D91-BCF7-8FD4D0708949
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_UPDATEALLOCPROPERTY, D3DDDI_UPDATEALLOCPROPERTY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_UPDATEALLOCPROPERTY
req.alt-loc: d3dukmdt.h
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

# D3DDDI_UPDATEALLOCPROPERTY structure



## -description
<p>D3DDDI_UPDATEALLOCPROPERTY describes the parameters needed to update an allocation.</p>


## -syntax

````
typedef struct D3DDDI_UPDATEALLOCPROPERTY {
  D3DKMT_HANDLE                        hPagingQueue;
  D3DKMT_HANDLE                        hAllocation;
  UINT                                 SupportedSegmentSet;
  DXGK_SEGMENTPREFERENCE               PreferredSegment;
  D3DDDI_UPDATEALLOCPROPERTY_FLAGS     Flags;
  UINT64                               PagingFenceValue;
  union {
    struct {
      UINT SetAccessedPhysically   :1;
      UINT SetSupportedSegmentSet   :1;
      UINT SetPreferredSegment   :1;
      UINT Reserved  :29;
    };
    UINT   PropertyMaskValue;
  };
} D3DDDI_UPDATEALLOCPROPERTY;
````


## -struct-fields
<dl>

### -field hPagingQueue

<dd>
<p>[in] A Handle to the paging queue used to synchronize paging operations for this call.</p>
</dd>

### -field hAllocation

<dd>
<p>[in] A handle to the allocation that will be updated.</p>
</dd>

### -field SupportedSegmentSet

<dd>
<p>[in] An index for the new supported segment set. If the current supported segment set is the same, then this will be ignored.</p>
</dd>

### -field PreferredSegment

<dd>
<p>[in] An index for the new preferred segment set. If the current preferred segment set is the same, then this will be ignored.</p>
</dd>

### -field Flags

<dd>
<p>[in] The flags that will be used to update the allocation.</p>
</dd>

### -field PagingFenceValue

<dd>
<p>[out] The paging fence value that will be synchronized with before using the new allocation. Applies to the monitored fence synchronization object associated with hPagingQueue.</p>
</dd>

### -field SetAccessedPhysically 

<dd>
<p>A UINT value that specifies whether the allocation is accessed by its physical address.</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>PropertyMaskValue</b> member (0x00000001).</p>
</dd>

### -field SetSupportedSegmentSet 

<dd>
<p>A UINT value that specifies whether the supported segment is set to a new value.</p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit <b>PropertyMaskValue</b> member (0x00000010).</p>
</dd>

### -field SetPreferredSegment 

<dd>
<p>A UINT value that specifies whether the preferred segment is set to a new value.</p>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>PropertyMaskValue</b> member (0x00000100).</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 29 bits (0xFFFFFFFE) of the 32-bit <b>PropertyMaskValue</b> member to zeros.</p>
</dd>

### -field PropertyMaskValue

<dd>
<p>A member in the union that is contained in D3DDDI_UPDATEALLOCPROPERTY that can hold one 32-bit value that identifies how to update an allocation.</p>
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
<p>Available in Windows 10 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>