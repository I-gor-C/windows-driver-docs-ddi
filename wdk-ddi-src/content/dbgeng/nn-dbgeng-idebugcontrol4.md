---
UID: NN.dbgeng.IDebugControl4
title: IDebugControl4
author: windows-driver-content
description: IDebugControl4 interface
old-location: debugger\idebugcontrol4.htm
old-project: debugger
ms.assetid: 693207c2-70d7-45be-ae22-436555225928
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
req.alt-api: IDebugControl4,IDebugControl4.GetManagedStatus,IDebugControl4.GetManagedStatusWide,IDebugControl4.ResetManagedStatus
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

# IDebugControl4 interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugControl4</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>. <b>IDebugControl4</b> also has these types of members:

The <b>IDebugControl4</b> interface has these methods.

Creates a new breakpoint for the current target.

Loads an extension library into the debugger engine.

Assembles a single processor instruction.

Calls a debugger extension.

Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.

Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.

Disassembles a processor instruction in the target's memory.

Evaluates an expression, returning the result.

Opens the specified file and executes the debugger commands that are contained within.

Executes the specified debugger commands.

Returns the breakpoint with the specified breakpoint ID.

Returns the breakpoint located at the specified index.

Returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame.


Returns the debugger command that the engine will execute when a specified event occurs.

Returns a short description of an event for a specific filter.

Describes the specified event in a static list of events for the current target.

Returns the command that will be executed by the debugger engine upon the second chance of a specified exception.

Returns the full and abbreviated names of an expression syntax.

Returns the handle for an already loaded extension library.

Returns a pointer to an extension function from an extension library.

Returns information about the last event that occurred in a target.

Returns the name of the currently open log file.

Returns the name of the currently open log file.

Returns the name of the currently open log file.





Returns the full name and abbreviated name of the specified processor type.

 Returns the standard prompt text that will be prepended to the formatted output specified in the <a href="debugger.outputprompt">OutputPrompt</a> and <a href="debugger.outputpromptvalist">OutputPromptVaList</a> methods.

Returns the value of filter argument for the specific filters that have an argument.

 Retrieves information about an event of interest available in the current target.


Returns a string that describes the target's operating system version.
(ANSI version)

Returns a string that describes the target's operating system version.
(Unicode version)

Returns version number information for the current target.

Returns the value of a fixed-name alias.

Returns the value of a user-named alias or an automatic alias.

Requests an input string from the debugger engine.

Opens a log file that will receive output from the <a href="debugger.client_objects#client_objects#client_objects">client objects</a>.

Opens a log file that will receive output from the <a href="debugger.client_objects#client_objects#client_objects">client objects</a>.

Opens a log file that will receive output from the client objects.

Prints the call stack specified by an array of stack frames and corresponding register contexts.


Formats and sends a user prompt to the output callback objects.

 Formats and sends a user prompt to the output callback objects.

Formats a string and sends the result to the output callbacks that are registered with the engine's clients.

 Formats a string and send the result to output callbacks that have been registered with the engine's clients.

Removes a breakpoint.



This method is used by <a href="..\dbgeng\nn-dbgeng-idebuginputcallbacks.md">IDebugInputCallbacks</a> objects to send an input string to the engine following a request for input.

Sets a debugger command for the engine to execute when a specified event occurs.

Sets the command that will be executed by the debugger engine on the second chance of a specified exception.

Sets the syntax that the engine will use to evaluate expressions.

Sets the value of filter argument for the specific filters that can have an argument.

Sets the value of a fixed-name alias.

Sets the value of a user-named alias.

 


