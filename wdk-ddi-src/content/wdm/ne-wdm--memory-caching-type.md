---
UID: NE.wdm._MEMORY_CACHING_TYPE
title: MEMORY_CACHING_TYPE
author: windows-driver-content
description: The MEMORY_CACHING_TYPE enumeration type specifies the permitted caching behavior when allocating or mapping memory.
old-location: kernel\memory_caching_type.htm
old-project: kernel
ms.assetid: 14cde545-e9bb-4b96-ba10-a63595e8a107
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Ntddk.h, Wdm.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MEMORY_CACHING_TYPE
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# MEMORY_CACHING_TYPE enumeration



## -description
<p>The <b>MEMORY_CACHING_TYPE</b> enumeration type specifies the permitted caching behavior when allocating or mapping memory.</p>


## -syntax

````
typedef enum _MEMORY_CACHING_TYPE { 
  MmNonCached               = 0,
  MmCached                  = 1,
  MmWriteCombined           = 2,
  MmHardwareCoherentCached  = 3,
  MmNonCachedUnordered      = 4,
  MmUSWCCached              = 5,
  MmMaximumCacheType        = 6
} MEMORY_CACHING_TYPE;
````


## -enum-fields
<dl>

### -field <a id="MmNonCached"></a><a id="mmnoncached"></a><a id="MMNONCACHED"></a><b>MmNonCached</b>

<dd>
<p>The requested memory should not be cached by the processor.</p>
</dd>

### -field <a id="MmCached"></a><a id="mmcached"></a><a id="MMCACHED"></a><b>MmCached</b>

<dd>
<p>The processor should cache the requested memory.</p>
</dd>

### -field <a id="MmWriteCombined"></a><a id="mmwritecombined"></a><a id="MMWRITECOMBINED"></a><b>MmWriteCombined</b>

<dd>
<p>The requested memory should not be cached by the processor, but writes to the memory can be combined by the processor.</p>
</dd>

### -field <a id="MmHardwareCoherentCached"></a><a id="mmhardwarecoherentcached"></a><a id="MMHARDWARECOHERENTCACHED"></a><b>MmHardwareCoherentCached</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="MmNonCachedUnordered"></a><a id="mmnoncachedunordered"></a><a id="MMNONCACHEDUNORDERED"></a><b>MmNonCachedUnordered</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="MmUSWCCached"></a><a id="mmuswccached"></a><a id="MMUSWCCACHED"></a><b>MmUSWCCached</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="MmMaximumCacheType"></a><a id="mmmaximumcachetype"></a><a id="MMMAXIMUMCACHETYPE"></a><b>MmMaximumCacheType</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>Processor translation buffers cache virtual to physical address translations. These translation buffers allow many virtual addresses to map a single physical address. However, only one caching behavior is allowed for any given physical address translation. Therefore, if a driver maps two different virtual address ranges to the same physical address, it must ensure that it specifies the same caching behavior for both. Otherwise, the processor behavior is undefined with unpredictable system results.</p>

<p>Processor translation buffers cache virtual to physical address translations. These translation buffers allow many virtual addresses to map a single physical address. However, only one caching behavior is allowed for any given physical address translation. Therefore, if a driver maps two different virtual address ranges to the same physical address, it must ensure that it specifies the same caching behavior for both. Otherwise, the processor behavior is undefined with unpredictable system results.</p>

<p>Processor translation buffers cache virtual to physical address translations. These translation buffers allow many virtual addresses to map a single physical address. However, only one caching behavior is allowed for any given physical address translation. Therefore, if a driver maps two different virtual address ranges to the same physical address, it must ensure that it specifies the same caching behavior for both. Otherwise, the processor behavior is undefined with unpredictable system results.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Ntddk.h or Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554464">MmAllocateContiguousMemorySpecifyCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554507">MmFreeContiguousMemorySpecifyCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554618">MmMapIoSpace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554629">MmMapLockedPagesSpecifyCache</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554640">MmMapLockedPagesWithReservedMapping</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MEMORY_CACHING_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
