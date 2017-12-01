---
UID: NF.fltkernel.FltCommitComplete
title: FltCommitComplete
author: windows-driver-content
description: The FltCommitComplete routine acknowledges a TRANSACTION_NOTIFY_COMMIT notification.
old-location: ifsk\fltcommitcomplete.htm
old-project: ifsk
ms.assetid: 26c553d1-5a71-4e96-a5ef-56e8e364faca
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltCommitComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltCommitComplete
req.alt-loc: Fltmgr.lib,Fltmgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fltmgr.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FltCommitComplete function



## -description
<p>The <b>FltCommitComplete</b> routine acknowledges a TRANSACTION_NOTIFY_COMMIT notification. </p>


## -syntax

````
NTSTATUS FltCommitComplete(
  _In_     PFLT_INSTANCE Instance,
  _In_     PKTRANSACTION Transaction,
  _In_opt_ PFLT_CONTEXT  TransactionContext
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the caller. </p>
</dd>

### -param <i>Transaction</i> [in]

<dd>
<p>Opaque transaction pointer for the transaction. </p>
</dd>

### -param <i>TransactionContext</i> [in, optional]

<dd>
<p>Pointer to the minifilter driver's context for the transaction. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltCommitComplete</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The minifilter driver did not set a context on the transaction. This is an error code. </p>

<p> </p>

## -remarks
<p>This routine is available on Windows Vista and later. </p>

<p>A minifilter driver that is enlisted in a transaction can receive a TRANSACTION_NOTIFY_COMMIT notification when the transaction is in the process of being committed. To send the notification to the minifilter driver, the filter manager calls the minifilter driver's <b>TransactionNotificationCallback</b> routine. The minifilter driver acknowledges this notification in one of two ways: </p>

<p>The minifilter driver's <i>TransactionNotificationCallback</i> routine performs any needed processing and returns STATUS_SUCCESS. In this case, the minifilter driver does not call <b>FltCommitComplete</b>. </p>

<p>The minifilter driver's <i>TransactionNotificationCallback</i> routine posts any needed processing to a worker thread and returns STATUS_PENDING. After performing the processing asynchronously, the minifilter driver's work routine must call <b>FltCommitComplete</b> to indicate that it has finished this processing. If the minifilter driver's work routine does not call <b>FltCommitComplete</b>, the transaction commit operation cannot be completed by the kernel transaction manager. </p>

<p>To register a <i>TransactionNotificationCallback</i> routine, a minifilter driver stores the address of a routine of type <a href="..\fltkernel\nc-fltkernel-pflt-transaction-notification-callback.md">PFLT_TRANSACTION_NOTIFICATION_CALLBACK</a> in the <b>TransactionNotificationCallback</b> member of the <a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a> structure that the minifilter driver passes as the <i>Registration</i> parameter of <a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>. </p>

<p>To enlist in a transaction, call <a href="..\fltkernel\nf-fltkernel-fltenlistintransaction.md">FltEnlistInTransaction</a>.</p>

<p>To allocate a new transaction context, call <a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>. </p>

<p>To retrieve a transaction context, call <a href="..\fltkernel\nf-fltkernel-fltgettransactioncontext.md">FltGetTransactionContext</a>. </p>

<p>To delete a transaction context, call <a href="..\fltkernel\nf-fltkernel-fltdeletetransactioncontext.md">FltDeleteTransactionContext</a> or <a href="..\fltkernel\nf-fltkernel-fltdeletecontext.md">FltDeleteContext</a>. </p>

<p>To set a transaction context, call <a href="..\fltkernel\nf-fltkernel-fltsettransactioncontext.md">FltSetTransactionContext</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-registration.md">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletecontext.md">FltDeleteContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltdeletetransactioncontext.md">FltDeleteTransactionContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltenlistintransaction.md">FltEnlistInTransaction</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgettransactioncontext.md">FltGetTransactionContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltpreparecomplete.md">FltPrepareComplete</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltprepreparecomplete.md">FltPrePrepareComplete</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltregisterfilter.md">FltRegisterFilter</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltrollbackcomplete.md">FltRollbackComplete</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltrollbackenlistment.md">FltRollbackEnlistment</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltsettransactioncontext.md">FltSetTransactionContext</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-transaction-notification-callback.md">PFLT_TRANSACTION_NOTIFICATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCommitComplete routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