## -members
The <b>IDebugControl4</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addbreakpoint2">AddBreakpoint2</a>
</td>
<td align="left" width="63%">
Creates a new breakpoint for the current target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addextensionwide">AddExtensionWide</a>
</td>
<td align="left" width="63%">
Loads an extension library into the debugger engine.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.assemblewide">AssembleWide</a>
</td>
<td align="left" width="63%">
Assembles a single processor instruction.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.callextensionwide">CallExtensionWide</a>
</td>
<td align="left" width="63%">
Calls a debugger extension.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.controlledoutputvalistwide">ControlledOutputVaListWide</a>
</td>
<td align="left" width="63%">
Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.controlledoutputwide">ControlledOutputWide</a>
</td>
<td align="left" width="63%">
Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.disassemblewide">DisassembleWide</a>
</td>
<td align="left" width="63%">
Disassembles a processor instruction in the target's memory.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.evaluatewide">EvaluateWide</a>
</td>
<td align="left" width="63%">
Evaluates an expression, returning the result.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.executecommandfilewide">ExecuteCommandFileWide</a>
</td>
<td align="left" width="63%">
Opens the specified file and executes the debugger commands that are contained within.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.executewide">ExecuteWide</a>
</td>
<td align="left" width="63%">
Executes the specified debugger commands.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getbreakpointbyid2">GetBreakpointById2</a>
</td>
<td align="left" width="63%">
Returns the breakpoint with the specified breakpoint ID.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getbreakpointbyindex2">GetBreakpointByIndex2</a>
</td>
<td align="left" width="63%">
Returns the breakpoint located at the specified index.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcontextstacktrace">GetContextStackTrace</a>
</td>
<td align="left" width="63%">
Returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame.


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.geteventfiltercommandwide">GetEventFilterCommandWide</a>
</td>
<td align="left" width="63%">
Returns the debugger command that the engine will execute when a specified event occurs.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.geteventfiltertextwide">GetEventFilterTextWide</a>
</td>
<td align="left" width="63%">
Returns a short description of an event for a specific filter.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.geteventindexdescriptionwide">GetEventIndexDescriptionWide</a>
</td>
<td align="left" width="63%">
Describes the specified event in a static list of events for the current target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getexceptionfiltersecondcommandwide">GetExceptionFilterSecondCommandWide</a>
</td>
<td align="left" width="63%">
Returns the command that will be executed by the debugger engine upon the second chance of a specified exception.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getexpressionsyntaxnameswide">GetExpressionSyntaxNamesWide</a>
</td>
<td align="left" width="63%">
Returns the full and abbreviated names of an expression syntax.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getextensionbypathwide">GetExtensionByPathWide</a>
</td>
<td align="left" width="63%">
Returns the handle for an already loaded extension library.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getextensionfunctionwide">GetExtensionFunctionWide</a>
</td>
<td align="left" width="63%">
Returns a pointer to an extension function from an extension library.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getlasteventinformationwide">GetLastEventInformationWide</a>
</td>
<td align="left" width="63%">
Returns information about the last event that occurred in a target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getlogfile2">GetLogFile2</a>
</td>
<td align="left" width="63%">
Returns the name of the currently open log file.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getlogfile2wide">GetLogFile2Wide</a>
</td>
<td align="left" width="63%">
Returns the name of the currently open log file.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getlogfilewide">GetLogFileWide</a>
</td>
<td align="left" width="63%">
Returns the name of the currently open log file.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetManagedStatus</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetManagedStatusWide</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getprocessortypenameswide">GetProcessorTypeNamesWide</a>
</td>
<td align="left" width="63%">
Returns the full name and abbreviated name of the specified processor type.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getprompttextwide">GetPromptTextWide</a>
</td>
<td align="left" width="63%">
 Returns the standard prompt text that will be prepended to the formatted output specified in the <a href="debugger.outputprompt">OutputPrompt</a> and <a href="debugger.outputpromptvalist">OutputPromptVaList</a> methods.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getspecificfilterargumentwide">GetSpecificFilterArgumentWide</a>
