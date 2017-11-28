---
UID: NF.ntifs.RtlFreeHeap
title: RtlFreeHeap
author: windows-driver-content
description: The RtlFreeHeap routine frees a memory block that was allocated from a heap by RtlAllocateHeap.
old-location: ifsk\rtlfreeheap.htm
old-project: ifsk
ms.assetid: 5e8b6bd7-71e7-45ad-985c-fe197693ce05
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlFreeHeap
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlFreeHeap
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# RtlFreeHeap function



## -description
<p>The <b>RtlFreeHeap</b> routine frees a memory block that was allocated from a heap by <a href="https://msdn.microsoft.com/library/windows/hardware/ff552108">RtlAllocateHeap</a>. </p>


## -syntax

````
BOOLEAN RtlFreeHeap(
  _In_     PVOID HeapHandle,
  _In_opt_ ULONG Flags,
  _In_     PVOID HeapBase
);
````


## -parameters
<dl>

### -param <i>HeapHandle</i> [in]

<dd>
<p>A handle for the heap whose memory block is to be freed. This parameter is a handle returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff552159">RtlCreateHeap</a>. </p>
</dd>

### -param <i>Flags</i> [in, optional]

<dd>
<p>A set of flags that controls aspects of freeing a memory block. Specifying the following value overrides the corresponding value that was specified in the <i>Flags</i> parameter when the heap was created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff552159">RtlCreateHeap</a>. </p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>HEAP_NO_SERIALIZE</p>
</td>
<td>
<p>Mutual exclusion will not be used when <b>RtlFreeHeap</b> is accessing the heap. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>HeapBase</i> [in]

<dd>
<p>A pointer to the memory block to free. This pointer is returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff552108">RtlAllocateHeap</a>. </p>
</dd>
</dl>

## -returns
<p><b>RtlFreeHeap</b> returns <b>TRUE</b> if the block was freed successfully;   <b> FALSE</b> otherwise.</p>

<p>
<div class="alert"><b>Note</b>  Starting with Windows 8 the return value is typed as <b>LOGICAL</b>, which has a different size than <b>BOOLEAN</b>.</div>
<div> </div>
</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552108">RtlAllocateHeap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552159">RtlCreateHeap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552233">RtlDestroyHeap</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlFreeHeap routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
