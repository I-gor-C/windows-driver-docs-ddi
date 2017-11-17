---
UID: NN.dbgeng.IDebugDataSpaces4
title: IDebugDataSpaces4
author: windows-driver-content
description: IDebugDataSpaces4 interface
old-location: debugger\idebugdataspaces4.htm
ms.assetid: e03202a5-2e4a-43f8-8183-fdd26df6ff8f
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
req.alt-api: IDebugDataSpaces4
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

# IDebugDataSpaces4 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugDataSpaces4</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff550537">IDebugDataSpaces3</a>. <b>IDebugDataSpaces4</b> also has these types of members:</p>

<p>The <b>IDebugDataSpaces4</b> interface has these methods.</p>

<p>Returns the offset of the next address whose validity might be different from the validity of the specified address.</p>

<p>Provides general information about an address in a process's data space.</p>

<p>Locates the first valid region of memory in a specified memory range.</p>

<p>Reads a null-terminated, multibyte string from the target.</p>

<p>Reads a null-terminated, multibyte string from the target and converts it to Unicode.</p>

<p>Reads the target's memory from the specified physical address.</p>

<p>Reads a null-terminated, Unicode string from the target and converts it to a multibyte string.</p>

<p>Reads a null-terminated, Unicode string from the target.</p>

<p>Searches the process's virtual memory for a specified pattern of bytes.</p>

<p>Writes data to the specified physical address in the target's memory.</p>

<p> </p>

## -members
<p>The <b>IDebugDataSpaces4</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547847">GetNextDifferentlyValidOffsetVirtual</a>
</td>
<td align="left" width="63%">
<p>Returns the offset of the next address whose validity might be different from the validity of the specified address.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548055">GetOffsetInformation</a>
</td>
<td align="left" width="63%">
<p>Provides general information about an address in a process's data space.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549471">GetValidRegionVirtual</a>
</td>
<td align="left" width="63%">
<p>Locates the first valid region of memory in a specified memory range.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554300">ReadMultiByteStringVirtual</a>
</td>
<td align="left" width="63%">
<p>Reads a null-terminated, multibyte string from the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554304">ReadMultiByteStringVirtualWide</a>
</td>
<td align="left" width="63%">
<p>Reads a null-terminated, multibyte string from the target and converts it to Unicode.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554311">ReadPhysical2</a>
</td>
<td align="left" width="63%">
<p>Reads the target's memory from the specified physical address.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554351">ReadUnicodeStringVirtual</a>
</td>
<td align="left" width="63%">
<p>Reads a null-terminated, Unicode string from the target and converts it to a multibyte string.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554357">ReadUnicodeStringVirtualWide</a>
</td>
<td align="left" width="63%">
<p>Reads a null-terminated, Unicode string from the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554755">SearchVirtual2</a>
</td>
<td align="left" width="63%">
<p>Searches the process's virtual memory for a specified pattern of bytes.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561441">WritePhysical2</a>
</td>
<td align="left" width="63%">
<p>Writes data to the specified physical address in the target's memory.</p>
</td>
</tr>
</table><p>Returns the offset of the next address whose validity might be different from the validity of the specified address.</p>

<p>Provides general information about an address in a process's data space.</p>

<p>Locates the first valid region of memory in a specified memory range.</p>

<p>Reads a null-terminated, multibyte string from the target.</p>

<p>Reads a null-terminated, multibyte string from the target and converts it to Unicode.</p>

<p>Reads the target's memory from the specified physical address.</p>

<p>Reads a null-terminated, Unicode string from the target and converts it to a multibyte string.</p>

<p>Reads a null-terminated, Unicode string from the target.</p>

<p>Searches the process's virtual memory for a specified pattern of bytes.</p>

<p>Writes data to the specified physical address in the target's memory.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550528">IDebugDataSpaces</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550531">IDebugDataSpaces2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550537">IDebugDataSpaces3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces4 interface%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
