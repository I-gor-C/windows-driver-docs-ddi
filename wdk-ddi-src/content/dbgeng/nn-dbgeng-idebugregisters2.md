---
UID: NN.dbgeng.IDebugRegisters2
title: IDebugRegisters2
author: windows-driver-content
description: IDebugRegisters2 interface
old-location: debugger\idebugregisters2.htm
old-project: debugger
ms.assetid: f92a75a9-6578-4bbf-8d80-680493b4d284
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
---

# IDebugRegisters2 interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugRegisters2</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugregisters.md">IDebugRegisters</a>. <b>IDebugRegisters2</b> also has these types of members:

The <b>IDebugRegisters2</b> interface has these methods.

Returns the description of a register.

Returns the location of the stack frame for the current function.

Returns the index of the named register.

Returns the location of the current thread's current instruction.

Returns the number of pseudo-registers that are maintained by the debugger engine.

Returns a description of a pseudo-register, including its name and type. (ANSI version)

Returns a description of a pseudo-register, including its name and type. (Unicode version)

Returns the index of a pseudo-register. (ANSI version)

Returns the index of a pseudo-register. (Unicode version)

Returns the values of a number of pseudo-registers.

Returns the current thread's current stack location.

Fetches the value of several of the target's registers.

Formats and outputs the target's registers.

Sets the value of several pseudo-registers.

Sets the value of several of the target's registers.

 

## -members
The <b>IDebugRegisters2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getdescriptionwide">GetDescriptionWide</a>
</td>
<td align="left" width="63%">
Returns the description of a register.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getframeoffset2">GetFrameOffset2</a>
</td>
<td align="left" width="63%">
Returns the location of the stack frame for the current function.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getindexbynamewide">GetIndexByNameWide</a>
</td>
<td align="left" width="63%">
Returns the index of the named register.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getinstructionoffset2">GetInstructionOffset2</a>
</td>
<td align="left" width="63%">
Returns the location of the current thread's current instruction.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnumberpseudoregisters">GetNumberPseudoRegisters</a>
</td>
<td align="left" width="63%">
Returns the number of pseudo-registers that are maintained by the debugger engine.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getpseudodescription">GetPseudoDescription</a>
</td>
<td align="left" width="63%">
Returns a description of a pseudo-register, including its name and type. (ANSI version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getpseudodescriptionwide">GetPseudoDescriptionWide</a>
</td>
<td align="left" width="63%">
Returns a description of a pseudo-register, including its name and type. (Unicode version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getpseudoindexbyname">GetPseudoIndexByName</a>
</td>
<td align="left" width="63%">
Returns the index of a pseudo-register. (ANSI version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getpseudoindexbynamewide">GetPseudoIndexByNameWide</a>
</td>
<td align="left" width="63%">
Returns the index of a pseudo-register. (Unicode version)
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getpseudovalues">GetPseudoValues</a>
</td>
<td align="left" width="63%">
Returns the values of a number of pseudo-registers.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getstackoffset2">GetStackOffset2</a>
</td>
<td align="left" width="63%">
Returns the current thread's current stack location.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getvalues2">GetValues2</a>
</td>
<td align="left" width="63%">
Fetches the value of several of the target's registers.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputregisters2">OutputRegisters2</a>
</td>
<td align="left" width="63%">
Formats and outputs the target's registers.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setpseudovalues">SetPseudoValues</a>
</td>
<td align="left" width="63%">
Sets the value of several pseudo-registers.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setvalues2">SetValues2</a>
</td>
<td align="left" width="63%">
Sets the value of several of the target's registers.
</td>
</tr>
</table>Returns the description of a register.

Returns the location of the stack frame for the current function.

Returns the index of the named register.

Returns the location of the current thread's current instruction.

Returns the number of pseudo-registers that are maintained by the debugger engine.

Returns a description of a pseudo-register, including its name and type. (ANSI version)

Returns a description of a pseudo-register, including its name and type. (Unicode version)

Returns the index of a pseudo-register. (ANSI version)

Returns the index of a pseudo-register. (Unicode version)

Returns the values of a number of pseudo-registers.

Returns the current thread's current stack location.

Fetches the value of several of the target's registers.

Formats and outputs the target's registers.

Sets the value of several pseudo-registers.

Sets the value of several of the target's registers.

 

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

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugregisters.md">IDebugRegisters</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters2 interface%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
