---
UID: NF.rxprocs.RxLockEnumerator
title: RxLockEnumerator
author: windows-driver-content
description: RxLockEnumerator is called from a network mini-redirector to enumerate the file locks on an FCB.
old-location: ifsk\rxlockenumerator.htm
ms.assetid: 8d14604f-c9e5-4a2d-bb51-ef1925b39118
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: rxprocs.h
req.include-header: Rxprocs.h, Mrxfcb.h, Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxLockEnumerator
req.alt-loc: rxprocs.h
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
ms.keywords: RxLockEnumerator
req.iface: 
req.product: Windows 10 or later.
---

# RxLockEnumerator function



## -description
<p><b>RxLockEnumerator</b> is called from a network mini-redirector to enumerate the file locks on an FCB.</p>


## -syntax

````
BOOLEAN RxLockEnumerator(
  _Inout_ PMRX_SRV_OPEN  SrvOpen,
  _Inout_ PVOID          *ContinuationHandle,
  _Out_   PLARGE_INTEGER FileOffset,
  _Out_   PLARGE_INTEGER LockRange,
  _Out_   PBOOLEAN       IsLockExclusive
);
````


## -parameters
<dl>

### -param <i>SrvOpen</i> [in, out]

<dd>
<p>A pointer to the SRV_OPEN structure on the FCB to be enumerated.</p>
</dd>

### -param <i>ContinuationHandle</i> [in, out]

<dd>
<p>A pointer to a handle passed back and forth representing the state of the enumeration. If this parameter is a <b>NULL</b> pointer, then this is the start of an lock enumeration.</p>
</dd>

### -param <i>FileOffset</i> [out]

<dd>
<p>A pointer to the file offset of the returned lock.</p>
</dd>

### -param <i>LockRange</i> [out]

<dd>
<p>A pointer to the lock range of the returned lock.</p>
</dd>

### -param <i>IsLockExclusive</i> [out]

<dd>
<p>A pointer to a BOOLEAN indicating if the returned lock is an exclusive lock.</p>
</dd>
</dl>

## -returns
<p><b>RxLockEnumerator </b>returns <b>TRUE</b> on success indicating that the returned lock data is valid. The <b>RxLockEnumerator </b>routine returns or <b>FALSE</b> on failure when no lock data is found or the end of the list of locks has been reached. </p>

## -remarks
<p><b>RxLockEnumerator</b> is normally called from a network min-redirector to enumerate the file locks on an FCB. <b>RxLockEnumerator</b> gets one lock on each call. so the caller needs to keep the enumeration state internally. As a result, only one enumeration process can be in progress at any time. </p>

<p>The <b>RxLockEnumerator</b> routine needs to allocate non-paged pool memory in order to enumerate locks. Consequently, <b>RxLockEnumerator</b> can fail if the memory allocation fails. </p>

<p><b>RxLockEnumerator</b> is normally called from a network min-redirector to enumerate the file locks on an FCB. <b>RxLockEnumerator</b> gets one lock on each call. so the caller needs to keep the enumeration state internally. As a result, only one enumeration process can be in progress at any time. </p>

<p>The <b>RxLockEnumerator</b> routine needs to allocate non-paged pool memory in order to enumerate locks. Consequently, <b>RxLockEnumerator</b> can fail if the memory allocation fails. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxprocs.h (include Rxprocs.h, Mrxfcb.h, or Fcb.h)</dt>
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
<a href="ifsk.the_fcb_structure">The FCB Structure</a>
</dt>
<dt>
<a href="ifsk.the_srv_open_structure">The SRV_OPEN Structure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxLockEnumerator function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
