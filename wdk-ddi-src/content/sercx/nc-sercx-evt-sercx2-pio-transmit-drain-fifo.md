---
UID: NC.sercx.EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO
title: EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO
author: windows-driver-content
description: The EvtSerCx2PioTransmitDrainFifo event callback function is called by version 2 of the serial framework extension (SerCx2) to drain the transmit FIFO in the serial controller hardware.
old-location: serports\evtsercx2piotransmitdrainfifo.htm
ms.assetid: A21E14DA-0B76-4DA2-B628-C3A4DE843FA9
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: serports
req.header: sercx.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EvtSerCx2PioTransmitDrainFifo
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
ms.keywords: SENSOR_VALUE_PAIR, SENSOR_VALUE_PAIR, *PSENSOR_VALUE_PAIR
req.iface: 
req.product: Windows 10 or later.
---

# EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO callback



## -description
<p>The <i>EvtSerCx2PioTransmitDrainFifo</i> event callback function is called by version 2 of the serial framework extension (SerCx2) to drain the transmit FIFO in the serial controller hardware.</p>


## -prototype

````
EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO EvtSerCx2PioTransmitDrainFifo;

VOID EvtSerCx2PioTransmitDrainFifo(
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
<p>Your serial controller driver can, as an option, implement this function. If your driver implements this function, it must also implement the <a href="https://msdn.microsoft.com/DAAE9C91-F83F-4D14-8851-7B5DEEA340B3">EvtSerCx2PioTransmitCancelDrainFifo</a> and <a href="https://msdn.microsoft.com/2BB02F84-01C1-432D-A4A9-6035F3ED32D7">EvtSerCx2PioTransmitPurgeFifo</a> event callback functions. A driver that implements these functions registers them in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265269">SerCx2PioTransmitCreate</a> call that creates the PIO-transmit object.</p>

<p>SerCx2 calls the <i>EvtSerCx2PioTransmitDrainFifo</i> function, if it is implemented, to drain the transmit FIFO in the serial controller hardware at the end of a PIO-transmit transaction. This function makes sure that any data bytes that remain in the transmit FIFO are transmitted to the serially connected peripheral device. After the last byte is transmitted from the FIFO, the <i>EvtSerCx2PioTransmitDrainFifo</i> function calls the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265270">SerCx2PioTransmitDrainFifoComplete</a> method to notify SerCx2.</p>

<p>If the serial controller driver implements an <i>EvtSerCx2PioTransmitDrainFifo</i> function, SerCx2 does not complete a pending write (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>) request until the driver calls <b>SerCx2PioTransmitDrainFifoComplete</b>.</p>

<p>If your serial controller has a hardware FIFO (or similar buffering mechanism) to hold transmit data, your driver should implement an <i>EvtSerCx2PioTransmitDrainFifo</i> function. Otherwise, SerCx2 cannot confirm that the transmit FIFO has drained before the pending write request is completed. Instead, SerCx2 completes this request after the last byte in the write buffer is written to the transmit FIFO. There can be no guarantee that data written to the transmit FIFO will be transmitted without a significant delay. Any data that remains in the FIFO after the write request is completed might be lost before it can be transmitted to the serially connected peripheral device. This unexpected data loss in a successfully completed write request can create reliability problems for the peripheral driver.</p>

<p>For example, a peripheral driver might send write requests to a serial port to which a peripheral device is connected. Until all outstanding write requests are completed, this driver should delay sending an IOCTL to change the baud rate at which the serial port transmits data. However, if no <i>EvtSerCx2PioTransmitDrainFifo</i> function is implemented, a write request to transmit 100 bytes of data might be completed while 50 data bytes still remain in the transmit FIFO. If the peripheral driver then sends an IOCTL to set a new baud rate, some of the remaining bytes in the FIFO might be transmitted at the new baud rate, causing an error.</p>

<p>Similarly, if a write request to transmit 100 bytes of data is completed while 50 data bytes still remain in the transmit FIFO, and the serial controller exits D0 to enter a low-power device state before the remaining bytes in the FIFO can be transmitted, the peripheral driver will not know that these bytes are lost.</p>

<p>For more information, see <a href="NULL">SerCx2 PIO-Transmit Transactions</a>.</p>

<p>To define an <i>EvtSerCx2PioTransmitDrainFifo</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2PioTransmitDrainFifo</i> callback function that is named <code>MyPioTransmitDrainFifo</code>, use the <b>EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

<p>Your serial controller driver can, as an option, implement this function. If your driver implements this function, it must also implement the <a href="https://msdn.microsoft.com/DAAE9C91-F83F-4D14-8851-7B5DEEA340B3">EvtSerCx2PioTransmitCancelDrainFifo</a> and <a href="https://msdn.microsoft.com/2BB02F84-01C1-432D-A4A9-6035F3ED32D7">EvtSerCx2PioTransmitPurgeFifo</a> event callback functions. A driver that implements these functions registers them in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265269">SerCx2PioTransmitCreate</a> call that creates the PIO-transmit object.</p>

<p>SerCx2 calls the <i>EvtSerCx2PioTransmitDrainFifo</i> function, if it is implemented, to drain the transmit FIFO in the serial controller hardware at the end of a PIO-transmit transaction. This function makes sure that any data bytes that remain in the transmit FIFO are transmitted to the serially connected peripheral device. After the last byte is transmitted from the FIFO, the <i>EvtSerCx2PioTransmitDrainFifo</i> function calls the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265270">SerCx2PioTransmitDrainFifoComplete</a> method to notify SerCx2.</p>

<p>If the serial controller driver implements an <i>EvtSerCx2PioTransmitDrainFifo</i> function, SerCx2 does not complete a pending write (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>) request until the driver calls <b>SerCx2PioTransmitDrainFifoComplete</b>.</p>

<p>If your serial controller has a hardware FIFO (or similar buffering mechanism) to hold transmit data, your driver should implement an <i>EvtSerCx2PioTransmitDrainFifo</i> function. Otherwise, SerCx2 cannot confirm that the transmit FIFO has drained before the pending write request is completed. Instead, SerCx2 completes this request after the last byte in the write buffer is written to the transmit FIFO. There can be no guarantee that data written to the transmit FIFO will be transmitted without a significant delay. Any data that remains in the FIFO after the write request is completed might be lost before it can be transmitted to the serially connected peripheral device. This unexpected data loss in a successfully completed write request can create reliability problems for the peripheral driver.</p>

<p>For example, a peripheral driver might send write requests to a serial port to which a peripheral device is connected. Until all outstanding write requests are completed, this driver should delay sending an IOCTL to change the baud rate at which the serial port transmits data. However, if no <i>EvtSerCx2PioTransmitDrainFifo</i> function is implemented, a write request to transmit 100 bytes of data might be completed while 50 data bytes still remain in the transmit FIFO. If the peripheral driver then sends an IOCTL to set a new baud rate, some of the remaining bytes in the FIFO might be transmitted at the new baud rate, causing an error.</p>

<p>Similarly, if a write request to transmit 100 bytes of data is completed while 50 data bytes still remain in the transmit FIFO, and the serial controller exits D0 to enter a low-power device state before the remaining bytes in the FIFO can be transmitted, the peripheral driver will not know that these bytes are lost.</p>

<p>For more information, see <a href="NULL">SerCx2 PIO-Transmit Transactions</a>.</p>

<p>To define an <i>EvtSerCx2PioTransmitDrainFifo</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2PioTransmitDrainFifo</i> callback function that is named <code>MyPioTransmitDrainFifo</code>, use the <b>EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<a href="https://msdn.microsoft.com/DAAE9C91-F83F-4D14-8851-7B5DEEA340B3">EvtSerCx2PioTransmitCancelDrainFifo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2BB02F84-01C1-432D-A4A9-6035F3ED32D7">EvtSerCx2PioTransmitPurgeFifo</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265270">SerCx2PioTransmitDrainFifoComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20EVT_SERCX2_PIO_TRANSMIT_DRAIN_FIFO callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
