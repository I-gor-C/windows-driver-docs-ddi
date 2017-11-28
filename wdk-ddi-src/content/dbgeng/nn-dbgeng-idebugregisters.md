---
UID: NN.dbgeng.IDebugRegisters
title: IDebugRegisters
author: windows-driver-content
description: IDebugRegisters interface
old-location: debugger\idebugregisters.htm
old-project: debugger
ms.assetid: a2587ea7-20cd-43be-ba71-750e699ee0ce
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
req.alt-api: IDebugRegisters
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

# IDebugRegisters interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugRegisters</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugRegisters</b> also has these types of members:</p>

<p>The <b>IDebugRegisters</b> interface has these methods.</p>

<p>Returns the description of a register.</p>

<p>Returns the location of the stack frame for the current function.</p>

<p>Returns the index of the named register.</p>

<p>Returns the location of the current thread's current instruction.</p>

<p>Returns the number of registers on the target computer.</p>

<p>Returns the current thread's current stack location.</p>

<p>Gets the value of one of the target's registers.</p>

<p>Gets the value of several of the target's registers.</p>

<p>Formats and sends the target's registers to the clients as output.</p>

<p>Sets the value of one of the target's registers.</p>

<p>Sets the value of several of the target's registers.</p>

<p> </p>

## -members
<p>The <b>IDebugRegisters</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546575">GetDescription</a>
</td>
<td align="left" width="63%">
<p>Returns the description of a register.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546806">GetFrameOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the stack frame for the current function.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546881">GetIndexByName</a>
</td>
<td align="left" width="63%">
<p>Returns the index of the named register.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546916">GetInstructionOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the current thread's current instruction.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547960">GetNumberRegisters</a>
</td>
<td align="left" width="63%">
<p>Returns the number of registers on the target computer.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548403">GetStackOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the current thread's current stack location.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff597624">GetValue</a>
</td>
<td align="left" width="63%">
<p>Gets the value of one of the target's registers.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549480">GetValues</a>
</td>
<td align="left" width="63%">
<p>Gets the value of several of the target's registers.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553242">OutputRegisters</a>
</td>
<td align="left" width="63%">
<p>Formats and sends the target's registers to the clients as output.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff597642">SetValue</a>
</td>
<td align="left" width="63%">
<p>Sets the value of one of the target's registers.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556883">SetValues</a>
</td>
<td align="left" width="63%">
<p>Sets the value of several of the target's registers.</p>
</td>
</tr>
</table><p>Returns the description of a register.</p>

<p>Returns the location of the stack frame for the current function.</p>

<p>Returns the index of the named register.</p>

<p>Returns the location of the current thread's current instruction.</p>

<p>Returns the number of registers on the target computer.</p>

<p>Returns the current thread's current stack location.</p>

<p>Gets the value of one of the target's registers.</p>

<p>Gets the value of several of the target's registers.</p>

<p>Formats and sends the target's registers to the clients as output.</p>

<p>Sets the value of one of the target's registers.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550835">IDebugRegisters2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters interface%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
