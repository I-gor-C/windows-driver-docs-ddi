---
UID: NF.ntifs.FsRtlIncrementCcFastReadWait
title: FsRtlIncrementCcFastReadWait function
author: windows-driver-content
description: The FsRtlIncrementCcFastReadWait routine increments the CcFastReadWait performance counter in a per processor control block of cache manager system counters.
old-location: ifsk\fsrtlincrementccfastreadwait.htm
old-project: ifsk
ms.assetid: f9d10593-28a6-4d57-a739-2d24dfe4631a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlIncrementCcFastReadWait
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlIncrementCcFastReadWait
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
req.irql: Any level
---

# FsRtlIncrementCcFastReadWait function



## -description
The <b>FsRtlIncrementCcFastReadWait</b> routine increments the CcFastReadWait performance counter in a per processor control block of cache manager system counters.


## -syntax

````
VOID FsRtlIncrementCcFastReadWait(
   VOID 
);
````


## -parameters

### -param  

None

## -returns
This routine does not return a value.

## -remarks
<b>FsRtlIncrementCcFastReadWait</b> increments the CcFastReadWait performance counter in the per processor control block of cache manager system counters. This counter indicates that a fast I/O read operation, <a href="ifsk.fsrtlcopyread">FsRtlCopyRead</a>, was called with the <i>Wait</i> parameter set to <b>TRUE</b> indicating that the caller can be put into a wait state until all the data has been copied.

File system drivers should call this function to update the performance counter if the driver chooses to override the default fast I/O read handler.

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
This routine is available on Microsoft Windows XP and later. 
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsrtlcopyread">FsRtlCopyRead</a>
</dt>
<dt>
<a href="ifsk.fsrtlincrementccfastreadnotpossible">FsRtlIncrementCcFastReadNotPossible</a>
</dt>
<dt>
<a href="ifsk.fsrtlincrementccfastreadnowait">FsRtlIncrementCcFastReadNoWait</a>
</dt>
<dt>
<a href="ifsk.fsrtlincrementccfastreadresourcemiss">FsRtlIncrementCcFastReadResourceMiss</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIncrementCcFastReadWait routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
