---
UID: NC.wdfdmatransaction.EVT_WDF_RESERVE_DMA
title: EVT_WDF_RESERVE_DMA
author: windows-driver-content
description: The EvtReserveDma event callback function is called when the framework has reserved resources to execute and release a transaction. Reserved resources include map registers and the WDM DMA adapter's lock.
old-location: wdf\evtreservedma.htm
old-project: wdf
ms.assetid: 3663EF19-5F16-43D1-BFBC-28280E28D4DE
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_DMA_SYSTEM_PROFILE_CONFIG, WDF_DMA_SYSTEM_PROFILE_CONFIG, *PWDF_DMA_SYSTEM_PROFILE_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfdmatransaction.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: EvtReserveDma
req.alt-loc: WdfDmaTransaction.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_RESERVE_DMA callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>
   The 
  <i>EvtReserveDma</i> event callback function is called when the framework has reserved resources to execute and release a transaction. Reserved resources include map registers and the WDM DMA adapter's lock.</p>


## -prototype

````
EVT_WDF_RESERVE_DMA EvtReserveDma;

VOID EvtReserveDma(
  _In_ WDFDMATRANSACTION DmaTransaction,
  _In_ PVOID             Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>DmaTransaction</i> [in]

<dd>
<p>A handle to the DMA transaction object that represents the transaction to which DMA resources were assigned.</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>The context pointer that the driver specified in a previous call to <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionallocateresources.md">WdfDmaTransactionAllocateResources</a>.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>Drivers register an <i>EvtReserveDma</i> event callback function by calling <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionallocateresources.md">WdfDmaTransactionAllocateResources</a>.</p>

<p>The framework calls a driver's <i>EvtReserveDma</i> event callback function when DMA resources have been assigned for exclusive use with the associated transaction object. The driver can initialize and execute the transaction multiple times while holding this reservation.</p>

<p>A driver typically initializes and then initiates the transaction from within its <i>EvtReserveDma</i> event callback function. For more information about the reservation sequence, see <a href="wdf.reserving_dma_resources">Reserving DMA Resources</a>.</p>

<p>  

The driver may call <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionfreeresources.md">WdfDmaTransactionFreeResources</a> from within <i>EvtReserveDma</i>.
</p>

<p>On operating systems earlier than Windows 8, <i>EvtReserveDma</i> must be used with an enabler that specifies a packet-mode DMA enabler.  Starting with  Windows 8, <i>EvtReserveDma</i> can also be used with an enabler that specifies a system-mode DMA enabler.</p>

<p>To define an <i>EvtReserveDma</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtReserveDma</i> callback function that is named <i>MyReserveDma</i>, use the <b>EVT_WDF_RESERVE_DMA</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows.</p>

<p>The <b>EVT_WDF_RESERVE_DMA</b> function type is defined in the WdfDmaTransaction.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_RESERVE_DMA</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<dt>WdfDmaTransaction.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionallocateresources.md">WdfDmaTransactionAllocateResources</a>
</dt>
<dt>
<a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionfreeresources.md">WdfDmaTransactionFreeResources</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_RESERVE_DMA callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
