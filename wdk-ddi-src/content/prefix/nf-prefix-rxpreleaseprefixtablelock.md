---
UID: NF.prefix.RxpReleasePrefixTableLock
title: RxpReleasePrefixTableLock
author: windows-driver-content
description: RxpReleasePrefixTableLock releases a previously acquired shared or exclusive prefix table lock.
old-location: ifsk\rxpreleaseprefixtablelock.htm
old-project: ifsk
ms.assetid: 57aef4ed-2ece-4af3-b1ca-e4fe5a306f82
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxpReleasePrefixTableLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prefix.h
req.include-header: Prefix.h
req.target-type: Desktop
req.target-min-winverclnt: RxpReleasePrefixTableLock routine is only available on Windows XP and Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxpReleasePrefixTableLock
req.alt-loc: prefix.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RxpReleasePrefixTableLock function



## -description
<p><b>RxpReleasePrefixTableLock</b> releases a previously acquired shared or exclusive prefix table lock. </p>


## -syntax

````
VOID RxpReleasePrefixTableLock(
   PRX_PREFIX_TABLE pTable
);
````


## -parameters
<dl>

### -param <i>pTable</i> 

<dd>
<p>A pointer to the RX_PREFIX_TABLE structure where the lock was previously acquired.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>On Windows Server 2003, this routine is implemented as a macro. The <b>RxReleasePrefixTableLock</b> macro can be used to call this routine. </p>

<p>Normal kernel APC delivery should be disabled before calling the <b>RxpAcquirePrefixTableLockExclusive</b> or <b>RxpAcquirePrefixTableLockShared</b> routines to acquire the lock. Normal kernel APC delivery can be disabled by calling <b>FsRtlEnterFileSystem</b> or <b>KeEnterCriticalRegion</b>. Delivery must remain disabled until the resource is released by calling <b>RxpReleasePrefixTableLock</b>, at which point it can be reenabled by calling <b>FsRtlExitFileSystem</b> or <b>KeLeaveCriticalRegion</b>.</p>

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
<p>RxpReleasePrefixTableLock routine is only available on Windows XP and Windows 2000. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prefix.h (include Prefix.h)</dt>
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
<a href="ifsk.fsrtlenterfilesystem">FsRtlEnterFileSystem</a>
</dt>
<dt>
<a href="ifsk.fsrtlexitfilesystem">FsRtlExitFileSystem</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-keentercriticalregion.md">KeEnterCriticalRegion</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-keleavecriticalregion.md">KeLeaveCriticalRegion</a>
</dt>
<dt>
<a href="..\prefix\nf-prefix-rxprefixtablelookupname.md">RxPrefixTableLookupName</a>
</dt>
<dt>
<a href="..\prefix\nf-prefix-rxpacquireprefixtablelockexclusive.md">RxpAcquirePrefixTableLockExclusive</a>
</dt>
<dt>
<a href="..\prefix\nf-prefix-rxpacquireprefixtablelockshared.md">RxpAcquirePrefixTableLockShared</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxpReleasePrefixTableLock function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
