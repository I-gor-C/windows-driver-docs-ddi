---
UID: NF.fcb.RxFinalizeSrvCall
title: RxFinalizeSrvCall function
author: windows-driver-content
description: RxFinalizeSrvCall finalizes the given SRV_CALL structure. The caller must have an exclusive lock on the netname table associated with the device object.
old-location: ifsk\rxfinalizesrvcall.htm
old-project: ifsk
ms.assetid: 293bb629-ac31-4ae3-bba3-b06812e9e6cb
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RxFinalizeSrvCall
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
req.alt-api: RxFinalizeSrvCall
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

# RxFinalizeSrvCall function



## -description
<b>RxFinalizeSrvCall</b> finalizes the given SRV_CALL structure. The caller must have an exclusive lock on the netname table associated with the device object. 



## -syntax

````
BOOLEAN RxFinalizeSrvCall(
  _Out_ PSRV_CALL ThisSrvCall,
  _In_  BOOLEAN   ForceFinalize
);
````


## -parameters

### -param ThisSrvCall [out]

A pointer to the SRV_CALL structure to finalize.


### -param ForceFinalize [in]

The value indicating whether the finalization should be forced, regardless of the reference count. 

If <i>ForceFinalize</i> is <b>FALSE</b>, then the <b>NodeReferenceCount</b> member of the SRV_CALL structure pointed to by <i>ThisSrvCall</i> must be 1 for the SRV_CALL to be finalized. 


## -returns
<b>RxFinalizeSrvCall</b> returns <b>TRUE</b> on success or <b>FALSE</b> if the finalization did not occur: 


## -remarks
The <b>RxFinalizeSrvCall</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally when the reference count on the SRV_CALL is decremented to 1. RDBSS also calls <b>RxFinalizeSrvCall</b> when the network mini-redirector driver is stopped or unloaded. 

Before calling <b>RxFinalizeSrvCall</b>, a lock on the netname table associated with the device object must be acquired in exclusive mode. 

If the current executing process ID is the same as the RDBSS process ID, then a delayed worker thread will be dispatched to destroy the SRV_CALL structure. This worker thread will later call the <b>MRxFinalizeSrvCall</b> routine provided by the network mini-redirector to finalize the SRV_CALL. Otherwise, the <b>MRxFinalizeSrvCall</b> routine will be called directly to finalize the SRV_CALL. 


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
<a href="ifsk.mrxfinalizesrvcall">MRxFinalizeSrvCall</a>
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
<a href="ifsk.the_srv_call_structure">The SRV_CALL Structure</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxFinalizeSrvCall function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

