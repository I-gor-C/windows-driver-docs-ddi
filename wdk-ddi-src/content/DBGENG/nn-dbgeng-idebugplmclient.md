---
UID: NN.dbgeng.IDebugPlmClient
title: IDebugPlmClient
author: windows-driver-content
description: This interface supports Process Lifecycle Management (PLM) for the debug client.
old-location: debugger\idebugplmclient.htm
ms.assetid: 2D713354-4C93-4DC1-A3E9-7E6BC991FD08
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
req.alt-api: IDebugPlmClient
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

# IDebugPlmClient interface



## -description
<p>This interface supports Process Lifecycle Management (PLM) for the debug client.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugPlmClient</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugPlmClient</b> also has these types of members:</p>

<p>The <b>IDebugPlmClient</b> interface has these methods.</p>

<p>Launches a suspended Process Lifecycle Management (PLM) application.</p>

<p> </p>

## -members
<p>The <b>IDebugPlmClient</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/DE11B4A5-5AE3-4369-AF6D-6CE34B9AAFAB">LaunchPlmPackageForDebugWide</a>
</td>
<td align="left" width="63%">
<p>Launches a suspended Process Lifecycle Management (PLM) application.</p>
</td>
</tr>
</table><p>Launches a suspended Process Lifecycle Management (PLM) application.</p>

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