---
UID: NC.mrx.PMRX_CALLDOWN
title: PMRX_CALLDOWN
author: windows-driver-content
description: The MRxCleanupFobx routine is called by RDBSS to request the network mini-redirector to close a file system object extension. RDBSS issues this call in response to receiving an IRP_MJ_CLEANUP request on a file object.
old-location: ifsk\mrxcleanupfobx.htm
old-project: ifsk
ms.assetid: 4b3b0add-4fa6-40c9-827a-59dc78bf4e27
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
req.alt-api: MRxCleanupFobx
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

# PMRX_CALLDOWN callback



## -description
<p>The <i>MRxCleanupFobx</i> routine is called by <a href="ifsk.the_rdbss_driver_and_library">RDBSS</a> to request the network mini-redirector to close a file system object extension. RDBSS issues this call in response to receiving an <a href="ifsk.irp_mj_cleanup">IRP_MJ_CLEANUP</a> request on a file object.</p>


## -prototype

````
PMRX_CALLDOWN MRxCleanupFobx;

NTSTATUS MRxCleanupFobx(
  _Inout_ PRX_CONTEXT RxContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>RxContext</i> [in, out]

<dd>
<p>A pointer to the RX_CONTEXT structure. This parameter contains the IRP that is requesting the operation. </p>
</dd>
</dl>

## -returns
<p><i>MRxCleanupFobx</i> returns STATUS_SUCCESS on success or an appropriate NTSTATUS value, such as the following: </p><dl>
<dt><b>STATUS_INTERNAL_ERROR</b></dt>
</dl><p>An internal error occurred in the network mini-redirector. </p>

<p> </p>

## -remarks
<p><i>MRxCleanupFobx</i> is called by RDBSS as part of cleanup and close operations on a file object. </p>

<p><i>MRxCleanupFobx</i> cannot return a value of STATUS_RETRY indicating that the call should be retried. If a retry loop is necessary, it must be handled internally in the <i>MRxCleanupFobx</i> routine by the network mini-redirector.</p>

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
<a href="ifsk.mrxislockrealizable">MRxIsLockRealizable</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxCleanupFobx routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
