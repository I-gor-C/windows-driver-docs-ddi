---
UID: NF.fltkernel.FltDeleteTransactionContext
title: FltDeleteTransactionContext function
author: windows-driver-content
description: The FltDeleteTransactionContext routine removes a context from a given transaction and marks the context for deletion.
old-location: ifsk\fltdeletetransactioncontext.htm
old-project: ifsk
ms.assetid: 120285ff-1cb4-4570-a1e7-0a7d22b43560
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltDeleteTransactionContext
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
req.alt-api: FltDeleteTransactionContext
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
---

# FltDeleteTransactionContext function



## -description
The <b>FltDeleteTransactionContext</b> routine removes a context from a given transaction and marks the context for deletion. 


## -syntax

````
NTSTATUS FltDeleteTransactionContext(
  _In_      PFLT_INSTANCE Instance,
  _In_      PKTRANSACTION Transaction,
  _Out_opt_ PFLT_CONTEXT  *OldContext
);
````


## -parameters

### -param Instance [in]

Opaque instance pointer for the caller. 

### -param Transaction [in]

Opaque transaction pointer for the transaction whose context is being deleted. 

### -param OldContext [out, optional]

Pointer to a caller-allocated variable that receives the address of the deleted context. This parameter is optional and can be <b>NULL</b>. If <i>OldContext</i> is not <b>NULL</b> and does not point to NULL_CONTEXT, the caller is responsible for calling <a href="ifsk.fltreleasecontext">FltReleaseContext</a> to release this context when it is no longer needed. 

## -returns
<b>FltDeleteTransactionContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: 
<dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl>No matching context was found. This is an error code. 

 

## -remarks
This routine is available on Windows Vista and later. 

Because contexts are reference-counted, it is not usually necessary for a minifilter driver to call a routine such as <b>FltDeleteTransactionContext</b> to explicitly delete a context. 

A minifilter driver calls <b>FltDeleteTransactionContext</b> to remove a context from a transaction and mark the context for deletion. The context is usually freed immediately unless there is an outstanding reference on it (for example, because the context is still being used by another thread). 

To allocate a new transaction context, call <a href="ifsk.fltallocatecontext">FltAllocateContext</a>. 

To retrieve a transaction context, call <a href="ifsk.fltgettransactioncontext">FltGetTransactionContext</a>. 

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
<a href="ifsk.fltallocatecontext">FltAllocateContext</a>
</dt>
<dt>
<a href="ifsk.fltcommitcomplete">FltCommitComplete</a>
</dt>
<dt>
<a href="ifsk.fltdeletecontext">FltDeleteContext</a>
</dt>
<dt>
<a href="ifsk.fltenlistintransaction">FltEnlistInTransaction</a>
</dt>
<dt>
<a href="ifsk.fltgettransactioncontext">FltGetTransactionContext</a>
</dt>
<dt>
<a href="ifsk.fltpreparecomplete">FltPrepareComplete</a>
</dt>
<dt>
<a href="ifsk.fltprepreparecomplete">FltPrePrepareComplete</a>
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
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltDeleteTransactionContext routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
