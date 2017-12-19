---
UID: NF.fcb.RxFinishFcbInitialization
title: RxFinishFcbInitialization function
author: windows-driver-content
description: RxFinishFcbInitialization is used to finish initializing an FCB after the successful completion of a create operation by the network mini-redirector.
old-location: ifsk\rxfinishfcbinitialization.htm
old-project: ifsk
ms.assetid: 290d0b06-ccf7-4792-b7bb-556092845e55
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RxFinishFcbInitialization
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fcb.h
req.include-header: Mrxfcb.h, Nodetype.h, Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxFinishFcbInitialization
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

# RxFinishFcbInitialization function



## -description
<b>RxFinishFcbInitialization</b> is used to finish initializing an FCB after the successful completion of a create operation by the network mini-redirector. 



## -syntax

````
VOID RxFinishFcbInitialization(
  _Inout_  PMRX_FCB         MrxFcb,
  _In_     RX_FILE_TYPE     RdbssStorageType,
  _In_opt_ PFCB_INIT_PACKET InitPacket
);
````


## -parameters

### -param MrxFcb [in, out]

A pointer to the MRX_FCB structure being initialized.


### -param RdbssStorageType [in]

The value indicating the storage type of entity that the FCB refers to. Possible options for this parameter include the following:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

### -param RDBSS_NTC_MAILSLOT

</td>
<td width="60%">
A mail slot.

</td>
</tr>
<tr>

### -param RDBSS_NTC_SPOOLFILE

</td>
<td width="60%">
A printer spool file.

</td>
</tr>
<tr>

### -param RDBSS_NTC_STORAGE_TYPE_DIRECTORY

</td>
<td width="60%">
A directory.

</td>
</tr>
<tr>

### -param RDBSS_NTC_STORAGE_TYPE_UNKNOWN

</td>
<td width="60%">
The storage type is unknown.

</td>
</tr>
<tr>

### -param RDBSS_NTC_STORAGE_TYPE_FILE

</td>
<td width="60%">
A file.

</td>
</tr>
</table>
 


### -param InitPacket [in, optional]

Pointer to extra data that is required for initialization depending on the storage type of the FCB being initialized. This parameter may be a <b>NULL</b> pointer if no extra data is provided.


## -returns
None


## -remarks
When called as a result of an IRP_MJ_CREATE, <a href="ifsk.rxcreatenetfcb">RxCreateNetFCB</a> is called first to create the FCB. If the <b>Type</b> member of the NET_ROOT to be created is not a NET_ROOT_MAILSLOT, then <b>RxFinishFcbInitialization</b> is called to finish the initialization of the FCB structure. 

If the <b>FcbState</b> member of the MRX_FCB structure pointed to by <i>MrxFcb</i> does not have the FCB_STATE_TIME_AND_SIZE_ALREADY_SET on, then the following members of the FCB will be updated from the <i>InitPacket</i> parameter if <i>InitPacket</i> is non <b>NULL</b>: <b>Attributes</b>, <b>NumberOfLinks</b>, <b>CreationTime</b>, <b>LastAccessTime</b>, <b>LastWriteTime</b>, <b>LastChangeTime</b>, <b>ActualAllocationLength</b>, <b>Header.AllocationSize</b>, <b>Header.FileSize</b>, and <b>Header.ValidDataLength</b>. The FCB_STATE_TIME_AND_SIZE_ALREADY_SET option is then set on in the <b>FcbState</b> member of the FCB structure.

If the storage type is an RDBSS_NTC_MAILSLOT and the FcbState member of the FCB does have the FCB_STATE_TIME_AND_SIZE_ALREADY_SET option set on, then the following members of the FCB structure for the mail slot will be initialized to 0: <b>Attributes</b>, <b>NumberOfLinks</b>,<b> CreationTime.QuadPart</b>,<b> LastAccessTime.QuadPart</b>, <b>LastWriteTime.QuadPart</b>, <b>LastChangeTime</b>.<b>QuadPart</b>, <b>ActualAllocationLength</b>, <b>Header.AllocationSize.QuadPart</b>, <b>Header.FileSize.QuadPart</b>, and <b>Header.ValidDataLength.QuadPart</b>


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
<dt>Fcb.h (include Mrxfcb.h, Nodetype.h, or Fcb.h)</dt>
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
<a href="ifsk.rxcreatenetfcb">RxCreateNetFCB</a>
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
<a href="ifsk.rxfinalizevnetroot">RxFinalizeVNetRoot</a>
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
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxFinishFcbInitialization function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

