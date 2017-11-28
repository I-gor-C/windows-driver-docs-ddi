---
UID: NN.dbgeng.IDebugControl2
title: IDebugControl2
author: windows-driver-content
description: IDebugControl2 interface
old-location: debugger\idebugcontrol2.htm
old-project: debugger
ms.assetid: c8371bbc-cbd1-4ff4-a055-99cc6cd6f8c6
ms.author: windowsdriverdev
ms.date: 11/15/2017
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
req.alt-api: IDebugControl2
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

# IDebugControl2 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugControl2</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>. <b>IDebugControl2</b> also has these types of members:</p>

<p>The <b>IDebugControl2</b> interface has these methods.</p>

<p>Returns the number of seconds the current target's computer has been running since it was last started.</p>

<p>Returns the time of the current target.
</p>

<p>Returns the flags that describe what information is available in a dump file target.</p>

<p>Returns the number of currently defined user-named and automatic aliases.</p>

<p>Returns the value of a user-named alias or an automatic alias.</p>

<p>Prints all the currently defined user-named aliases to the debugger's output stream.</p>

<p>Removes all user-named aliases.</p>

<p>Sets the value of a user-named alias.  </p>

<p> </p>

## -members
<p>The <b>IDebugControl2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545883">GetCurrentSystemUpTime</a>
</td>
<td align="left" width="63%">
<p>Returns the number of seconds the current target's computer has been running since it was last started.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546553">GetCurrentTimeDate</a>
</td>
<td align="left" width="63%">
<p>Returns the time of the current target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546592">GetDumpFormatFlags</a>
</td>
<td align="left" width="63%">
<p>Returns the flags that describe what information is available in a dump file target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547988">GetNumberTextReplacements</a>
</td>
<td align="left" width="63%">
<p>Returns the number of currently defined user-named and automatic aliases.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549280">GetTextReplacement</a>
</td>
<td align="left" width="63%">
<p>Returns the value of a user-named alias or an automatic alias.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553268">OutputTextReplacements</a>
</td>
<td align="left" width="63%">
<p>Prints all the currently defined user-named aliases to the debugger's output stream.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554548">RemoveTextReplacements</a>
</td>
<td align="left" width="63%">
<p>Removes all user-named aliases.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556818">SetTextReplacement</a>
</td>
<td align="left" width="63%">
<p>Sets the value of a user-named alias.  </p>
</td>
</tr>
</table><p>Returns the number of seconds the current target's computer has been running since it was last started.</p>

<p>Returns the time of the current target.
</p>

<p>Returns the flags that describe what information is available in a dump file target.</p>

<p>Returns the number of currently defined user-named and automatic aliases.</p>

<p>Returns the value of a user-named alias or an automatic alias.</p>

<p>Prints all the currently defined user-named aliases to the debugger's output stream.</p>

<p>Removes all user-named aliases.</p>

<p>Sets the value of a user-named alias.  </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550526">IDebugControl4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl2 interface%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
