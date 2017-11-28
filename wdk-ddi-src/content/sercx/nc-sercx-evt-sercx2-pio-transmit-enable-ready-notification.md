---
UID: NC.sercx.EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION
title: EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION
author: windows-driver-content
description: The EvtSerCx2PioTransmitEnableReadyNotification event callback function is called by version 2 of the serial framework extension (SerCx2) to enable the serial controller driver to notify SerCx2 when the transmit FIFO in the serial controller is ready to accept more data.
old-location: serports\evtsercx2piotransmitenablereadynotification.htm
old-project: serports
ms.assetid: 05E5F48B-4E82-4BC3-B6D1-7E9E3435BDB3
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
req.alt-api: EvtSerCx2PioTransmitEnableReadyNotification
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

# EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION callback



## -description
<p>The <i>EvtSerCx2PioTransmitEnableReadyNotification</i> event callback function is called by version 2 of the serial framework extension (SerCx2) to enable the serial controller driver to notify SerCx2 when the transmit FIFO in the serial controller is ready to accept more data.</p>


## -prototype

````
EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION EvtSerCx2PioTransmitEnableReadyNotification;

VOID EvtSerCx2PioTransmitEnableReadyNotification(
  _In_ SERCX2PIOTRANSMIT PioTransmit
)
{ ... }
````


## -parameters
<dl>

### -param <i>PioTransmit</i> [in]

<dd>
<p>A <a href="serports.sercx2piotransmit_object_handle">SERCX2PIOTRANSMIT</a> handle to a PIO-transmit object. The serial controller driver previously called the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265269">SerCx2PioTransmitCreate</a> method to create this object.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Your serial controller driver must implement this function. The driver registers the function in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265269">SerCx2PioTransmitCreate</a> call that creates the PIO-transmit object.</p>

<p>If the ready notification for PIO-transmit transactions is enabled, the serial controller driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265273">SerCx2PioTransmitReady</a> method to notify SerCx2 when the driver detects that the transmit FIFO in the serial controller hardware is ready to accept more data. If the transmit FIFO is ready to accept data when the ready notification is enabled, the driver immediately calls this method to notify SerCx2.</p>

<p>The ready notification for a PIO-transmit transaction is a one-shot notification. After sending a ready notification to SerCx2, the serial controller driver sends no further notifications until SerCx2 calls the <i>EvtSerCx2PioTransmitEnableReadyNotification</i> function to enable another notification.</p>

<p>An <a href="..\sercx\nc-sercx-evt-sercx2-pio-transmit-write-buffer.md">EvtSerCx2PioTransmitWriteBuffer</a> function call might only partially complete a PIO-transmit transaction because no more room is immediately available in the transmit FIFO to write more data. In this case, SerCx2 calls the <i>EvtSerCx2PioTransmitEnableReadyNotification</i> function to enable a ready notification, in which case the serial controller driver must notify SerCx2 when the transmit FIFO has room for more data. In response to this notification, SerCx2 resumes the partially completed transmit transaction by calling the <i>EvtSerCx2PioTransmitWriteBuffer</i> function again.</p>

<p>Typically, an <i>EvtSerCx2PioTransmitEnableReadyNotification</i> function enables an interrupt that occurs when the transmit FIFO in the serial controller is ready to accept more data. In response to this interrupt, the serial controller driver calls <b>SerCx2PioTransmitReady</b>.</p>

<p>No more than one ready notification can be pending at a time. SerCx2 never calls the <i>EvtSerCx2PioTransmitEnableReadyNotification</i> function if the ready notification is already enabled.</p>

<p>SerCx2 never calls the <i>EvtSerCx2PioTransmitWriteBuffer</i> function when the ready notification is enabled.</p>

<p>A pending ready notification can be canceled if the associated write request times out or is canceled. To cancel a ready notification for a PIO-transmit transaction, SerCx2 calls the <a href="..\sercx\nc-sercx-evt-sercx2-pio-transmit-cancel-ready-notification.md">EvtSerCx2PioTransmitCancelReadyNotification</a> event callback function.</p>

<p>For more information, see <a href="NULL">SerCx2 PIO-Transmit Transactions</a>.</p>

<p>To define an <i>EvtSerCx2PioTransmitEnableReadyNotification</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2PioTransmitEnableReadyNotification</i> callback function that is named <code>MyPioTransmitEnableReadyNotification</code>, use the <b>EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

<p>Your serial controller driver must implement this function. The driver registers the function in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265269">SerCx2PioTransmitCreate</a> call that creates the PIO-transmit object.</p>

<p>If the ready notification for PIO-transmit transactions is enabled, the serial controller driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265273">SerCx2PioTransmitReady</a> method to notify SerCx2 when the driver detects that the transmit FIFO in the serial controller hardware is ready to accept more data. If the transmit FIFO is ready to accept data when the ready notification is enabled, the driver immediately calls this method to notify SerCx2.</p>

<p>The ready notification for a PIO-transmit transaction is a one-shot notification. After sending a ready notification to SerCx2, the serial controller driver sends no further notifications until SerCx2 calls the <i>EvtSerCx2PioTransmitEnableReadyNotification</i> function to enable another notification.</p>

<p>An <a href="..\sercx\nc-sercx-evt-sercx2-pio-transmit-write-buffer.md">EvtSerCx2PioTransmitWriteBuffer</a> function call might only partially complete a PIO-transmit transaction because no more room is immediately available in the transmit FIFO to write more data. In this case, SerCx2 calls the <i>EvtSerCx2PioTransmitEnableReadyNotification</i> function to enable a ready notification, in which case the serial controller driver must notify SerCx2 when the transmit FIFO has room for more data. In response to this notification, SerCx2 resumes the partially completed transmit transaction by calling the <i>EvtSerCx2PioTransmitWriteBuffer</i> function again.</p>

<p>Typically, an <i>EvtSerCx2PioTransmitEnableReadyNotification</i> function enables an interrupt that occurs when the transmit FIFO in the serial controller is ready to accept more data. In response to this interrupt, the serial controller driver calls <b>SerCx2PioTransmitReady</b>.</p>

<p>No more than one ready notification can be pending at a time. SerCx2 never calls the <i>EvtSerCx2PioTransmitEnableReadyNotification</i> function if the ready notification is already enabled.</p>

<p>SerCx2 never calls the <i>EvtSerCx2PioTransmitWriteBuffer</i> function when the ready notification is enabled.</p>

<p>A pending ready notification can be canceled if the associated write request times out or is canceled. To cancel a ready notification for a PIO-transmit transaction, SerCx2 calls the <a href="..\sercx\nc-sercx-evt-sercx2-pio-transmit-cancel-ready-notification.md">EvtSerCx2PioTransmitCancelReadyNotification</a> event callback function.</p>

<p>For more information, see <a href="NULL">SerCx2 PIO-Transmit Transactions</a>.</p>

<p>To define an <i>EvtSerCx2PioTransmitEnableReadyNotification</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2PioTransmitEnableReadyNotification</i> callback function that is named <code>MyPioTransmitEnableReadyNotification</code>, use the <b>EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<a href="..\sercx\nc-sercx-evt-sercx2-pio-transmit-write-buffer.md">EvtSerCx2PioTransmitWriteBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>
</dt>
<dt>
<a href="serports.sercx2piotransmit_object_handle">SERCX2PIOTRANSMIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265269">SerCx2PioTransmitCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265273">SerCx2PioTransmitReady</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20EVT_SERCX2_PIO_TRANSMIT_ENABLE_READY_NOTIFICATION callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
