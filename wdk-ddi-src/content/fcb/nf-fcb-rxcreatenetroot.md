---
UID: NF.fcb.RxCreateNetRoot
title: RxCreateNetRoot
author: windows-driver-content
description: RxCreateNetRoot allocates and initializes a NET_ROOT structure and inserts the name into the net name table on the associated device object.
old-location: ifsk\rxcreatenetroot.htm
old-project: ifsk
ms.assetid: 076624d3-96f5-4e93-8598-b880a6b2289b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxCreateNetRoot
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fcb.h
req.include-header: Rxcontx.h, Mrxfcb.h, Prefix.h, Struchdr.h, Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCreateNetRoot
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
req.iface: 
---

# RxCreateNetRoot function



## -description
<p><b>RxCreateNetRoot</b> allocates and initializes a NET_ROOT structure and inserts the name into the net name table on the associated device object. </p>


## -syntax

````
PNET_ROOT RxCreateNetRoot(
  _In_     PSRV_CALL         SrvCall,
  _In_     PUNICODE_STRING   Name,
  _In_     ULONG             NetRootFlags,
  _In_opt_ PRX_CONNECTION_ID RxConnectionId
);
````


## -parameters
<dl>

### -param <i>SrvCall</i> [in]

<dd>
<p>A pointer to the associated SRV_CALL structure.</p>
</dd>

### -param <i>Name</i> [in]

<dd>
<p>A pointer to the name to be inserted in the name table.</p>
</dd>

### -param <i>NetRootFlags</i> [in]

<dd>
<p>The value to set the <b>Flags</b> member of the NET_ROOT which is used to denote the state of the NET_ROOT structure.</p>
</dd>

### -param <i>RxConnectionId</i> [in, optional]

<dd>
<p>A pointer to the connection ID to be associated with the name to be inserted in the prefix name table. This parameter can be <b>NULL</b> in which case no connection ID will be associated with the name inserted in the prefix name table.</p>
</dd>
</dl>

## -returns
<p><b>RxCreateNetRoot</b> returns a pointer to a newly created NET_ROOT data structure on success or a <b>NULL</b> pointer on failure. </p>

## -remarks
<p>The <b>RxCreateNetRoot</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when an I/O request packet is received for IRP_MJ_CREATE and a NET_ROOT needs to be created. This IRP is normally received by RDBSS in response to a user-mode application requesting a file create operation on a network share. It is also possible for another kernel driver to issue such an IRP. </p>

<p>Before calling <b>RxCreateNetRoot</b>, a lock on the name table associated with the device object member of the <i>SrvCall</i> parameter must be acquired in exclusive mode. </p>

<p>The NET_ROOT flags are split into two groups, those visible to network mini redirectors and those invisible to network mini redirectors. The visible ones are the lower 16-bits of the <b>Flags</b> member of the NET_ROOT. This routine does not check or test which flags are being set. </p>

<p>On success, the reference count for the SRV_CALL structure is incremented. </p>

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
<dt>Fcb.h (include Rxcontx.h, Mrxfcb.h, Prefix.h, Struchdr.h, or Fcb.h)</dt>
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
<a href="ifsk.the_net_root_structure">The NET_ROOT Structure</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxcreatenetfcb.md">RxCreateNetFcb</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxcreatenetfobx.md">RxCreateNetFobx</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxcreatesrvcall.md">RxCreateSrvCall</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxcreatesrvopen.md">RxCreateSrvOpen</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxcreatevnetroot.md">RxCreateVNetRoot</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxdereference.md">RxDereference</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxfinalizeconnection.md">RxFinalizeConnection</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxfinalizenetfcb.md">RxFinalizeNetFcb</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxfinalizenetfobx.md">RxFinalizeNetFobx</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxfinalizenetroot.md">RxFinalizeNetRoot</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxfinalizesrvcall.md">RxFinalizeSrvCall</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxfinalizesrvopen.md">RxFinalizeSrvOpen</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxfinalizevnetroot.md">RxFinalizeVNetRoot</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxfinishfcbinitialization.md">RxFinishFcbInitialization</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxforcefinalizeallvnetroots.md">RxForceFinalizeAllVNetRoots</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxreference.md">RxReference</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxsetsrvcalldomainname.md">RxSetSrvCallDomainName</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxpdereferencenetfcb.md">RxpDereferenceNetFcb</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxpreferencenetfcb.md">RxpReferenceNetFcb</a>
</dt>
<dt>
<a href="ifsk.the_srv_call_structure">The SRV_CALL Structure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCreateNetRoot function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
