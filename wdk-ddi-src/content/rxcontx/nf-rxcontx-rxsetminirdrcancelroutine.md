---
UID: NF.rxcontx.RxSetMinirdrCancelRoutine
title: RxSetMinirdrCancelRoutine function
author: windows-driver-content
description: RxSetMinirdrCancelRoutine is called by a network mini-redirector driver to set up a network mini-redirector cancel routine for an RX_CONTEXT structure.
old-location: ifsk\rxsetminirdrcancelroutine.htm
old-project: ifsk
ms.assetid: 5b74b4c4-d1a3-4587-900a-b54eebfeb553
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxSetMinirdrCancelRoutine
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxcontx.h
req.include-header: Mrx.h, Rxcontx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxSetMinirdrCancelRoutine
req.alt-loc: rxcontx.h
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
req.product: Windows 10 or later.
---

# RxSetMinirdrCancelRoutine function



## -description
<b>RxSetMinirdrCancelRoutine</b> is called by a network mini-redirector driver to set up a network mini-redirector cancel routine for an RX_CONTEXT structure.



## -syntax

````
NTSTATUS RxSetMinirdrCancelRoutine(
  _Inout_ PRX_CONTEXT   RxContext,
  _In_    PMRX_CALLDOWN MRxCancelRoutine
);
````


## -parameters

### -param RxContext [in, out]

A pointer to the RX_CONTEXT structure. 


### -param MRxCancelRoutine [in]

A pointer to a cancel routine. 


## -returns
<b>RxSetMinirdrCancelRoutine</b> returns STATUS_SUCCESS on success or one of the following error values on failure: 
<dl>
<dt><b>STATUS_CANCELLED</b></dt>
</dl>The <i>RxContext</i> parameter was already canceled. The error will be returned if the <b>Flags</b> member of <i>RxContext</i> has the RX_CONTEXT_FLAG_CANCELLED bit set. 

 


## -remarks
The <b>RxSetMinirdrCancelRoutine</b> routine sets the <b>MRxCancelRoutine</b> member of the <i>RxContext</i> parameter to the value of the <i>MRxCancelRoutine</i> parameter. This operation is protected by a spinlock.


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
<dt>Rxcontx.h (include Mrx.h or Rxcontx.h)</dt>
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
<a href="ifsk.rxcompleterequest">RxCompleteRequest</a>
</dt>
<dt>
<a href="ifsk.rxcompleterequest_real">RxCompleteRequest_Real</a>
</dt>
<dt>
<a href="ifsk.rxcreaterxcontext">RxCreateRxContext</a>
</dt>
<dt>
<a href="ifsk.rxdereference">RxDereference</a>
</dt>
<dt>
<a href="ifsk.rxdereferenceanddeleterxcontext_real">RxDereferenceAndDeleteRxContext_Real</a>
</dt>
<dt>
<a href="ifsk.rxinitializecontext">RxInitializeContext</a>
</dt>
<dt>
<a href="ifsk.rxpreparecontextforreuse">RxPrepareContextForReuse</a>
</dt>
<dt>
<a href="ifsk.rxresumeblockedoperations_serially">RxResumeBlockedOperations_Serially</a>
</dt>
<dt>
<a href="ifsk.rx_context">RX_CONTEXT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxSetMinirdrCancelRoutine routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

