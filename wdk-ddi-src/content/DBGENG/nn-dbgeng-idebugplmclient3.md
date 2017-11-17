---
UID: NN.dbgeng.IDebugPlmClient3
title: IDebugPlmClient3
author: windows-driver-content
description: This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location: debugger\idebugplmclient3.htm
ms.assetid: 5B0580FF-0829-406A-B511-C0CD91A08D5F
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugPlmClient3
req.alt-loc: dbgeng.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
req.iface: IDebugSystemObjects4
---

# IDebugPlmClient3 interface



## -description
<p>This interface supports Process Lifecycle Management (PLM) for the debug client.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugPlmClient3</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugPlmClient3</b> also has these types of members:</p>

<p>The <b>IDebugPlmClient3</b> interface has these methods.</p>

<p>    Launches and attaches to a Process Lifecycle Management (PLM) background task.</p>

<p>Disables a Process Lifecycle Management (PLM) package debug.</p>

<p>Enables a Process Lifecycle Management (PLM) package debug.</p>

<p>    Launches and attaches to a Process Lifecycle Management (PLM) application. </p>

<p>Query a Process Lifecycle Management (PLM) package list.</p>

<p>Query a Process Lifecycle Management (PLM) package.</p>

<p>Resumes a Process Lifecycle Management (PLM) package.</p>

<p>Suspends a Process Lifecycle Management (PLM) package.</p>

<p>Ends a Process Lifecycle Management (PLM) package.</p>

<p> </p>

## -members
<p>The <b>IDebugPlmClient3</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/77358032-1777-46F4-BF16-5DFFAC15E672">ActivateAndDebugPlmBgTaskWide</a>
</td>
<td align="left" width="63%">
<p>    Launches and attaches to a Process Lifecycle Management (PLM) background task.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/23A5BAC2-E8F3-47FF-9B63-3FFF447C33B4">DisablePlmPackageDebugWide</a>
</td>
<td align="left" width="63%">
<p>Disables a Process Lifecycle Management (PLM) package debug.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/6373B8BD-264D-4D03-9FE9-F87E45D617EE">EnablePlmPackageDebugWide</a>
</td>
<td align="left" width="63%">
<p>Enables a Process Lifecycle Management (PLM) package debug.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/F3DD5912-46E5-43E5-A920-940FC8FCD83F">LaunchAndDebugPlmAppWide</a>
</td>
<td align="left" width="63%">
<p>    Launches and attaches to a Process Lifecycle Management (PLM) application. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/BAAAF09B-F39D-44E0-9409-1C98B0C6A56B">QueryPlmPackageList</a>
</td>
<td align="left" width="63%">
<p>Query a Process Lifecycle Management (PLM) package list.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/29BAAEF9-5B69-4723-BC23-A8B668E2A867">QueryPlmPackageWide</a>
</td>
<td align="left" width="63%">
<p>Query a Process Lifecycle Management (PLM) package.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/CC69357E-425B-440B-93D0-918E8586D5DF">ResumePlmPackageWide</a>
</td>
<td align="left" width="63%">
<p>Resumes a Process Lifecycle Management (PLM) package.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/B887CCD2-0747-483E-A4CF-632471AB19A2">SuspendPlmPackageWide</a>
</td>
<td align="left" width="63%">
<p>Suspends a Process Lifecycle Management (PLM) package.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/EBEEF2C7-AD2E-4BE5-B20C-D4E148F1454C">TerminatePlmPackageWide</a>
</td>
<td align="left" width="63%">
<p>Ends a Process Lifecycle Management (PLM) package.</p>
</td>
</tr>
</table><p>    Launches and attaches to a Process Lifecycle Management (PLM) background task.</p>

<p>Disables a Process Lifecycle Management (PLM) package debug.</p>

<p>Enables a Process Lifecycle Management (PLM) package debug.</p>

<p>    Launches and attaches to a Process Lifecycle Management (PLM) application. </p>

<p>Query a Process Lifecycle Management (PLM) package list.</p>

<p>Query a Process Lifecycle Management (PLM) package.</p>

<p>Resumes a Process Lifecycle Management (PLM) package.</p>

<p>Suspends a Process Lifecycle Management (PLM) package.</p>

<p>Ends a Process Lifecycle Management (PLM) package.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>