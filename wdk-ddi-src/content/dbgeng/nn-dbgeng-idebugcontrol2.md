---
UID: NN.dbgeng.IDebugControl2
title: IDebugControl2
author: windows-driver-content
description: IDebugControl2 interface
old-location: debugger\idebugcontrol2.htm
old-project: debugger
ms.assetid: c8371bbc-cbd1-4ff4-a055-99cc6cd6f8c6
ms.author: windowsdriverdev
ms.date: 12/8/2017
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
---

# IDebugControl2 interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugControl2</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>. <b>IDebugControl2</b> also has these types of members:

The <b>IDebugControl2</b> interface has these methods.

Returns the number of seconds the current target's computer has been running since it was last started.

Returns the time of the current target.


Returns the flags that describe what information is available in a dump file target.

Returns the number of currently defined user-named and automatic aliases.

Returns the value of a user-named alias or an automatic alias.

Prints all the currently defined user-named aliases to the debugger's output stream.

Removes all user-named aliases.

Sets the value of a user-named alias.  

 


## -members
The <b>IDebugControl2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentsystemuptime">GetCurrentSystemUpTime</a>
</td>
<td align="left" width="63%">
Returns the number of seconds the current target's computer has been running since it was last started.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrenttimedate">GetCurrentTimeDate</a>
</td>
<td align="left" width="63%">
Returns the time of the current target.


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getdumpformatflags">GetDumpFormatFlags</a>
</td>
<td align="left" width="63%">
Returns the flags that describe what information is available in a dump file target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnumbertextreplacements">GetNumberTextReplacements</a>
</td>
<td align="left" width="63%">
Returns the number of currently defined user-named and automatic aliases.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettextreplacement">GetTextReplacement</a>
</td>
<td align="left" width="63%">
Returns the value of a user-named alias or an automatic alias.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputtextreplacements">OutputTextReplacements</a>
</td>
<td align="left" width="63%">
Prints all the currently defined user-named aliases to the debugger's output stream.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removetextreplacements">RemoveTextReplacements</a>
</td>
<td align="left" width="63%">
Removes all user-named aliases.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.settextreplacement">SetTextReplacement</a>
</td>
<td align="left" width="63%">
Sets the value of a user-named alias.  

</td>
</tr>
</table>Returns the number of seconds the current target's computer has been running since it was last started.

Returns the time of the current target.


Returns the flags that describe what information is available in a dump file target.

Returns the number of currently defined user-named and automatic aliases.

Returns the value of a user-named alias or an automatic alias.

Prints all the currently defined user-named aliases to the debugger's output stream.

Removes all user-named aliases.

Sets the value of a user-named alias.  

 


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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol4.md">IDebugControl4</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl2 interface%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

