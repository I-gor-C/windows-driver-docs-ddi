---
UID: NF.wdfdmatransaction.WdfDmaTransactionInitialize
title: WdfDmaTransactionInitialize
author: windows-driver-content
description: The WdfDmaTransactionInitialize method initializes a specified DMA transaction.
old-location: wdf\wdfdmatransactioninitialize.htm
old-project: wdf
ms.assetid: cb17b31a-a069-4d41-a613-81a9815ac9a3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDmaTransactionInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdmatransaction.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDmaTransactionInitialize
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DeferredRequestCompleted, DriverCreate, KmdfIrql, KmdfIrql2, MdlAfterReqCompletedIntIoctlA, MdlAfterReqCompletedIoctlA, MdlAfterReqCompletedReadA, MdlAfterReqCompletedWriteA, RequestCompleted, RequestCompletedLocal
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

# WdfDmaTransactionInitialize function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDmaTransactionInitialize</b> method initializes a specified DMA transaction.  </p>


## -syntax

````
NTSTATUS WdfDmaTransactionInitialize(
  _In_ WDFDMATRANSACTION   DmaTransaction,
  _In_ PFN_WDF_PROGRAM_DMA EvtProgramDmaFunction,
  _In_ WDF_DMA_DIRECTION   DmaDirection,
  _In_ PMDL                Mdl,
  _In_ PVOID               VirtualAddress,
  _In_ size_t              Length
);
````


## -parameters
<dl>

### -param DmaTransaction [in]

<dd>
<p>A handle to a DMA transaction object that the driver obtained from a previous call to <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioncreate.md">WdfDmaTransactionCreate</a>.</p>
</dd>

### -param EvtProgramDmaFunction [in]

<dd>
<p>A pointer to the driver's <a href="wdf.evtprogramdma">EvtProgramDma</a> event callback function. </p>
</dd>

### -param DmaDirection [in]

<dd>
<p>A <a href="..\wdfdmaenabler\ne-wdfdmaenabler--wdf-dma-direction.md">WDF_DMA_DIRECTION</a>-typed value.</p>
</dd>

### -param Mdl [in]

<dd>
<p>A pointer to a memory descriptor list (MDL) that describes the buffer that will be used for the DMA transaction. See more information in <b>Remarks</b>.</p>
</dd>

### -param VirtualAddress [in]

<dd>
<p>The virtual address of the buffer that will be used for the DMA transaction.</p>
</dd>

### -param Length [in]

<dd>
<p>The number of bytes to be transferred.</p>
</dd>
</dl>

## -returns
<p><b>WdfDmaTransactionInitialize</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A scatter/gather list could not be allocated.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_WDF_TOO_FRAGMENTED</b></dt>
</dl><p>The number of scatter/gather elements that was needed to handle the transaction was greater than the value that the driver's call to <a href="..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablersetmaximumscattergatherelements.md">WdfDmaEnablerSetMaximumScatterGatherElements</a> specified. </p>

<p>For transactions that were set for <a href="https://msdn.microsoft.com/windows/hardware/drivers/wdf/">single transfer</a>, one way 
  to fix this is to copy the data to a physically contiguous buffer and then initialize the transaction with that buffer. For example, call <a href="..\ntddk\nf-ntddk-mmallocatecontiguousmemory.md">MmAllocateContiguousMemory</a>, copy the original buffers into the new one, and then call <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioninitialize.md">WdfDmaTransactionInitialize</a> again.</p><dl>
<dt><b>STATUS_WDF_NOT_ENOUGH_MAP_REGISTERS</b></dt>
</dl><p>This return value applies only to transactions that were set for <a href="https://msdn.microsoft.com/windows/hardware/drivers/wdf/">single transfer</a>.  </p>

<p>The number of map registers needed to map the transaction is larger than the number the DMA adapter has reserved.</p>

<p>To fix, 	the driver might reduce the number of required map registers by combining an MDL chain into a single MDL.</p>

<p>	Drivers using packet and system DMA can call <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionallocateresources.md">WdfDmaTransactionAllocateResources</a> to reserve a number of map registers from the total allocated to the device. Suppose your driver reserved 4 out of 8 total map registers, but the DMA transfer requires 6. In this case, <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioninitialize.md">WdfDmaTransactionInitialize</a> fails. To fix, call <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionfreeresources.md">WdfDmaTransactionFreeResources</a> and then call <b>WdfDmaTransactionInitialize</b> again.</p>

