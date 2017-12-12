---
UID: NN.dbgeng.IDebugPlmClient3
title: IDebugPlmClient3
author: windows-driver-content
description: This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location: debugger\idebugplmclient3.htm
old-project: debugger
ms.assetid: 5B0580FF-0829-406A-B511-C0CD91A08D5F
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: DebugCreateEx
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
---

# IDebugPlmClient3 interface



## -description
This interface supports Process Lifecycle Management (PLM) for the debug client.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugPlmClient3</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugPlmClient3</b> also has these types of members:

The <b>IDebugPlmClient3</b> interface has these methods.

    Launches and attaches to a Process Lifecycle Management (PLM) background task.

Disables a Process Lifecycle Management (PLM) package debug.

Enables a Process Lifecycle Management (PLM) package debug.

    Launches and attaches to a Process Lifecycle Management (PLM) application. 

Query a Process Lifecycle Management (PLM) package list.

Query a Process Lifecycle Management (PLM) package.

Resumes a Process Lifecycle Management (PLM) package.

Suspends a Process Lifecycle Management (PLM) package.

Ends a Process Lifecycle Management (PLM) package.

 


## -members
The <b>IDebugPlmClient3</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_activateanddebugplmbgtaskwide">ActivateAndDebugPlmBgTaskWide</a>
</td>
<td align="left" width="63%">
    Launches and attaches to a Process Lifecycle Management (PLM) background task.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_disableplmpackagedebugwide">DisablePlmPackageDebugWide</a>
</td>
<td align="left" width="63%">
Disables a Process Lifecycle Management (PLM) package debug.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_enableplmpackagedebugwide">EnablePlmPackageDebugWide</a>
</td>
<td align="left" width="63%">
Enables a Process Lifecycle Management (PLM) package debug.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_launchanddebugplmappwide">LaunchAndDebugPlmAppWide</a>
</td>
<td align="left" width="63%">
    Launches and attaches to a Process Lifecycle Management (PLM) application. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_queryplmpackagelist">QueryPlmPackageList</a>
</td>
<td align="left" width="63%">
Query a Process Lifecycle Management (PLM) package list.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_queryplmpackagewide">QueryPlmPackageWide</a>
</td>
<td align="left" width="63%">
Query a Process Lifecycle Management (PLM) package.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_resumeplmpackagewide">ResumePlmPackageWide</a>
</td>
<td align="left" width="63%">
Resumes a Process Lifecycle Management (PLM) package.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_suspendplmpackagewide">SuspendPlmPackageWide</a>
</td>
<td align="left" width="63%">
Suspends a Process Lifecycle Management (PLM) package.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient3_terminateplmpackagewide">TerminatePlmPackageWide</a>
</td>
<td align="left" width="63%">
Ends a Process Lifecycle Management (PLM) package.

</td>
</tr>
</table>    Launches and attaches to a Process Lifecycle Management (PLM) background task.

Disables a Process Lifecycle Management (PLM) package debug.

Enables a Process Lifecycle Management (PLM) package debug.

    Launches and attaches to a Process Lifecycle Management (PLM) application. 

Query a Process Lifecycle Management (PLM) package list.

Query a Process Lifecycle Management (PLM) package.

Resumes a Process Lifecycle Management (PLM) package.

Suspends a Process Lifecycle Management (PLM) package.

Ends a Process Lifecycle Management (PLM) package.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>