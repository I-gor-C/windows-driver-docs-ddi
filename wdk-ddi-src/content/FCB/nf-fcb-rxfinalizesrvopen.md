---
UID: NF.fcb.RxFinalizeSrvOpen
title: RxFinalizeSrvOpen
author: windows-driver-content
description: RxFinalizeSrvOpen finalizes the given SRV_OPEN structure. The caller must have an exclusive lock on the FCB associated with the SRV_OPEN and either a shared or exclusive lock on the table lock of the NET_ROOT associated with the FCB.
old-location: ifsk\rxfinalizesrvopen.htm
ms.assetid: 9a756606-90df-4bb8-a87a-f000616812fa
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fcb.h
req.include-header: Mrxfcb.h, Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxFinalizeSrvOpen
req.alt-loc: fcb.h
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
ms.keywords: RxFinalizeSrvOpen
req.iface: 
---

# RxFinalizeSrvOpen function



## -description
<p><b>RxFinalizeSrvOpen</b> finalizes the given SRV_OPEN structure. The caller must have an exclusive lock on the FCB associated with the SRV_OPEN and either a shared or exclusive lock on the table lock of the NET_ROOT associated with the FCB.</p>


## -syntax

````
BOOLEAN RxFinalizeSrvOpen(
  _Out_ PSRV_OPEN ThisSrvOpen,
  _In_  BOOLEAN   RecursiveFinalize,
  _In_  BOOLEAN   ForceFinalize
);
````


## -parameters
<dl>

### -param <i>ThisSrvOpen</i> [out]

<dd>
<p>A pointer to the SRV_OPEN structure to finalize.</p>
</dd>

### -param <i>RecursiveFinalize</i> [in]

<dd>
<p>The value indicating whether the finalization should be done recursively. </p>
</dd>

### -param <i>ForceFinalize</i> [in]

<dd>
<p>The value indicating whether the finalization should be forced, regardless of the reference count. </p>
<p>If <i>ForceFinalize</i> is <b>FALSE</b>, then the <b>NodeReferenceCount</b> member of the SRV_OPEN structure pointed to by <i>ThisSrvOpen</i> must be 0 for the SRV_OPEN to be finalized. </p>
</dd>
</dl>

## -returns
<p><b>RxFinalizeSrvOpen</b> returns <b>TRUE</b> on success or <b>FALSE</b> if the finalization did not occur: </p>

## -remarks
<p>The <b>RxFinalizeSrvOpen</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when the reference count on the SRV_OPEN is decremented to 1. RDBSS also calls <b>RxFinalizeSrvOpen</b> when the <b>RxFinalizeNetFcb </b>routine is called with the <i>RecursiveFinalize</i> set to <b>TRUE</b>. RDBSS calls <b>RxFinalizeNetFcb</b> when an I/O request packet is received for IRP_MJ_CLOSE. This IRP is normally received by RDBSS in response to a user-mode application requesting a file close operation. It is also possible for another kernel driver to issue such an IRP. </p>

<p>Before calling <b>RxFinalizeSrvOpen</b>, the caller must have acquired an exclusive lock on the FCB associated with the SRV_OPEN and acquired either a shared or exclusive lock on the table lock of the NET_ROOT associated with the FCB. </p>

<p>If the <i>RecursiveFinalize</i> parameter is <b>TRUE</b>, then <b>RxFinalizeSrvOpen</b> will finalize any FOBX structures associated with this SRV_OPEN by calling <b>RxFinalizeNetFobx</b> with the <i>RecursiveFinalize </i>parameter set to <b>TRUE</b> and the <i>ForceFinalize</i> parameter. </p>

<p>If the <b>FcbState</b> member of the associated FCB does not have the FCB_STATE_ORPHANED flag set, then <b>RxFinalizeSrvCall</b> will call the <b>MRxForceClosed</b> routine provided by the network mini-redirector to finalize the SRV_CALL. If the SRV_CALL structure was not originally allocated as part of creating the FCB, then the memory for the SRV_CALL structure will also be released. </p>

<p>The <b>RxFinalizeSrvOpen</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when the reference count on the SRV_OPEN is decremented to 1. RDBSS also calls <b>RxFinalizeSrvOpen</b> when the <b>RxFinalizeNetFcb </b>routine is called with the <i>RecursiveFinalize</i> set to <b>TRUE</b>. RDBSS calls <b>RxFinalizeNetFcb</b> when an I/O request packet is received for IRP_MJ_CLOSE. This IRP is normally received by RDBSS in response to a user-mode application requesting a file close operation. It is also possible for another kernel driver to issue such an IRP. </p>

<p>Before calling <b>RxFinalizeSrvOpen</b>, the caller must have acquired an exclusive lock on the FCB associated with the SRV_OPEN and acquired either a shared or exclusive lock on the table lock of the NET_ROOT associated with the FCB. </p>

<p>If the <i>RecursiveFinalize</i> parameter is <b>TRUE</b>, then <b>RxFinalizeSrvOpen</b> will finalize any FOBX structures associated with this SRV_OPEN by calling <b>RxFinalizeNetFobx</b> with the <i>RecursiveFinalize </i>parameter set to <b>TRUE</b> and the <i>ForceFinalize</i> parameter. </p>

<p>If the <b>FcbState</b> member of the associated FCB does not have the FCB_STATE_ORPHANED flag set, then <b>RxFinalizeSrvCall</b> will call the <b>MRxForceClosed</b> routine provided by the network mini-redirector to finalize the SRV_CALL. If the SRV_CALL structure was not originally allocated as part of creating the FCB, then the memory for the SRV_CALL structure will also be released. </p>

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
<dt>Fcb.h (include Mrxfcb.h or Fcb.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550677">MRxForceClosed</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554356">RxCreateNetFcb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554358">RxCreateNetFobx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554366">RxCreateNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554370">RxCreateSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554376">RxCreateSrvOpen</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554380">RxCreateVNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554388">RxDereference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554409">RxFinalizeConnection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554412">RxFinalizeNetFcb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554418">RxFinalizeNetFobx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554421">RxFinalizeNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554426">RxFinalizeSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554450">RxFinalizeVNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554454">RxFinishFcbInitialization</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554463">RxForceFinalizeAllVNetRoots</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554688">RxReference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554728">RxSetSrvCallDomainName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554608">RxpDereferenceNetFcb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554627">RxpReferenceNetFcb</a>
</dt>
<dt>
<a href="ifsk.the_srv_open_structure">The SRV_OPEN Structure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxFinalizeSrvOpen function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