<p>
 Drivers using scatter/gather DMA cannot reserve map registers.</p><dl>
<dt><b>STATUS_WDF_TOO_MANY_TRANSFERS</b></dt>
</dl><p>This return value applies only to transactions that were set for <a href="https://msdn.microsoft.com/windows/hardware/drivers/wdf/">single transfer</a>.  </p>

<p>The transaction’s total length exceeds the device’s maximum transfer size.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>The <b>WdfDmaTransactionInitialize</b> method prepares a DMA operation for execution, by performing initialization operations such as allocating a transaction's scatter/gather list. After your driver calls <b>WdfDmaTransactionInitialize</b>, the driver must call <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionexecute.md">WdfDmaTransactionExecute</a> to begin executing the transaction.</p>

<p>Framework-based drivers typically call <b>WdfDmaTransactionInitialize</b> from within an <a href="wdf.request_handlers">I/O queue event callback function</a>. </p>

<p>If you are creating a DMA transaction that is based on information that a framework request object contains, your driver should call <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioninitializeusingrequest.md">WdfDmaTransactionInitializeUsingRequest</a>.  If you are creating a DMA transaction that is not based on a request object, use either  <b>WdfDmaTransactionInitialize</b> or <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioninitializeusingoffset.md">WdfDmaTransactionInitializeUsingOffset</a>.</p>

<p>The driver can specify an MDL chain in the <i>Mdl</i> parameter of this method. An MDL chain is a sequence of MDL structures that the driver chained together using the <b>Next</b> member of the MDL structure. In framework versions prior to 1.11, only scatter/gather DMA transfers can use MDL chains.  Starting in version 1.11, if the driver is using  DMA version 3, single-packet transfers can also use chained MDLs.</p>

<p>If the buffer that the driver specifies is larger than the maximum transfer length that your driver specified when it called <a href="..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablercreate.md">WdfDmaEnablerCreate</a> or <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionsetmaximumlength.md">WdfDmaTransactionSetMaximumLength</a>, the framework breaks the transaction into multiple <a href="wdf.dma_transactions_and_dma_transfers">transfers</a>.  </p>

<p>For more information about DMA transactions, see <a href="wdf.creating_and_initializing_a_dma_transaction">Creating and Initializing a DMA Transaction</a>. </p>

<p>The following code example is from the <a href="http://go.microsoft.com/fwlink/p/?linkid=256157">PLX9x5x</a> sample driver. First, the example initializes a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure and creates a DMA transaction object. Next, it obtains an MDL that represents a received I/O request's input buffer, and it obtains the virtual address and length of the buffer. Finally, the example calls <b>WdfDmaTransactionInitialize</b> to initialize the transaction.</p>

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
<a href="devtest.kmdf_deferredrequestcompleted">DeferredRequestCompleted</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_mdlafterreqcompletedintioctla">MdlAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_mdlafterreqcompletedioctla">MdlAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_mdlafterreqcompletedreada">MdlAfterReqCompletedReadA</a>, <a href="devtest.kmdf_mdlafterreqcompletedwritea">MdlAfterReqCompletedWriteA</a>, <a href="devtest.kmdf_requestcompleted">RequestCompleted</a>, <a href="devtest.kmdf_requestcompletedlocal">RequestCompletedLocal</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evtprogramdma">EvtProgramDma</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-mmgetmdlbytecount.md">MmGetMdlByteCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554539">MmGetMdlVirtualAddress</a>
</dt>
<dt>
<a href="..\wdfdmaenabler\ne-wdfdmaenabler--wdf-dma-direction.md">WDF_DMA_DIRECTION</a>
</dt>
<dt>
<a href="..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablersetmaximumscattergatherelements.md">WdfDmaEnablerSetMaximumScatterGatherElements</a>
</dt>
<dt>
<a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioncreate.md">WdfDmaTransactionCreate</a>
</dt>
<dt>
<a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionexecute.md">WdfDmaTransactionExecute</a>
</dt>
<dt>
<a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioninitializeusingrequest.md">WdfDmaTransactionInitializeUsingRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionInitialize method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
