---
UID: NC.dispmprt.DXGKCB_MAP_MEMORY
title: DXGKCB_MAP_MEMORY
author: windows-driver-content
description: The DxgkCbMapMemory function maps a range of translated physical addresses (associated with a memory resource assigned to a display adapter) into system space or the virtual address space of a user-mode process.
old-location: display\dxgkcbmapmemory.htm
ms.assetid: 916a4d1d-0c40-4125-89ae-488251b04810
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkCbMapMemory
req.alt-loc: dispmprt.h
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
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DXGKCB_MAP_MEMORY callback



## -description
<p>The <b>DxgkCbMapMemory</b> function maps a range of translated physical addresses (associated with a memory resource assigned to a display adapter) into system space or the virtual address space of a user-mode process.</p>


## -prototype

````
DXGKCB_MAP_MEMORY DxgkCbMapMemory;

NTSTATUS DxgkCbMapMemory(
  _In_  HANDLE              DeviceHandle,
  _In_  PHYSICAL_ADDRESS    TranslatedAddress,
  _In_  ULONG               Length,
  _In_  BOOLEAN             InIoSpace,
  _In_  BOOLEAN             MapToUserMode,
  _In_  MEMORY_CACHING_TYPE CacheType,
  _Out_ PVOID               *VirtualAddress
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceHandle</i> [in]

<dd>
<p>A handle that represents a display adapter. The display miniport driver previously obtained this handle in the <b>DeviceHandle</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560942">DXGKRNL_INTERFACE</a> structure that was passed to <a href="https://msdn.microsoft.com/ffacbb39-2581-4207-841d-28ce57fbc64d">DxgkDdiStartDevice</a>.</p>
</dd>

### -param <i>TranslatedAddress</i> [in]

<dd>
<p>The base translated physical address of the memory range to be mapped. The display miniport driver previously obtained this address by calling <a href="https://msdn.microsoft.com/cb627eab-93b9-49c5-bd35-4a57220366e7">DxgkCbGetDeviceInformation</a>.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The size, in bytes, of the range to be mapped.</p>
</dd>

### -param <i>InIoSpace</i> [in]

<dd>
<p>A Boolean value that specifies whether the range is in I/O space (<b>TRUE</b>) or memory space (<b>FALSE</b>).</p>
</dd>

### -param <i>MapToUserMode</i> [in]

<dd>
<p>A Boolean value that specifies whether the range is mapped into user-mode space or system space. If <b>TRUE</b>, the range is mapped into the (user-mode) virtual address space of the current process. If <b>FALSE</b>, the range is mapped into system space. If <i>InIoSpace</i> is <b>TRUE</b>, this parameter is ignored.</p>
</dd>

### -param <i>CacheType</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a> enumerator that specifies the caching behavior of the mapped range.</p>
</dd>

### -param <i>VirtualAddress</i> [out]

<dd>
<p>A pointer to a variable that receives the address of the beginning of the mapped range. The way that the mapped range is accessed depends on the values of <i>InIoSpace</i> and <i>MapToUserMode</i>. The following table summarizes the different ways that the mapped range is accessed.</p>
<table>
<tr>
<td></td>
<td><i>MapToUserMode</i> is <b>FALSE</b></td>
<td><i>MapToUserMode</i> is <b>TRUE</b></td>
</tr>
<tr>
<td><i>InIoSpace</i> is <b>FALSE</b></td>
<td>READ_REGISTER_X WRITE_REGISTER_X</td>
<td>User-mode code performs ordinary memory access.</td>
</tr>
<tr>
<td><i>InIoSpace</i> is <b>TRUE</b></td>
<td>READ_PORT_X WRITE_PORT_X</td>
<td>Not possible.</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>DxgkCbMapMemory</b> returns STATUS_SUCCESS if it succeeds. Otherwise, it returns one of the error codes defined in <i>Ntstatus.h</i>.</p>

## -remarks
<p>The PHYSICAL_ADDRESS data type is defined in <i>Ntdef.h</i>.</p>

<p>The PHYSICAL_ADDRESS data type is defined in <i>Ntdef.h</i>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_MAP_MEMORY callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
