---
UID: NF.wdfdmatransaction.WdfDmaTransactionSetTransferCompleteCallback
title: WdfDmaTransactionSetTransferCompleteCallback
author: windows-driver-content
description: The WdfDmaTransactionSetTransferCompleteCallback method registers a transfer completion event callback function for a system-mode DMA transaction.
old-location: wdf\wdfdmatransactionsettransfercompletecallback.htm
old-project: wdf
ms.assetid: B97FF6B1-BFCB-4293-B2F0-EE08E12CFCFF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDmaTransactionSetTransferCompleteCallback
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdmatransaction.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WdfDmaTransactionSetTransferCompleteCallback
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDmaTransactionSetTransferCompleteCallback function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>
   The <b>WdfDmaTransactionSetTransferCompleteCallback</b> method registers a transfer completion event callback function for a system-mode DMA transaction.</p>


## -syntax

````
void WdfDmaTransactionSetTransferCompleteCallback(
  _In_     WDFDMATRANSACTION                             DmaTransaction,
  _In_opt_ PFN_WDF_DMA_TRANSACTION_DMA_TRANSFER_COMPLETE DmaCompletionRoutine,
  _In_opt_ PVOID                                         DmaCompletionContext
);
````


## -parameters
<dl>

### -param <i>DmaTransaction</i> [in]

<dd>
<p>A handle to an initialized DMA transaction object for which to set or clear the transfer completion callback.</p>
</dd>

### -param <i>DmaCompletionRoutine</i> [in, optional]

<dd>
<p>A pointer to the driver's <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-dma-transaction-dma-transfer-complete.md">EvtDmaTransactionDmaTransferComplete</a> event callback function, or NULL to clear a previously set callback function.</p>
</dd>

### -param <i>DmaCompletionContext</i> [in, optional]

<dd>
<p>A pointer to a buffer containing the driver-specified context to be provided to the driver's <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-dma-transaction-dma-transfer-complete.md">EvtDmaTransactionDmaTransferComplete</a> event callback function, or NULL.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>The driver calls this method to set a completion routine that the framework calls after the system DMA controller completes a transfer.  The framework calls the driver's <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-dma-transaction-dma-transfer-complete.md">EvtDmaTransactionDmaTransferComplete</a> callback once for each transfer in the transaction.</p>

<p>Typically from within an <a href="wdf.request_handlers">I/O queue event callback function</a>, a driver performs the following steps, in this order:</p>

<p>If the driver has specified an <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-dma-transaction-dma-transfer-complete.md">EvtDmaTransactionDmaTransferComplete</a> event callback function by calling <b>WdfDmaTransactionSetTransferCompleteCallback</b> and the driver subsequently calls <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionrelease.md">WdfDmaTransactionRelease</a>, the callback is cleared.</p>

<p><b>WdfDmaTransactionSetTransferCompleteCallback</b> can only be used with a DMA enabler that specifies a system-mode DMA profile.</p>

<p>If your driver calls this method on an operating system earlier than Windows 8, <a href="wdf.using_kmdf_verifier">the framework's verifier</a> reports an error.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-dma-transaction-dma-transfer-complete.md">EvtDmaTransactionDmaTransferComplete</a>
</dt>
<dt>
<a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionrelease.md">WdfDmaTransactionRelease</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionSetTransferCompleteCallback method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
