---
UID: NF.wdfdmatransaction.WdfDmaTransactionGetTransferInfo
title: WdfDmaTransactionGetTransferInfo
author: windows-driver-content
description: The WdfDmaTransactionGetTransferInfo method returns the number of map registers and scatter/gather list entries required for an initialized DMA transaction.
old-location: wdf\wdfdmatransactiongettransferinfo.htm
old-project: wdf
ms.assetid: 9EE04529-D322-4498-B802-BB6A53FBC716
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDmaTransactionGetTransferInfo
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
req.alt-api: WdfDmaTransactionGetTransferInfo
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

# WdfDmaTransactionGetTransferInfo function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDmaTransactionGetTransferInfo</b> method returns the number of map registers and scatter/gather list entries required for an initialized DMA transaction.</p>


## -syntax

````
void WdfDmaTransactionGetTransferInfo(
  _In_      WDFDMATRANSACTION DmaTransaction,
  _Out_opt_ ULONG             *MapRegisterCount,
  _Out_opt_ ULONG             *ScatterGatherElementCount
);
````


## -parameters
<dl>

### -param <i>DmaTransaction</i> [in]

<dd>
<p>A handle to an initialized DMA transaction object.</p>
</dd>

### -param <i>MapRegisterCount</i> [out, optional]

<dd>
<p>A caller-supplied location that, on return, contains the number of map registers required for the specified transaction. This parameter is optional and can be NULL.</p>
</dd>

### -param <i>ScatterGatherElementCount</i> [out, optional]

<dd>
<p>A caller-supplied location that, on return, contains the number of scatter/gather elements required for the specified transaction. This parameter is optional and can be NULL.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>The driver might call <b>WdfDmaTransactionGetTransferInfo</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451123">WdfDmaTransactionAllocateResources</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff547062">WdfDmaTransactionExecute</a>.</p>

<p>When using DMA version 3, this method returns an accurate count of the number of map registers needed. When using earlier DMA versions, this method assumes that each page requires a map register.</p>

<p>The driver might call <b>WdfDmaTransactionGetTransferInfo</b> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451123">WdfDmaTransactionAllocateResources</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff547062">WdfDmaTransactionExecute</a>.</p>

<p>When using DMA version 3, this method returns an accurate count of the number of map registers needed. When using earlier DMA versions, this method assumes that each page requires a map register.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451123">WdfDmaTransactionAllocateResources</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547062">WdfDmaTransactionExecute</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionGetTransferInfo method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
