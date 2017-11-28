---
UID: NC.mrx.PMRX_FINALIZE_V_NET_ROOT_CALLDOWN
title: PMRX_FINALIZE_V_NET_ROOT_CALLDOWN
author: windows-driver-content
description: The MRxFinalizeVNetRoot routine is called by RDBSS to request that a network mini-redirector finalize a V_NET_ROOT structure.
old-location: ifsk\mrxfinalizevnetroot.htm
old-project: ifsk
ms.assetid: 13d0c903-57b6-4a57-977a-bf1bd651660f
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
req.alt-api: MRxFinalizeVNetRoot
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

# PMRX_FINALIZE_V_NET_ROOT_CALLDOWN callback



## -description
<p>The <i>MRxFinalizeVNetRoot</i> routine is called by <a href="ifsk.the_rdbss_driver_and_library">RDBSS</a> to request that a network mini-redirector finalize a V_NET_ROOT structure.</p>


## -prototype

````
PMRX_FINALIZE_V_NET_ROOT_CALLDOWN MRxFinalizeVNetRoot;

NTSTATUS MRxFinalizeVNetRoot(
  _Inout_ PMRX_V_NET_ROOT pVNetRoot,
  _In_    PBOOLEAN        ForceDisconnect
)
{ ... }
````


## -parameters
<dl>

### -param <i>pVNetRoot</i> [in, out]

<dd>
<p>A pointer to the V_NET_ROOT structure to finalize. </p>
</dd>

### -param <i>ForceDisconnect</i> [in]

<dd>
<p>A pointer to a Boolean value that indicates if the disconnect is to be forced. RDBSS currently passes <b>FALSE</b> for this parameter in all cases.</p>
</dd>
</dl>

## -returns
<p><i>MRxFinalizeVNetRoot</i> returns STATUS_SUCCESS on success. </p>

## -remarks
<p><i>MRxFinalizeVNetRoot</i> is called by RDBSS when it finalizes a NET_ROOT structure. </p>

<p>After the <i>MRxFinalizeVNetRoot</i> returns, RDBSS uninitializes the V_NET_ROOT structure members, dereferences the NET_ROOT structure, and releases the memory for the V_NET_ROOT structure.</p>

<p>RDBSS ignores the return value from <i>MRxFinalizeVNetRoot</i>. </p>

<p><i>MRxFinalizeVNetRoot</i> is called by RDBSS when it finalizes a NET_ROOT structure. </p>

<p>After the <i>MRxFinalizeVNetRoot</i> returns, RDBSS uninitializes the V_NET_ROOT structure members, dereferences the NET_ROOT structure, and releases the memory for the V_NET_ROOT structure.</p>

<p>RDBSS ignores the return value from <i>MRxFinalizeVNetRoot</i>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549864">MRxCreateSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549869">MRxCreateVNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550649">MRxExtractNetRootName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550653">MRxFinalizeNetRoot</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554426">RxFinalizeSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550750">MRxPreparseName</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550824">MRxSrvCallWinnerNotify</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxFinalizeVNetRoot routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
