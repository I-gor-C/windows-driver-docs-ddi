---
UID: NF.fltkernel.FltSetTransactionContext
title: FltSetTransactionContext
author: windows-driver-content
description: The FltSetTransactionContext routine sets a context on a transaction.
old-location: ifsk\fltsettransactioncontext.htm
old-project: ifsk
ms.assetid: bb68ee38-1726-4493-9c3b-71a1352dd9f2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltSetTransactionContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available and supported in Windows Vista and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltSetTransactionContext
req.alt-loc: FltMgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: FltMgr.sys
req.irql: <= APC_LEVEL.
req.iface: 
---

# FltSetTransactionContext function



## -description
<p>The <b>FltSetTransactionContext</b> routine sets a context on a transaction. </p>


## -syntax

````
NTSTATUS FltSetTransactionContext(
  _In_      PFLT_INSTANCE             Instance,
  _In_      PKTRANSACTION             Transaction,
  _In_      FLT_SET_CONTEXT_OPERATION Operation,
  _In_      PFLT_CONTEXT              NewContext,
  _Out_opt_ PFLT_CONTEXT              *OldContext
);
````


## -parameters
<dl>

### -param Instance [in]

<dd>
<p>Opaque instance pointer for the caller. </p>
</dd>

### -param Transaction [in]

<dd>
<p>Opaque transaction pointer for the transaction on which the context is being set. </p>
</dd>

### -param Operation [in]

<dd>
<p>Flag that specifies the details of the operation to be performed. This parameter must be one of the following: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="FLT_SET_CONTEXT_REPLACE_IF_EXISTS"></a><a id="flt_set_context_replace_if_exists"></a><dl>

### -param FLT_SET_CONTEXT_REPLACE_IF_EXISTS

</dl>
</td>
<td width="60%">
<p>If a context is already set for the transaction pointed to by the <i>Transaction</i> parameter, replace the existing context with the context pointed to by the <i>NewContext</i> parameter. Otherwise, set the context pointed to by the <i>NewContext</i> parameter as the context for the transaction pointed to by the <i>Transaction</i> parameter. </p>
</td>
</tr>
<tr>
<td width="40%"><a id="FLT_SET_CONTEXT_KEEP_IF_EXISTS"></a><a id="flt_set_context_keep_if_exists"></a><dl>

### -param FLT_SET_CONTEXT_KEEP_IF_EXISTS

</dl>
</td>
<td width="60%">
<p>If a context is already set for the transaction pointed to by the <i>Transaction</i> parameter, return STATUS_FLT_CONTEXT_ALREADY_DEFINED. Otherwise, set the context pointed to by the <i>NewContext</i> parameter as the context for transaction pointed to by the <i>Transaction</i> parameter. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param NewContext [in]

<dd>
<p>Pointer to the new context to be set for the instance. The context must have been allocated by a previous call to <a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param OldContext [out, optional]

<dd>
<p>Pointer to a caller-allocated variable that receives the address of the existing transaction context, if one is already set. This parameter is optional and can be <b>NULL</b>. (For more information about this parameter, see the following Remarks section.) </p>
</dd>
</dl>

## -returns
<p><b>FltSetTransactionContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_FLT_CONTEXT_ALREADY_DEFINED</b></dt>
</dl><p>If FLT_SET_CONTEXT_KEEP_IF_EXISTS was specified for the <i>Operation</i> parameter, this error code indicates that a context is already attached to the transaction. Only one context can be attached to a transaction for a given minifilter driver. </p><dl>
<dt><b>STATUS_FLT_CONTEXT_ALREADY_LINKED</b></dt>
</dl><p>The context pointed to by the <i>NewContext</i> parameter is already linked to an object.  In other words, this error code indicates that <i>NewContext</i> is already in use due to a successful prior call of an <b>FltSet</b><i>Xxx</i><b>Context</b> routine.</p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The instance specified in the Instance parameter is being torn down. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>STATUS_INVALID_PARAMETER</p>

<p>One of the following:</p>

<p>STATUS_INVALID_PARAMETER is an error code. </p>

<p> </p>

## -remarks
<p>A minifilter driver calls <b>FltSetTransactionContext</b> to attach a context to a transaction or to remove or replace an existing transaction context. A minifilter driver can attach only one context to a given transaction. </p>

<p>Before calling <b>FltSetTransactionContext</b> to set a new transaction context, the caller must call <a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a> to allocate the context object. </p>

<p>A successful call to <b>FltSetTransactionContext</b> increments the reference count on <i>NewContext</i>. If <b>FltSetTransactionContext</b> fails, the reference count remains unchanged. In either case, the filter calling <b>FltSetTransactionContext</b> must call <a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a> to decrement the <i>NewContext</i> object. If <b>FltSetTransactionContext</b> fails and if the <i>OldContext</i> parameter is not <b>NULL</b> and does not point to NULL_CONTEXT then <i>OldContext</i> is a referenced pointer to the context currently associated with the transaction. The filter calling <b>FltSetTransactionContext</b> must call <b>FltReleaseContext</b> for <i>OldContext</i> as well.</p>

<p>Note that the <i>OldContext</i> pointer returned by <b>FltSetTransactionContext</b> must also be released by calling <a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a> when it is no longer needed. For more information, see <a href="ifsk.setting_contexts">Setting Contexts</a> and <a href="ifsk.releasing_contexts">Releasing Contexts</a>. </p>

<p>To retrieve a transaction context, call <a href="..\fltkernel\nf-fltkernel-fltgettransactioncontext.md">FltGetTransactionContext</a>. </p>

<p>To allocate a new transaction context, call <a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>. </p>

<p>To delete a transaction context, call <a href="..\fltkernel\nf-fltkernel-fltdeletetransactioncontext.md">FltDeleteTransactionContext</a> or <a href="..\fltkernel\nf-fltkernel-fltdeletecontext.md">FltDeleteContext</a>. </p>

<p>For more information about context reference counting, see <a href="ifsk.referencing_contexts">Referencing Contexts</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available and supported in Windows Vista and later operating systems.</p>
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
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltcommitcomplete.md">FltCommitComplete</a>
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
<a href="..\fltkernel\nf-fltkernel-fltreleasecontext.md">FltReleaseContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltrollbackcomplete.md">FltRollbackComplete</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltrollbackenlistment.md">FltRollbackEnlistment</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSetTransactionContext routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
