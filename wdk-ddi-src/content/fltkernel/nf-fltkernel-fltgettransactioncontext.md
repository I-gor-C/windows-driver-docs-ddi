---
UID: NF.fltkernel.FltGetTransactionContext
title: FltGetTransactionContext function
author: windows-driver-content
description: The FltGetTransactionContext routine retrieves a context that was set for a transaction by a given minifilter driver.
old-location: ifsk\fltgettransactioncontext.htm
old-project: ifsk
ms.assetid: fcd41baf-43ff-4f3a-8211-9fb5cb1cd2fd
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltGetTransactionContext
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
req.alt-api: FltGetTransactionContext
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
req.irql: <= APC_LEVEL
---

# FltGetTransactionContext function



## -description
The <b>FltGetTransactionContext</b> routine retrieves a context that was set for a transaction by a given minifilter driver. 



## -syntax

````
NTSTATUS FltGetTransactionContext(
  _In_  PFLT_INSTANCE Instance,
  _In_  PKTRANSACTION Transaction,
  _Out_ PFLT_CONTEXT  *Context
);
````


## -parameters

### -param Instance [in]

Opaque instance pointer for the caller. 


### -param Transaction [in]

Opaque transaction pointer for the transaction whose context is being retrieved. 


### -param Context [out]

Pointer to a caller-allocated variable that receives the address of the transaction context. 


## -returns
<b>FltGetTransactionContext</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as the following: 
<dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl>No matching context was found. This is an error code. 

 


## -remarks
<b>FltGetTransactionContext</b> is available on Windows Vista and later. 

<b>FltGetTransactionContext</b> increments the reference count on the context that the <i>Context </i>parameter points to. When this context pointer is no longer needed, the caller must decrement its reference count by calling <a href="ifsk.fltreleasecontext">FltReleaseContext</a>. Thus every successful call to <b>FltGetTransactionContext</b> must be matched by a subsequent call to <b>FltReleaseContext</b>. 

To set a context for a transaction, call <a href="ifsk.fltsettransactioncontext">FltSetTransactionContext</a>. 

To allocate a new transaction context, call <a href="ifsk.fltallocatecontext">FltAllocateContext</a>. 

To delete a transaction context, call <a href="ifsk.fltdeletetransactioncontext">FltDeleteTransactionContext</a> or <a href="ifsk.fltdeletecontext">FltDeleteContext</a>. 


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
DLL

</th>
<td width="70%">
<dl>
<dt>FltMgr.sys</dt>
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
<a href="ifsk.fltdeletetransactioncontext">FltDeleteTransactionContext</a>
</dt>
<dt>
<a href="ifsk.fltenlistintransaction">FltEnlistInTransaction</a>
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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetTransactionContext routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

