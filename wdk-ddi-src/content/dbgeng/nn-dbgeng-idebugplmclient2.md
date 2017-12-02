---
UID: NN.dbgeng.IDebugPlmClient2
title: IDebugPlmClient2
author: windows-driver-content
description: This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location: debugger\idebugplmclient2.htm
old-project: debugger
ms.assetid: 22AACAD1-292B-42D9-95F7-A3654E2077FB
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
req.alt-api: IDebugPlmClient2
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

# IDebugPlmClient2 interface



## -description
<p>This interface supports Process Lifecycle Management (PLM) for the debug client.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugPlmClient2</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugPlmClient2</b> also has these types of members:</p>

<p>The <b>IDebugPlmClient2</b> interface has these methods.</p>

<p>Launches a suspended Process Lifecycle Management (PLM) background task.</p>

<p> </p>

## -members
<p>The <b>IDebugPlmClient2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugplmclient2_launchplmbgtaskfordebugwide">LaunchPlmBgTaskForDebugWide</a>
</td>
<td align="left" width="63%">
<p>Launches a suspended Process Lifecycle Management (PLM) background task.</p>
</td>
</tr>
</table><p>Launches a suspended Process Lifecycle Management (PLM) background task.</p>

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