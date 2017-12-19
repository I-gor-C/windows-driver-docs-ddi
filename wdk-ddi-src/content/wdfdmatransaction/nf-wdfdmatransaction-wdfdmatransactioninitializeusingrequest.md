---
UID: NF.wdfdmatransaction.WdfDmaTransactionInitializeUsingRequest
title: WdfDmaTransactionInitializeUsingRequest function
author: windows-driver-content
description: The WdfDmaTransactionInitializeUsingRequest method initializes a specified DMA transaction by using the parameters of a specified I/O request.
old-location: wdf\wdfdmatransactioninitializeusingrequest.htm
old-project: wdf
ms.assetid: 5a59c1cc-b5a9-4e94-966d-9998a98d6ad2
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDmaTransactionInitializeUsingRequest
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
req.alt-api: WdfDmaTransactionInitializeUsingRequest
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DeferredRequestCompleted, DriverCreate, KmdfIrql, KmdfIrql2, RequestCompleted, RequestCompletedLocal
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDmaTransactionInitializeUsingRequest function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDmaTransactionInitializeUsingRequest</b> method initializes a specified DMA transaction by using the parameters of a specified I/O request. 



## -syntax

````
NTSTATUS WdfDmaTransactionInitializeUsingRequest(
  _In_ WDFDMATRANSACTION   DmaTransaction,
  _In_ WDFREQUEST          Request,
  _In_ PFN_WDF_PROGRAM_DMA EvtProgramDmaFunction,
  _In_ WDF_DMA_DIRECTION   DmaDirection
);
````


## -parameters

### -param DmaTransaction [in]

A handle to a DMA transaction object that the driver obtained from a previous call to <a href="wdf.wdfdmatransactioncreate">WdfDmaTransactionCreate</a>.


### -param Request [in]

A handle to a framework request object.


### -param EvtProgramDmaFunction [in]

A pointer to the driver's <a href="wdf.evtprogramdma">EvtProgramDma</a> event callback function. 


### -param DmaDirection [in]

A <a href="wdf.wdf_dma_direction">WDF_DMA_DIRECTION</a>-typed value that specifies the direction of the DMA transfer.


## -returns
<b>WdfDmaTransactionInitializeUsingRequest</b> returns STATUS_SUCCESS if the operation succeeds.  Otherwise, the method might return one of the values described in the Return values section of <a href="wdf.wdfdmatransactioninitialize">WdfDmaTransactionInitialize</a>.

This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
The <b>WdfDmaTransactionInitializeUsingRequest</b> method prepares a DMA operation for execution, by performing initialization operations such as setting up a transaction's scatter/gather list. After your driver calls <b>WdfDmaTransactionInitializeUsingRequest</b>, the driver must call <a href="wdf.wdfdmatransactionexecute">WdfDmaTransactionExecute</a>.

The driver can call <a href="wdf.wdfrequestgetparameters">WdfRequestGetParameters</a> to obtain a request's type. The value that the driver specifies for the <i>DmaDirection</i> parameter must be appropriate for the request type, as follows:

 The <i>DmaDirection</i> value must be <b>WdfDmaDirectionWriteToDevice</b> if: 

 The request type is <b>WdfRequestTypeWrite</b>

The request type is <b>WdfRequestTypeDeviceControl</b> or <b>WdfRequestTypeDeviceControlInternal</b> and the I/O control code specifies a transfer type of METHOD_IN_DIRECT  

For more information about transfer types for I/O control codes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543023">Defining I/O Control Codes</a>.

Framework-based drivers typically call <b>WdfDmaTransactionInitializeUsingRequest</b> from within an <a href="wdf.request_handlers">I/O queue event callback function</a>. 

Your driver should call <b>WdfDmaTransactionInitializeUsingRequest</b> if you are creating a DMA transaction that is based on information that a framework request object contains. Use <a href="wdf.wdfdmatransactioninitialize">WdfDmaTransactionInitialize</a> if you are creating a DMA transaction that is not based on a request object.

If the buffer that the request object describes is larger than the maximum transfer length that your driver specified when it called <a href="wdf.wdfdmaenablercreate">WdfDmaEnablerCreate</a> or <a href="wdf.wdfdmatransactionsetmaximumlength">WdfDmaTransactionSetMaximumLength</a>, the framework breaks the transaction into multiple <a href="wdf.dma_transactions_and_dma_transfers">transfers</a>.  

For more information about DMA transactions, see <a href="wdf.creating_and_initializing_a_dma_transaction">Creating and Initializing a DMA Transaction</a>. 

For a code example that uses <b>WdfDmaTransactionInitializeUsingRequest</b>, see <a href="wdf.wdfdmatransactionexecute">WdfDmaTransactionExecute</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdmatransaction.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_deferredrequestcompleted">DeferredRequestCompleted</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_requestcompleted">RequestCompleted</a>, <a href="devtest.kmdf_requestcompletedlocal">RequestCompletedLocal</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evtprogramdma">EvtProgramDma</a>
</dt>
<dt>
<a href="wdf.wdf_dma_direction">WDF_DMA_DIRECTION</a>
</dt>
<dt>
<a href="wdf.wdfdmaenablersetmaximumscattergatherelements">WdfDmaEnablerSetMaximumScatterGatherElements</a>
</dt>
<dt>
<a href="wdf.wdfdmatransactioncreate">WdfDmaTransactionCreate</a>
</dt>
<dt>
<a href="wdf.wdfdmatransactionexecute">WdfDmaTransactionExecute</a>
</dt>
<dt>
<a href="wdf.wdfdmatransactioninitialize">WdfDmaTransactionInitialize</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionInitializeUsingRequest method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

