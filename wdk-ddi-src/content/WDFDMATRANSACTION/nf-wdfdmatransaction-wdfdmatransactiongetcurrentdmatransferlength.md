---
UID: NF.wdfdmatransaction.WdfDmaTransactionGetCurrentDmaTransferLength
title: WdfDmaTransactionGetCurrentDmaTransferLength
author: windows-driver-content
description: The WdfDmaTransactionGetCurrentDmaTransferLength method returns the size of the current DMA transfer.
old-location: wdf\wdfdmatransactiongetcurrentdmatransferlength.htm
ms.assetid: 20a27ad7-0b27-494e-b761-fc3edf71e8c9
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdmatransaction.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDmaTransactionGetCurrentDmaTransferLength
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WdfDmaTransactionGetCurrentDmaTransferLength
req.iface: 
req.product: Windows 10 or later.
---

# WdfDmaTransactionGetCurrentDmaTransferLength function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDmaTransactionGetCurrentDmaTransferLength</b> method returns the size of the current DMA transfer.</p>


## -syntax

````
size_t WdfDmaTransactionGetCurrentDmaTransferLength(
  _In_ WDFDMATRANSACTION DmaTransaction
);
````


## -parameters
<dl>

### -param <i>DmaTransaction</i> [in]

<dd>
<p>A handle to a DMA transaction object that the driver obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547027">WdfDmaTransactionCreate</a>.</p>
</dd>
</dl>

## -returns
<p><b>WdfDmaTransactionGetCurrentDmaTransferLength</b> returns the length of the current DMA transfer.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>If a driver calls <b>WdfDmaTransactionGetCurrentDmaTransferLength</b>, it must do so before it calls one of the transfer completion routines, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff547039">WdfDmaTransactionDmaCompleted</a>, to complete the current DMA transfer. Typically, drivers call <b>WdfDmaTransactionGetCurrentDmaTransferLength</b> from within an <a href="https://msdn.microsoft.com/d2d505e0-aeac-4871-8c60-d026b2833043">EvtInterruptDpc</a> event callback function.</p>

<p>Typically, a driver calls <b>WdfDmaTransactionGetCurrentDmaTransferLength</b> for devices that report residual DMA transfer lengths (that is, byte counts of data that was not transferred). By subtracting the residual transfer length from the value that <b>WdfDmaTransactionGetCurrentDmaTransferLength</b> returned, the driver can determine the actual transfer length. The driver then calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff547052">WdfDmaTransactionDmaCompletedWithLength</a> to let the framework know the number of bytes that the device actually transferred.</p>

<p>For more information about complete DMA transfers, see <a href="NULL">Completing a DMA Transfer</a>. </p>

<p>For a code example that uses <b>WdfDmaTransactionGetCurrentDmaTransferLength</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547052">WdfDmaTransactionDmaCompletedWithLength</a>.</p>

<p>If a driver calls <b>WdfDmaTransactionGetCurrentDmaTransferLength</b>, it must do so before it calls one of the transfer completion routines, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff547039">WdfDmaTransactionDmaCompleted</a>, to complete the current DMA transfer. Typically, drivers call <b>WdfDmaTransactionGetCurrentDmaTransferLength</b> from within an <a href="https://msdn.microsoft.com/d2d505e0-aeac-4871-8c60-d026b2833043">EvtInterruptDpc</a> event callback function.</p>

<p>Typically, a driver calls <b>WdfDmaTransactionGetCurrentDmaTransferLength</b> for devices that report residual DMA transfer lengths (that is, byte counts of data that was not transferred). By subtracting the residual transfer length from the value that <b>WdfDmaTransactionGetCurrentDmaTransferLength</b> returned, the driver can determine the actual transfer length. The driver then calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff547052">WdfDmaTransactionDmaCompletedWithLength</a> to let the framework know the number of bytes that the device actually transferred.</p>

<p>For more information about complete DMA transfers, see <a href="NULL">Completing a DMA Transfer</a>. </p>

<p>For a code example that uses <b>WdfDmaTransactionGetCurrentDmaTransferLength</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547052">WdfDmaTransactionDmaCompletedWithLength</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdmatransaction.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/d2d505e0-aeac-4871-8c60-d026b2833043">EvtInterruptDpc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547027">WdfDmaTransactionCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547039">WdfDmaTransactionDmaCompleted</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547052">WdfDmaTransactionDmaCompletedWithLength</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionGetCurrentDmaTransferLength method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
