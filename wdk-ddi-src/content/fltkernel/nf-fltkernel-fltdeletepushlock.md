---
UID: NF.fltkernel.FltDeletePushLock
title: FltDeletePushLock
author: windows-driver-content
description: The FltDeletePushLock routine deletes a given push lock.
old-location: ifsk\fltdeletepushlock.htm
old-project: ifsk
ms.assetid: 93b4914c-53a1-4594-ac8d-4be1b0c9e4d7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltDeletePushLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltDeletePushLock
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
req.iface: 
---

# FltDeletePushLock function



## -description
<p>The <b>FltDeletePushLock</b> routine deletes a given push lock. </p>


## -syntax

````
VOID FltDeletePushLock(
  _In_ PEX_PUSH_LOCK PushLock
);
````


## -parameters
<dl>

### -param <i>PushLock</i> [in]

<dd>
<p>Opaque push lock pointer. This pointer must have been initialized by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543297">FltInitializePushLock</a>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later. </p>

<p>After calling <b>FltDeletePushLock</b>, the caller can free the memory that it allocated for the push lock. </p>

<p>For more information about push locks, see the reference entry for <a href="https://msdn.microsoft.com/library/windows/hardware/ff543297">FltInitializePushLock</a>. </p>

<p>To acquire a push lock for exclusive access, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541667">FltAcquirePushLockExclusive</a>. </p>

<p>To acquire a push lock for shared access, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541672">FltAcquirePushLockShared</a>. </p>

<p>To release a push lock, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544326">FltReleasePushLock</a>. </p>

<p>To initialize a push lock, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543297">FltInitializePushLock</a>. </p>

<p>This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later. </p>

<p>After calling <b>FltDeletePushLock</b>, the caller can free the memory that it allocated for the push lock. </p>

<p>For more information about push locks, see the reference entry for <a href="https://msdn.microsoft.com/library/windows/hardware/ff543297">FltInitializePushLock</a>. </p>

<p>To acquire a push lock for exclusive access, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541667">FltAcquirePushLockExclusive</a>. </p>

<p>To acquire a push lock for shared access, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541672">FltAcquirePushLockShared</a>. </p>

<p>To release a push lock, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544326">FltReleasePushLock</a>. </p>

<p>To initialize a push lock, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543297">FltInitializePushLock</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541667">FltAcquirePushLockExclusive</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541672">FltAcquirePushLockShared</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543297">FltInitializePushLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544326">FltReleasePushLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltDeletePushLock routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
