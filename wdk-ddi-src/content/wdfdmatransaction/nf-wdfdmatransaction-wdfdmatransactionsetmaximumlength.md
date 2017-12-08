---
UID: NF.wdfdmatransaction.WdfDmaTransactionSetMaximumLength
title: WdfDmaTransactionSetMaximumLength function
author: windows-driver-content
description: The WdfDmaTransactionSetMaximumLength method sets the maximum length for the DMA transfers that are associated with a specified DMA transaction.
old-location: wdf\wdfdmatransactionsetmaximumlength.htm
old-project: wdf
ms.assetid: b195c6df-79c4-427d-b722-309f43a4e150
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDmaTransactionSetMaximumLength
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
req.alt-api: WdfDmaTransactionSetMaximumLength
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

# WdfDmaTransactionSetMaximumLength function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfDmaTransactionSetMaximumLength</b> method sets the maximum length for the DMA transfers that are associated with a specified DMA transaction.


## -syntax

````
VOID WdfDmaTransactionSetMaximumLength(
  _In_ WDFDMATRANSACTION DmaTransaction,
  _In_ size_t            MaximumLength
);
````


## -parameters

### -param DmaTransaction [in]

A handle to a DMA transaction object that the driver obtained from a previous call to <a href="wdf.wdfdmatransactioncreate">WdfDmaTransactionCreate</a>.

### -param MaximumLength [in]

The maximum size, in bytes, that the device can handle in a single DMA transfer operation. If your driver must run on versions of the Microsoft Windows operating systems that support a maximum of 16 <a href="https://msdn.microsoft.com/library/windows/hardware/ff554406">map registers</a>, <i>MaximumLength</i> must be less than 65536.
The <i>MaximumLength</i> value applies only to the specified DMA transaction, as follows:
<ul>
<li>
If the specified value is less than the default value that the driver specified in its <a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a> structure, the specified value overrides the default value. 
</li>
<li>
If the specified value is greater than the default value, the specified value is ignored.
</li>
</ul>

## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
Your driver  must initialize the DMA transaction before calling <b>WdfDmaTransactionSetMaximumLength</b>.

For information about initializing a DMA transaction, see <a href="wdf.creating_and_initializing_a_dma_transaction">Creating and Initializing a DMA Transaction</a>.

The following code example sets the maximum transfer length to a driver-defined value, for a specified DMA transaction.

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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdmatransactioncreate">WdfDmaTransactionCreate</a>
</dt>
<dt>
<a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionSetMaximumLength method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>