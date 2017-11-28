---
UID: NF.wdfdmatransaction.WdfDmaTransactionCancel
title: WdfDmaTransactionCancel
author: windows-driver-content
description: The WdfDmaTransactionCancel method attempts to cancel a DMA transaction that is waiting for the allocation of map registers.
old-location: wdf\wdfdmatransactioncancel.htm
old-project: wdf
ms.assetid: A0EB188E-D5C7-4C7B-A462-2C3792825FD8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDmaTransactionCancel
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
req.alt-api: WdfDmaTransactionCancel
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

# WdfDmaTransactionCancel function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDmaTransactionCancel</b> method attempts to cancel a DMA transaction that is waiting for the allocation of map registers.</p>


## -syntax

````
BOOLEAN WdfDmaTransactionCancel(
  _In_ WDFDMATRANSACTION DmaTransaction
);
````


## -parameters
<dl>

### -param <i>DmaTransaction</i> [in]

<dd>
<p>A handle to the DMA transaction object that represents the transaction that is being canceled. This transaction must have already been initialized by the driver. </p>
</dd>
</dl>

## -returns
<p><b>WdfDmaTransactionCancel</b> returns TRUE if the framework successfully cancels map register allocation.  In this case, no transfers are completed, and the framework makes no additional DMA callbacks on the transaction until it is reinitiated.</p>

<p> The method returns FALSE if another thread is already processing this transaction, or if the driver has not yet called <a href="https://msdn.microsoft.com/library/windows/hardware/ff547062">WdfDmaTransactionExecute</a>.  In the first case, the framework is currently calling or will call <a href="wdf.evtprogramdma">EvtProgramDma</a> or <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-reserve-dma.md">EvtReserveDma</a>. At this point, a driver that specified a system-mode DMA profile might call <a href="https://msdn.microsoft.com/library/windows/hardware/hh439264">WdfDmaTransactionStopSystemTransfer</a>.</p>

<p>The method also returns FALSE if called with a transaction that was allocated from a DMA version 2 enabler.</p>

## -remarks
<p>The driver might call <b>WdfDmaTransactionCancel</b> from an <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-cancel.md">EvtRequestCancel</a> event callback function that it supplies in a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a>. For a code example that shows how to do this, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh439264">WdfDmaTransactionStopSystemTransfer</a>.</p>

<p>The driver might also call <b>WdfDmaTransactionCancel</b> from an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-canceled-on-queue.md">EvtIoCanceledOnQueue</a> event callback function.</p>

<p>

Cancellation can only succeed if the call to <b>WdfDmaTransactionCancel</b> occurs after the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547062">WdfDmaTransactionExecute</a>, but before the <b>WdfDmaTransactionExecute</b> method has started the DMA allocation.  For more information, see <a href="wdf.canceling_dma_transactions">Canceling DMA Transactions</a>.</p>

<p>The driver must call <b>WdfDmaTransactionCancel</b> after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547099">WdfDmaTransactionInitialize</a>, but before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547114">WdfDmaTransactionRelease</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a> to delete the transaction object.</p>

<p> Do not call <b>WdfDmaTransactionCancel</b> after the framework has called <a href="wdf.evtprogramdma">EvtProgramDma</a> or <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-reserve-dma.md">EvtReserveDma</a>.</p>

<p>A driver must request use of DMA version 3 prior to calling  <b>WdfDmaTransactionCancel</b>. 
 To select DMA version 3, set the <b>WdmDmaVersionOverride</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> to 3.</p>

<p> If a driver calls <b>WdfDmaTransactionCancel</b> on a transaction that was allocated from a DMA version 2 enabler, the framework generates a verifier error and <b>WdfDmaTransactionCancel</b> returns FALSE. In this case, no attempt is made to cancel the transaction.</p>

<p>The driver might call <b>WdfDmaTransactionCancel</b> from an <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-cancel.md">EvtRequestCancel</a> event callback function that it supplies in a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549984">WdfRequestMarkCancelableEx</a>. For a code example that shows how to do this, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh439264">WdfDmaTransactionStopSystemTransfer</a>.</p>

<p>The driver might also call <b>WdfDmaTransactionCancel</b> from an <a href="..\wdfio\nc-wdfio-evt-wdf-io-queue-io-canceled-on-queue.md">EvtIoCanceledOnQueue</a> event callback function.</p>

<p>

Cancellation can only succeed if the call to <b>WdfDmaTransactionCancel</b> occurs after the call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547062">WdfDmaTransactionExecute</a>, but before the <b>WdfDmaTransactionExecute</b> method has started the DMA allocation.  For more information, see <a href="wdf.canceling_dma_transactions">Canceling DMA Transactions</a>.</p>

<p>The driver must call <b>WdfDmaTransactionCancel</b> after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547099">WdfDmaTransactionInitialize</a>, but before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547114">WdfDmaTransactionRelease</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a> to delete the transaction object.</p>

<p> Do not call <b>WdfDmaTransactionCancel</b> after the framework has called <a href="wdf.evtprogramdma">EvtProgramDma</a> or <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-reserve-dma.md">EvtReserveDma</a>.</p>

<p>A driver must request use of DMA version 3 prior to calling  <b>WdfDmaTransactionCancel</b>. 
 To select DMA version 3, set the <b>WdmDmaVersionOverride</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> to 3.</p>

<p> If a driver calls <b>WdfDmaTransactionCancel</b> on a transaction that was allocated from a DMA version 2 enabler, the framework generates a verifier error and <b>WdfDmaTransactionCancel</b> returns FALSE. In this case, no attempt is made to cancel the transaction.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evtprogramdma">EvtProgramDma</a>
</dt>
<dt>
<a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-reserve-dma.md">EvtReserveDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439264">WdfDmaTransactionStopSystemTransfer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionCancel method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
