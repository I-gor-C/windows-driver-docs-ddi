---
UID: NF.wdfdmatransaction.WdfDmaTransactionFreeResources
title: WdfDmaTransactionFreeResources
author: windows-driver-content
description: The WdfDmaTransactionFreeResources method releases DMA resources that the driver previously allocated by calling WdfDmaTransactionAllocateResources.
old-location: wdf\wdfdmatransactionfreeresources.htm
old-project: wdf
ms.assetid: F35F80E7-E1B6-4219-96AF-687E0014CCB3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDmaTransactionFreeResources
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdmatransaction.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WdfDmaTransactionFreeResources
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

# WdfDmaTransactionFreeResources function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDmaTransactionFreeResources</b> method releases DMA resources that the driver previously allocated by calling <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionallocateresources.md">WdfDmaTransactionAllocateResources</a>.</p>


## -syntax

````
void WdfDmaTransactionFreeResources(
  _In_ WDFDMATRANSACTION DmaTransaction
);
````


## -parameters
<dl>

### -param DmaTransaction [in]

<dd>
<p>A handle to the DMA transaction object that the driver provided in a previous call to <a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionallocateresources.md">WdfDmaTransactionAllocateResources</a>.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p><b>WdfDmaTransactionFreeResources</b> must be used with a DMA enabler that specifies a packet or system profile.</p>

<p>On operating systems earlier than Windows 8, <b>WdfDmaTransactionFreeResources</b> must be used with an enabler that specifies a single-packet DMA enabler.  Starting with  Windows 8, <b>WdfDmaTransactionFreeResources</b> can also be used with an enabler that specifies a system-mode DMA enabler.</p>

<p>  When called with a scatter/gather DMA enabler, <b>WdfDmaTransactionFreeResources</b> causes a verifier bug check.</p>

<p>

The driver's call to <b>WdfDmaTransactionFreeResources</b> may cause the framework to call <a href="wdf.evtprogramdma">EvtProgramDma</a> or <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-reserve-dma.md">EvtReserveDma</a> immediately.</p>

<p>For more information about system-mode DMA, see <a href="wdf.supporting_system-mode_dma">Supporting System-Mode DMA</a>.
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionallocateresources.md">WdfDmaTransactionAllocateResources</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionFreeResources method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
