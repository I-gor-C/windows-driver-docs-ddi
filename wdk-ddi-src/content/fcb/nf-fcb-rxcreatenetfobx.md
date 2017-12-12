---
UID: NF.fcb.RxCreateNetFobx
title: RxCreateNetFobx function
author: windows-driver-content
description: RxCreateNetFobx allocates, initializes, and inserts a new file object extension (FOBX) structure into the in-memory data structures for a FCB that this FOBX is being opened on.
old-location: ifsk\rxcreatenetfobx.htm
old-project: ifsk
ms.assetid: 4ea03ea5-31df-4220-982c-0102d20c2d4a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxCreateNetFobx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fcb.h
req.include-header: Rxcontx.h, Mrxfcb.h, Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCreateNetFobx
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
---

# RxCreateNetFobx function



## -description
<b>RxCreateNetFobx</b> allocates, initializes, and inserts a new file object extension (FOBX) structure into the in-memory data structures for a FCB that this FOBX is being opened on. 



## -syntax

````
PMRX_FOBX RxCreateNetFobx(
  _Out_ PRX_CONTEXT   RxContext,
  _In_  PMRX_SRV_OPEN MrxSrvOpen
);
````


## -parameters

### -param RxContext [out]

A pointer to the RX_CONTEXT structure describing a create operation.


### -param MrxSrvOpen [in]

A pointer to the associated SRV_OPEN structure.


## -returns
<b>RxCreateNetFobx</b> returns a pointer to a newly allocated FOBX data structure on success or a <b>NULL</b> pointer on failure. 


## -remarks
Network mini-redirectors should call <b>RxCreateNetFobx</b> to create an FOBX at the end of a successful create operation.

Before calling <b>RxCreateNetFobx</b>, the FCB associated with the FOBX structure must be acquired in exclusive mode. 

<b>RxCreateNetFobx </b>will try and use the FOBX allocated as part of the associated FCB structure if it is available. If the FOBX allocated with the FCB is not available, then <b>RxCreateNetFobx </b>will try and use the FOBX allocated as part of the associated SRV_OPEN structure if it is available. In either of these cases, <b>RxCreateNetFobx</b> only needs to initialize the existing FOBX structure, no memory allocation is required. If both of the FOBX structures on the associated FCB and SRV_OPEN structure are not available, then <b>RxCreateNetFobx</b> will allocate a new FOBX structure. 

If the associated FCB is a paging file, <b>RxCreateNetFobx</b> allocates non-paged pool memory when creating the new FOBX data structure. If the associated FCB is a not a paging file, <b>RxCreateNetFobx</b> allocates paged pool memory when creating the new FOBX data structure.

Windows does not currently allow having a paging file on a remote machine.

On success, the following FOBX members in the FOBX structure are set:

The <b>NodeReference</b> member is set to 1.

The <b>FobxSerialNumber</b> member is set to 0.

The <b>SrvOpen</b> member is set to the associated SRV_OPEN structure.

The <b>fOpenCountDecremented</b> member is set to <b>FALSE</b>.

The <b>Flags</b> member is set to a value based on parameters from the RX_CONTEXT and whether a new FOBX needed to be allocated. 

On success, the reference count for the SRV_OPEN structure is incremented and the <b>NumberOfFobxs</b> member on the associated V_NET_ROOT structure is incremented. 


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
<dt>Fcb.h (include Rxcontx.h, Mrxfcb.h, or Fcb.h)</dt>
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
<a href="ifsk.rxcreatenetfcb">RxCreateNetFcb</a>
</dt>
<dt>
<a href="ifsk.rxcreatenetroot">RxCreateNetRoot</a>
</dt>
<dt>
<a href="ifsk.rxcreatesrvcall">RxCreateSrvCall</a>
</dt>
<dt>
<a href="ifsk.rxcreatesrvopen">RxCreateSrvOpen</a>
</dt>
<dt>
<a href="ifsk.rxcreatevnetroot">RxCreateVNetRoot</a>
</dt>
<dt>
<a href="ifsk.rxdereference">RxDereference</a>
</dt>
<dt>
<a href="ifsk.rxfinalizeconnection">RxFinalizeConnection</a>
</dt>
<dt>
<a href="ifsk.rxfinalizenetfcb">RxFinalizeNetFcb</a>
</dt>
<dt>
<a href="ifsk.rxfinalizenetfobx">RxFinalizeNetFobx</a>
</dt>
<dt>
<a href="ifsk.rxfinalizenetroot">RxFinalizeNetRoot</a>
</dt>
<dt>
<a href="ifsk.rxfinalizesrvcall">RxFinalizeSrvCall</a>
</dt>
<dt>
<a href="ifsk.rxfinalizesrvopen">RxFinalizeSrvOpen</a>
</dt>
<dt>
<a href="ifsk.rxfinalizevnetroot">RxFinalizeVNetRoot</a>
</dt>
<dt>
<a href="ifsk.rxfinishfcbinitialization">RxFinishFcbInitialization</a>
</dt>
<dt>
<a href="ifsk.rxforcefinalizeallvnetroots">RxForceFinalizeAllVNetRoots</a>
</dt>
<dt>
<a href="ifsk.rxreference">RxReference</a>
</dt>
<dt>
<a href="ifsk.rxsetsrvcalldomainname">RxSetSrvCallDomainName</a>
</dt>
<dt>
<a href="ifsk.rxpdereferencenetfcb">RxpDereferenceNetFcb</a>
</dt>
<dt>
<a href="ifsk.rxpreferencenetfcb">RxpReferenceNetFcb</a>
</dt>
<dt>
<a href="ifsk.rx_context">RX_CONTEXT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCreateNetFobx function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

