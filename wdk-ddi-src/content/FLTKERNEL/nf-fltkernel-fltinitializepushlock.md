---
UID: NF.fltkernel.FltInitializePushLock
title: FltInitializePushLock
author: windows-driver-content
description: The FltInitializePushLock routine initializes a push lock variable.
old-location: ifsk\fltinitializepushlock.htm
ms.assetid: 49b624d6-ef06-4e73-98ac-b0be1669afc7
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltInitializePushLock
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
ms.keywords: FltInitializePushLock
req.iface: 
---

# FltInitializePushLock function



## -description
<p>The <b>FltInitializePushLock</b> routine initializes a push lock variable.</p>


## -syntax

````
VOID FltInitializePushLock(
  _Out_ PEX_PUSH_LOCK PushLock
);
````


## -parameters
<dl>

### -param <i>PushLock</i> [out]

<dd>
<p>Pointer to the caller-supplied storage, which must be at least the value of <b>sizeof(</b>EX_PUSH_LOCK<b>)</b>, for the push lock variable to be initialized. The storage must be 4-byte aligned on 32-bit platforms, and 8-byte aligned on 64-bit platforms.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Push locks are similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544281">ERESOURCE structures</a> (also called "resources") in the following ways: </p>

<p>Push locks can be used for synchronization by a set of threads. </p>

<p>Push locks can be acquired for shared or exclusive access. </p>

<p>Although the caller provides the storage for the push lock variable, the EX_PUSH_LOCK structure is opaque: that is, its members are reserved for system use. </p>

<p>Push locks offer the following advantages over ERESOURCE structures: </p>

<p>When push locks are mostly acquired for shared access, they are more efficient than ERESOURCE structures. </p>

<p>The storage for push locks can be allocated from paged or nonpaged pool. ERESOURCE structures must be allocated only from nonpaged pool. </p>

<p>EX_PUSH_LOCK structures are much smaller than ERESOURCE structures. </p>

<p>Push locks have the following disadvantages when compared with ERESOURCE structures: </p>

<p>The algorithm for granting exclusive access is not fair to all threads. If there is a high level of exclusive-lock contention, there is no guarantee about the order in which threads will be granted exclusive access. </p>

<p>There are no support routines for determining the current owner of a push lock. (Users of ERESOURCE structures can call routines such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff545458">ExIsResourceAcquiredExclusiveLite</a> to determine whether the current thread has exclusive access to the resource.) </p>

<p>Push locks cannot be acquired recursively.</p>

<p>To acquire a push lock for exclusive access, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541667">FltAcquirePushLockExclusive</a>. </p>

<p>To acquire a push lock for shared access, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541672">FltAcquirePushLockShared</a>. </p>

<p>To release a push lock, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544326">FltReleasePushLock</a>. </p>

<p>To delete a push lock, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541993">FltDeletePushLock</a>. </p>

<p>Push locks are similar to <a href="https://msdn.microsoft.com/library/windows/hardware/ff544281">ERESOURCE structures</a> (also called "resources") in the following ways: </p>

<p>Push locks can be used for synchronization by a set of threads. </p>

<p>Push locks can be acquired for shared or exclusive access. </p>

<p>Although the caller provides the storage for the push lock variable, the EX_PUSH_LOCK structure is opaque: that is, its members are reserved for system use. </p>

<p>Push locks offer the following advantages over ERESOURCE structures: </p>

<p>When push locks are mostly acquired for shared access, they are more efficient than ERESOURCE structures. </p>

<p>The storage for push locks can be allocated from paged or nonpaged pool. ERESOURCE structures must be allocated only from nonpaged pool. </p>

<p>EX_PUSH_LOCK structures are much smaller than ERESOURCE structures. </p>

<p>Push locks have the following disadvantages when compared with ERESOURCE structures: </p>

<p>The algorithm for granting exclusive access is not fair to all threads. If there is a high level of exclusive-lock contention, there is no guarantee about the order in which threads will be granted exclusive access. </p>

<p>There are no support routines for determining the current owner of a push lock. (Users of ERESOURCE structures can call routines such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff545458">ExIsResourceAcquiredExclusiveLite</a> to determine whether the current thread has exclusive access to the resource.) </p>

<p>Push locks cannot be acquired recursively.</p>

<p>To acquire a push lock for exclusive access, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541667">FltAcquirePushLockExclusive</a>. </p>

<p>To acquire a push lock for shared access, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541672">FltAcquirePushLockShared</a>. </p>

<p>To release a push lock, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544326">FltReleasePushLock</a>. </p>

<p>To delete a push lock, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541993">FltDeletePushLock</a>. </p>

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
<p>This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545458">ExIsResourceAcquiredExclusiveLite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541667">FltAcquirePushLockExclusive</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541672">FltAcquirePushLockShared</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541993">FltDeletePushLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544326">FltReleasePushLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltInitializePushLock routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
