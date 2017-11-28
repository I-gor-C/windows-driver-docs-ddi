---
UID: NS.d3dkmddi._DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY
title: DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY
author: windows-driver-content
description: DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY describes a residency allocation change operation.
old-location: display\dxgk_buildpagingbuffer_notifyresidency.htm
old-project: display
ms.assetid: 0E70F621-03CD-4593-88C7-DF6F2ADC902A
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY, DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY
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
req.alt-api: DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY
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

# DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY structure



## -description
<p><b> DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY</b> describes a residency allocation change operation.</p>


## -syntax

````
typedef struct _DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY {
  HANDLE                  hAllocation;
  D3DGPU_PHYSICAL_ADDRESS PhysicalAddress;
  union {
    UINT Resident  :1;
    UINT Reserved  :31;
  };
} DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY;
````


## -struct-fields
<dl>

### -field <b>hAllocation</b>

<dd>
<p>The kernel mode driver handle returned from <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>.</p>
</dd>

### -field <b>PhysicalAddress</b>

<dd>
<p>The physical address of the allocation. The physical address (0, 0) is invalid and is used when the allocation is being evicted.  </p>
</dd>

### -field <b>Resident</b>

<dd>
<p>Set to 0 when the allocation is evicted and set to 1 when the allocation is committed.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is not used and should be set to zero.</p>
</dd>
</dl>

## -remarks
<p>The paging operations is issued only for allocations, for which the kernel mode driver sets the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560966">DXGK_ALLOCATIONINFOFLAGS</a>::<b>ExplicitResidencyNotification</b> and <b>AccessedPhysically</b> flags.</p>

<p>The operation is issued after <i>FillVirtual</i> or <i>TransferVirtual</i> operations when the allocation is committed to a memory segment (<b>Resident</b> == 1). Note that the previous paging operations might not yet be finished by graphics processing unit (GPU).</p>

<p>The operation is issued before <i>TransferVirtual</i> operation when the allocation is evicted (<b>Resident</b> == 0) from a memory segment.
</p>

<p>Note that the <i>NotifyResidency</i> operation will be issued only once during allocation eviction/commitment, while there might be several <i>TransferVirtual</i>/<i>FillVirtual</i> operations for a single allocation.
</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557540">DXGKARG_BUILDPAGINGBUFFER</a>
</dt>
<dt>
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BUILDPAGINGBUFFER_NOTIFYRESIDENCY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
