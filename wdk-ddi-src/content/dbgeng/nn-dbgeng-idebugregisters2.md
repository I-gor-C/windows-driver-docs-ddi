---
UID: NN.dbgeng.IDebugRegisters2
title: IDebugRegisters2
author: windows-driver-content
description: IDebugRegisters2 interface
old-location: debugger\idebugregisters2.htm
old-project: debugger
ms.assetid: f92a75a9-6578-4bbf-8d80-680493b4d284
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
req.alt-api: IDebugRegisters2
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

# IDebugRegisters2 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugRegisters2</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff550825">IDebugRegisters</a>. <b>IDebugRegisters2</b> also has these types of members:</p>

<p>The <b>IDebugRegisters2</b> interface has these methods.</p>

<p>Returns the description of a register.</p>

<p>Returns the location of the stack frame for the current function.</p>

<p>Returns the index of the named register.</p>

<p>Returns the location of the current thread's current instruction.</p>

<p>Returns the number of pseudo-registers that are maintained by the debugger engine.</p>

<p>Returns a description of a pseudo-register, including its name and type. (ANSI version)</p>

<p>Returns a description of a pseudo-register, including its name and type. (Unicode version)</p>

<p>Returns the index of a pseudo-register. (ANSI version)</p>

<p>Returns the index of a pseudo-register. (Unicode version)</p>

<p>Returns the values of a number of pseudo-registers.</p>

<p>Returns the current thread's current stack location.</p>

<p>Fetches the value of several of the target's registers.</p>

<p>Formats and outputs the target's registers.</p>

<p>Sets the value of several pseudo-registers.</p>

<p>Sets the value of several of the target's registers.</p>

<p> </p>

## -members
<p>The <b>IDebugRegisters2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546578">GetDescriptionWide</a>
</td>
<td align="left" width="63%">
<p>Returns the description of a register.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546815">GetFrameOffset2</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the stack frame for the current function.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546889">GetIndexByNameWide</a>
</td>
<td align="left" width="63%">
<p>Returns the index of the named register.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546933">GetInstructionOffset2</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the current thread's current instruction.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547957">GetNumberPseudoRegisters</a>
</td>
<td align="left" width="63%">
<p>Returns the number of pseudo-registers that are maintained by the debugger engine.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548189">GetPseudoDescription</a>
</td>
<td align="left" width="63%">
<p>Returns a description of a pseudo-register, including its name and type. (ANSI version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548194">GetPseudoDescriptionWide</a>
</td>
<td align="left" width="63%">
<p>Returns a description of a pseudo-register, including its name and type. (Unicode version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548206">GetPseudoIndexByName</a>
</td>
<td align="left" width="63%">
<p>Returns the index of a pseudo-register. (ANSI version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548211">GetPseudoIndexByNameWide</a>
</td>
<td align="left" width="63%">
<p>Returns the index of a pseudo-register. (Unicode version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548215">GetPseudoValues</a>
</td>
<td align="left" width="63%">
<p>Returns the values of a number of pseudo-registers.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548414">GetStackOffset2</a>
</td>
<td align="left" width="63%">
<p>Returns the current thread's current stack location.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549487">GetValues2</a>
</td>
<td align="left" width="63%">
<p>Fetches the value of several of the target's registers.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553245">OutputRegisters2</a>
</td>
<td align="left" width="63%">
<p>Formats and outputs the target's registers.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556767">SetPseudoValues</a>
</td>
<td align="left" width="63%">
<p>Sets the value of several pseudo-registers.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556884">SetValues2</a>
</td>
<td align="left" width="63%">
<p>Sets the value of several of the target's registers.</p>
</td>
</tr>
</table><p>Returns the description of a register.</p>

<p>Returns the location of the stack frame for the current function.</p>

<p>Returns the index of the named register.</p>

<p>Returns the location of the current thread's current instruction.</p>

<p>Returns the number of pseudo-registers that are maintained by the debugger engine.</p>

<p>Returns a description of a pseudo-register, including its name and type. (ANSI version)</p>

<p>Returns a description of a pseudo-register, including its name and type. (Unicode version)</p>

<p>Returns the index of a pseudo-register. (ANSI version)</p>

<p>Returns the index of a pseudo-register. (Unicode version)</p>

<p>Returns the values of a number of pseudo-registers.</p>

<p>Returns the current thread's current stack location.</p>

<p>Fetches the value of several of the target's registers.</p>

<p>Formats and outputs the target's registers.</p>

<p>Sets the value of several pseudo-registers.</p>

<p>Sets the value of several of the target's registers.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550825">IDebugRegisters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters2 interface%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
