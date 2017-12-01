---
UID: NF.ntifs.PsReturnPoolQuota
title: PsReturnPoolQuota
author: windows-driver-content
description: The PsReturnPoolQuota routine returns pool quota of the specified pool type to the specified process.
old-location: ifsk\psreturnpoolquota.htm
old-project: ifsk
ms.assetid: 12ceb592-97ca-41c9-89d0-26fd2dc87981
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: PsReturnPoolQuota
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsReturnPoolQuota
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

# PsReturnPoolQuota function



## -description
<p>The <b>PsReturnPoolQuota</b> routine returns pool quota of the specified pool type to the specified process. </p>


## -syntax

````
VOID PsReturnPoolQuota(
  _In_ PEPROCESS Process,
  _In_ POOL_TYPE PoolType,
  _In_ ULONG_PTR Amount
);
````


## -parameters
<dl>

### -param <i>Process</i> [in]

<dd>
<p>Pointer to the process whose quota is to be returned.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>Type of pool quota to return, which can be one of the following: </p>
<ul>
<li><b>NonPagedPool</b></li>
<li><b>PagedPool</b></li>
<li><b>NonPagedPoolCacheAligned</b></li>
<li><b>PagedPoolCacheAligned</b></li>
</ul>
<p></p>
<p><b>Note</b>: The <b>NonPagedPoolMustSucceed</b> and <b>NonPagedPoolCacheAlignedMustS</b> pool types are obsolete and should no longer be used. </p>
</dd>

### -param <i>Amount</i> [in]

<dd>
<p>Number of bytes to return to the pool quota for this process. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If the quota return would exceed the quota for the process, <b>PsReturnPoolQuota</b> raises an exception with the status value STATUS_QUOTA_EXCEEDED. Callers are responsible for handling this exception. Thus calls to <b>PsReturnPoolQuota</b> must be wrapped within a driver-supplied exception handler.</p>

<p>Every successful call to <b>PsChargePoolQuota</b> must be matched by a subsequent call to <b>PsReturnPoolQuota</b>.</p>

<p>For more information about memory management, see <a href="https://msdn.microsoft.com/e030a37c-26ab-4177-9980-4336928975e1">Memory Management</a>. </p>

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
<a href="..\ntifs\nf-ntifs-pschargepoolquota.md">PsChargePoolQuota</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PsReturnPoolQuota routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
