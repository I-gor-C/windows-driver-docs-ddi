---
UID: NN.dbgeng.IDebugControl6
title: IDebugControl6
author: windows-driver-content
description: .
old-location: debugger\idebugcontrol6.htm
ms.assetid: 3361EB55-0765-405E-AA75-D1DF3BDE0003
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
req.alt-api: IDebugControl6
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

# IDebugControl6 interface



## -description
<p></p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugControl6</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/dn818562">IDebugControl5</a>. <b>IDebugControl6</b> also has these types of members:</p>

<p>The <b>IDebugControl6</b> interface has these methods.</p>

<p>The GetExecutionStatusEx method returns information about the execution status of the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>.</p>

<p>The GetSynchronizationStatus method returns information about the synchronization status of the debugger engine.</p>

<p> </p>

## -members
<p>The <b>IDebugControl6</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn818569">GetExecutionStatusEx</a>
</td>
<td align="left" width="63%">
<p>The GetExecutionStatusEx method returns information about the execution status of the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn818570">GetSynchronizationStatus</a>
</td>
<td align="left" width="63%">
<p>The GetSynchronizationStatus method returns information about the synchronization status of the debugger engine.</p>
</td>
</tr>
</table><p>The GetExecutionStatusEx method returns information about the execution status of the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a>.</p>

<p>The GetSynchronizationStatus method returns information about the synchronization status of the debugger engine.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550526">IDebugControl4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn818562">IDebugControl5</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl6 interface%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
