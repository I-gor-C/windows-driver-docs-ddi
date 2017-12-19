---
UID: NF.fltkernel.FltAcquirePushLockShared
title: FltAcquirePushLockShared macro
author: windows-driver-content
description: The FltAcquirePushLockShared routine acquires the given push lock for shared access by the calling thread.
old-location: ifsk\fltacquirepushlockshared.htm
old-project: ifsk
ms.assetid: ee85e9fb-2112-4b36-af7f-7d142159bd2d
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FltAcquirePushLockShared
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltAcquirePushLockShared
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
---

# FltAcquirePushLockShared macro



## -description
The <b>FltAcquirePushLockShared</b> routine acquires the given push lock for shared access by the calling thread. 



## -syntax

````
VOID FltAcquirePushLockShared(
  _Inout_ PEX_PUSH_LOCK PushLock
);
````


## -parameters

### -param PushLock [in, out]

Opaque push lock pointer. This pointer must have been initialized by a previous call to <a href="ifsk.fltinitializepushlock">FltInitializePushLock</a>. 


## -remarks
This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later. 

The <b>FltAcquirePushLockShared</b> routine acquires the given push lock for shared access by the calling thread. 

Push locks are similar to ERESOURCE structures (also called resources) in that they can be acquired for shared or exclusive access. For more information about push locks, see the reference entry for <a href="ifsk.fltinitializepushlock">FltInitializePushLock</a>. 

Unlike ERESOURCE structures, push locks cannot be acquired recursively. If the caller already has acquired the push lock for exclusive access, the system will hang. If the caller already has acquired the push lock for shared access, it can receive shared access again. However, each call to <b>FltAcquirePushLockShared</b> must be matched by a subsequent call to <a href="ifsk.fltreleasepushlock">FltReleasePushLock</a>. 

When the caller will be given shared access to the given push lock depends on the following:

If the push lock is currently unowned, shared access is granted immediately to the current thread.

If the push lock has already been acquired for shared access by another thread and no thread is waiting for exclusive access to the push lock, shared access is granted to the caller immediately. The caller is put into a wait state if there is an exclusive waiter. 

If the push lock has already been acquired for exclusive access by another thread or if there is another thread waiting for exclusive access, the current thread is put into a wait state until the push lock can be acquired. 

Because <b>FltAcquirePushLockShared</b> disables normal kernel APC delivery, it is not necessary to call <a href="kernel.keentercriticalregion">KeEnterCriticalRegion</a> or <a href="ifsk.fsrtlenterfilesystem">FsRtlEnterFileSystem</a> before calling <b>FltAcquirePushLockShared</b>. 

To release the push lock after it is acquired, call <a href="ifsk.fltreleasepushlock">FltReleasePushLock</a>. Every call to <b>FltAcquirePushLockShared</b> must be matched by a subsequent call to <b>FltReleasePushLock</b>. 

To acquire a push lock for exclusive access, call <a href="ifsk.fltacquirepushlockexclusive">FltAcquirePushLockExclusive</a>. 

To initialize a push lock, call <a href="ifsk.fltinitializepushlock">FltInitializePushLock</a>. 

To delete a push lock, call <a href="ifsk.fltdeletepushlock">FltDeletePushLock</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fltacquirepushlockexclusive">FltAcquirePushLockExclusive</a>
</dt>
<dt>
<a href="ifsk.fltdeletepushlock">FltDeletePushLock</a>
</dt>
<dt>
<a href="ifsk.fltinitializepushlock">FltInitializePushLock</a>
</dt>
<dt>
<a href="ifsk.fltreleasepushlock">FltReleasePushLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlenterfilesystem">FsRtlEnterFileSystem</a>
</dt>
<dt>
<a href="kernel.keentercriticalregion">KeEnterCriticalRegion</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltAcquirePushLockShared routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

