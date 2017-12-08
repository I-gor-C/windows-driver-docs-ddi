---
UID: NF.ntifs._FSRTL_ADVANCED_FCB_HEADER.FsRtlNotifyInitializeSync
title: FsRtlNotifyInitializeSync function
author: windows-driver-content
description: The FsRtlNotifyInitializeSync routine allocates and initializes a synchronization object for a notify list.
old-location: ifsk\fsrtlnotifyinitializesync.htm
old-project: ifsk
ms.assetid: 7db82e70-3090-4526-ba10-792ccdbef660
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlNotifyInitializeSync
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later versions of Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlNotifyInitializeSync
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
req.irql: <= APC_LEVEL
---

# FsRtlNotifyInitializeSync function



## -description
The <b>FsRtlNotifyInitializeSync</b> routine allocates and initializes a synchronization object for a notify list.


## -syntax

````
VOID FsRtlNotifyInitializeSync(
  _In_ PNOTIFY_SYNC *NotifySync
);
````


## -parameters

### -param NotifySync [in]

A pointer to a location in which to return a pointer to the opaque synchronization object.

## -returns
None

## -remarks
The system allocates the synchronization object from nonpaged pool. If a pool allocation failure occurs, <b>FsRtlNotifyInitializeSync</b> raises a STATUS_INSUFFICIENT_RESOURCES exception. To gain control if this pool allocation failure occurs, the driver should wrap the call to <b>FsRtlNotifyInitializeSync</b> in a <b>try-except</b> or <b>try-finally</b> statement.

Every successful call to <b>FsRtlNotifyInitializeSync</b> must be matched by a subsequent call to <a href="ifsk.fsrtlnotifyuninitializesync">FsRtlNotifyUninitializeSync</a>.

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
This routine is available on Microsoft Windows 2000 and later versions of Windows operating systems. 
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<a href="ifsk.fsrtlnotifyuninitializesync">FsRtlNotifyUninitializeSync</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlNotifyInitializeSync routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>