---
UID: NN.dbgeng.IDebugPlmClient3
title: IDebugPlmClient3
author: windows-driver-content
description: This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location: debugger\idebugplmclient3.htm
old-project: debugger
ms.assetid: 5B0580FF-0829-406A-B511-C0CD91A08D5F
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
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
<a href="debugger.idebugplmclient3_activateanddebugplmbgtaskwide">ActivateAndDebugPlmBgTaskWide</a>
</td>
<td align="left" width="63%">
<p>    Launches and attaches to a Process Lifecycle Management (PLM) background task.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_disableplmpackagedebugwide">DisablePlmPackageDebugWide</a>
</td>
<td align="left" width="63%">
<p>Disables a Process Lifecycle Management (PLM) package debug.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_enableplmpackagedebugwide">EnablePlmPackageDebugWide</a>
</td>
<td align="left" width="63%">
<p>Enables a Process Lifecycle Management (PLM) package debug.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_launchanddebugplmappwide">LaunchAndDebugPlmAppWide</a>
</td>
<td align="left" width="63%">
<p>    Launches and attaches to a Process Lifecycle Management (PLM) application. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_queryplmpackagelist">QueryPlmPackageList</a>
</td>
<td align="left" width="63%">
<p>Query a Process Lifecycle Management (PLM) package list.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_queryplmpackagewide">QueryPlmPackageWide</a>
</td>
<td align="left" width="63%">
<p>Query a Process Lifecycle Management (PLM) package.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_resumeplmpackagewide">ResumePlmPackageWide</a>
</td>
<td align="left" width="63%">
<p>Resumes a Process Lifecycle Management (PLM) package.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_suspendplmpackagewide">SuspendPlmPackageWide</a>
</td>
<td align="left" width="63%">
<p>Suspends a Process Lifecycle Management (PLM) package.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_terminateplmpackagewide">TerminatePlmPackageWide</a>
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