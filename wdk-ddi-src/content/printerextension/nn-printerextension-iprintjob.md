---
UID: NN.printerextension.IPrintJob
title: IPrintJob
author: windows-driver-content
description: Contains properties that represent a print job.
old-location: print\iprintjob.htm
old-project: print
ms.assetid: 068E53EC-26B8-48E7-A605-081709C94043
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
req.alt-api: IPrintJob
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

# IPrintJob interface



## -description
<p>Contains properties that represent a print job.</p>
<p>This interface also provides a method that allows a print job to be cancelled.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintJob</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPrintJob</b> also has these types of members:</p>

<p>The <b>IPrintJob</b> interface has these methods.</p>

<p>Requests the cancellation of a print job.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintJob</b> interface has these properties.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn895599">Id</a>
</p>

<p>Read-only</p>

<p>Gets the print job identifier (ID).</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971602">Name</a>
</p>

<p>Read-only</p>

<p>Gets the name of the print job.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265403">PrintedPages</a>
</p>

<p>Read-only</p>

<p>Gets the number of pages that have been printed.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265407">Status</a>
</p>

<p>Read-only</p>

<p>Gets the current status of the print job.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265410">SubmissionTime</a>
</p>

<p>Read-only</p>

<p>Gets the submission time, in the “DATE” format, provided in the user’s local time (not in the UTC format that is provided by the spooler).</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265411">TotalPages</a>
</p>

<p>Read-only</p>

<p>Gets the total number of pages that the document contains.</p>

<p> </p>

## -members
<p>The <b>IPrintJob</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265404">RequestCancel</a>
</td>
<td align="left" width="63%">
<p>Requests the cancellation of a print job.</p>
</td>
</tr>
</table><p>Requests the cancellation of a print job.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintJob</b> interface has these properties.</p><table class="members" id="memberListProperties">
<tr>
<th align="left" width="27%">Property</th>
<th align="left" width="10%">Access type</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn895599">Id</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the print job identifier (ID).</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971602">Name</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the name of the print job.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265403">PrintedPages</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the number of pages that have been printed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265407">Status</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the current status of the print job.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265410">SubmissionTime</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the submission time, in the “DATE” format, provided in the user’s local time (not in the UTC format that is provided by the spooler).</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="27%" xml:space="preserve">
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265411">TotalPages</a>
</p>
</td>
<td align="left" width="10%">
<p>Read-only</p>
</td>
<td align="left" width="63%">
<p>Gets the total number of pages that the document contains.</p>
</td>
</tr>
</table><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn895599">Id</a>
</p>

<p>Read-only</p>

<p>Gets the print job identifier (ID).</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh971602">Name</a>
</p>

<p>Read-only</p>

<p>Gets the name of the print job.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265403">PrintedPages</a>
</p>

<p>Read-only</p>

<p>Gets the number of pages that have been printed.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265407">Status</a>
</p>

<p>Read-only</p>

<p>Gets the current status of the print job.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265410">SubmissionTime</a>
</p>

<p>Read-only</p>

<p>Gets the submission time, in the “DATE” format, provided in the user’s local time (not in the UTC format that is provided by the spooler).</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265411">TotalPages</a>
</p>

<p>Read-only</p>

<p>Gets the total number of pages that the document contains.</p>

<p> </p>

## -remarks
<p>The <b>IPrintJob</b> interface provides a wrapper around select properties of the spooler’s <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019(v=vs.85).aspx">JOB_INFO_1</a> structure.</p>

<p><b>IPrintJob</b> also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see <a href="NULL">Job Management</a>.</p>

<p>The <b>IPrintJob</b> interface provides a wrapper around select properties of the spooler’s <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019(v=vs.85).aspx">JOB_INFO_1</a> structure.</p>

<p><b>IPrintJob</b> also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see <a href="NULL">Job Management</a>.</p>

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
<a href="NULL">Job Management</a>
</dt>
<dt><a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019(v=vs.85).aspx">JOB_INFO_1</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintJob interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
