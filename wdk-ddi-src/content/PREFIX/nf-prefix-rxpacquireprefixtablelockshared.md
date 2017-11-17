---
UID: NF.prefix.RxpAcquirePrefixTableLockShared
title: RxpAcquirePrefixTableLockShared
author: windows-driver-content
description: RxpAcquirePrefixTableLockShared acquires the prefix table lock shared.
old-location: ifsk\rxpacquireprefixtablelockshared.htm
ms.assetid: 89924d1d-80c2-4778-9647-c3add9e7d013
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: prefix.h
req.include-header: Prefix.h
req.target-type: Desktop
req.target-min-winverclnt: On Windows Server 2003, the RxpAcquirePrefixTableLockShared routine is implemented as a macro. This routine is only available onWindows XP and Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxpAcquirePrefixTableLockShared
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
ms.keywords: RxpAcquirePrefixTableLockShared
req.iface: 
req.product: Windows 10 or later.
---

# RxpAcquirePrefixTableLockShared function



## -description
<p><b>RxpAcquirePrefixTableLockShared</b> acquires the prefix table lock shared. </p>


## -syntax

````
BOOLEAN RxpAcquirePrefixTableLockShared(
   PRX_PREFIX_TABLE pTable,
   BOOLEAN          Wait
);
````


## -parameters
<dl>

### -param <i>pTable</i> 

<dd>
<p>A pointer to the RX_PREFIX_TABLE structure where the lock will be acquired.</p>
</dd>

### -param <i>Wait</i> 

<dd>
<p>A Boolean value that specifies the behavior whenever the resource cannot be acquired immediately. If <b>TRUE</b>, the caller is put into a wait state until the resource can be acquired. If <b>FALSE</b>, the routine immediately returns, whether the shared resource can be acquired. </p>
</dd>
</dl>

## -returns
<p><b>RxpAcquirePrefixTableLockShared</b> returns <b>TRUE</b> if the resource is acquired. This routine returns <b>FALSE</b> if the <i>Wait</i> parameter is <b>FALSE</b> and shared access cannot be granted immediately.</p>

## -remarks
<p>The <b>RxAcquirePrefixTableLockShared</b> macro calls the <b>RxpAcquirePrefixTableLockShared</b> routine. The <b>RxIsPrefixTableLockAcquired</b> macro can be used to determine whether an exclusive or shared prefix table lock was previously acquired. </p>

<p>Normal kernel APC delivery should be disabled before calling this routine. Normal kernel APC delivery can be disabled by calling <b>FsRtlEnterFileSystem</b> or <b>KeEnterCriticalRegion</b>. Delivery must remain disabled until the resource is released, at which point it can be reenabled by calling <b>FsRtlExitFileSystem</b> or <b>KeLeaveCriticalRegion</b>.</p>

<p>The <b>RxAcquirePrefixTableLockShared</b> macro calls the <b>RxpAcquirePrefixTableLockShared</b> routine. The <b>RxIsPrefixTableLockAcquired</b> macro can be used to determine whether an exclusive or shared prefix table lock was previously acquired. </p>

<p>Normal kernel APC delivery should be disabled before calling this routine. Normal kernel APC delivery can be disabled by calling <b>FsRtlEnterFileSystem</b> or <b>KeEnterCriticalRegion</b>. Delivery must remain disabled until the resource is released, at which point it can be reenabled by calling <b>FsRtlExitFileSystem</b> or <b>KeLeaveCriticalRegion</b>.</p>

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
<p>On Windows Server 2003, the RxpAcquirePrefixTableLockShared routine is implemented as a macro. This routine is only available onWindows XP and Windows 2000.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545900">FsRtlEnterFileSystem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545908">FsRtlExitFileSystem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552021">KeEnterCriticalRegion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552964">KeLeaveCriticalRegion</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554632">RxPrefixTableLookupName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554595">RxpAcquirePrefixTableLockExclusive</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554637">RxpReleasePrefixTableLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxpAcquirePrefixTableLockShared function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
