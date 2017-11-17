---
UID: NN.wudfddi.IWDFIoTarget2~r1
title: IWDFIoTarget2
author: windows-driver-content
description: To obtain the IWDFIoTarget2 interface, drivers call IWDFIoTarget::QueryInterface.
old-location: wdf\iwdfiotarget2.htm
ms.assetid: 52ce1c63-b2cf-4eda-b056-4f1f999110c5
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFIoTarget2
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IWDFIoTarget2 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>To obtain the <b>IWDFIoTarget2</b> interface, drivers call <b>IWDFIoTarget::QueryInterface</b>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFIoTarget2</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a>. <b>IWDFIoTarget2</b> also has these types of members:</p>

<p>The <b>IWDFIoTarget2</b> interface has these methods.</p>

<p>The <a href="https://msdn.microsoft.com/28509e28-0e81-4531-947c-9ce452564682">FormatRequestForFlush</a> method builds an I/O request for a flush operation but does not send the request to an I/O target.</p>

<p>The <a href="https://msdn.microsoft.com/24ce2918-1d9f-41eb-add1-a50b888f0a99">FormatRequestForQueryInformation</a> method formats an I/O request to obtain information about a file, but it does not send the request to an I/O target.</p>

<p>The <a href="https://msdn.microsoft.com/2bfdc5c6-da5a-43c1-9165-02d6c448a690">FormatRequestForSetInformation</a> method formats an I/O request to set information about a file, but it does not send the request to an I/O target.</p>

<p> </p>

## -members
<p>The <b>IWDFIoTarget2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559182">IWDFIoTarget2::FormatRequestForFlush</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/28509e28-0e81-4531-947c-9ce452564682">FormatRequestForFlush</a> method builds an I/O request for a flush operation but does not send the request to an I/O target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559184">IWDFIoTarget2::FormatRequestForQueryInformation</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/24ce2918-1d9f-41eb-add1-a50b888f0a99">FormatRequestForQueryInformation</a> method formats an I/O request to obtain information about a file, but it does not send the request to an I/O target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559191">IWDFIoTarget2::FormatRequestForSetInformation</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/2bfdc5c6-da5a-43c1-9165-02d6c448a690">FormatRequestForSetInformation</a> method formats an I/O request to set information about a file, but it does not send the request to an I/O target.</p>
</td>
</tr>
</table><p>The <a href="https://msdn.microsoft.com/28509e28-0e81-4531-947c-9ce452564682">FormatRequestForFlush</a> method builds an I/O request for a flush operation but does not send the request to an I/O target.</p>

<p>The <a href="https://msdn.microsoft.com/24ce2918-1d9f-41eb-add1-a50b888f0a99">FormatRequestForQueryInformation</a> method formats an I/O request to obtain information about a file, but it does not send the request to an I/O target.</p>

<p>The <a href="https://msdn.microsoft.com/2bfdc5c6-da5a-43c1-9165-02d6c448a690">FormatRequestForSetInformation</a> method formats an I/O request to set information about a file, but it does not send the request to an I/O target.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>