---
UID: NC.sercx.EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION
title: EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION
author: windows-driver-content
description: The EvtSerCx2EvtSerCx2SystemDmaReceiveInitializeTransaction event callback function is called by version 2 of the serial framework extension (SerCx2) to prepare the serial controller driver to perform a system-DMA-receive transaction.
old-location: serports\evtsercx2systemdmareceiveinitializetransaction.htm
old-project: serports
ms.assetid: 34E016AF-439C-44CC-A2AE-78CD7B2B5443
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
req.alt-api: EvtSerCx2SystemDmaReceiveInitializeTransaction
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

# EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION callback



## -description
<p>The <i>EvtSerCx2EvtSerCx2SystemDmaReceiveInitializeTransaction</i> event callback function is called by version 2 of the serial framework extension (SerCx2) to prepare the serial controller driver to perform a system-DMA-receive transaction.</p>


## -prototype

````
EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION EvtSerCx2SystemDmaReceiveInitializeTransaction;

VOID EvtSerCx2SystemDmaReceiveInitializeTransaction(
  _In_ SERCX2SYSTEMDMARECEIVE SystemDmaReceive,
  _In_ ULONG                  Length
)
{ ... }
````


## -parameters
<dl>

### -param <i>SystemDmaReceive</i> [in]

<dd>
<p>A <a href="serports.sercx2systemdmareceive_object_handle">SERCX2SYSTEMDMARECEIVE</a> handle to a system-DMA-receive object. The serial controller driver previously called the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265279">SerCx2SystemDmaReceiveCreate</a> method to create this object.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes to be transferred in the system-DMA-receive transaction.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Your serial controller driver can, as an option, implement this function. If implemented, the driver registers the function in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265279">SerCx2SystemDmaReceiveCreate</a> call that creates the system-DMA-receive object.</p>

<p>Your driver should implement an <i>EvtSerCx2EvtSerCx2SystemDmaReceiveInitializeTransaction</i> function if it needs to initialize the serial controller and associated hardware in preparation for a new system-DMA-receive transaction. SerCx2 calls this function, if it is implemented, before a system-DMA-receive transaction starts. In response to this call, the serial controller driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265281">SerCx2SystemDmaReceiveInitializeTransactionComplete</a> method to notify SerCx2 after the initialization is finished.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265343">SerCx2 System-DMA-Receive Transactions</a>.</p>

<p>To define an <i>EvtSerCx2EvtSerCx2SystemDmaReceiveInitializeTransaction</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2EvtSerCx2SystemDmaReceiveInitializeTransaction</i> callback function that is named <code>MySystemDmaReceiveInitializeTransaction</code>, use the <b>EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

<p>Your serial controller driver can, as an option, implement this function. If implemented, the driver registers the function in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265279">SerCx2SystemDmaReceiveCreate</a> call that creates the system-DMA-receive object.</p>

<p>Your driver should implement an <i>EvtSerCx2EvtSerCx2SystemDmaReceiveInitializeTransaction</i> function if it needs to initialize the serial controller and associated hardware in preparation for a new system-DMA-receive transaction. SerCx2 calls this function, if it is implemented, before a system-DMA-receive transaction starts. In response to this call, the serial controller driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265281">SerCx2SystemDmaReceiveInitializeTransactionComplete</a> method to notify SerCx2 after the initialization is finished.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265343">SerCx2 System-DMA-Receive Transactions</a>.</p>

<p>To define an <i>EvtSerCx2EvtSerCx2SystemDmaReceiveInitializeTransaction</i> callback function, you must first provide a function declaration that identifies the type of callback function you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtSerCx2EvtSerCx2SystemDmaReceiveInitializeTransaction</i> callback function that is named <code>MySystemDmaReceiveInitializeTransaction</code>, use the <b>EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION</b> function type, as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION</b> function type is defined in the Sercx.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For more information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?LinkId=286697">Annotating Function Behavior</a>.</p>

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
<a href="serports.sercx2systemdmareceive_object_handle">SERCX2SYSTEMDMARECEIVE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265279">SerCx2SystemDmaReceiveCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265281">SerCx2SystemDmaReceiveInitializeTransactionComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [serports\serports]:%20EVT_SERCX2_SYSTEM_DMA_RECEIVE_INITIALIZE_TRANSACTION callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
