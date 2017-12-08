---
UID: NS.d3dukmdt.D3DDDI_RESERVEGPUVIRTUALADDRESS
title: D3DDDI_RESERVEGPUVIRTUALADDRESS
author: windows-driver-content
description: D3DDDI_RESERVEGPUVIRTUALADDRESS is used with pfnReserveGpuVirtualAddressCb to reserve an address range in the graphics processing unit (GPU) virtual address space of the current process.
old-location: display\d3dddi_reservegpuvirtualaddress.htm
old-project: display
ms.assetid: 89E8FCC6-B618-4D7E-B1E6-59E85261BE3C
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_RESERVEGPUVIRTUALADDRESS, D3DDDI_RESERVEGPUVIRTUALADDRESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_RESERVEGPUVIRTUALADDRESS
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

# D3DDDI_RESERVEGPUVIRTUALADDRESS structure



## -description
<p><b>D3DDDI_RESERVEGPUVIRTUALADDRESS</b> is used with <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reservegpuvirtualaddresscb.md">pfnReserveGpuVirtualAddressCb</a> to reserve an address range in the graphics processing unit (GPU) virtual address space of the current process.</p>


## -syntax

````
typedef struct D3DDDI_RESERVEGPUVIRTUALADDRESS {
  union {
    D3DKMT_HANDLE hPagingQueue;
    D3DKMT_HANDLE hAdapter;
  };
  D3DGPU_VIRTUAL_ADDRESS BaseAddress;
  D3DGPU_VIRTUAL_ADDRESS MinimumAddress;
  D3DGPU_VIRTUAL_ADDRESS MaximumAddress;
  D3DGPU_SIZE_T          Size;
  union {
    D3DDDIGPUVIRTUALADDRESS_RESERVATION_TYPE ReservationType;
    UINT                                     Reserved0;
  };
  union {
    UINT64 DriverProtection;
    UINT64 Reserved1;
  };
  D3DGPU_VIRTUAL_ADDRESS VirtualAddress;
  union {
    UINT64 PagingFenceValue;
    UINT64 Reserved2;
  };
} D3DDDI_RESERVEGPUVIRTUALADDRESS;
````


## -struct-fields
<dl>

### -field hPagingQueue

<dd>
<p>Paging queue to synchronize the operation on.</p>
</dd>

### -field hAdapter

<dd>
<p>DirectX graphics adapter handle. </p>
</dd>

### -field BaseAddress

<dd>
<p>(Optional) If <b>non-NULL</b>, the video memory manager will attempt to use this address as the base address for the reserved range. If the range from <b>BaseAddress</b> to <b>BaseAddress</b>+<b>Size</b> isn’t free, the call will fail. When this parameter is <b>non-NULL</b>, <b>MinimumAddress</b> and <b>MaximumAddress</b> are ignored.</p>
<p><b>BaseAddress</b> is in bytes and must be aligned to 64KB boundary.
</p>
<p>If <b>NULL</b> is specified the video memory manager will pick the base address for the allocation within the specified <b>MinimumAddress</b> and <b>MaximumAddress</b>.
</p>
</dd>

### -field MinimumAddress

<dd>
<p>(Optional) Specifies the minimum GPU virtual address to consider for the reserved range.</p>
<p><b>MinimumAddress</b> is in bytes and must be aligned to 64KB boundary.</p>
<p>This parameter is ignored when <b>BaseAddress</b> != <b>NULL</b>.</p>
</dd>

### -field MaximumAddress

<dd>
<p>(Optional) Specifies the maximum GPU virtual address to consider for the reserved range. the video memory manager will guarantee that <b>BaseAddress</b>+<b>Size</b> &lt;= <b>MaximumAddress</b>. If this is set to NULL the video memory manager will not apply any limit.</p>
<p><b>MaximumAddress</b> is in bytes and must be aligned to 64KB boundary.</p>
<p>This parameter is ignored when <b>BaseAddress</b> != <b>NULL</b>.</p>
</dd>

### -field Size

<dd>
<p>Specify the size of the range to reserve in bytes. Must be a multiple of 64KB.</p>
</dd>

### -field ReservationType

<dd>
<p>Specifies the virtual address reservation type.</p>
</dd>

### -field Reserved0

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field DriverProtection

<dd>
<p>Specifies the driver-specific protection</p>
</dd>

### -field Reserved1

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field VirtualAddress

<dd>
<p>[out] The reserved virtual address.</p>
</dd>

### -field PagingFenceValue

<dd>
<p>Paging fence identifier for synchronization</p>
</dd>

### -field Reserved2

<dd>
<p>This member is reserved and should be set to zero.</p>
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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reservegpuvirtualaddresscb.md">pfnReserveGpuVirtualAddressCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_RESERVEGPUVIRTUALADDRESS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
