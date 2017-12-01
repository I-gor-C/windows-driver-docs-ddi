---
UID: NN.dbgeng.IDebugDataSpaces
title: IDebugDataSpaces
author: windows-driver-content
description: IDebugDataSpaces interface
old-location: debugger\idebugdataspaces.htm
old-project: debugger
ms.assetid: 9477821c-4f4f-4ea2-9968-d43f87c496b2
ms.author: windowsdriverdev
ms.date: 11/27/2017
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
req.alt-api: IDebugDataSpaces
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

# IDebugDataSpaces interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugDataSpaces</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugDataSpaces</b> also has these types of members:</p>

<p>The <b>IDebugDataSpaces</b> interface has these methods.</p>

<p>Checks for memory corruption in the low 4 GB of memory.</p>

<p>Reads data from a system bus.</p>

<p>Reads implementation-specific system data.</p>

<p>Returns information about the target that the debugger engine has queried or determined during the current session.</p>

<p>Reads from the system and bus I/O memory.</p>

<p>Reads a specified Model-Specific Register (MSR).</p>

<p>Reads the target's memory from the specified physical address.</p>

<p> Reads pointers from the target's virtual address space.
</p>

<p>Returns data about the specified processor.</p>

<p>Reads memory from the target's virtual address space.</p>

<p>Reads memory from the target's virtual address space.</p>

<p>Searches the target's virtual memory for a specified pattern of bytes.</p>

<p>Writes data to a system bus.</p>

<p>Writes implementation-specific system data.</p>

<p>Writes to the system and bus I/O memory.</p>

<p>Writes a value to the specified Model-Specific Register (MSR).</p>

<p>Writes data to the specified physical address in the target's memory.</p>

<p>Writes pointers to the target's virtual address space.</p>

<p>Writes data to the target's virtual address space.</p>

<p>Writes data to the target's virtual address space.</p>

<p> </p>

## -members
<p>The <b>IDebugDataSpaces</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.checklowmemory">CheckLowMemory</a>
</td>
<td align="left" width="63%">
<p>Checks for memory corruption in the low 4 GB of memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readbusdata">ReadBusData</a>
</td>
<td align="left" width="63%">
<p>Reads data from a system bus.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readcontrol">ReadControl</a>
</td>
<td align="left" width="63%">
<p>Reads implementation-specific system data.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readdebuggerdata">ReadDebuggerData</a>
</td>
<td align="left" width="63%">
<p>Returns information about the target that the debugger engine has queried or determined during the current session.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readio">ReadIo</a>
</td>
<td align="left" width="63%">
<p>Reads from the system and bus I/O memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="..\wdbgexts\nf-wdbgexts-readmsr.md">ReadMsr</a>
</td>
<td align="left" width="63%">
<p>Reads a specified Model-Specific Register (MSR).</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="..\wdbgexts\nf-wdbgexts-readphysical.md">ReadPhysical</a>
</td>
<td align="left" width="63%">
<p>Reads the target's memory from the specified physical address.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readpointersvirtual">ReadPointersVirtual</a>
</td>
<td align="left" width="63%">
<p> Reads pointers from the target's virtual address space.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readprocessorsystemdata">ReadProcessorSystemData</a>
</td>
<td align="left" width="63%">
<p>Returns data about the specified processor.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readvirtual">ReadVirtual</a>
</td>
<td align="left" width="63%">
<p>Reads memory from the target's virtual address space.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readvirtualuncached">ReadVirtualUncached</a>
</td>
<td align="left" width="63%">
<p>Reads memory from the target's virtual address space.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.searchvirtual">SearchVirtual</a>
</td>
<td align="left" width="63%">
<p>Searches the target's virtual memory for a specified pattern of bytes.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writebusdata">WriteBusData</a>
</td>
<td align="left" width="63%">
<p>Writes data to a system bus.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writecontrol">WriteControl</a>
</td>
<td align="left" width="63%">
<p>Writes implementation-specific system data.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writeio">WriteIo</a>
</td>
<td align="left" width="63%">
<p>Writes to the system and bus I/O memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="..\wdbgexts\nf-wdbgexts-writemsr.md">WriteMsr</a>
</td>
<td align="left" width="63%">
<p>Writes a value to the specified Model-Specific Register (MSR).</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="..\wdbgexts\nf-wdbgexts-writephysical.md">WritePhysical</a>
</td>
<td align="left" width="63%">
<p>Writes data to the specified physical address in the target's memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writepointersvirtual">WritePointersVirtual</a>
</td>
<td align="left" width="63%">
<p>Writes pointers to the target's virtual address space.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writevirtual">WriteVirtual</a>
</td>
<td align="left" width="63%">
<p>Writes data to the target's virtual address space.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writevirtualuncached">WriteVirtualUncached</a>
</td>
<td align="left" width="63%">
<p>Writes data to the target's virtual address space.</p>
</td>
</tr>
</table><p>Checks for memory corruption in the low 4 GB of memory.</p>

<p>Reads data from a system bus.</p>

<p>Reads implementation-specific system data.</p>

<p>Returns information about the target that the debugger engine has queried or determined during the current session.</p>

<p>Reads from the system and bus I/O memory.</p>

<p>Reads a specified Model-Specific Register (MSR).</p>

<p>Reads the target's memory from the specified physical address.</p>

<p> Reads pointers from the target's virtual address space.
</p>

<p>Returns data about the specified processor.</p>

<p>Reads memory from the target's virtual address space.</p>

<p>Reads memory from the target's virtual address space.</p>

<p>Searches the target's virtual memory for a specified pattern of bytes.</p>

<p>Writes data to a system bus.</p>

<p>Writes implementation-specific system data.</p>

<p>Writes to the system and bus I/O memory.</p>

<p>Writes a value to the specified Model-Specific Register (MSR).</p>

<p>Writes data to the specified physical address in the target's memory.</p>

<p>Writes pointers to the target's virtual address space.</p>

<p>Writes data to the target's virtual address space.</p>

<p>Writes data to the target's virtual address space.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces2.md">IDebugDataSpaces2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces3.md">IDebugDataSpaces3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces4.md">IDebugDataSpaces4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces interface%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