</td>
<td align="left" width="63%">
Returns the value of filter argument for the specific filters that have an argument.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getstoredeventinformation">GetStoredEventInformation</a>
</td>
<td align="left" width="63%">
 Retrieves information about an event of interest available in the current target.


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsystemversionstring">GetSystemVersionString</a>
</td>
<td align="left" width="63%">
Returns a string that describes the target's operating system version.
(ANSI version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsystemversionstringwide">GetSystemVersionStringWide</a>
</td>
<td align="left" width="63%">
Returns a string that describes the target's operating system version.
(Unicode version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsystemversionvalues">GetSystemVersionValues</a>
</td>
<td align="left" width="63%">
Returns version number information for the current target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettextmacrowide">GetTextMacroWide</a>
</td>
<td align="left" width="63%">
Returns the value of a fixed-name alias.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettextreplacementwide">GetTextReplacementWide</a>
</td>
<td align="left" width="63%">
Returns the value of a user-named alias or an automatic alias.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.inputwide">InputWide</a>
</td>
<td align="left" width="63%">
Requests an input string from the debugger engine.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.openlogfile2">OpenLogFile2</a>
</td>
<td align="left" width="63%">
Opens a log file that will receive output from the <a href="debugger.client_objects#client_objects#client_objects">client objects</a>.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.openlogfile2wide">OpenLogFile2Wide</a>
</td>
<td align="left" width="63%">
Opens a log file that will receive output from the <a href="debugger.client_objects#client_objects#client_objects">client objects</a>.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.openlogfilewide">OpenLogFileWide</a>
</td>
<td align="left" width="63%">
Opens a log file that will receive output from the client objects.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputcontextstacktrace">OutputContextStackTrace</a>
</td>
<td align="left" width="63%">
Prints the call stack specified by an array of stack frames and corresponding register contexts.


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputpromptvalistwide">OutputPromptVaListWide</a>
</td>
<td align="left" width="63%">
Formats and sends a user prompt to the output callback objects.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputpromptwide">OutputPromptWide</a>
</td>
<td align="left" width="63%">
 Formats and sends a user prompt to the output callback objects.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputvalistwide">OutputVaListWide</a>
</td>
<td align="left" width="63%">
Formats a string and sends the result to the output callbacks that are registered with the engine's clients.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputwide">OutputWide</a>
</td>
<td align="left" width="63%">
 Formats a string and send the result to output callbacks that have been registered with the engine's clients.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removebreakpoint2">RemoveBreakpoint2</a>
</td>
<td align="left" width="63%">
Removes a breakpoint.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>ResetManagedStatus</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.returninputwide">ReturnInputWide</a>
</td>
<td align="left" width="63%">
This method is used by <a href="..\dbgeng\nn-dbgeng-idebuginputcallbacks.md">IDebugInputCallbacks</a> objects to send an input string to the engine following a request for input.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.seteventfiltercommandwide">SetEventFilterCommandWide</a>
</td>
<td align="left" width="63%">
Sets a debugger command for the engine to execute when a specified event occurs.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setexceptionfiltersecondcommandwide">SetExceptionFilterSecondCommandWide</a>
</td>
<td align="left" width="63%">
Sets the command that will be executed by the debugger engine on the second chance of a specified exception.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setexpressionsyntaxbynamewide">SetExpressionSyntaxByNameWide</a>
</td>
<td align="left" width="63%">
Sets the syntax that the engine will use to evaluate expressions.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setspecificfilterargumentwide">SetSpecificFilterArgumentWide</a>
</td>
<td align="left" width="63%">
Sets the value of filter argument for the specific filters that can have an argument.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.settextmacrowide">SetTextMacroWide</a>
</td>
<td align="left" width="63%">
Sets the value of a fixed-name alias.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.settextreplacementwide">SetTextReplacementWide</a>
</td>
<td align="left" width="63%">
Sets the value of a user-named alias.

</td>
</tr>
</table>Creates a new breakpoint for the current target.

Loads an extension library into the debugger engine.

Assembles a single processor instruction.

Calls a debugger extension.

Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.

Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.

Disassembles a processor instruction in the target's memory.

Evaluates an expression, returning the result.

Opens the specified file and executes the debugger commands that are contained within.

Executes the specified debugger commands.

Returns the breakpoint with the specified breakpoint ID.

Returns the breakpoint located at the specified index.

Returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame.


Returns the debugger command that the engine will execute when a specified event occurs.

Returns a short description of an event for a specific filter.

Describes the specified event in a static list of events for the current target.

Returns the command that will be executed by the debugger engine upon the second chance of a specified exception.

Returns the full and abbreviated names of an expression syntax.

Returns the handle for an already loaded extension library.

Returns a pointer to an extension function from an extension library.

Returns information about the last event that occurred in a target.

Returns the name of the currently open log file.

Returns the name of the currently open log file.

Returns the name of the currently open log file.





Returns the full name and abbreviated name of the specified processor type.

 Returns the standard prompt text that will be prepended to the formatted output specified in the <a href="debugger.outputprompt">OutputPrompt</a> and <a href="debugger.outputpromptvalist">OutputPromptVaList</a> methods.

Returns the value of filter argument for the specific filters that have an argument.

 Retrieves information about an event of interest available in the current target.


Returns a string that describes the target's operating system version.
(ANSI version)

Returns a string that describes the target's operating system version.
(Unicode version)

Returns version number information for the current target.

Returns the value of a fixed-name alias.

Returns the value of a user-named alias or an automatic alias.

Requests an input string from the debugger engine.

Opens a log file that will receive output from the <a href="debugger.client_objects#client_objects#client_objects">client objects</a>.

Opens a log file that will receive output from the <a href="debugger.client_objects#client_objects#client_objects">client objects</a>.

Opens a log file that will receive output from the client objects.

Prints the call stack specified by an array of stack frames and corresponding register contexts.


Formats and sends a user prompt to the output callback objects.

 Formats and sends a user prompt to the output callback objects.

Formats a string and sends the result to the output callbacks that are registered with the engine's clients.

 Formats a string and send the result to output callbacks that have been registered with the engine's clients.

Removes a breakpoint.



This method is used by <a href="..\dbgeng\nn-dbgeng-idebuginputcallbacks.md">IDebugInputCallbacks</a> objects to send an input string to the engine following a request for input.

Sets a debugger command for the engine to execute when a specified event occurs.

Sets the command that will be executed by the debugger engine on the second chance of a specified exception.

Sets the syntax that the engine will use to evaluate expressions.

Sets the value of filter argument for the specific filters that can have an argument.

Sets the value of a fixed-name alias.

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4 interface%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

