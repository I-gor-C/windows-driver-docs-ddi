---
UID: NC.sercx.EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION
title: EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION
author: windows-driver-content
description: The EvtSerCx2PioReceiveCancelReadyNotification event callback function is called by version 2 of the serial framework extension (SerCx2) to cancel a ready notification that SerCx2 enabled in a previous call to the EvtSerCx2PioReceiveEnableReadyNotification event callback function.
old-location: serports\evtsercx2pioreceivecancelreadynotification.htm
old-project: serports
ms.assetid: 6173896B-FF8C-42A0-A42A-963F6311C059
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SENSOR_VALUE_PAIR, SENSOR_VALUE_PAIR, *PSENSOR_VALUE_PAIR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: sercx.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EvtSerCx2PioReceiveCancelReadyNotification
req.alt-loc: 2.0\Sercx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Called at IRQL <= DISPATCH_LEVEL.
req.iface: 
req.product: Windows 10 or later.
---

# EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION callback



## -description
<p>The <i>EvtSerCx2PioReceiveCancelReadyNotification</i> event callback function is called by version 2 of the serial framework extension (SerCx2) to cancel a ready notification that SerCx2 enabled in a previous call to the <a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-enable-ready-notification.md">EvtSerCx2PioReceiveEnableReadyNotification</a> event callback function.</p>


## -prototype

````
EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION EvtSerCx2PioReceiveCancelReadyNotification;

BOOLEAN EvtSerCx2PioReceiveCancelReadyNotification(
  _In_ SERCX2PIORECEIVE PioReceive
)
{ ... }
````


## -parameters
<dl>

### -param <i>PioReceive</i> [in]

<dd>
<p>A <a href="serports.sercx2pioreceive_object_handle">SERCX2PIORECEIVE</a> handle to a PIO-receive object. The serial controller driver previously called the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265264">SerCx2PioReceiveCreate</a> method to create this object.</p>
</dd>
</dl>

## -returns
<p>The <i>EvtSerCx2PioReceiveCancelReadyNotification</i> function returns <b>TRUE</b> if the ready notification was successfully disabled and the serial controller driver can guarantee that this notification will not cause the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265266">SerCx2PioReceiveReady</a> method to be called. The function returns <b>FALSE</b> if the driver has already called <b>SerCx2PioReceiveReady</b>, or is about to call this method.</p>

## -remarks
<p>Your serial controller driver must implement this function. The driver registers the function in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265264">SerCx2PioReceiveCreate</a> call that creates the PIO-receive object.</p>

<p>If the associated read request times out or is canceled while a ready notification is enabled, SerCx2 calls the <i>EvtSerCx2PioReceiveCancelReadyNotification</i> function to cancel the pending notification. If this call returns <b>FALSE</b>, SerCx2 expects the serial controller driver to call <a href="https://msdn.microsoft.com/library/windows/hardware/dn265266">SerCx2PioReceiveReady</a>; only after this call does SerCx2 call the <a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-cleanup-transaction.md">EvtSerCx2PioReceiveCleanupTransaction</a> event callback function, if it is implemented, and complete the request.</p>

<p>To cancel the ready notification, the <i>EvtSerCx2PioReceiveCancelReadyNotification</i> function typically disables the interrupt in the serial controller that indicates that more data is available to be read from the receive FIFO. This interrupt was enabled by a previous call to the <a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-enable-ready-notification.md">EvtSerCx2PioReceiveEnableReadyNotification</a> function.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265332">SerCx2 PIO-Receive Transactions</a>.</p>

<p>To define an <i>EvtSerCx2PioReceiveCancelReadyNotification</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2PioReceiveCancelReadyNotification</i> callback function that is named <code>MyPioReceiveCancelReadyNotification</code>, use the <b>EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

<p>Your serial controller driver must implement this function. The driver registers the function in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265264">SerCx2PioReceiveCreate</a> call that creates the PIO-receive object.</p>

<p>If the associated read request times out or is canceled while a ready notification is enabled, SerCx2 calls the <i>EvtSerCx2PioReceiveCancelReadyNotification</i> function to cancel the pending notification. If this call returns <b>FALSE</b>, SerCx2 expects the serial controller driver to call <a href="https://msdn.microsoft.com/library/windows/hardware/dn265266">SerCx2PioReceiveReady</a>; only after this call does SerCx2 call the <a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-cleanup-transaction.md">EvtSerCx2PioReceiveCleanupTransaction</a> event callback function, if it is implemented, and complete the request.</p>

<p>To cancel the ready notification, the <i>EvtSerCx2PioReceiveCancelReadyNotification</i> function typically disables the interrupt in the serial controller that indicates that more data is available to be read from the receive FIFO. This interrupt was enabled by a previous call to the <a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-enable-ready-notification.md">EvtSerCx2PioReceiveEnableReadyNotification</a> function.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265332">SerCx2 PIO-Receive Transactions</a>.</p>

<p>To define an <i>EvtSerCx2PioReceiveCancelReadyNotification</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2PioReceiveCancelReadyNotification</i> callback function that is named <code>MyPioReceiveCancelReadyNotification</code>, use the <b>EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>2.0\Sercx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Called at IRQL &lt;= DISPATCH_LEVEL.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-enable-ready-notification.md">EvtSerCx2PioReceiveEnableReadyNotification</a>
</dt>
<dt>
<a href="serports.sercx2pioreceive_object_handle">SERCX2PIORECEIVE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265264">SerCx2PioReceiveCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265266">SerCx2PioReceiveReady</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20EVT_SERCX2_PIO_RECEIVE_CANCEL_READY_NOTIFICATION callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
