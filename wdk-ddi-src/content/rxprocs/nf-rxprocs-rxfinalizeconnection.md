---
UID : NF:rxprocs.RxFinalizeConnection
title : RxFinalizeConnection function
author : windows-driver-content
description : RxFinalizeConnection deletes a connection to a share.
old-location : ifsk\rxfinalizeconnection.htm
old-project : ifsk
ms.assetid : 3f3e6c56-937e-4a4b-885a-71be2e9513d8
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : RxFinalizeConnection
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : rxprocs.h
req.include-header : Rxprocs.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RxFinalizeConnection
req.alt-loc : rxprocs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= APC_LEVEL
req.typenames : RX_CONTEXT, *PRX_CONTEXT
req.product : Windows 10 or later.
---


# RxFinalizeConnection function
<b>RxFinalizeConnection</b> deletes a connection to a share. Any files open on the connection are closed depending on the level of force specified. The network mini-redirector might choose to keep the transport connection open for performance reasons, unless some option is specified to force a close of connection.

## Syntax

````
NTSTATUS RxFinalizeConnection(
  _Inout_     PNET_ROOT   NetRoot,
  _Inout_opt_ PV_NET_ROOT VNetRoot,
  _In_        LOGICAL     Level
);
````

## Parameters

`NetRoot`

A pointer to the NET_ROOT structure being finalized.

`OPTIONAL`



`ForceFilesClosed`




## Return Value

<b>RxFinalizeConnection</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: 
<dl>
<dt><b>STATUS_CANCELLED</b></dt>
</dl>The <b>Flags</b> member of the RX_CONTEXT structure indicates the IRP was canceled.
<dl>
<dt><b>STATUS_CONNECTION_IN_USE</b></dt>
</dl>The connection is still in use.
<dl>
<dt><b>STATUS_FILES_OPEN</b></dt>
</dl>The file was open, so the remote connection should not be deleted.
<dl>
<dt><b>STATUS_LOCK_NOT_GRANTED</b></dt>
</dl>An exclusive lock on the associated

## Remarks

<b>RxFinalizeConnection</b> is normally called by a network mini-redirector driver in response to receiving a custom IOCTL request from user mode. For example, a user might execute from the command line a "NET USE x: /d" to delete a share. This request would be mapped through the network provider DLL provided by the network mini-redirector to a custom IOCTL request sent to the network mini-redirector kernel driver which would call the <b>RxFinalizeConnection</b> routine to delete the connection.

<b>RxFinalizeConnection</b> cancels all the outstanding requests for a given V_NET_ROOT structure. These V_NET_ROOT structures are created and deleted independent of the files that are opened and manipulated on them. Therefore it is imperative that when a delete operation is attempted, all the outstanding requests are canceled.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rxprocs.h (include Rxprocs.h) |
| **Library** |  |
| **IRQL** | <= APC_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/f7846343-9af6-4b7f-9c8d-190abb524946">The NET_ROOT Structure</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/866eba91-13b6-4b15-93de-4f627a635c92">The V_NET_ROOT Structure</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxcreatenetfcb.md">RxCreateNetFcb</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxcreatenetfobx.md">RxCreateNetFobx</a>
</dt>
<dt>
<a href="..\fcb\nf-fcb-rxcreatenetroot.md">RxCreateNetRoot</a>
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
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxFinalizeConnection function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>