---
UID: NF.wdm.ExAcquireSharedWaitForExclusive
title: ExAcquireSharedWaitForExclusive
author: windows-driver-content
description: The ExAcquireSharedWaitForExclusive routine acquires the given resource for shared access if shared access can be granted and there are no exclusive waiters.
old-location: kernel\exacquiresharedwaitforexclusive.htm
old-project: kernel
ms.assetid: 745b014d-7ab4-4e07-a24c-7a74949a9d7b
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ExAcquireSharedWaitForExclusive
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExAcquireSharedWaitForExclusive
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlExApcLte3, WithinCriticalRegion, HwStorPortProhibitedDDIs, SpNoWait, WithinCriticalRegion(storport)
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# ExAcquireSharedWaitForExclusive function



## -description
<p>The <b>ExAcquireSharedWaitForExclusive</b> routine acquires the given resource for shared access if shared access can be granted and there are no exclusive waiters. </p>


## -syntax

````
BOOLEAN ExAcquireSharedWaitForExclusive(
  _Inout_ PERESOURCE Resource,
  _In_    BOOLEAN    Wait
);
````


## -parameters
<dl>

### -param <i>Resource</i> [in, out]

<dd>
<p>A pointer to the resource to be acquired for shared access.</p>
</dd>

### -param <i>Wait</i> [in]

<dd>
<p>Specifies the routine's behavior whenever the resource cannot be acquired immediately. If <b>TRUE</b>, the caller is put into a wait state until the resource can be acquired. If <b>FALSE</b>, the routine immediately returns, regardless of whether the resource can be acquired. </p>
</dd>
</dl>

## -returns
<p><b>ExAcquireSharedWaitForExclusive</b> returns <b>TRUE</b> if the requested access is granted or an exclusive owner releases the resource. This routine returns <b>FALSE</b> if the input <i>Wait</i> is <b>FALSE</b> and shared access cannot be granted immediately. </p>

## -remarks
<p>Most drivers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544363">ExAcquireResourceSharedLite</a> instead of <b>ExAcquireSharedWaitForExclusive</b>.</p>

<p>The caller can release the resource by calling either <a href="https://msdn.microsoft.com/library/windows/hardware/ff545597">ExReleaseResourceLite</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545585">ExReleaseResourceForThreadLite</a>.</p>

<p>If shared access cannot be granted immediately, the caller can wait for other threads to acquire and release exclusive ownership of the resource.</p>

<p>Whether or when the caller is given shared access to the given resource depends on the following:</p>

<p>If the resource is currently unowned, shared access is granted immediately to the current thread.</p>

<p>If the caller already has exclusive access to the resource, the current thread is granted the same type of access recursively. </p>

<p>If the resource is currently owned as shared and there are no pending attempts to acquire exclusive access, shared access is granted to the caller immediately. </p>

<p>If the resource is currently owned as shared but there is a pending attempt to acquire exclusive access, the caller either is put into a wait state (<i>Wait</i> set to <b>TRUE</b>) or <b>ExAcquireSharedWaitForExclusive</b> returns <b>FALSE</b>.</p>

<p>When the current thread waits to acquire the resource until after a pending exclusive ownership has been released, <b>ExAcquireSharedWaitForExclusive</b> returns <b>TRUE</b> when the current thread is granted shared access to the resource and resumes execution. </p>

<p>The behavior of <b>ExAcquireSharedWaitForExclusive</b> is identical to that of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544363">ExAcquireResourceSharedLite</a> unless the calling thread already owns the resource as shared and there are exclusive waiters. In that case, <b>ExAcquireSharedWaitForExclusive</b> allows the exclusive waiters to acquire exclusive ownership of the resource.</p>

<p>If the caller specifies <b>TRUE</b> for the <i>Wait</i> parameter, the caller blocks until another thread frees the resource on behalf of the caller, using <a href="https://msdn.microsoft.com/library/windows/hardware/ff545577">ExReleaseResourceForThread</a>. Driver writers must be careful to ensure that another thread actually releases the resource; otherwise the caller is deadlocked. <b>ExAcquireResourceSharedLite</b> does not have this property, so drivers should use that routine unless they require the particular behavior of <b>ExAcquireSharedWaitForExclusive</b>.</p>

<p>Normal kernel APC delivery must be disabled before calling this routine. Disable normal kernel APC delivery by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552021">KeEnterCriticalRegion</a>. Delivery must remain disabled until the resource is released, at which point it can be reenabled by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543219">Disabling APCs</a>.</p>

<p>Most drivers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544363">ExAcquireResourceSharedLite</a> instead of <b>ExAcquireSharedWaitForExclusive</b>.</p>

<p>The caller can release the resource by calling either <a href="https://msdn.microsoft.com/library/windows/hardware/ff545597">ExReleaseResourceLite</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545585">ExReleaseResourceForThreadLite</a>.</p>

<p>If shared access cannot be granted immediately, the caller can wait for other threads to acquire and release exclusive ownership of the resource.</p>

<p>Whether or when the caller is given shared access to the given resource depends on the following:</p>

<p>If the resource is currently unowned, shared access is granted immediately to the current thread.</p>

<p>If the caller already has exclusive access to the resource, the current thread is granted the same type of access recursively. </p>

<p>If the resource is currently owned as shared and there are no pending attempts to acquire exclusive access, shared access is granted to the caller immediately. </p>

<p>If the resource is currently owned as shared but there is a pending attempt to acquire exclusive access, the caller either is put into a wait state (<i>Wait</i> set to <b>TRUE</b>) or <b>ExAcquireSharedWaitForExclusive</b> returns <b>FALSE</b>.</p>

<p>When the current thread waits to acquire the resource until after a pending exclusive ownership has been released, <b>ExAcquireSharedWaitForExclusive</b> returns <b>TRUE</b> when the current thread is granted shared access to the resource and resumes execution. </p>

<p>The behavior of <b>ExAcquireSharedWaitForExclusive</b> is identical to that of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544363">ExAcquireResourceSharedLite</a> unless the calling thread already owns the resource as shared and there are exclusive waiters. In that case, <b>ExAcquireSharedWaitForExclusive</b> allows the exclusive waiters to acquire exclusive ownership of the resource.</p>

<p>If the caller specifies <b>TRUE</b> for the <i>Wait</i> parameter, the caller blocks until another thread frees the resource on behalf of the caller, using <a href="https://msdn.microsoft.com/library/windows/hardware/ff545577">ExReleaseResourceForThread</a>. Driver writers must be careful to ensure that another thread actually releases the resource; otherwise the caller is deadlocked. <b>ExAcquireResourceSharedLite</b> does not have this property, so drivers should use that routine unless they require the particular behavior of <b>ExAcquireSharedWaitForExclusive</b>.</p>

<p>Normal kernel APC delivery must be disabled before calling this routine. Disable normal kernel APC delivery by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552021">KeEnterCriticalRegion</a>. Delivery must remain disabled until the resource is released, at which point it can be reenabled by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543219">Disabling APCs</a>.</p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547753">IrqlExApcLte3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh466453">WithinCriticalRegion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454255">SpNoWait</a>, <a href="devtest.storport_withincriticalregion">WithinCriticalRegion(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544363">ExAcquireResourceSharedLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544367">ExAcquireSharedStarveExclusive</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544558">ExConvertExclusiveToSharedLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544618">ExGetExclusiveWaiterCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545458">ExIsResourceAcquiredExclusiveLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545477">ExIsResourceAcquiredSharedLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545577">ExReleaseResourceForThread</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExAcquireSharedWaitForExclusive routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
