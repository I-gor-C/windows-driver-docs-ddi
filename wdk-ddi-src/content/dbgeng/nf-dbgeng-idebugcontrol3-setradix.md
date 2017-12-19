---
UID: NF.dbgeng.IDebugControl3.SetRadix
title: IDebugControl3::SetRadix method
author: windows-driver-content
description: The SetRadix method sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information.
old-location: debugger\setradix.htm
old-project: Debugger
ms.assetid: 7346733d-2ac7-4eee-9f9c-ea6e1ee2ce5d
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugControl3, IDebugControl3::SetRadix, SetRadix
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.SetRadix,IDebugControl2.SetRadix,IDebugControl3.SetRadix
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

# IDebugControl3::SetRadix method



## -description
The <b>SetRadix</b> method sets the default radix (number base) used by the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> when it evaluates and displays MASM expressions, and when it displays symbol information.



## -syntax

````
HRESULT SetRadix(
  [in] ULONG Radix
);
````


## -parameters

### -param Radix [in]

Specifies the new default radix.  The following table contains the possible values for the radix.

<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
8

</td>
<td>
Octal

</td>
</tr>
<tr>
<td>
10

</td>
<td>
Decimal

</td>
</tr>
<tr>
<td>
16

</td>
<td>
Hexadecimal

</td>
</tr>
</table>
 


## -returns
This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.
<dl>
<dt><b>S_OK</b></dt>
</dl>The method was successful.

 


## -remarks
When the radix is changed, the engine notifies the event callbacks by passing the DEBUG_CES_RADIX flag to the <a href="debugger.idebugeventcallbacks_changeenginestate">IDebugEventCallbacks::ChangeEngineState</a> callback method.

For more information about the default radix, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560116">Using Input and Output</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="debugger.getradix">GetRadix</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552287">n (Set Number Base)</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugControl::SetRadix method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

