---
UID: NF.wdfdmatransaction.WdfDmaTransactionDmaCompletedWithLength
title: WdfDmaTransactionDmaCompletedWithLength
author: windows-driver-content
description: The WdfDmaTransactionDmaCompletedWithLength method notifies the framework that a device's DMA transfer operation is complete and supplies the length of the completed transfer.
old-location: wdf\wdfdmatransactiondmacompletedwithlength.htm
ms.assetid: 7f436ac1-1e36-449c-a23f-b5729e5a20c2
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
req.alt-api: WdfDmaTransactionDmaCompletedWithLength
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
ms.keywords: WdfDmaTransactionDmaCompletedWithLength
req.iface: 
req.product: Windows 10 or later.
---

# WdfDmaTransactionDmaCompletedWithLength function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDmaTransactionDmaCompletedWithLength</b> method notifies the framework that a device's DMA transfer operation is complete and supplies the length of the completed transfer. </p>


## -syntax

````
BOOLEAN WdfDmaTransactionDmaCompletedWithLength(
  _In_  WDFDMATRANSACTION DmaTransaction,
  _In_  size_t            TransferredLength,
  _Out_ NTSTATUS          *Status
);
````


## -parameters
<dl>

### -param <i>DmaTransaction</i> [in]

<dd>
<p>A handle to a DMA transaction object that the driver obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547027">WdfDmaTransactionCreate</a>.</p>
</dd>

### -param <i>TransferredLength</i> [in]

<dd>
<p>The number of bytes that the device transferred in the current DMA transfer.</p>
</dd>

### -param <i>Status</i> [out]

<dd>
<p>A pointer to a location that receives the status of the DMA transfer. For more information, see the Remarks section for <a href="https://msdn.microsoft.com/library/windows/hardware/ff547039">WdfDmaTransactionDmaCompleted</a>.</p>
</dd>
</dl>

## -returns
<p><b>WdfDmaTransactionDmaCompletedWithLength</b> returns <b>FALSE</b> and <i>Status</i> receives STATUS_MORE_PROCESSING_REQUIRED if additional transfers are needed to complete the DMA transaction. The method returns <b>TRUE</b> if no additional transfers are required. </p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>When your driver calls the <b>WdfDmaTransactionDmaCompletedWithLength</b> method, the framework ends the current transfer and, if necessary, starts a new one.</p>

<p>The <b>WdfDmaTransactionDmaCompletedWithLength</b> method behaves the same as <a href="https://msdn.microsoft.com/library/windows/hardware/ff547039">WdfDmaTransactionDmaCompleted</a>, except that drivers call <b>WdfDmaTransactionDmaCompletedWithLength</b> for devices that report the number of bytes that were transferred. The framework uses the reported byte count to determine the beginning of the next DMA transfer for the specified DMA transaction, if multiple transfers are needed to complete the transaction.</p>

<p>For more information about completing DMA transfers, see <a href="NULL">Completing a DMA Transfer</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">PLX9x5x</a> sample driver. This example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff547081">WdfDmaTransactionGetCurrentDmaTransferLength</a> to determine the current transfer's original length, and then it calculates the actual transfer length. Next, the example calls <b>WdfDmaTransactionDmaCompletedWithLength</b> to report the actual transfer length to the framework. If the current transfer is the last one for the transaction, the example calls a private routine that completes the I/O request.</p>

<p>When your driver calls the <b>WdfDmaTransactionDmaCompletedWithLength</b> method, the framework ends the current transfer and, if necessary, starts a new one.</p>

<p>The <b>WdfDmaTransactionDmaCompletedWithLength</b> method behaves the same as <a href="https://msdn.microsoft.com/library/windows/hardware/ff547039">WdfDmaTransactionDmaCompleted</a>, except that drivers call <b>WdfDmaTransactionDmaCompletedWithLength</b> for devices that report the number of bytes that were transferred. The framework uses the reported byte count to determine the beginning of the next DMA transfer for the specified DMA transaction, if multiple transfers are needed to complete the transaction.</p>

<p>For more information about completing DMA transfers, see <a href="NULL">Completing a DMA Transfer</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">PLX9x5x</a> sample driver. This example calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff547081">WdfDmaTransactionGetCurrentDmaTransferLength</a> to determine the current transfer's original length, and then it calculates the actual transfer length. Next, the example calls <b>WdfDmaTransactionDmaCompletedWithLength</b> to report the actual transfer length to the framework. If the current transfer is the last one for the transaction, the example calls a private routine that completes the I/O request.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547027">WdfDmaTransactionCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547039">WdfDmaTransactionDmaCompleted</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547081">WdfDmaTransactionGetCurrentDmaTransferLength</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionDmaCompletedWithLength method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
