---
UID: NF.prefix.RxpAcquirePrefixTableLockExclusive
title: RxpAcquirePrefixTableLockExclusive function
author: windows-driver-content
description: RxpAcquirePrefixTableLockExclusive acquires the prefix table lock exclusively.
old-location: ifsk\rxpacquireprefixtablelockexclusive.htm
old-project: ifsk
ms.assetid: 62f0bfd3-b8d9-4b29-a811-91a6c66dc24f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RxpAcquirePrefixTableLockExclusive
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prefix.h
req.include-header: Prefix.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxpAcquirePrefixTableLockExclusive
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
req.product: Windows 10 or later.
---

# RxpAcquirePrefixTableLockExclusive function



## -description
<b>RxpAcquirePrefixTableLockExclusive</b> acquires the prefix table lock exclusively. 



## -syntax

````
BOOLEAN RxpAcquirePrefixTableLockExclusive(
   PRX_PREFIX_TABLE pTable,
   BOOLEAN          Wait
);
````


## -parameters

### -param pTable 

A pointer to the RX_PREFIX_TABLE where the lock will be acquired.


### -param Wait 

A Boolean value that specifies the behavior whenever the resource cannot be acquired immediately. If <b>TRUE</b>, the caller is put into a wait state until the resource can be acquired. If <b>FALSE</b>, the routine immediately returns, whether the resource can be acquired. 


## -returns
<b>RxpAcquirePrefixTableLockExclusive</b> returns <b>TRUE</b> if the resource is acquired. This routine returns <b>FALSE</b> if the input <i>Wait</i> is <b>FALSE</b> and exclusive access cannot be granted immediately.


## -remarks
The <b>RxAcquirePrefixTableLockExclusive</b> routine is implemented as a macro on Windows Server 2003. On Windows XP and Windows 2000, <b>RxAcquirePrefixTableLockExclusive </b>is implemented as a routine. 

The <b>RxAcquirePrefixTableLockExclusive</b> macro calls the  <b>RxpAcquirePrefixTableLockExclusive</b> routine. The <b>RxIsPrefixTableLockExclusive</b> macro can be used to determine if an exclusive prefix table lock was previously acquired. The <b>RxIsPrefixTableLockAcquired</b> macro can also be used to determine if either an exclusive or shared prefix table lock was previously acquired. 

Normal kernel APC delivery should be disabled before calling this routine. Disable normal kernel APC delivery by calling <b>FsRtlEnterFileSystem</b> or <b>KeEnterCriticalRegion</b>. Delivery must remain disabled until the resource is released, at which point it can be reenabled by calling <b>FsRtlExitFileSystem</b> or <b>KeLeaveCriticalRegion</b>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Prefix.h (include Prefix.h)</dt>
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
<a href="ifsk.fsrtlenterfilesystem">FsRtlEnterFileSystem</a>
</dt>
<dt>
<a href="ifsk.fsrtlexitfilesystem">FsRtlExitFileSystem</a>
</dt>
<dt>
<a href="kernel.keentercriticalregion">KeEnterCriticalRegion</a>
</dt>
<dt>
<a href="kernel.keleavecriticalregion">KeLeaveCriticalRegion</a>
</dt>
<dt>
<a href="ifsk.rxprefixtablelookupname">RxPrefixTableLookupName</a>
</dt>
<dt>
<a href="ifsk.rxpacquireprefixtablelockshared">RxpAcquirePrefixTableLockShared</a>
</dt>
<dt>
<a href="ifsk.rxpreleaseprefixtablelock">RxpReleasePrefixTableLock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxpAcquirePrefixTableLockExclusive function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

