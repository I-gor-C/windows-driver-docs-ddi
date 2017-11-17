---
UID: NF.wdfdmatransaction.WdfDmaTransactionWdmGetTransferContext
title: WdfDmaTransactionWdmGetTransferContext
author: windows-driver-content
description: The WdfDmaTransactionWdmGetTransferContext method retrieves the WDM transfer context that is associated with a DMA transaction.
old-location: wdf\wdfdmatransactionwdmgettransfercontext.htm
ms.assetid: EB156381-FC0E-40A3-A4AF-341AE70B97FF
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdmatransaction.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WdfDmaTransactionWdmGetTransferContext
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
ms.keywords: WdfDmaTransactionWdmGetTransferContext
req.iface: 
req.product: Windows 10 or later.
---

# WdfDmaTransactionWdmGetTransferContext function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>
   The <b>WdfDmaTransactionWdmGetTransferContext</b> method retrieves the WDM transfer context that is associated with a DMA transaction.</p>


## -syntax

````
PVOID WdfDmaTransactionWdmGetTransferContext(
  _In_ WDFDMATRANSACTION DmaTransaction
);
````


## -parameters
<dl>

### -param <i>DmaTransaction</i> [in]

<dd>
<p>A handle to an initialized DMA transaction object from which to retrieve the transfer context.</p>
</dd>
</dl>

## -returns
<p>A pointer to the DMA transfer context (PTRANSFER_CONTEXT) associated with the transaction.</p>

## -remarks
<p>The DMA transfer context for a transaction is allocated when the driver creates the transaction.</p>

<p><b>WdfDmaTransactionWdmGetTransferContext</b> must be used with a DMA enabler that uses DMA version 3. To select version 3, set the <b>WdmDmaVersionOverride</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> to 3.</p>

<p>Your driver can use the DMA transfer context to call the following WDM DMA library routines directly:</p>

<p>You must initialize the DMA transaction before calling <b>WdfDmaTransactionWdmGetTransferContext</b>.</p>

<p>The DMA transfer context for a transaction is allocated when the driver creates the transaction.</p>

<p><b>WdfDmaTransactionWdmGetTransferContext</b> must be used with a DMA enabler that uses DMA version 3. To select version 3, set the <b>WdmDmaVersionOverride</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> to 3.</p>

<p>Your driver can use the DMA transfer context to call the following WDM DMA library routines directly:</p>

<p>You must initialize the DMA transaction before calling <b>WdfDmaTransactionWdmGetTransferContext</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547027">WdfDmaTransactionCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionWdmGetTransferContext method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
