---
UID: NF.lowio.RxLowIoCompletion
title: RxLowIoCompletion
author: windows-driver-content
description: RxLowIoCompletion must be called by the network mini-redirector low I/O routines when they complete, if the low I/O routines have initially returned STATUS_PENDING.
old-location: ifsk\rxlowiocompletion.htm
old-project: ifsk
ms.assetid: d9018a68-e72c-4149-a6a5-095654d0363c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxLowIoCompletion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: lowio.h
req.include-header: Lowio.h, Rxcontx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxLowIoCompletion
req.alt-loc: lowio.h
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
---

# RxLowIoCompletion function



## -description
<p><b>RxLowIoCompletion</b> must be called by the network mini-redirector low I/O routines when they complete, if the low I/O routines have initially returned STATUS_PENDING.</p>


## -syntax

````
NTSTATUS RxLowIoCompletion(
   PRX_CONTEXT RxContext
);
````


## -parameters
<dl>

### -param RxContext 

<dd>
<p>A pointer to the RX_CONTEXT structure for this IRP.</p>
</dd>
</dl>

## -returns
<p><b>RxLowIoCompletion</b>
      returns different values depending on whether the <i>RxContext</i> parameter indicates this is synchronous or asynchornous I/O.</p>

<p>If the <i>RxContext</i> parameter indicates this is synchronous I/O, then <b>RxLowIoCompletion</b> returns STATUS_MORE_PROCESSING_REQUIRED. </p>

<p>If the <i>RxContext</i> parameter indicates this is asynchronous I/O, then <b>RxLowIoCompletion</b> will try to call the <b>LowIoContext.CompletionRoutine</b> member of the RX_CONTEXT. The completion routine will only be called if the <b>LowIoContext.Flags</b>member indicates that the completion routine can be called at DPC level and the current IRQL is less than dispatch level. In this case, the return value is the result returned by the completion routine. If these conditions are not met, then <b>RxLowIoCompletion</b> returns STATUS_MORE_PROCESSING_REQUIRED. </p>

## -remarks


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
<dt>Lowio.h (include Lowio.h or Rxcontx.h)</dt>
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
<a href="..\lowio\nf-lowio-rxlowiogetbufferaddress.md">RxLowIoGetBufferAddress</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-rxmapsystembuffer.md">RxMapSystemBuffer</a>
</dt>
<dt>
<a href="ifsk.rxnewmapuserbuffer">RxNewMapUserBuffer</a>
</dt>
<dt>
<a href="..\rxcontx\ns-rxcontx--rx-context.md">RX_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxLowIoCompletion routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
