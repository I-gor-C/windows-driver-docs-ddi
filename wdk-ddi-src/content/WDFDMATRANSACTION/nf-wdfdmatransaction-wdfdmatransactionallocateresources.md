---
UID: NF.wdfdmatransaction.WdfDmaTransactionAllocateResources
title: WdfDmaTransactionAllocateResources
author: windows-driver-content
description: The WdfDmaTransactionAllocateResources method reserves a single-packet or system-mode DMA enabler for exclusive (and repeated) use with the specified transaction object.
old-location: wdf\wdfdmatransactionallocateresources.htm
ms.assetid: 69D251D9-1B33-49FD-8D48-EFCBD6640632
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
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WdfDmaTransactionAllocateResources
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
ms.keywords: WdfDmaTransactionAllocateResources
req.iface: 
req.product: Windows 10 or later.
---

# WdfDmaTransactionAllocateResources function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>
   The <b>WdfDmaTransactionAllocateResources</b> method reserves a single-packet or system-mode DMA enabler for exclusive (and repeated) use with the specified transaction object. The driver can initialize and initiate the transaction multiple times while holding reserved resources.</p>


## -syntax

````
NTSTATUS WdfDmaTransactionAllocateResources(
  _In_ WDFDMATRANSACTION   DmaTransaction,
  _In_ WDF_DMA_DIRECTION   DmaDirection,
  _In_ ULONG               RequiredMapRegisters,
  _In_ PFN_WDF_RESERVE_DMA EvtReserveDmaFunction,
  _In_ PVOID               EvtReserveDmaContext
);
````


## -parameters
<dl>

### -param <i>DmaTransaction</i> [in]

<dd>
<p>A handle to the DMA transaction object for which DMA resources should be reserved.</p>
</dd>

### -param <i>DmaDirection</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff551288">WDF_DMA_DIRECTION</a>-typed value specifying the DMA transfer direction for which the resources are being reserved. If the driver did not specify a duplex profile, the framework ignores this value.</p>
</dd>

### -param <i>RequiredMapRegisters</i> [in]

<dd>
<p>The number of map registers the driver wants to reserve. If zero, the framework derives the required number of map registers from the initialized transaction.</p>
</dd>

### -param <i>EvtReserveDmaFunction</i> [in]

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/3663EF19-5F16-43D1-BFBC-28280E28D4DE">EvtReserveDma</a> event callback function.</p>
</dd>

### -param <i>EvtReserveDmaContext</i> [in]

<dd>
<p>A pointer to a buffer containing the context to be provided to the driver's <a href="https://msdn.microsoft.com/3663EF19-5F16-43D1-BFBC-28280E28D4DE">EvtReserveDma</a> event callback function.</p>
</dd>
</dl>

## -returns
<p><b>WdfDmaTransactionAllocateResources</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method returns one of the following values.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>DmaDirection</i> parameter contains an invalid value.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The number of map register requests exceeds the number assigned to the enabler, or the driver previously called <a href="https://msdn.microsoft.com/library/windows/hardware/hh451190">WdfDmaTransactionSetImmediateExecution</a> and the resources needed for the request are unavailable.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>DMA version 3 or later is not enabled, or the driver called this method for a scatter-gather DMA enabler.</p>

<p> </p>

## -remarks
<p><b>WdfDmaTransactionAllocateResources</b> sends a request for map registers to the system DMA engine.  When the request has been fulfilled, the framework calls the driver's <a href="https://msdn.microsoft.com/3663EF19-5F16-43D1-BFBC-28280E28D4DE">EvtReserveDma</a> event callback function. For more information about reserving resources, see <a href="wdf.reserving_dma_resources">Reserving DMA Resources</a>.</p>

<p>Framework-based drivers typically call <b>WdfDmaTransactionAllocateResources</b> from within an <a href="wdf.request_handlers">I/O request handler</a>.  A driver can also call <b>WdfDmaTransactionAllocateResources</b> from its <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback function, after creating a DMA enabler object.</p>

<p>  When called with a scatter/gather DMA enabler, <b>WdfDmaTransactionAllocateResources</b> causes a verifier bug check.</p>

