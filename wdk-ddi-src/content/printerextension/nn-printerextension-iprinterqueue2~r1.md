---
UID: NN.printerextension.IPrinterQueue2~r1
title: IPrinterQueue2
author: windows-driver-content
description: Represents a single printer queue.
old-location: print\iprinterqueue2.htm
old-project: print
ms.assetid: 06459A1F-A14B-43BA-9771-47205CC3F388
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterQueue2
req.alt-loc: Printerextension.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# IPrinterQueue2 interface



## -description
<p>Represents a single printer queue. </p>
<p>This interface extends <a href="https://msdn.microsoft.com/library/windows/hardware/hh439635">IPrinterQueue</a> and allows a user to manage print jobs and device maintenance from within a UWP  device app for printers, or from a printer extension.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrinterQueue2</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/hh439635">IPrinterQueue</a>. <b>IPrinterQueue2</b> also has these types of members:</p>

<p>The <b>IPrinterQueue2</b> interface has these methods.</p>

<p>Retrieves an <a href="https://msdn.microsoft.com/library/windows/hardware/dn265392">IPrinterQueueView</a> object, and initializes the object with the range of jobs to be monitored.</p>

<p>Uses an XML string value to send a Bidi Set request as an asynchronous operation.</p>

<p> </p>

## -members
<p>The <b>IPrinterQueue2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265390">GetPrinterQueueView</a>
</td>
<td align="left" width="63%">
<p>Retrieves an <a href="https://msdn.microsoft.com/library/windows/hardware/dn265392">IPrinterQueueView</a> object, and initializes the object with the range of jobs to be monitored.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265391">SendBidiSetRequestAsync</a>
</td>
<td align="left" width="63%">
<p>Uses an XML string value to send a Bidi Set request as an asynchronous operation.</p>
</td>
</tr>
</table><p>Retrieves an <a href="https://msdn.microsoft.com/library/windows/hardware/dn265392">IPrinterQueueView</a> object, and initializes the object with the range of jobs to be monitored.</p>

<p>Uses an XML string value to send a Bidi Set request as an asynchronous operation.</p>

<p> </p>

## -remarks
<p><b>IPrinterQueue2</b> also helps to make it possible to perform device maintenance and job management from a UWP  device app or from a printer extension. For more information, see <a href="NULL">Device Maintenance</a> and <a href="NULL">Job Management</a>.</p>

<p><b>IPrinterQueue2</b> also helps to make it possible to perform device maintenance and job management from a UWP  device app or from a printer extension. For more information, see <a href="NULL">Device Maintenance</a> and <a href="NULL">Job Management</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">Device Maintenance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439635">IPrinterQueue</a>
</dt>
<dt>
<a href="NULL">Job Management</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterQueue2 interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
