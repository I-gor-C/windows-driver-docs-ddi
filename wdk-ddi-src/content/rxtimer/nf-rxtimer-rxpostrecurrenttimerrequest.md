---
UID: NF.rxtimer.RxPostRecurrentTimerRequest
title: RxPostRecurrentTimerRequest
author: windows-driver-content
description: RxPostRecurrentTimerRequest initializes a recurrent timer request. The passed in pointer to a worker thread routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine.
old-location: ifsk\rxpostrecurrenttimerrequest.htm
old-project: ifsk
ms.assetid: a44fb478-4f78-415e-b557-bf383199578c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxPostRecurrentTimerRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxtimer.h
req.include-header: Rxtimer.h, Rxworkq.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxPostRecurrentTimerRequest
req.alt-loc: rxtimer.h
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

# RxPostRecurrentTimerRequest function



## -description
<p><b>RxPostRecurrentTimerRequest</b> initializes a recurrent timer request. The passed in pointer to a worker thread routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine. </p>


## -syntax

````
NTSTATUS RxPostRecurrentTimerRequest(
  _In_ PRDBSS_DEVICE_OBJECT     pDeviceObject,
  _In_ PRX_WORKERTHREAD_ROUTINE Routine,
  _In_ PVOID                    pContext,
  _In_ LARGE_INTEGER            TimeInterval
);
````


## -parameters
<dl>

### -param pDeviceObject [in]

<dd>
<p>A pointer to the device object to be associated with this timer. </p>
</dd>

### -param Routine [in]

<dd>
<p>A pointer to the worker thread routine to call when this timer expires. </p>
</dd>

### -param pContext [in]

<dd>
<p>A pointer to the context parameter to be associated with this timer.</p>
</dd>

### -param TimeInterval [in]

<dd>
<p>The time interval, in 100-nanosecond ticks.</p>
</dd>
</dl>

## -returns
<p><b>RxPostRecurrentTimerRequest</b> returns STATUS_SUCCESS on success or one of the following error codes: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The allocation of non-paged pool memory required by this routine failed. </p>

<p> </p>

## -remarks
<p>A recurrent timer can be canceled by calling <b>RxCancelTimerRequest</b>.</p>

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
<dt>Rxtimer.h (include Rxtimer.h or Rxworkq.h)</dt>
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
<a href="..\rxtimer\nf-rxtimer-rxcanceltimerrequest.md">RxCancelTimerRequest</a>
</dt>
<dt>
<a href="..\rxtimer\nf-rxtimer-rxpostoneshottimerrequest.md">RxPostOneShotTimerRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxPostRecurrentTimerRequest routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
