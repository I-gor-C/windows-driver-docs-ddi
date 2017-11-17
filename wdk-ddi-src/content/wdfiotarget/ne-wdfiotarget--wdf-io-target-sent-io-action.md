---
UID: NE.wdfiotarget._WDF_IO_TARGET_SENT_IO_ACTION
title: WDF_IO_TARGET_SENT_IO_ACTION
author: windows-driver-content
description: The WDF_IO_TARGET_SENT_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls WdfIoTargetStop to stop an I/O target.
old-location: wdf\wdf_io_target_sent_io_action.htm
ms.assetid: 4295ef73-b9a8-4593-8114-d0b836275b13
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_IO_TARGET_SENT_IO_ACTION
req.alt-loc: wdfiotarget.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY, WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY, *PWDF_IO_QUEUE_FORWARD_PROGRESS_POLICY
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_TARGET_SENT_IO_ACTION enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_IO_TARGET_SENT_IO_ACTION</b> enumeration identifies the actions that the framework can take when a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> to stop an I/O target.</p>


## -syntax

````
typedef enum _WDF_IO_TARGET_SENT_IO_ACTION { 
  WdfIoTargetSentIoUndefined          = 0,
  WdfIoTargetCancelSentIo             = 1,
  WdfIoTargetWaitForSentIoToComplete  = 2,
  WdfIoTargetLeaveSentIoPending       = 3
} WDF_IO_TARGET_SENT_IO_ACTION;
````


## -enum-fields
<dl>

### -field <a id="WdfIoTargetSentIoUndefined"></a><a id="wdfiotargetsentioundefined"></a><a id="WDFIOTARGETSENTIOUNDEFINED"></a><b>WdfIoTargetSentIoUndefined</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="WdfIoTargetCancelSentIo"></a><a id="wdfiotargetcancelsentio"></a><a id="WDFIOTARGETCANCELSENTIO"></a><b>WdfIoTargetCancelSentIo</b>

<dd>
<p>Before the framework stops the I/O target, it will attempt to cancel I/O requests that are in the I/O target's queue. The framework cancels all of the target queue's I/O requests, and waits for all I/O requests to complete, before <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> returns. The framework also attempts to cancel I/O requests that have left the I/O target's queue and entered lower drivers.</p>
</dd>

### -field <a id="WdfIoTargetWaitForSentIoToComplete"></a><a id="wdfiotargetwaitforsentiotocomplete"></a><a id="WDFIOTARGETWAITFORSENTIOTOCOMPLETE"></a><b>WdfIoTargetWaitForSentIoToComplete</b>

<dd>
<p>Before the framework stops the I/O target, it will wait for I/O requests that are in the I/O target's queue to be completed. The framework completes all of the target queue's I/O requests, and calls each request's <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function, before <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> returns.</p>
</dd>

### -field <a id="WdfIoTargetLeaveSentIoPending"></a><a id="wdfiotargetleavesentiopending"></a><a id="WDFIOTARGETLEAVESENTIOPENDING"></a><b>WdfIoTargetLeaveSentIoPending</b>

<dd>
<p>The framework will leave I/O requests in the I/O target's queue. The requests remain in the target's queue until the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a> or the device is removed.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_IO_TARGET_SENT_IO_ACTION</b> enumeration is used as an input parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> method.</p>

<p>If your driver specifies the <b>WdfIoTargetWaitForSentIoToComplete</b> flag, the driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> from a request handler, a <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function, or an <a href="https://msdn.microsoft.com/a9e21f47-1a60-419a-839e-8869f9fd4dd7">EvtUsbTargetPipeReadersFailed</a> callback function.</p>

<p>For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561418">WDF_IO_TARGET_SENT_IO_ACTION (UMDF)</a>.</p>

<p>The <b>WDF_IO_TARGET_SENT_IO_ACTION</b> enumeration is used as an input parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> method.</p>

<p>If your driver specifies the <b>WdfIoTargetWaitForSentIoToComplete</b> flag, the driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> from a request handler, a <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function, or an <a href="https://msdn.microsoft.com/a9e21f47-1a60-419a-839e-8869f9fd4dd7">EvtUsbTargetPipeReadersFailed</a> callback function.</p>

<p>For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561418">WDF_IO_TARGET_SENT_IO_ACTION (UMDF)</a>.</p>

<p>The <b>WDF_IO_TARGET_SENT_IO_ACTION</b> enumeration is used as an input parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> method.</p>

<p>If your driver specifies the <b>WdfIoTargetWaitForSentIoToComplete</b> flag, the driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> from a request handler, a <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function, or an <a href="https://msdn.microsoft.com/a9e21f47-1a60-419a-839e-8869f9fd4dd7">EvtUsbTargetPipeReadersFailed</a> callback function.</p>

<p>For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561418">WDF_IO_TARGET_SENT_IO_ACTION (UMDF)</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfiotarget.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_TARGET_SENT_IO_ACTION enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
