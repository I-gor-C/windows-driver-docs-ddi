---
UID: NS.d3dukmdt.D3DDDI_MAPGPUVIRTUALADDRESS
title: D3DDDI_MAPGPUVIRTUALADDRESS
author: windows-driver-content
description: D3DDDI_MAPGPUVIRTUALADDRESS is used with pfnMapGpuVirtualAddressCb to map a graphics processing unit (GPU) virtual address ranges to a specific allocation range or to put it to the Invalid or Zero state.
old-location: display\d3dddi_mapgpuvirtualaddress.htm
old-project: display
ms.assetid: A23F5847-0DA9-4F3F-B1C1-DACCA35DBC53
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_MAPGPUVIRTUALADDRESS, D3DDDI_MAPGPUVIRTUALADDRESS
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
req.alt-api: D3DDDI_MAPGPUVIRTUALADDRESS
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

# D3DDDI_MAPGPUVIRTUALADDRESS structure



## -description
<p><b>D3DDDI_MAPGPUVIRTUALADDRESS</b> is used with <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-mapgpuvirtualaddresscb.md">pfnMapGpuVirtualAddressCb</a> to map a graphics processing unit (GPU) virtual address ranges to a specific allocation range or to put it to the <i>Invalid</i> or <i>Zero</i> state.</p>


## -syntax

````
typedef struct D3DDDI_MAPGPUVIRTUALADDRESS {
  D3DKMT_HANDLE                           hPagingQueue;
  D3DGPU_VIRTUAL_ADDRESS                  BaseAddress;
  D3DGPU_VIRTUAL_ADDRESS                  MinimumAddress;
  D3DGPU_VIRTUAL_ADDRESS                  MaximumAddress;
  D3DKMT_HANDLE                           hAllocation;
  D3DGPU_SIZE_T                           OffsetInPages;
  D3DGPU_SIZE_T                           SizeInPages;
  D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE Protection;
  UINT64                                  DriverProtection;
  UINT                                    Reserved0;
  UINT64                                  Reserved1;
  D3DGPU_VIRTUAL_ADDRESS                  VirtualAddress;
  UINT64                                  PagingFenceValue;
} D3DDDI_MAPGPUVIRTUALADDRESS;
````


## -struct-fields
<dl>

### -field <b>hPagingQueue</b>

<dd>
<p>A handle for the device paging queue, used for the operation.</p>
</dd>

### -field <b>BaseAddress</b>

<dd>
<p>(Optional) If non-<b>NULL</b>, the video memory manager will attempt to use this address as the base address for the mapping. If the range from <b>BaseAddress</b> to <b>BaseAddress</b>+<b>Size</b> isn’t free, it must belong to a range, previously obtained by calling <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reservegpuvirtualaddresscb.md">pfnReserveGpuVirtualAddressCb</a> or <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-mapgpuvirtualaddresscb.md">pfnMapGpuVirtualAddressCb</a>. 
The <b>BaseAddress</b> value is in bytes and must be aligned to CPU page boundary.
If <b>NULL</b> is specified, the video memory manager will pick the base address for the allocation within the specified <b>MinimumAddress</b> and <b>MaximumAddress</b>.</p>
</dd>

### -field <b>MinimumAddress</b>

<dd>
<p>(Optional) Specifies the minimum GPU virtual address to consider for the mapped range. 
The <b>MinimumAddress</b> value is in bytes and must be aligned to 4KB page. 
This parameter is ignored when <b>BaseAddress</b> != <b>NULL.</b></p>
</dd>

### -field <b>MaximumAddress</b>

<dd>
<p>
(Optional) Specifies the maximum GPU virtual address to consider for the mapped range. the video memory manager will guarantee that <b>BaseAddress</b>+<b>Size</b> &lt;= <b>MaximumAddress</b>. If this is set to <b>NULL</b> the video memory manager will not apply any limit.
The <b>MaximumAddress</b> value is in bytes and must be aligned to the 4KB page.
This parameter is ignored when <b>BaseAddress</b> != NULL.
</p>
</dd>

### -field <b>hAllocation</b>

<dd>
<p>Handle to the allocation being mapped into the GPU virtual address space. Must be <b>NULL</b> when <b>Protection.NoAccess</b> or <b>Protection.Zero</b> is specified.</p>
</dd>

### -field <b>OffsetInPages</b>

<dd>
<p>Specifies the offset, in 4KB, to the starting page within the specified allocation that must be mapped.</p>
</dd>

### -field <b>SizeInPages</b>

<dd>
<p>Specifies the size of the range to map in 4KB pages.</p>
</dd>

### -field <b>Protection</b>

<dd>
<p>
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddigpuvirtualaddress-protection-type.md">D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE</a> structure that specifies the protection on the GPU virtual address that is mapped.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="Write"></a><a id="write"></a><a id="WRITE"></a><dl>

### -field <b>Write</b>

</dl>
</td>
<td width="60%">
<p>The pages will be allowed read-write access.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="Execute"></a><a id="execute"></a><a id="EXECUTE"></a><dl>

### -field <b>Execute</b>

</dl>
</td>
<td width="60%">
<p>The pages will be allowed the execute access.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NoAccess"></a><a id="noaccess"></a><a id="NOACCESS"></a><dl>

### -field <b>NoAccess</b>

</dl>
</td>
<td width="60%">
<p>The pages will be put to the invalid state (<b>hAllocation</b> must be <b>NULL</b>).</p>
</td>
</tr>
<tr>
<td width="40%"><a id="Zero"></a><a id="zero"></a><a id="ZERO"></a><dl>

### -field <b>Zero</b>

</dl>
</td>
<td width="60%">
<p>The pages will be put to the Zero state (<b>hAllocation</b> must be <b>NULL</b>).In this state reads will return zero and writes will be discarded.
</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DriverProtection</b>

<dd>
<p>Specifies a driver specific 64bits protection value associated with the VA range being allocated. The specified driver protection will be used in call to <a href="display.dxgkddiupdatepagetable">DxgkDdiUpdatePageTable</a> for page table entries corresponding to this virtual address range.</p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>This member is reserved and should be set to zero.</p>
</dd>

### -field <b>VirtualAddress</b>

<dd>
<p>The virtual address assigned to the allocation.</p>
</dd>

### -field <b>PagingFenceValue</b>

<dd>
<p>Represents the device paging fence value that the video memory manager will signal when the map operation completes on the GPU.
The user mode driver must ensure that this fence is retired or explicitly wait on either the CPU or the GPU on that fence before allowing the GPU to access the mapped range or an unrecoverable fault may occur.
A zero fence value might be returned, meaning that the operation is already completed.</p>
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
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddigpuvirtualaddress-protection-type.md">D3DDDIGPUVIRTUALADDRESS_PROTECTION_TYPE</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-reservegpuvirtualaddresscb.md">pfnReserveGpuVirtualAddressCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-mapgpuvirtualaddresscb.md">pfnMapGpuVirtualAddressCb</a>
</dt>
<dt>
<a href="display.dxgkddiupdatepagetable">DxgkDdiUpdatePageTable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_MAPGPUVIRTUALADDRESS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
