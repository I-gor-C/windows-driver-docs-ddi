---
UID: NS.d3dkmthk._D3DKMT_EVICT
title: D3DKMT_EVICT
author: windows-driver-content
description: D3DKMT_EVICT is used with D3DKMTEvict to subtract one from the residency reference count.
old-location: display\d3dkmt_evict.htm
ms.assetid: 07785939-C3D1-4085-BA1A-91E8FEE52B70
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_EVICT
req.alt-loc: d3dkmthk.h
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
ms.keywords: D3DKMT_EVICT, D3DKMT_EVICT
req.iface: 
---

# D3DKMT_EVICT structure



## -description
<p><b>D3DKMT_EVICT</b> is used with <a href="https://msdn.microsoft.com/library/windows/hardware/dn906774">D3DKMTEvict</a> to subtract one from the residency reference count.</p>
<p>Once this count reaches zero, it will remove the allocation from the device residency list.
  </p>


## -syntax

````
typedef struct _D3DKMT_EVICT {
  D3DKMT_HANDLE       hDevice;
  UINT                NumAllocations;
  const D3DKMT_HANDLE *AllocationList;
  D3DDDI_EVICT_FLAGS  Flags;
  UINT64              NumBytesToTrim;
} D3DKMT_EVICT;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] Device that created the allocations passed to this call.</p>
</dd>

### -field <b>NumAllocations</b>

<dd>
<p>[in] Number of allocation handles in the <b>AllocationList</b> array.</p>
</dd>

### -field <b>AllocationList</b>

<dd>
<p>[in] An array of <b>NumAllocations</b> allocation handles to mark for eviction. All allocations must be created on <b>hDevice</b>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] Specifies eviction behavior as documented in <a href="https://msdn.microsoft.com/library/windows/hardware/dn906322">D3DDDI_EVICT_FLAGS</a>. </p>
</dd>

### -field <b>NumBytesToTrim</b>

<dd>
<p>[out] When non-zero, specifies how much the application should evict in order to meet its current memory budget.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906322">D3DDDI_EVICT_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906774">D3DKMTEvict</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_EVICT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
