---
UID: NF.rxtimer.RxPostOneShotTimerRequest
title: RxPostOneShotTimerRequest
author: windows-driver-content
description: RxPostOneShotTimerRequest initializes a one-shot timer entry. The passed-in pointer to a worker thread routine is called once when the timer expires.
old-location: ifsk\rxpostoneshottimerrequest.htm
ms.assetid: d3ae6401-6d1b-428f-ae74-e262682bcb10
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: rxtimer.h
req.include-header: Rxtimer.h, Rxworkq.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxPostOneShotTimerRequest
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
ms.keywords: RxPostOneShotTimerRequest
req.iface: 
req.product: Windows 10 or later.
---

# RxPostOneShotTimerRequest function



## -description
<p><b>RxPostOneShotTimerRequest</b> initializes a one-shot timer entry. The passed-in pointer to a worker thread routine is called once when the timer expires. </p>


## -syntax

````
NTSTATUS RxPostOneShotTimerRequest(
  _In_ PRDBSS_DEVICE_OBJECT     pDeviceObject,
  _In_ PRX_WORK_ITEM            pWorkItem,
  _In_ PRX_WORKERTHREAD_ROUTINE Routine,
  _In_ PVOID                    pContext,
  _In_ LARGE_INTEGER            TimeInterval
);
````


## -parameters
<dl>

### -param <i>pDeviceObject</i> [in]

<dd>
<p>A pointer to the device object to be associated with this timer. </p>
</dd>

### -param <i>pWorkItem</i> [in]

<dd>
<p>A pointer to the worker item.</p>
</dd>

### -param <i>Routine</i> [in]

<dd>
<p>A pointer to the worker thread routine to call when this timer expires. </p>
</dd>

### -param <i>pContext</i> [in]

<dd>
<p>A pointer to the context parameter associated with this timer.</p>
</dd>

### -param <i>TimeInterval</i> [in]

<dd>
<p>The time interval, in 100-nanosecond ticks.</p>
</dd>
</dl>

## -returns
<p><b>RxPostOneShotTimerRequest</b>
      returns STATUS_SUCCESS on success. </p>

<p>If a <b>NULL</b> pointer is passed as the <i>pWorkItem</i> parameter, this routine causes the system to ASSERT on checked builds.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553395">RxCancelTimerRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554615">RxPostRecurrentTimerRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxPostOneShotTimerRequest routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
