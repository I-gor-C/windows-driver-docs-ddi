---
UID: NN.dbgeng.IDebugControl3
title: IDebugControl3
author: windows-driver-content
description: IDebugControl3 interface
old-location: debugger\idebugcontrol3.htm
ms.assetid: 95e714b4-4167-41a1-ab2c-b088dbaf5fe2
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
req.alt-api: IDebugControl3
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

# IDebugControl3 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugControl3</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>. <b>IDebugControl3</b> also has these types of members:</p>

<p>The <b>IDebugControl3</b> interface has these methods.</p>

<p>Turns on some of the assembly and disassembly options.
</p>

<p>Returns the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target.</p>

<p>Returns the index of the current event within the current list of events for the current target, if such a list exists.
</p>

<p>Describes the specified event in a static list of events for the current target.
</p>

<p>Returns the current syntax that the engine is using for evaluating expressions.
</p>

<p>Returns the full and abbreviated names of an expression syntax.
</p>

<p>Returns the number of events for the current target, if the number of events is fixed.
</p>

<p>Returns the number of expression syntaxes that are supported by the engine.
</p>

<p> Turns off some of the assembly and disassembly options.</p>

<p>Sets the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target.
</p>

<p>Sets the syntax that the engine will use to evaluate expressions.
</p>

<p>Sets the syntax that the engine will use to evaluate expressions.
</p>

<p>Sets the next event for the current target by selecting the event from the static list of events for the target, if such a list exists.
</p>

<p> </p>

## -members
<p>The <b>IDebugControl3</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537852">AddAssemblyOptions</a>
</td>
<td align="left" width="63%">
<p>Turns on some of the assembly and disassembly options.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545605">GetAssemblyOptions</a>
</td>
<td align="left" width="63%">
<p>Returns the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545755">GetCurrentEventIndex</a>
</td>
<td align="left" width="63%">
<p>Returns the index of the current event within the current list of events for the current target, if such a list exists.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546630">GetEventIndexDescription</a>
</td>
<td align="left" width="63%">
<p>Describes the specified event in a static list of events for the current target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546701">GetExpressionSyntax</a>
</td>
<td align="left" width="63%">
<p>Returns the current syntax that the engine is using for evaluating expressions.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546708">GetExpressionSyntaxNames</a>
</td>
<td align="left" width="63%">
<p>Returns the full and abbreviated names of an expression syntax.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547906">GetNumberEvents</a>
</td>
<td align="left" width="63%">
<p>Returns the number of events for the current target, if the number of events is fixed.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547913">GetNumberExpressionSyntaxes</a>
</td>
<td align="left" width="63%">
<p>Returns the number of expression syntaxes that are supported by the engine.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554483">RemoveAssemblyOptions</a>
</td>
<td align="left" width="63%">
<p> Turns off some of the assembly and disassembly options.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556626">SetAssemblyOptions</a>
</td>
<td align="left" width="63%">
<p>Sets the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556696">SetExpressionSyntax</a>
</td>
<td align="left" width="63%">
<p>Sets the syntax that the engine will use to evaluate expressions.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556697">SetExpressionSyntaxByName</a>
</td>
<td align="left" width="63%">
<p>Sets the syntax that the engine will use to evaluate expressions.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556737">SetNextEventIndex</a>
</td>
<td align="left" width="63%">
<p>Sets the next event for the current target by selecting the event from the static list of events for the target, if such a list exists.
</p>
</td>
</tr>
</table><p>Turns on some of the assembly and disassembly options.
</p>

<p>Returns the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target.</p>

<p>Returns the index of the current event within the current list of events for the current target, if such a list exists.
</p>

<p>Describes the specified event in a static list of events for the current target.
</p>

<p>Returns the current syntax that the engine is using for evaluating expressions.
</p>

<p>Returns the full and abbreviated names of an expression syntax.
</p>

<p>Returns the number of events for the current target, if the number of events is fixed.
</p>

<p>Returns the number of expression syntaxes that are supported by the engine.
</p>

<p> Turns off some of the assembly and disassembly options.</p>

<p>Sets the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target.
</p>

<p>Sets the syntax that the engine will use to evaluate expressions.
</p>

<p>Sets the syntax that the engine will use to evaluate expressions.
</p>

<p>Sets the next event for the current target by selecting the event from the static list of events for the target, if such a list exists.
</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550526">IDebugControl4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl3 interface%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
