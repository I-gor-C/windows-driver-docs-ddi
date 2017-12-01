---
UID: NC.sercx.EVT_SERCX2_SELECT_NEXT_TRANSMIT_TRANSACTION_TYPE
title: EVT_SERCX2_SELECT_NEXT_TRANSMIT_TRANSACTION_TYPE
author: windows-driver-content
description: The EvtSerCx2SelectNextTransmitTransactionType event callback function is called by version 2 of the serial framework extension (SerCx2) to determine which data-transfer mechanism to use for the next write operation.
old-location: serports\evtsercx2selectnexttransmittransactiontype.htm
old-project: serports
ms.assetid: EE46CB43-18BA-4FD7-A60D-07DB1760B8E7
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
req.alt-api: EvtSerCx2SelectNextTransmitTransactionType
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

# EVT_SERCX2_SELECT_NEXT_TRANSMIT_TRANSACTION_TYPE callback



## -description
<p>The <i>EvtSerCx2SelectNextTransmitTransactionType</i> event callback function is called by version 2 of the serial framework extension (SerCx2) to determine which data-transfer mechanism to use for the next write operation.</p>


## -prototype

````
EVT_SERCX2_SELECT_NEXT_TRANSMIT_TRANSACTION_TYPE EvtSerCx2SelectNextTransmitTransactionType;

SERCX2_TRANSACTION_TYPE EvtSerCx2SelectNextTransmitTransactionType(
  _In_  WDFDEVICE            Device,
  _In_  PMDL                 Mdl,
  _In_  ULONG                Offset,
  _In_  ULONG                RemainingLength,
  _Out_ SERCX2CUSTOMTRANSMIT *CustomTransmit,
  _Out_ PULONG               NextTransactionLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A WDFDEVICE handle to the framework device object that represents the serial controller. The serial controller driver created this object in its <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function. For more information, see <a href="..\sercx\nf-sercx-sercx2initializedevice.md">SerCx2InitializeDevice</a>.</p>
</dd>

### -param <i>Mdl</i> [in]

<dd>
<p>A pointer to an <a href="..\wdm\ns-wdm--mdl.md">MDL</a> that describes the memory pages that are spanned by the write buffer for the next transmit transaction. The scatter/gather list for the DMA transfer will use the region of this memory that is specified by the <i>Offset</i> and <i>Length</i> parameters.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>The starting offset for the next data transfer. This parameter is a byte offset from the start of the buffer region described by the MDL. If the MDL specifies a total of N bytes of buffer space, possible values of <i>Offset</i> are in the range 0 to N–1.</p>
</dd>

### -param <i>RemainingLength</i> [in]

<dd>
<p>The total number of bytes of data that remain to be transferred in the current write (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>) request. If the MDL specifies a total of N bytes of buffer space, possible values of <i>Length</i> are in the range 1 to N–<i>Offset</i>.</p>
</dd>

### -param <i>CustomTransmit</i> [out]

<dd>
<p>A pointer to a location to which the function writes the <a href="serports.sercx2customtransmit">SERCX2CUSTOMTRANSMIT</a> handle to the custom-transmit object. If the function returns <b>SerCx2TransactionTypeCustom</b>, the function must supply the object handle that the serial controller driver created in a previous call to the <a href="..\sercx\nf-sercx-sercx2customtransmitcreate.md">SerCx2CustomTransmitCreate</a> method. If the return value is not <b>SerCx2TransactionTypeCustom</b>, this output value is ignored by SerCx2.</p>
</dd>

### -param <i>NextTransactionLength</i> [out]

<dd>
<p>A pointer to a location to which the function writes the number of bytes to transfer in the next transmit transaction. If the return value is <b>SerCx2TransactionTypeDefault</b>, this output value is ignored by SerCx2.</p>
</dd>
</dl>

## -returns
<p>The <i>EvtSerCx2SelectNextTransmitTransactionType</i> function returns a <a href="..\sercx\ne-sercx--sercx2-transaction-type.md">SERCX2_TRANSACTION_TYPE</a> enumeration constant to indicate whether to use a driver-selected transaction type (programmed I/O (PIO), system DMA, or custom data transfer), or to let SerCx2 choose which transaction type to use for the next transmit transaction.</p>

## -remarks
<p>Your serial controller driver can, as an option, implement this function. If implemented, the driver registers this function in the call to the <a href="..\sercx\nf-sercx-sercx2initializedevice.md">SerCx2InitializeDevice</a> method that finishes the initialization of the framework device object for the serial controller.</p>

<p>If your serial controller driver does not implement an <i>EvtSerCx2SelectNextTransmitTransactionType</i> function, then SerCx2 always decides what type of data-transfer mechanism (PIO, system DMA, or custom) to use for the next transmit transaction. SerCx2 bases its decisions on the I/O configuration information supplied by the serial controller driver. A driver that supports system-DMA-transmit transactions supplies a <a href="..\sercx\ns-sercx--sercx2-system-dma-transmit-config.md">SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG</a> structure that contains this information. A driver that supports custom-transmit transactions supplies a <a href="..\sercx\ns-sercx--sercx2-custom-transmit-config.md">SERCX2_CUSTOM_TRANSMIT_CONFIG</a> structure that contains this information.</p>

<p>If your serial controller driver implements an <i>EvtSerCx2SelectNextTransmitTransactionType</i> function, SerCx2 calls this function to determine what type of data-transfer mechanism (PIO, system DMA, or custom) to use for the next transmit transaction. You might want to implement this function if the serial controller has special hardware capabilities that cannot adequately be described by the I/O configuration information in the <b>SERCX2_<i>XXX</i>_TRANSMIT_CONFIG</b> structures.</p>

<p>For more information, see <a href="NULL">Overview of SerCx2 I/O Transactions</a>.</p>

<p>To define an <i>EvtSerCx2CustomTransmitSelectNextTransactionType</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2CustomTransmitSelectNextTransactionType</i> callback function that is named <code>MyCustomTransmitSelectNextTransactionType</code>, use the <b>EVT_SERCX2_CUSTOM_TRANSMIT_SELECT_NEXT_TRANSACTION_TYPE</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_CUSTOM_TRANSMIT_SELECT_NEXT_TRANSACTION_TYPE</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_CUSTOM_TRANSMIT_SELECT_NEXT_TRANSACTION_TYPE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--mdl.md">MDL</a>
</dt>
<dt>
<a href="serports.sercx2customtransmit">SERCX2CUSTOMTRANSMIT</a>
</dt>
<dt>
<a href="..\sercx\ns-sercx--sercx2-custom-transmit-config.md">SERCX2_CUSTOM_TRANSMIT_CONFIG</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercx2customtransmitcreate.md">SerCx2CustomTransmitCreate</a>
</dt>
<dt>
<a href="..\sercx\nf-sercx-sercx2initializedevice.md">SerCx2InitializeDevice</a>
</dt>
<dt>
<a href="..\sercx\ns-sercx--sercx2-system-dma-transmit-config.md">SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG</a>
</dt>
<dt>
<a href="..\sercx\ne-sercx--sercx2-transaction-type.md">SERCX2_TRANSACTION_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20EVT_SERCX2_SELECT_NEXT_TRANSMIT_TRANSACTION_TYPE callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
