---
UID: NC.sercx.EVT_SERCX2_PIO_TRANSMIT_PURGE_FIFO
title: EVT_SERCX2_PIO_TRANSMIT_PURGE_FIFO
author: windows-driver-content
description: The EvtSerCx2PioTransmitPurgeFifo event callback function is called by version 2 of the serial framework extension (SerCx2) to discard any bytes of unsent data that remain in the transmit FIFO in the serial controller.
old-location: serports\evtsercx2piotransmitpurgefifo.htm
old-project: serports
ms.assetid: 2BB02F84-01C1-432D-A4A9-6035F3ED32D7
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
req.alt-api: EvtSerCx2PioTransmitPurgeFifo
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

# EVT_SERCX2_PIO_TRANSMIT_PURGE_FIFO callback



## -description
<p>The <i>EvtSerCx2PioTransmitPurgeFifo</i> event callback function is called by version 2 of the serial framework extension (SerCx2) to discard any bytes of unsent data that remain in the transmit FIFO in the serial controller.</p>


## -prototype

````
EVT_SERCX2_PIO_TRANSMIT_PURGE_FIFO EvtSerCx2PioTransmitPurgeFifo;

VOID EvtSerCx2PioTransmitPurgeFifo(
  _In_ SERCX2PIOTRANSMIT PioTransmit,
  _In_ ULONG             BytesAlreadyTransmittedToHardware
)
{ ... }
````


## -parameters
<dl>

### -param <i>PioTransmit</i> [in]

<dd>
<p>A <a href="serports.sercx2piotransmit_object_handle">SERCX2PIOTRANSMIT</a> handle to a PIO-transmit object. The serial controller driver previously called the <a href="..\sercx\nf-sercx-sercx2piotransmitcreate.md">SerCx2PioTransmitCreate</a> method to create this object.</p>
</dd>

### -param <i>BytesAlreadyTransmittedToHardware</i> [in]

<dd>
<p>The number of bytes that have already been loaded into the transmit FIFO during the current PIO-transmit transaction. This parameter is the sum of all the bytes transferred in previous calls to the <a href="..\sercx\nc-sercx-evt-sercx2-pio-transmit-write-buffer.md">EvtSerCx2PioTransmitWriteBuffer</a> event callback function that are part of this transaction.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Your serial controller driver can, as an option, implement this function. If implemented, the driver registers the function in the <a href="..\sercx\nf-sercx-sercx2piotransmitcreate.md">SerCx2PioTransmitCreate</a> call that creates the PIO-transmit object.</p>

<p>Your driver should implement an <i>EvtSerCx2PioTransmitPurgeFifo</i> function if the serial controller has a hardware FIFO (or similar buffering mechanism) to hold transmit data. If your driver implements this function, it must also implement the <a href="..\sercx\nc-sercx-evt-sercx2-pio-transmit-drain-fifo.md">EvtSerCx2PioTransmitDrainFifo</a> and <a href="..\sercx\nc-sercx-evt-sercx2-pio-transmit-cancel-drain-fifo.md">EvtSerCx2PioTransmitCancelDrainFifo</a> event callback functions.</p>

<p>SerCx2 initiates a PIO-transmit transaction in response to a write (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>) request from a client. If this request times out or is canceled before it completes, SerCx2 calls the <i>EvtSerCx2PioTransmitPurgeFifo</i> function, if it is implemented, to purge any unsent data that might remain the transmit FIFO.</p>

<p>After the transmit FIFO is purged, the <i>EvtSerCx2PioTransmitPurgeFifo</i> function must call the <a href="..\sercx\nf-sercx-sercx2piotransmitpurgefifocomplete.md">SerCx2PioTransmitPurgeFifoComplete</a> method to notify SerCx2 that the FIFO was purged, and SerCx2 then completes the write request.</p>

<p>For more information, see <a href="NULL">SerCx2 PIO-Transmit Transactions</a>.</p>

<p>To define an <i>EvtSerCx2PioTransmitPurgeFifo</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2PioTransmitPurgeFifo</i> callback function that is named <code>MyPioTransmitPurgeFifo</code>, use the <b>EVT_SERCX2_PIO_TRANSMIT_PURGE_FIFO</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_PIO_TRANSMIT_PURGE_FIFO</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_PIO_TRANSMIT_PURGE_FIFO</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<a href="..\sercx\nc-sercx-evt-sercx2-system-dma-transmit-drain-fifo.md">EvtSerCx2SystemDmaTransmitDrainFifo</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx2-system-dma-transmit-cancel-drain-fifo.md">EvtSerCx2SystemDmaTransmitCancelDrainFifo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>
</dt>
<dt>
<a href="serports.sercx2piotransmit_object_handle">SERCX2PIOTRANSMIT</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercx2piotransmitcreate.md">SerCx2PioTransmitCreate</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercx2piotransmitpurgefifocomplete.md">SerCx2PioTransmitPurgeFifoComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20EVT_SERCX2_PIO_TRANSMIT_PURGE_FIFO callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
