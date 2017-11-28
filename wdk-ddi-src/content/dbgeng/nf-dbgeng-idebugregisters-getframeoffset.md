---
UID: NF.dbgeng.IDebugRegisters.GetFrameOffset
title: IDebugRegisters::GetFrameOffset
author: windows-driver-content
description: The GetFrameOffset method returns the location of the stack frame for the current function.
old-location: debugger\getframeoffset.htm
old-project: debugger
ms.assetid: 09473106-3ab8-43ee-a424-2930b6bd3fcf
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugRegisters, GetFrameOffset, IDebugRegisters::GetFrameOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugRegisters.GetFrameOffset,IDebugRegisters2.GetFrameOffset
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
req.iface: IDebugRegisters
---

# IDebugRegisters::GetFrameOffset method



## -description
<p>The <b>GetFrameOffset</b> method returns the location of the stack frame for the current function.</p>


## -syntax

````
HRESULT GetFrameOffset(
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Offset</i> [out]

<dd>
<p>The location in the target's virtual address space of the stack frame for the current function.</p>
</dd>
</dl>

## -returns
<p>This list does not contain all the errors that might occur.  For a list of possible errors, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff549771">HRESULT Values</a>.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The meaning of value returned by this method is architecture-specific.</p>

<p>The method <a href="https://msdn.microsoft.com/library/windows/hardware/ff546815">GetFrameOffset2</a> performs the same task as this method but also allows the register source to be specified.</p>

<p>For an overview of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550825">IDebugRegisters</a> interface and other register-related methods, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554369">Registers</a>.</p>

<p>The meaning of value returned by this method is architecture-specific.</p>

<p>The method <a href="https://msdn.microsoft.com/library/windows/hardware/ff546815">GetFrameOffset2</a> performs the same task as this method but also allows the register source to be specified.</p>

<p>For an overview of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550825">IDebugRegisters</a> interface and other register-related methods, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554369">Registers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550825">IDebugRegisters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550835">IDebugRegisters2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546815">GetFrameOffset2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugRegisters::GetFrameOffset method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
