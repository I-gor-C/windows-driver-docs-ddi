---
UID: NF.fcb.RxCreateSrvOpen
title: RxCreateSrvOpen
author: windows-driver-content
description: RxCreateSrvOpen allocates, initializes, and inserts a new SRV_OPEN structure into the in-memory data structures used by RDBSS. If a new structure has to be allocated, it has space for an FOBX structure.
old-location: ifsk\rxcreatesrvopen.htm
ms.assetid: e2cb8b92-2894-4515-bdf1-944c7f6ed3b0
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
req.alt-api: RxCreateSrvOpen
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
ms.keywords: RxCreateSrvOpen
req.iface: 
---

# RxCreateSrvOpen function



## -description
<p><b>RxCreateSrvOpen</b> allocates, initializes, and inserts a new SRV_OPEN structure into the in-memory data structures used by RDBSS. If a new structure has to be allocated, it has space for an FOBX structure. </p>


## -syntax

````
PSRV_OPEN RxCreateSrvOpen(
  _In_    PV_NET_ROOT VNetRoot,
  _Inout_ PFCB        Fcb
);
````


## -parameters
<dl>

### -param <i>VNetRoot</i> [in]

<dd>
<p>A pointer to the V_NET_ROOT structure.</p>
</dd>

### -param <i>Fcb</i> [in, out]

<dd>
<p>A pointer to the associated FCB structure.</p>
</dd>
</dl>

## -returns
<p><b>RxCreateSrvOpen</b> returns a pointer to a newly created SRV_OPEN data structure on success or a <b>NULL</b> pointer on failure. </p>

## -remarks
<p>The <b>RxCreateSrvOpen</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when an I/O request packet is received for IRP_MJ_CREATE and a SRV_OPEN needs to be created. This IRP is normally received by RDBSS in response to a user-mode application requesting a file create operation on a network share. It is also possible for another kernel driver to issue such an IRP. </p>

<p>Before calling <b>RxCreateSrvOpen</b>, a lock on the associated FCB structure must be acquired in exclusive mode. </p>

<p><b>RxCreateSrvOpen </b>will try and use the SRV_CALL allocated as part of the associated FCB structure if it is available. If the SRV_CALL allocated with the FCB is not available, then <b>RxCreateSrvOpen</b> will allocate a new SRV_CALL structure. </p>

<p>If the associated FCB is a paging file, <b>RxCreateSrvOpen</b> allocates non-paged pool memory when creating the new SRV_OPEN data structure. If the associated FCB is a not a paging file, <b>RxCreateSrvOpen</b> allocates paged pool memory when creating the new SRV_OPEN data structure.</p>

<p>Windows does not currently allow having a paging file on a remote machine. </p>

<p>The <b>RxCreateSrvOpen</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when an I/O request packet is received for IRP_MJ_CREATE and a SRV_OPEN needs to be created. This IRP is normally received by RDBSS in response to a user-mode application requesting a file create operation on a network share. It is also possible for another kernel driver to issue such an IRP. </p>

<p>Before calling <b>RxCreateSrvOpen</b>, a lock on the associated FCB structure must be acquired in exclusive mode. </p>

<p><b>RxCreateSrvOpen </b>will try and use the SRV_CALL allocated as part of the associated FCB structure if it is available. If the SRV_CALL allocated with the FCB is not available, then <b>RxCreateSrvOpen</b> will allocate a new SRV_CALL structure. </p>

<p>If the associated FCB is a paging file, <b>RxCreateSrvOpen</b> allocates non-paged pool memory when creating the new SRV_OPEN data structure. If the associated FCB is a not a paging file, <b>RxCreateSrvOpen</b> allocates paged pool memory when creating the new SRV_OPEN data structure.</p>

<p>Windows does not currently allow having a paging file on a remote machine. </p>

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
<a href="ifsk.the_fcb_structure">The FCB Structure</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554432">RxFinalizeSrvOpen</a>
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
<dt>
<a href="ifsk.the_v_net_root_structure">The V_NET_ROOT Structure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCreateSrvOpen function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
