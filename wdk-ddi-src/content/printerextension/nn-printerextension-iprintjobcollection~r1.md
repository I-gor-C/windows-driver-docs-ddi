---
UID: NN.printerextension.IPrintJobCollection~r1
title: IPrintJobCollection
author: windows-driver-content
description: This interfaces provides an enumeration of the jobs in the print queue.
old-location: print\iprintjobcollection.htm
old-project: print
ms.assetid: 757328A6-DD2C-4057-820B-39EB83277194
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
req.alt-api: IPrintJobCollection
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

# IPrintJobCollection interface



## -description
<p>This interfaces provides an enumeration of the jobs in the print queue.</p>
<p>The enumerated list of jobs represents a snapshot of the current job status.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintJobCollection</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPrintJobCollection</b> also has these types of members:</p>

<p>The <b>IPrintJobCollection</b> interface has these methods.</p>

<p>Gets a pointer to an <a href="..\printerextension\nn-printerextension-iprintjob.md">IPrintJob</a> object.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintJobCollection</b> interface has these properties.</p>

<p>
<a href="print.iprintjobcollection_count">Count</a>
</p>

<p>Read-only</p>

<p>Gets the number of jobs in the print queue.</p>

<p>
<a href="print.iprintjobcollection_newenum">NewEnum</a>
</p>

<p>Read-only</p>

<p>Gets a pointer to the enumerants of <b>IPrintJobCollection</b> objects.</p>

<p> </p>

## -members
<p>The <b>IPrintJobCollection</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.iprintjobcollection_getat">GetAt</a>
</td>
<td align="left" width="63%">
<p>Gets a pointer to an <a href="..\printerextension\nn-printerextension-iprintjob.md">IPrintJob</a> object.</p>
</td>
</tr>
</table><p>Gets a pointer to an <a href="..\printerextension\nn-printerextension-iprintjob.md">IPrintJob</a> object.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintJobCollection</b> interface has these properties.</p><table class="members" id="memberListProperties">
<tr>
<th align="left" width="27%">Property</th>
<th align="left" width="10%">Access type</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="print.iprintjobcollection_count">Count</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the number of jobs in the print queue.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="print.iprintjobcollection_newenum">NewEnum</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets a pointer to the enumerants of <b>IPrintJobCollection</b> objects.</p>
</td>
</tr>
</table><p>
<a href="print.iprintjobcollection_count">Count</a>
</p>

<p>Read-only</p>

<p>Gets the number of jobs in the print queue.</p>

<p>
<a href="print.iprintjobcollection_newenum">NewEnum</a>
</p>

<p>Read-only</p>

<p>Gets a pointer to the enumerants of <b>IPrintJobCollection</b> objects.</p>

<p> </p>

## -remarks
<p>The order of print jobs in the enumerated list is the same as the order provided by <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd162625(v=vs.85).aspx">EnumJobs</a>, which is the actual print queue order.</p>

<p><b>IPrintJobCollection</b> also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see <a href="NULL">Job Management</a>.</p>

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
<dt><a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd162625(v=vs.85).aspx">EnumJobs</a></dt>
<dt>
<a href="NULL">Job Management</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintJobCollection interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
