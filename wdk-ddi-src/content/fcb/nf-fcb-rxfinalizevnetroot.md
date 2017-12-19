---
UID: NF.fcb.RxFinalizeVNetRoot
title: RxFinalizeVNetRoot function
author: windows-driver-content
description: RxFinalizeVNetRoot finalizes the given V_NET_ROOT structure. The caller must have an exclusive lock on the netname table associated with the device object.
old-location: ifsk\rxfinalizevnetroot.htm
old-project: ifsk
ms.assetid: 7a24d8b4-cd07-453c-9813-d794b75b039e
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RxFinalizeVNetRoot
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fcb.h
req.include-header: Mrxfcb.h, Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxFinalizeVNetRoot
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

# RxFinalizeVNetRoot function



## -description
<b>RxFinalizeVNetRoot</b> finalizes the given V_NET_ROOT structure. The caller must have an exclusive lock on the netname table associated with the device object. 



## -syntax

````
BOOLEAN RxFinalizeVNetRoot(
  _Out_ PV_NET_ROOT ThisVNetRoot,
  _In_  BOOLEAN     RecursiveFinalize,
  _In_  BOOLEAN     ForceFinalize
);
````


## -parameters

### -param ThisVNetRoot [out]

A pointer to the V_NET_ROOT structure to finalize.


### -param RecursiveFinalize [in]

The value indicating whether the finalization should be done recursively. This parameter in not currently used.


### -param ForceFinalize [in]

The value indicating whether the finalization should be forced, regardless of the reference count. 

If <i>ForceFinalize</i> is <b>FALSE</b>, then the <b>NodeReferenceCount</b> member of the V_NET_ROOT structure pointed to by <i>ThisVNetRoot</i> must be 1 for the V_NET_ROOT to be finalized. 


## -returns
<b>RxFinalizeVNetRoot</b> returns <b>TRUE</b> on success or <b>FALSE</b> if the finalization did not occur: 


## -remarks
The <b>RxFinalizeVNetRoot</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when the reference count on the V_NET_ROOT is decremented to 1. 

<b>RxFinalizeVNetRoot</b> is also called by the <b>RxFinalizeConnection</b> routine if the <i>Level</i> parameter to <b>RxFinalizeConnection</b> is set to <b>TRUE</b>. <b>RxFinalizeConnection</b> is normally called by a network mini-redirector driver in response to receiving a custom IOCTL request from user mode. For example, a user might execute from the command line a "NET USE x: /d" to delete a share. This request would be mapped through the network provider DLL provided by the network mini-redirector to a custom IOCTL request sent to the network mini-redirector kernel driver which would call the <b>RxFinalizeConnection</b> routine to delete the connection and any associated V_NET_ROOT structures.

<b>RxFinalizeVNetRoot</b> is also called by the <b>RxForceFinalizeAllVNetRoots</b> routine to finalize each V_NET_ROOT associated with a NET_ROOT structure.

Before calling <b>RxFinalizeVNetRoot</b>, a lock on the netname table associated with the device object must be acquired in exclusive mode. 

If the <b>UpperFinalization</b> member of the V_NET_ROOT is 0, then <b>RxFinalizeVNetRoot</b> will iterate through all the FCBs that belong to the NET_ROOT associated with this V_NET_ROOT and orphan all of the SRV_OPEN structures that are associated with the V_NET_ROOT. 

<b>RxFinalizeVNetRoot</b> will call the <b>MRxFinalizeVNetRoot</b> routine provided by the network mini-redirector to finalize the V_NET_ROOT before the memory for the V_NET_ROOT structure will be released. 


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
<dt>Fcb.h (include Mrxfcb.h or Fcb.h)</dt>
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
<a href="ifsk.mrxfinalizevnetroot">MRxFinalizeVNetRoot</a>
</dt>
<dt>
<a href="ifsk.rxcreatenetfcb">RxCreateNetFcb</a>
</dt>
<dt>
<a href="ifsk.rxcreatenetfobx">RxCreateNetFobx</a>
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
<a href="ifsk.the_v_net_root_structure">The V_NET_ROOT Structure</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxFinalizeVNetRoot function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

