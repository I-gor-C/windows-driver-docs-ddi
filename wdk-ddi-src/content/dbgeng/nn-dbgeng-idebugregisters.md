---
UID: NN.dbgeng.IDebugRegisters
title: IDebugRegisters
author: windows-driver-content
description: IDebugRegisters interface
old-location: debugger\idebugregisters.htm
old-project: debugger
ms.assetid: a2587ea7-20cd-43be-ba71-750e699ee0ce
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
---

# IDebugRegisters interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugRegisters</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugRegisters</b> also has these types of members:

The <b>IDebugRegisters</b> interface has these methods.

Returns the description of a register.

Returns the location of the stack frame for the current function.

Returns the index of the named register.

Returns the location of the current thread's current instruction.

Returns the number of registers on the target computer.

Returns the current thread's current stack location.

Gets the value of one of the target's registers.

Gets the value of several of the target's registers.

Formats and sends the target's registers to the clients as output.

Sets the value of one of the target's registers.

Sets the value of several of the target's registers.

 

## -members
The <b>IDebugRegisters</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getdescription">GetDescription</a>
</td>
<td align="left" width="63%">
Returns the description of a register.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getframeoffset">GetFrameOffset</a>
</td>
<td align="left" width="63%">
Returns the location of the stack frame for the current function.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getindexbyname">GetIndexByName</a>
</td>
<td align="left" width="63%">
Returns the index of the named register.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getinstructionoffset">GetInstructionOffset</a>
</td>
<td align="left" width="63%">
Returns the location of the current thread's current instruction.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnumberregisters">GetNumberRegisters</a>
</td>
<td align="left" width="63%">
Returns the number of registers on the target computer.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getstackoffset">GetStackOffset</a>
</td>
<td align="left" width="63%">
Returns the current thread's current stack location.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getvalue">GetValue</a>
</td>
<td align="left" width="63%">
Gets the value of one of the target's registers.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getvalues">GetValues</a>
</td>
<td align="left" width="63%">
Gets the value of several of the target's registers.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputregisters">OutputRegisters</a>
</td>
<td align="left" width="63%">
Formats and sends the target's registers to the clients as output.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setvalue">SetValue</a>
</td>
<td align="left" width="63%">
Sets the value of one of the target's registers.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setvalues">SetValues</a>
</td>
<td align="left" width="63%">
Sets the value of several of the target's registers.
</td>
</tr>
</table>Returns the description of a register.

Returns the location of the stack frame for the current function.

Returns the index of the named register.

Returns the location of the current thread's current instruction.

Returns the number of registers on the target computer.

Returns the current thread's current stack location.

Gets the value of one of the target's registers.

Gets the value of several of the target's registers.

Formats and sends the target's registers to the clients as output.

Sets the value of one of the target's registers.

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
<a href="..\dbgeng\nn-dbgeng-idebugregisters2.md">IDebugRegisters2</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters interface%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
