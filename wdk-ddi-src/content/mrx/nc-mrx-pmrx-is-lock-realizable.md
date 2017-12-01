---
UID: NC.mrx.PMRX_IS_LOCK_REALIZABLE
title: PMRX_IS_LOCK_REALIZABLE
author: windows-driver-content
description: The MRxIsLockRealizable routine is called by RDBSS to request that a network mini-redirector indicate whether a specific byte-range lock is supported on this NET_ROOT structure.
old-location: ifsk\mrxislockrealizable.htm
old-project: ifsk
ms.assetid: 4b8c9a94-a81e-4a02-b68c-10b2fb64157f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SetDSMCounters_IN, SetDSMCounters_IN, *PSetDSMCounters_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: mrx.h
req.include-header: Mrx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MRxIsLockRealizable
req.alt-loc: mrx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# PMRX_IS_LOCK_REALIZABLE callback



## -description
<p>The<i> MRxIsLockRealizable</i> routine is called by <a href="ifsk.the_rdbss_driver_and_library">RDBSS</a> to request that a network mini-redirector indicate whether a specific byte-range lock is supported on this NET_ROOT structure.</p>


## -prototype

````
PMRX_IS_LOCK_REALIZABLE MRxIsLockRealizable;

NTSTATUS MRxIsLockRealizable(
  _Inout_ PMRX_FCB       pFcb,
  _In_    PLARGE_INTEGER ByteOffset,
  _In_    PLARGE_INTEGER Length,
  _In_    ULONG          LowIoLockFlags
)
{ ... }
````


## -parameters
<dl>

### -param <i>pFcb</i> [in, out]

<dd>
<p>A pointer to the FCB structure. </p>
</dd>

### -param <i>ByteOffset</i> [in]

<dd>
<p>A value indicating the byte offset for the byte range lock. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>A value indicating the length for the byte range lock. </p>
</dd>

### -param <i>LowIoLockFlags</i> [in]

<dd>
<p>A value indicating the I/O lock flags. This parameter is a bitmask that contains any combination of the following values: </p>
</dd>
</dl>

## -returns
<p><i>MRxIsLockRealizable</i> returns STATUS_SUCCESS on success or an appropriate NTSTATUS value, such as the following: </p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The byte range lock that is requested is not supported. A network mini-redirector would return this value for a lock request that is not supported even if other types of byte range locks are supported. Unsupported locks might include 64-bit locks (the <b>ByteOffset-&gt;HighPart</b> member is nonzero), zero-length locks (the <b>Length</b> parameter is zero), or shared locks (the LOWIO_LOCKSFLAG_EXCLUSIVELOCK bit of the <i>LowIoLockFlags</i> parameter is not set). </p>

<p> </p>

## -remarks
<p><i>MRxIsLockRealizable</i> determines whether the specific byte-range lock requested is supported on this NET_ROOT structure. A network mini-redirector might support certain byte range locks and not support others. For example, a network mini-redirector might only support 32-bit byte range locks or exclusive locks.</p>

<p><i>MRxIsLockRealizable</i> is called in response to receiving an IRP with the IRP_MN_LOCK minor function.</p>

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
<dt>Mrx.h (include Mrx.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.mrxarefilesaliased">MRxAreFilesAliased</a>
</dt>
<dt>
<a href="ifsk.mrxcleanupfobx">MRxCleanupFobx</a>
</dt>
<dt>
<a href="ifsk.mrxclosesrvopen">MRxCloseSrvOpen</a>
</dt>
<dt>
<a href="ifsk.mrxcollapseopen">MRxCollapseOpen</a>
</dt>
<dt>
<a href="ifsk.mrxcreate">MRxCreate</a>
</dt>
<dt>
<a href="ifsk.mrxdeallocateforfcb">MRxDeallocateForFcb</a>
</dt>
<dt>
<a href="ifsk.mrxdeallocateforfobx">MRxDeallocateForFobx</a>
</dt>
<dt>
<a href="ifsk.mrxextendforcache">MRxExtendForCache</a>
</dt>
<dt>
<a href="ifsk.mrxextendfornoncache">MRxExtendForNonCache</a>
</dt>
<dt>
<a href="ifsk.mrxflush">MRxFlush</a>
</dt>
<dt>
<a href="ifsk.mrxforceclosed">MRxForceClosed</a>
</dt>
<dt>
<a href="ifsk.mrxshouldtrytocollapsethisopen">MRxShouldTryToCollapseThisOpen</a>
</dt>
<dt>
<a href="ifsk.mrxtruncate">MRxTruncate</a>
</dt>
<dt>
<a href="ifsk.mrxzeroextend">MRxZeroExtend</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxIsLockRealizable routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
