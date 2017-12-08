---
UID: NF.wdfdmatransaction.WdfDmaTransactionSetChannelConfigurationCallback
title: WdfDmaTransactionSetChannelConfigurationCallback function
author: windows-driver-content
description: The WdfDmaTransactionSetChannelConfigurationCallback method registers a channel configuration event callback function for a system-mode DMA transaction.
old-location: wdf\wdfdmatransactionsetchannelconfigurationcallback.htm
old-project: wdf
ms.assetid: B38BD937-5027-4EED-9ECA-3333F56DFFA8
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDmaTransactionSetChannelConfigurationCallback
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
req.alt-api: WdfDmaTransactionSetChannelConfigurationCallback
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
req.product: Windows 10 or later.
---

# WdfDmaTransactionSetChannelConfigurationCallback function



## -description
<p class="CCE_Message">[Applies to KMDF only]

   The <b>WdfDmaTransactionSetChannelConfigurationCallback</b> method registers a channel configuration event callback function for a system-mode DMA transaction.


## -syntax

````
void WdfDmaTransactionSetChannelConfigurationCallback(
  _In_     WDFDMATRANSACTION                             DmaTransaction,
  _In_opt_ PFN_WDF_DMA_TRANSACTION_CONFIGURE_DMA_CHANNEL ConfigureRoutine,
  _In_opt_ PVOID                                         ConfigureContext
);
````


## -parameters

### -param DmaTransaction [in]

A handle to an initialized DMA transaction object for which to set or clear the channel configuration callback.

### -param ConfigureRoutine [in, optional]

A pointer to the driver's <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt_wdf_dma_transaction_configure_dma_channel.md">EvtDmaTransactionConfigureDmaChannel</a> event callback function, or NULL to clear it.



### -param ConfigureContext [in, optional]

A pointer to a buffer containing the context to be provided to the driver's <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt_wdf_dma_transaction_configure_dma_channel.md">EvtDmaTransactionConfigureDmaChannel</a> event callback function, or NULL.

## -returns
This method does not return a value.

## -remarks
This method allows the driver to customize the adapter configuration before programming the system DMA controller.

Typically from within an <a href="wdf.request_handlers">I/O queue event callback function</a>, a driver performs the following steps, in this order:

If the driver has specified an <a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt_wdf_dma_transaction_configure_dma_channel.md">EvtDmaTransactionConfigureDmaChannel</a> event callback function by calling <b>WdfDmaTransactionSetChannelConfigurationCallback</b> and the driver subsequently calls <a href="wdf.wdfdmatransactionrelease">WdfDmaTransactionRelease</a>, the callback is cleared.

<b>WdfDmaTransactionSetChannelConfigurationCallback</b> must be used with a DMA enabler that specifies a system-mode DMA profile.

If your driver calls this method on an operating system earlier than Windows 8, <a href="wdf.using_kmdf_verifier">the framework's verifier</a> reports an error.

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
Minimum support
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.11
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdmatransaction\nc-wdfdmatransaction-evt_wdf_dma_transaction_configure_dma_channel.md">EvtDmaTransactionConfigureDmaChannel</a>
</dt>
<dt>
<a href="wdf.wdfdmatransactionrelease">WdfDmaTransactionRelease</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionSetChannelConfigurationCallback method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
