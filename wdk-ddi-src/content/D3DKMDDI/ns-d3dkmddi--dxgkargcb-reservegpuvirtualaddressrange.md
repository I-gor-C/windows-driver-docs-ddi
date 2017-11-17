---
UID: NS.d3dkmddi._DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE
title: DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE
author: windows-driver-content
description: DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE is used with the DxgkCbReserveGpuVirtualAddressRangedevice driver interface (DDI) to allow the kernel mode driver to reserve a graphics processing unit (GPU) virtual address range during creation of a process.
old-location: display\dxgkargcb_reservegpuvirtualaddressrange.htm
ms.assetid: D555E595-4319-4FCC-84A7-52FA3F278FFD
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
req.alt-api: DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE
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
ms.keywords: DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE, DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE
req.iface: 
---

# DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE structure



## -description
<p><b>DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE</b> is used with the <a href="https://msdn.microsoft.com/26A827F1-1094-4A7D-9C63-758925EE6273">DxgkCbReserveGpuVirtualAddressRange</a>device driver interface (DDI) to allow the kernel mode driver to reserve a graphics processing unit (GPU) virtual address range during creation of a process. </p>


## -syntax

````
typedef struct _DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE {
  HANDLE hDxgkProcess;
  UINT64 SizeInBytes;
  UINT   Alignment;
  UINT64 StartVirtualAddress;
  UINT64 BaseAddress;
  union {
    struct {
      UINT AllowUserModeMapping  :1;
    };
    UINT   Flags;
  };
} DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE;
````


## -struct-fields
<dl>

### -field <b>hDxgkProcess</b>

<dd>
<p>The handle that was passed to <a href="https://msdn.microsoft.com/E5AAEEB1-C29E-4AA7-9F8E-2C2DCFADED81">DxgkDdiCreateProcess</a>.</p>
</dd>

### -field <b>SizeInBytes</b>

<dd>
<p>The size of the address range in bytes, this must be set to an integral multiple of the address space covered by a single page table entry.</p>
</dd>

### -field <b>Alignment</b>

<dd>
<p>The number of bytes to align the start address to. Must be a multiple of the address space covered by a single page table entry and a power of 2.</p>
</dd>

### -field <b>StartVirtualAddress</b>

<dd>
<p>The starting location of the reserved address range.</p>
</dd>

### -field <b>BaseAddress</b>

<dd>
<p>The base virtual address of the virtual address range in bytes. It must be aligned to the size of the address space, covered by a single page table entry.</p>
</dd>

### -field <b>AllowUserModeMapping</b>

<dd>
<p>Allow the user mode driver to map allocations to the range.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A single value containing the flags set in the structure.</p>
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
<a href="https://msdn.microsoft.com/26A827F1-1094-4A7D-9C63-758925EE6273">DxgkCbReserveGpuVirtualAddressRange</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/E5AAEEB1-C29E-4AA7-9F8E-2C2DCFADED81">DxgkDdiCreateProcess</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARGCB_RESERVEGPUVIRTUALADDRESSRANGE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