<p>The driver must create the transaction specified by <i>DmaTransaction</i> prior to calling <b>WdfDmaTransactionAllocateResources</b>. After calling <b>WdfDmaTransactionAllocateResources</b>, the driver initializes and initiates the transaction. The driver can reinitialize and reinitiate the same transaction object multiple times, avoiding the delay that would otherwise occur between transactions as map registers were freed back to the HAL and then reallocated.</p>

<p>A driver could call <b>WdfDmaTransactionAllocateResources</b> in the following situations:</p>

<p>Before calling <b>WdfDmaTransactionAllocateResources</b>, the driver must determine the number of map registers needed for any transaction that it will initiate using this reservation. To do so, the driver can call either the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540562">ADDRESS_AND_SIZE_TO_SPAN_PAGES</a> macro or <a href="https://msdn.microsoft.com/library/windows/hardware/hh451179">WdfDmaTransactionGetTransferInfo</a>.</p>

<p> When calling <b>WdfDmaTransactionAllocateResources</b>, the driver should not request more map registers than it requested when it created the enabler.</p>

<p>To call <b>WdfDmaTransactionAllocateResources</b> in a non-blocking manner, the driver should first call <a href="https://msdn.microsoft.com/library/windows/hardware/hh451190">WdfDmaTransactionSetImmediateExecution</a>.</p>

<p><b>WdfDmaTransactionAllocateResources</b> requires DMA version 3.
 To select DMA version 3, set the <b>WdmDmaVersionOverride</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> to 3.
</p>

<p><b>WdfDmaTransactionAllocateResources</b> sends a request for map registers to the system DMA engine.  When the request has been fulfilled, the framework calls the driver's <a href="https://msdn.microsoft.com/3663EF19-5F16-43D1-BFBC-28280E28D4DE">EvtReserveDma</a> event callback function. For more information about reserving resources, see <a href="wdf.reserving_dma_resources">Reserving DMA Resources</a>.</p>

<p>Framework-based drivers typically call <b>WdfDmaTransactionAllocateResources</b> from within an <a href="wdf.request_handlers">I/O request handler</a>.  A driver can also call <b>WdfDmaTransactionAllocateResources</b> from its <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback function, after creating a DMA enabler object.</p>

<p>  When called with a scatter/gather DMA enabler, <b>WdfDmaTransactionAllocateResources</b> causes a verifier bug check.</p>

<p>The driver must create the transaction specified by <i>DmaTransaction</i> prior to calling <b>WdfDmaTransactionAllocateResources</b>. After calling <b>WdfDmaTransactionAllocateResources</b>, the driver initializes and initiates the transaction. The driver can reinitialize and reinitiate the same transaction object multiple times, avoiding the delay that would otherwise occur between transactions as map registers were freed back to the HAL and then reallocated.</p>

<p>A driver could call <b>WdfDmaTransactionAllocateResources</b> in the following situations:</p>

<p>Before calling <b>WdfDmaTransactionAllocateResources</b>, the driver must determine the number of map registers needed for any transaction that it will initiate using this reservation. To do so, the driver can call either the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540562">ADDRESS_AND_SIZE_TO_SPAN_PAGES</a> macro or <a href="https://msdn.microsoft.com/library/windows/hardware/hh451179">WdfDmaTransactionGetTransferInfo</a>.</p>

<p> When calling <b>WdfDmaTransactionAllocateResources</b>, the driver should not request more map registers than it requested when it created the enabler.</p>

<p>To call <b>WdfDmaTransactionAllocateResources</b> in a non-blocking manner, the driver should first call <a href="https://msdn.microsoft.com/library/windows/hardware/hh451190">WdfDmaTransactionSetImmediateExecution</a>.</p>

<p><b>WdfDmaTransactionAllocateResources</b> requires DMA version 3.
 To select DMA version 3, set the <b>WdmDmaVersionOverride</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> to 3.
</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547027">WdfDmaTransactionCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547062">WdfDmaTransactionExecute</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451177">WdfDmaTransactionFreeResources</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a3d4a983-8a75-44be-bd72-8673d89f9f87">EvtDevicePrepareHardware</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546983">WdfDmaEnablerCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451190">WdfDmaTransactionSetImmediateExecution</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionAllocateResources method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
