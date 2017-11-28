---
UID: NF.wdm.ExAcquireResourceExclusiveLite
title: ExAcquireResourceExclusiveLite
author: windows-driver-content
description: The ExAcquireResourceExclusiveLite routine acquires the given resource for exclusive access by the calling thread.
old-location: kernel\exacquireresourceexclusivelite.htm
old-project: kernel
ms.assetid: c7f8a6c5-15d5-4a24-a351-4fa5d6c72fbd
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ExAcquireResourceExclusiveLite
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
req.alt-api: ExAcquireResourceExclusiveLite
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: ExclusiveResourceAccess, IrqlExApcLte3, WithinCriticalRegion, HwStorPortProhibitedDDIs, WithinCriticalRegion(storport)
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

# ExAcquireResourceExclusiveLite function



## -description
<p>The <b>ExAcquireResourceExclusiveLite</b> routine acquires the given resource for exclusive access by the calling thread.</p>


## -syntax

````
BOOLEAN ExAcquireResourceExclusiveLite(
  _Inout_ PERESOURCE Resource,
  _In_    BOOLEAN    Wait
);
````


## -parameters
<dl>

### -param <i>Resource</i> [in, out]

<dd>
<p>A pointer to the resource to acquire.</p>
</dd>

### -param <i>Wait</i> [in]

<dd>
<p>Specifies the routine's behavior whenever the resource cannot be acquired immediately. If <b>TRUE</b>, the caller is put into a wait state until the resource can be acquired. If <b>FALSE</b>, the routine immediately returns, regardless of whether the resource can be acquired. </p>
</dd>
</dl>

## -returns
<p><b>ExAcquireResourceExclusiveLite</b> returns <b>TRUE</b> if the resource is acquired. This routine returns <b>FALSE</b> if the input <i>Wait</i> is <b>FALSE</b> and exclusive access cannot be granted immediately.</p>

## -remarks
<p>The following list describes whether and when a caller is given exclusive access to a given resource:</p>

<p>If the resource is currently not owned, exclusive access is granted immediately to the current thread.</p>

<p>If the caller already had acquired the resource for exclusive access, the current thread is granted the same type of access recursively.</p>

<p>If the caller has shared access to the resource, the caller must release the lock before it attempts to reacquire it exclusively.</p>

<p>If the resource is currently owned as exclusive by another thread, or if the caller only has shared access to the resource, the current thread is put into a wait state until the resource can be acquired.</p>

<p>The caller can release the resource by calling either <a href="https://msdn.microsoft.com/library/windows/hardware/ff545597">ExReleaseResourceLite</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545585">ExReleaseResourceForThreadLite</a>.</p>

<p>Normal kernel APC delivery must be disabled before calling this routine. Disable normal kernel APC delivery by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552021">KeEnterCriticalRegion</a>. Delivery must remain disabled until the resource is released, at which point it can be reenabled by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543219">Disabling APCs</a>.</p>

<p>The following list describes whether and when a caller is given exclusive access to a given resource:</p>

<p>If the resource is currently not owned, exclusive access is granted immediately to the current thread.</p>

<p>If the caller already had acquired the resource for exclusive access, the current thread is granted the same type of access recursively.</p>

<p>If the caller has shared access to the resource, the caller must release the lock before it attempts to reacquire it exclusively.</p>

<p>If the resource is currently owned as exclusive by another thread, or if the caller only has shared access to the resource, the current thread is put into a wait state until the resource can be acquired.</p>

<p>The caller can release the resource by calling either <a href="https://msdn.microsoft.com/library/windows/hardware/ff545597">ExReleaseResourceLite</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545585">ExReleaseResourceForThreadLite</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546004">ExclusiveResourceAccess</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547753">IrqlExApcLte3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh466453">WithinCriticalRegion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_withincriticalregion">WithinCriticalRegion(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544363">ExAcquireResourceSharedLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544618">ExGetExclusiveWaiterCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545290">ExGetSharedWaiterCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545317">ExInitializeResourceLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545542">ExReinitializeResourceLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545458">ExIsResourceAcquiredExclusiveLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545585">ExReleaseResourceForThreadLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552021">KeEnterCriticalRegion</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ExAcquireResourceExclusiveLite routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
