---
UID: NF.rxprocs.RxCompleteRequest
title: RxCompleteRequest
author: windows-driver-content
description: RxCompleteRequest completes the IRP request associated with an RX_CONTEXT structure.
old-location: ifsk\rxcompleterequest.htm
old-project: ifsk
ms.assetid: f5e9219b-0697-427e-b92e-7cd647a0e0b6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxCompleteRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxprocs.h
req.include-header: Rxprocs.h, Rxcontx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCompleteRequest
req.alt-loc: rxprocs.h
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
req.product: Windows 10 or later.
---

# RxCompleteRequest function



## -description
<p><b>RxCompleteRequest</b> completes the IRP request associated with an RX_CONTEXT structure.</p>


## -syntax

````
NTSTATUS RxCompleteRequest(
   PRX_CONTEXT RxContext,
   NTSTATUS    Status
);
````


## -parameters
<dl>

### -param <i>RxContext</i> 

<dd>
<p>A pointer to the RX_CONTEXT. This parameter contains the IRP requesting the operation to complete. </p>
</dd>

### -param <i>Status</i> 

<dd>
<p>The status value to return when the IRP request is complete. This is the value that will be stored in the <b>IoStatus.Status</b> member of the associated IRP on completion.</p>
</dd>
</dl>

## -returns
<p><b>RxCompleteRequest</b> returns the value of the <i>Status</i> parameter.</p>

## -remarks
<p>The <b>RxCompleteRequest</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally to complete an I/O request packet. </p>

<p><b>RxCompleteRequest</b> internally calls <b>RxCompleteRequest_Real</b> to complete the request. Before calling <b>RxCompleteRequest_Real</b>, the <b>RxCompleteRequest</b> routine checks the value of the <b>LoudCompletionString</b> member in the RX_CONTEXT structure pointed to by the <i>RxContext</i> parameter and prints extra debugging information if <i>Status</i> is not equal to STATUS_SUCCESS. </p>

<p>The <b>RxCompleteRequest</b> routine is not normally called by network mini-redirector drivers directly. RDBSS calls this routine internally to complete an I/O request packet. </p>

<p><b>RxCompleteRequest</b> internally calls <b>RxCompleteRequest_Real</b> to complete the request. Before calling <b>RxCompleteRequest_Real</b>, the <b>RxCompleteRequest</b> routine checks the value of the <b>LoudCompletionString</b> member in the RX_CONTEXT structure pointed to by the <i>RxContext</i> parameter and prints extra debugging information if <i>Status</i> is not equal to STATUS_SUCCESS. </p>

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
<dt>Rxprocs.h (include Rxprocs.h or Rxcontx.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554348">RxCompleteRequest_Real</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554367">RxCreateRxContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554388">RxDereference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554393">RxDereferenceAndDeleteRxContext_Real</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554502">RxInitializeContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554643">RxPrepareContextForReuse</a>
</dt>
<dt>
<a href="..\rxcontx\nf-rxcontx-rxresumeblockedoperations-serially.md">RxResumeBlockedOperations_Serially</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557377">__RxSynchronizeBlockingOperations</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557382">__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCompleteRequest function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
