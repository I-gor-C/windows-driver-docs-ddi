---
UID: NF.fltkernel.FltPrepareComplete
title: FltPrepareComplete function
author: windows-driver-content
description: The FltPrepareComplete routine acknowledges a TRANSACTION_NOTIFY_PREPARE notification.
old-location: ifsk\fltpreparecomplete.htm
old-project: ifsk
ms.assetid: 5b6322a3-3813-4ca8-a966-d6b8bddbe794
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltPrepareComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: The FltPrepareComplete routine is available on Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltPrepareComplete
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
---

# FltPrepareComplete function



## -description
The <b>FltPrepareComplete</b> routine acknowledges a TRANSACTION_NOTIFY_PREPARE notification. 



## -syntax

````
NTSTATUS FltPrepareComplete(
  _In_     PFLT_INSTANCE Instance,
  _In_     PKTRANSACTION Transaction,
  _In_opt_ PFLT_CONTEXT  TransactionContext
);
````


## -parameters

### -param Instance [in]

Opaque instance pointer for the caller. 


### -param Transaction [in]

Opaque transaction pointer for the transaction. 


### -param TransactionContext [in, optional]

Pointer to the minifilter driver's transaction context. 


## -returns
<b>FltPrepareComplete</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as the following: 
<dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl>The minifilter driver did not set a context on the transaction. This is an error code. 

 


## -remarks
A minifilter driver that is enlisted in a transaction can receive a TRANSACTION_NOTIFY_PREPARE notification when the transaction enters the prepare for commit phase. To send the notification to the minifilter driver, the filter manager calls the minifilter driver's <i>TransactionNotificationCallback</i> routine. The minifilter driver acknowledges this notification in one of two ways: 

The minifilter driver's <i>TransactionNotificationCallback</i> routine performs any needed processing and returns STATUS_SUCCESS. In this case, the minifilter driver does not call <b>FltPrepareComplete</b>. 

The minifilter driver's <i>TransactionNotificationCallback</i> routine posts any needed processing to a worker thread and returns STATUS_PENDING. After performing the processing asynchronously, the minifilter driver's work routine must call <b>FltPrepareComplete</b> to indicate that it has finished this processing. If the minifilter driver's work routine does not call <b>FltPrepareComplete</b>, the transaction prepare operation cannot be completed by the kernel transaction manager. 

To register a <i>TransactionNotificationCallback</i> routine, a minifilter driver stores the address of a routine of type <a href="..\fltkernel\nc-fltkernel-pflt_transaction_notification_callback.md">PFLT_TRANSACTION_NOTIFICATION_CALLBACK</a> in the <b>TransactionNotificationCallback</b> member of the <a href="ifsk.flt_registration">FLT_REGISTRATION</a> structure that the minifilter driver passes as the <i>Registration</i> parameter of <a href="ifsk.fltregisterfilter">FltRegisterFilter</a>. 

To enlist in a transaction, call <a href="ifsk.fltenlistintransaction">FltEnlistInTransaction</a>.

To allocate a new transaction context, call <a href="ifsk.fltallocatecontext">FltAllocateContext</a>. 

To retrieve a transaction context, call <a href="ifsk.fltgettransactioncontext">FltGetTransactionContext</a>. 

To delete a transaction context, call <a href="ifsk.fltdeletetransactioncontext">FltDeleteTransactionContext</a> or <a href="ifsk.fltdeletecontext">FltDeleteContext</a>. 

To set a transaction context, call <a href="ifsk.fltsettransactioncontext">FltSetTransactionContext</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
The FltPrepareComplete routine is available on Windows Vista and later. 

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
<a href="ifsk.flt_registration">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="ifsk.fltallocatecontext">FltAllocateContext</a>
</dt>
<dt>
<a href="ifsk.fltcommitcomplete">FltCommitComplete</a>
</dt>
<dt>
<a href="ifsk.fltdeletecontext">FltDeleteContext</a>
</dt>
<dt>
<a href="ifsk.fltdeletetransactioncontext">FltDeleteTransactionContext</a>
</dt>
<dt>
<a href="ifsk.fltenlistintransaction">FltEnlistInTransaction</a>
</dt>
<dt>
<a href="ifsk.fltgettransactioncontext">FltGetTransactionContext</a>
</dt>
<dt>
<a href="ifsk.fltprepreparecomplete">FltPrePrepareComplete</a>
</dt>
<dt>
<a href="ifsk.fltregisterfilter">FltRegisterFilter</a>
</dt>
<dt>
<a href="ifsk.fltreleasecontext">FltReleaseContext</a>
</dt>
<dt>
<a href="ifsk.fltrollbackcomplete">FltRollbackComplete</a>
</dt>
<dt>
<a href="ifsk.fltrollbackenlistment">FltRollbackEnlistment</a>
</dt>
<dt>
<a href="ifsk.fltsettransactioncontext">FltSetTransactionContext</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt_transaction_notification_callback.md">PFLT_TRANSACTION_NOTIFICATION_CALLBACK</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltPrepareComplete routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

