---
UID: NF.wdm.ExInitializeFastMutex
title: ExInitializeFastMutex
author: windows-driver-content
description: The ExInitializeFastMutex routine initializes a fast mutex variable, used to synchronize mutually exclusive access by a set of threads to a shared resource.
old-location: kernel\exinitializefastmutex.htm
old-project: kernel
ms.assetid: edd189f9-1089-470f-95a9-670bdba9c210
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ExInitializeFastMutex
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExInitializeFastMutex
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ExInitializeFastMutex function



## -description
<p>The <b>ExInitializeFastMutex</b> routine initializes a fast mutex variable, used to synchronize mutually exclusive access by a set of threads to a shared resource.</p>


## -syntax

````
VOID ExInitializeFastMutex(
  _Out_ PFAST_MUTEX FastMutex
);
````


## -parameters
<dl>

### -param <i>FastMutex</i> [out]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff545715">FAST_MUTEX</a> structure, which represents the fast mutex, in the nonpaged memory pool. The allocation must be 4-byte aligned on 32-bit platforms, and 8-byte aligned on 64-bit platforms.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>ExInitializeFastMutex</b> must be called before any calls to other <b>Ex<i>Xxx</i>FastMutex</b> routines occur. </p>

<p>Although the caller supplies the storage for the given fast mutex, the <b>FAST_MUTEX</b> structure is opaque: that is, its members are reserved for system use. </p>

<p>For better performance, use the <b>Ex<i>Xxx</i>FastMutex</b> routines instead of the <b>Ke<i>Xxx</i>Mutex</b> routines. However, a fast mutex cannot be acquired recursively, as a kernel mutex can. </p>

<p>For more information about fast mutexes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545716">Fast Mutexes and Guarded Mutexes</a>.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545715">FAST_MUTEX</a>
</dt>
<dt>
<a href="kernel.exacquirefastmutex">ExAcquireFastMutex</a>
</dt>
<dt>
<a href="kernel.exacquirefastmutexunsafe">ExAcquireFastMutexUnsafe</a>
</dt>
<dt>
<a href="kernel.exreleasefastmutex">ExReleaseFastMutex</a>
</dt>
<dt>
<a href="kernel.exreleasefastmutexunsafe">ExReleaseFastMutexUnsafe</a>
</dt>
<dt>
<a href="kernel.extrytoacquirefastmutex">ExTryToAcquireFastMutex</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinitializemutex.md">KeInitializeMutex</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExInitializeFastMutex routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
