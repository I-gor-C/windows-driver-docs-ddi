---
UID: NC.sercx.EVT_SERCX2_PIO_RECEIVE_READ_BUFFER
title: EVT_SERCX2_PIO_RECEIVE_READ_BUFFER
author: windows-driver-content
description: The EvtSerCx2PioReceiveReadBuffer event callback function is called by version 2 of the serial framework extension (SerCx2) to use programmed I/O (PIO) to transfer data from the receive FIFO in the serial controller to a read buffer.
old-location: serports\evtsercx2pioreceivereadbuffer.htm
old-project: serports
ms.assetid: B69A128A-B1B0-47BC-9783-32780FC9C447
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
req.alt-api: EvtSerCx2PioReceiveReadBuffer
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

# EVT_SERCX2_PIO_RECEIVE_READ_BUFFER callback



## -description
<p>The <i>EvtSerCx2PioReceiveReadBuffer</i> event callback function is called by version 2 of the serial framework extension (SerCx2) to use programmed I/O (PIO) to transfer data from the receive FIFO in the serial controller to a read buffer.</p>


## -prototype

````
EVT_SERCX2_PIO_RECEIVE_READ_BUFFER EvtSerCx2PioReceiveReadBuffer;

ULONG EvtSerCx2PioReceiveReadBuffer(
  _In_  SERCX2PIORECEIVE PioReceive,
  _Out_ PUCHAR           Buffer,
  _In_  ULONG            Length
)
{ ... }
````


## -parameters
<dl>

### -param <i>PioReceive</i> [in]

<dd>
<p>A <a href="serports.sercx2pioreceive_object_handle">SERCX2PIORECEIVE</a> handle to a PIO-receive object. The serial controller driver previously called the <a href="..\sercx\nf-sercx-sercx2pioreceivecreate.md">SerCx2PioReceiveCreate</a> method to create this object.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to the read buffer. This parameter is the virtual address of a locked-down buffer in system memory.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes in the read buffer that are available to store received data.</p>
</dd>
</dl>

## -returns
<p>The <i>EvtSerCx2PioReceiveReadBuffer</i> function returns the number of bytes of data that it successfully transferred from the receive FIFO in the serial controller hardware to the read buffer.</p>

## -remarks
<p>Your serial controller driver must implement this function. The driver registers the function in the <a href="..\sercx\nf-sercx-sercx2pioreceivecreate.md">SerCx2PioReceiveCreate</a> call that creates the PIO-receive object.</p>

<p>SerCx2 might call the <i>EvtSerCx2PioReceiveReadBuffer</i> function more than once during a PIO-receive transaction. A single <i>EvtSerCx2PioReceiveReadBuffer</i> call is sufficient if this call can fill the read buffer with data from the receive FIFO. Otherwise, SerCx2 continues to call this function, as more data becomes available in the receive FIFO, until the read buffer is filled.</p>

<p>The <i>EvtSerCx2PioReceiveReadBuffer</i> function uses PIO to transfer as many bytes as it can from the receive FIFO to the read buffer. The function continues to transfer data from the FIFO for as long as the buffer passed to this function is not full and the line status register (LSR) indicates that more data is available from the FIFO. If the LSR indicates that the FIFO is empty, the function returns without filling the buffer. Otherwise, the function fills the buffer and returns. In either case, the value returned by this function is the number of bytes of data that were successfully transferred to the read buffer from the receive FIFO.</p>

<p>Typically, the <i>EvtSerCx2PioReceiveReadBuffer</i> function does not enable any interrupts. Instead, if the receive FIFO runs out of data before the function can fill the read buffer, SerCx2 calls the <a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-enable-ready-notification.md">EvtSerCx2PioReceiveEnableReadyNotification</a> event callback function to enable a ready notification, and this function enables an interrupt that occurs when more data is available in the receive FIFO.</p>

<p>For each successive call to the <i>EvtSerCx2PioReceiveReadBuffer</i> function, SerCx2 adjusts <i>Buffer</i> to point to the next buffer region to be filled, and sets <i>Length</i> to the number of bytes of unfilled space that remain in the buffer.</p>

<p>The ready notification is never enabled when SerCx2 calls the <i>EvtSerCx2PioReceiveEnableReadyNotification</i> function. However, SerCx2 might call this function from the same thread from which the driver called the <a href="..\sercx\nf-sercx-sercx2pioreceiveready.md">SerCx2PioReceiveReady</a> method.</p>

<p>If the driver implements an <a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-initialize-transaction.md">EvtSerCx2PioReceiveInitializeTransaction</a> function, SerCx2 calls this function at the start of a PIO-transmit transaction, before the first call to the <i>EvtSerCx2PioReceiveReadBuffer</i> function. If the driver implements an <a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-cleanup-transaction.md">EvtSerCx2PioReceiveCleanupTransaction</a> function, SerCx2 calls this function at the end of a PIO-receive transaction, after the final call to the <i>EvtSerCx2PioReceiveReadBuffer</i> function.</p>

<p>In addition to calling the <i>EvtSerCx2PioReceiveReadBuffer</i> function during PIO-receive transactions, SerCx2 calls this function to save the state of the receive FIFO just before the serial controller exits the D0 device power state. For more information, see <a href="..\sercx\nf-sercx-sercx2savereceivefifoond0exit.md">SerCx2SaveReceiveFifoOnD0Exit</a>.</p>

<p>For more information about PIO-receive transactions, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265332">SerCx2 PIO-Receive Transactions</a>.</p>

<p>To define an <i>EvtSerCx2PioReceiveReadBuffer</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2PioReceiveReadBuffer</i> callback function that is named <code>MyPioReceiveReadBuffer</code>, use the <b>EVT_SERCX2_PIO_RECEIVE_READ_BUFFER</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_PIO_RECEIVE_READ_BUFFER</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_PIO_RECEIVE_READ_BUFFER</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-cleanup-transaction.md">EvtSerCx2PioReceiveCleanupTransaction</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-enable-ready-notification.md">EvtSerCx2PioReceiveEnableReadyNotification</a>
</dt>
<dt>
<a href="..\sercx\nc-sercx-evt-sercx2-pio-receive-initialize-transaction.md">EvtSerCx2PioReceiveInitializeTransaction</a>
</dt>
<dt>
<a href="serports.sercx2pioreceive_object_handle">SERCX2PIORECEIVE</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercx2pioreceivecreate.md">SerCx2PioReceiveCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20EVT_SERCX2_PIO_RECEIVE_READ_BUFFER callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
