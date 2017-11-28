---
UID: NF.fcb.RxCreateVNetRoot
title: RxCreateVNetRoot
author: windows-driver-content
description: RxCreateVNetRoot allocates and initializes a NET_ROOT structure and inserts the name into the net name table on the associated device object.
old-location: ifsk\rxcreatevnetroot.htm
old-project: ifsk
ms.assetid: 852cc319-4bcd-427d-802f-3c82c72901f0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxCreateVNetRoot
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
req.alt-api: RxCreateVNetRoot
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

# RxCreateVNetRoot function



## -description
<p><b>RxCreateVNetRoot</b> allocates and initializes a NET_ROOT structure and inserts the name into the net name table on the associated device object. </p>


## -syntax

````
PV_NET_ROOT RxCreateVNetRoot(
  _In_ PRX_CONTEXT       RxContext,
  _In_ PNET_ROOT         NetRoot,
  _In_ PUNICODE_STRING   CanonicalName,
  _In_ PUNICODE_STRING   LocalNetRootName,
  _In_ PUNICODE_STRING   FilePath,
  _In_ PRX_CONNECTION_ID RxConnectionId
);
````


## -parameters
<dl>

### -param <i>RxContext</i> [in]

<dd>
<p>A pointer to the RDBSS RX_CONTEXT containing the IRP describing a create operation.</p>
</dd>

### -param <i>NetRoot</i> [in]

<dd>
<p>A pointer to the associated NET_ROOT structure.</p>
</dd>

### -param <i>CanonicalName</i> [in]

<dd>
<p>A pointer to the canonical name to be inserted in the name table.</p>
</dd>

### -param <i>LocalNetRootName</i> [in]

<dd>
<p>A pointer to the local NET_ROOT name without the prefix name.</p>
</dd>

### -param <i>FilePath</i> [in]

<dd>
<p>A pointer to a file pathname. This parameter is not currently used and can be <b>NULL</b>.</p>
</dd>

### -param <i>RxConnectionId</i> [in]

<dd>
<p>A pointer to the connection ID to be associated with the name to be inserted in the prefix name table. This parameter can be <b>NULL</b> in which case no connection ID will be associated with the name inserted in the name table.</p>
</dd>
</dl>

## -returns
<p><b>RxCreateVNetRoot</b> returns a pointer to a newly created V_NET_ROOT data structure on success or a <b>NULL</b> pointer on failure. </p>

## -remarks
<p>The <b>RxCreateVNetRoot</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when an I/O request packet is received for IRP_MJ_CREATE and a V_NET_ROOT needs to be created. This IRP is normally received by RDBSS in response to a user-mode application requesting a file create operation on a network share. It is also possible for another kernel driver to issue such an IRP. </p>

<p>Before calling <b>RxCreateVNetRoot</b>, a lock on the name table associated with the device object member of the <i>RxContext</i> parameter must be acquired in exclusive mode. </p>

<p><b>RxCreateVNetRoot</b> sets a variety of security context parameters on the V_NET_ROOT structure based on parameters from the RX_CONTEXT. These parameters include the following: <i>LogonId</i>, <i>SessionId</i>, <i>pUserName</i>, <i>pUserDomainName</i>, <i>pPassword</i>, and <i>Flags</i>. </p>

<p>The <b>RxCreateVNetRoot</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when an I/O request packet is received for IRP_MJ_CREATE and a V_NET_ROOT needs to be created. This IRP is normally received by RDBSS in response to a user-mode application requesting a file create operation on a network share. It is also possible for another kernel driver to issue such an IRP. </p>

<p>Before calling <b>RxCreateVNetRoot</b>, a lock on the name table associated with the device object member of the <i>RxContext</i> parameter must be acquired in exclusive mode. </p>

<p><b>RxCreateVNetRoot</b> sets a variety of security context parameters on the V_NET_ROOT structure based on parameters from the RX_CONTEXT. These parameters include the following: <i>LogonId</i>, <i>SessionId</i>, <i>pUserName</i>, <i>pUserDomainName</i>, <i>pPassword</i>, and <i>Flags</i>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554356">RxCreateNetFcb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554358">RxCreateNetFobx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554370">RxCreateSrvCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554376">RxCreateSrvOpen</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554366">RxCreateNetRoot</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554493">RxInferFileType</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554751">RX_CONTEXT</a>
</dt>
<dt>
<a href="ifsk.the_v_net_root_structure">The V_NET_ROOT Structure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCreateVNetRoot function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
