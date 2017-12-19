---
UID: NF.fltkernel.FltReleasePushLock
title: FltReleasePushLock macro
author: windows-driver-content
description: The FltReleasePushLock routine releases a specified push lock owned by the current thread.
old-location: ifsk\fltreleasepushlock.htm
old-project: ifsk
ms.assetid: 34d1b945-329c-47ff-913d-5576eef665b8
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FltReleasePushLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltReleasePushLock
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
---

# FltReleasePushLock macro



## -description
The <b>FltReleasePushLock</b> routine releases a specified push lock owned by the current thread.



## -syntax

````
VOID FltReleasePushLock(
  _Inout_ PEX_PUSH_LOCK PushLock
);
````


## -parameters

### -param PushLock [in, out]

Opaque push lock pointer. This pointer must have been initialized by a previous call to <a href="ifsk.fltinitializepushlock">FltInitializePushLock</a>. 


## -remarks
<b>FltReleasePushLock</b> releases a push lock that was previously acquired by calling <a href="ifsk.fltacquirepushlockexclusive">FltAcquirePushLockExclusive</a> or <a href="ifsk.fltacquirepushlockshared">FltAcquirePushLockShared</a>. 

Because <b>FltReleasePushLock</b> reenables normal kernel APC delivery, it is not necessary to call <a href="kernel.keleavecriticalregion">KeLeaveCriticalRegion</a> or <a href="ifsk.fsrtlexitfilesystem">FsRtlExitFileSystem</a> after calling <b>FltReleasePushLock</b>. 

For more information about push locks, see the reference entry for <a href="ifsk.fltinitializepushlock">FltInitializePushLock</a>. 

To acquire a push lock for exclusive access, call <a href="ifsk.fltacquirepushlockexclusive">FltAcquirePushLockExclusive</a>. 

To acquire a push lock for shared access, call <a href="ifsk.fltacquirepushlockshared">FltAcquirePushLockShared</a>. 

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
Version

</th>
<td width="70%">
This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later. 

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
DLL

</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
<a href="ifsk.fltacquirepushlockshared">FltAcquirePushLockShared</a>
</dt>
<dt>
<a href="ifsk.fltdeletepushlock">FltDeletePushLock</a>
</dt>
<dt>
<a href="ifsk.fltinitializepushlock">FltInitializePushLock</a>
</dt>
<dt>
<a href="ifsk.fsrtlexitfilesystem">FsRtlExitFileSystem</a>
</dt>
<dt>
<a href="kernel.keleavecriticalregion">KeLeaveCriticalRegion</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltReleasePushLock routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

