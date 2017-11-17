---
UID: NN.dbgeng.IDebugControl
title: IDebugControl
author: windows-driver-content
description: IDebugControl interface
old-location: debugger\idebugcontrol.htm
ms.assetid: 6ff5b9ff-d2b8-4ade-8b8b-20284efdf266
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
req.alt-api: IDebugControl,IDebugControl.GetWindbgExtensionApis32
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

# IDebugControl interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugControl</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugControl</b> also has these types of members:</p>

<p>The <b>IDebugControl</b> interface has these methods.</p>

<p>Creates a new breakpoint for the current target.
</p>

<p> Turns on some of the debugger engine's options.</p>

<p>Loads an extension library into the debugger engine.
</p>

<p>Assembles a single processor instruction. The assembled instruction is placed in the target's memory.</p>

<p>Calls a debugger extension.</p>

<p>Closes the currently-open log file.</p>

<p>Converts a value of one type into a value of another type.
</p>

<p>Converts an array of values into an array of values of different types.</p>

<p>Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.
</p>

<p>Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.
</p>

<p>Disassembles a processor instruction in the target's memory.
</p>

<p>Evaluates an expression, returning the result.</p>

<p>Executes the specified debugger commands.
</p>

<p>Opens the specified file and executes the debugger commands that are contained within.
</p>

<p>Returns the processor type of the physical processor of the computer that is running the target.
</p>

<p>Returns the breakpoint with the specified breakpoint ID.
</p>

<p>Returns the breakpoint located at the specified index.
</p>

<p>Returns the parameters of one or more breakpoints.
</p>

<p>Returns the current code level and is mainly used when stepping through code.
</p>

<p>Describes the nature of the current target.
</p>

<p>Returns the address of the last instruction disassembled using Disassemble.
</p>

<p>Returns the effective processor type of the processor of the computer that is running the target.
</p>

<p>Returns the engine's options.</p>

<p>Returns the debugger command that the engine will execute when a specified event occurs.
</p>

<p>Returns a short description of an event for a specific filter.
</p>

<p>Returns the parameters for exception filters specified by exception codes or by index.
</p>

<p>Returns the command that will be executed by the debugger engine upon the second chance of a specified exception.
</p>

<p>Returns the executing processor type for the processor for which the last event occurred.
</p>

<p>Returns information about the execution status of the debugger engine.
</p>

<p>Returns the handle for an already loaded extension library.
</p>

<p>Returns a pointer to an extension function from an extension library.
</p>

<p>Checks whether a user interrupt was issued.</p>

<p>Returns the number of seconds that the engine will wait when requesting a break into the debugger.</p>

<p>Returns information about the last event that occurred in a target.
</p>

<p>Returns the name of the currently open log file.</p>

<p>Returns the output mask for the currently open log file.

HRESULT

</p>

<p>Returns the location of a processor instruction relative to a given location.
</p>

<p>Receives the handle of the event that will be signaled after the next exception in a target.
</p>

<p>Returns the number of breakpoints for the current process.
</p>

<p>Returns the number of event filters currently used by the engine.
</p>

<p>Returns the number of processor types that are supported by the computer running the current target.</p>

<p>Returns the number of processors on the computer running the current target.
</p>

<p>Returns the number of processor types supported by the engine.
</p>

<p>Returns the page size for the effective processor mode.</p>

<p>Returns the processor types that are supported by the computer running the current target.
</p>

<p>Returns the full name and abbreviated name of the specified processor type.
</p>

<p>Returns the standard prompt text that will be prepended to the formatted output specified in the <b>OutputPrompt</b> and <b>OutputPromptVaList</b> methods.</p>

<p>Returns the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information.</p>

<p> Returns the return address for the current function.</p>

<p>Returns the value of filter argument for thespecific filters that have an argument.
</p>

<p>Returns the parameters for specific event filters.
</p>

<p>Returns the frames at the top of the specified call stack.</p>

<p>Returns the processor types supported by the debugger engine. 
</p>

<p>Returns the control values for handling system errors.
</p>

<p>Returns information that identifies the operating system on the computer that is running the current target.</p>

<p>Returns the value of a fixed-name alias.</p>

<p></p>

<p>returns a structure that facilitates using the WdbgExts API.
</p>

<p>Requests an input string from the debugger engine.
</p>

<p>Determines if the effective processor uses 64-bit pointers.</p>

<p>Opens a log file that will receive output from the client objects.</p>

<p>Formats a string and sends the result to output callbacks that have been registered with the engine's clients.</p>

<p>Prints the current state of the current target to the debugger console.
</p>

<p>Disassembles a processor instruction and sends the disassembly to the output callbacks.
</p>

<p>Disassembles several processor instructions and sends the resulting assembly instructions to the output callbacks.</p>

<p> Formats and sends a user prompt to the output callback objects.
</p>

<p>Formats and sends a user prompt to the output callback objects.
</p>

<p>Outputs either the supplied stack frame or the current stack frames.
</p>

<p> Formats a string and sends the result to the output callbacks that are registered with the engine's clients.
</p>

<p>Prints version information about the debugger engine to the debugger console.
</p>

<p>Reads the kernel bug check code and related parameters.
</p>

<p>Removes a breakpoint.
</p>

<p>Turns off some of the engine's options.
</p>

<p>Unloads an extension library.</p>

<p>This method is used by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550785">IDebugInputCallbacks</a> objects to send an input string to the engine following a request for input.
</p>

<p>Sets the current code level and is mainly used when stepping through code.
</p>

<p>Sets the effective processor type of the processor of the computer that is running the target.
</p>

<p>Changes the engine's options.
</p>

<p>Sets a debugger command for the engine to execute when a specified event occurs.
</p>

<p>Changes the break status and handling status for some exception filters.
</p>

<p>Sets the command that will be executed by the debugger engine on the second chance of a specified exception.</p>

<p>Requests that the debugger engine enter an executable state. Actual execution will not occur until the next time <b>WaitForEvent</b> is called.
</p>

<p>Registers a user interrupt or breaks into the debugger.</p>

<p>Sets the number of seconds that the debugger engine should wait when requesting a break into the debugger.</p>

<p>Sets the output mask for the currently open log file.
</p>

<p>Sets the event that will be signaled after the next exception in a target.
</p>

<p>Sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information.</p>

<p>Sets the value of filter argument for the specific filters that can have an argument.
</p>

<p>Changes the break status and handling status for some specific event filters.
</p>

<p>Sets the control values for handling system errors.</p>

<p>Sets the value of a fixed-name alias.</p>

<p>Waits for an event that breaks into the debugger engine application.
</p>

<p> </p>

## -members
<p>The <b>IDebugControl</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537856">AddBreakpoint</a>
</td>
<td align="left" width="63%">
<p>Creates a new breakpoint for the current target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537884">AddEngineOptions</a>
</td>
<td align="left" width="63%">
<p> Turns on some of the debugger engine's options.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537892">AddExtension</a>
</td>
<td align="left" width="63%">
<p>Loads an extension library into the debugger engine.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538121">Assemble</a>
</td>
<td align="left" width="63%">
<p>Assembles a single processor instruction. The assembled instruction is placed in the target's memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539023">CallExtension</a>
</td>
<td align="left" width="63%">
<p>Calls a debugger extension.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539148">CloseLogFile</a>
</td>
<td align="left" width="63%">
<p>Closes the currently-open log file.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539158">CoerceValue</a>
</td>
<td align="left" width="63%">
<p>Converts a value of one type into a value of another type.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539162">CoerceValues</a>
</td>
<td align="left" width="63%">
<p>Converts an array of values into an array of values of different types.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539248">ControlledOutput</a>
</td>
<td align="left" width="63%">
<p>Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539252">ControlledOutputVaList</a>
</td>
<td align="left" width="63%">
<p>Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541948">Disassemble</a>
</td>
<td align="left" width="63%">
<p>Disassembles a processor instruction in the target's memory.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543046">Evaluate</a>
</td>
<td align="left" width="63%">
<p>Evaluates an expression, returning the result.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543208">Execute</a>
</td>
<td align="left" width="63%">
<p>Executes the specified debugger commands.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543215">ExecuteCommandFile</a>
</td>
<td align="left" width="63%">
<p>Opens the specified file and executes the debugger commands that are contained within.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545572">GetActualProcessorType</a>
</td>
<td align="left" width="63%">
<p>Returns the processor type of the physical processor of the computer that is running the target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545617">GetBreakpointById</a>
</td>
<td align="left" width="63%">
<p>Returns the breakpoint with the specified breakpoint ID.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545639">GetBreakpointByIndex</a>
</td>
<td align="left" width="63%">
<p>Returns the breakpoint located at the specified index.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545656">GetBreakpointParameters</a>
</td>
<td align="left" width="63%">
<p>Returns the parameters of one or more breakpoints.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545670">GetCodeLevel</a>
</td>
<td align="left" width="63%">
<p>Returns the current code level and is mainly used when stepping through code.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546559">GetDebuggeeType</a>
</td>
<td align="left" width="63%">
<p>Describes the nature of the current target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546581">GetDisassembleEffectiveOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the address of the last instruction disassembled using Disassemble.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546595">GetEffectiveProcessorType</a>
</td>
<td align="left" width="63%">
<p>Returns the effective processor type of the processor of the computer that is running the target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546598">GetEngineOptions</a>
</td>
<td align="left" width="63%">
<p>Returns the engine's options.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546611">GetEventFilterCommand</a>
</td>
<td align="left" width="63%">
<p>Returns the debugger command that the engine will execute when a specified event occurs.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546618">GetEventFilterText</a>
</td>
<td align="left" width="63%">
<p>Returns a short description of an event for a specific filter.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546650">GetExceptionFilterParameters</a>
</td>
<td align="left" width="63%">
<p>Returns the parameters for exception filters specified by exception codes or by index.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546653">GetExceptionFilterSecondCommand</a>
</td>
<td align="left" width="63%">
<p>Returns the command that will be executed by the debugger engine upon the second chance of a specified exception.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546670">GetExecutingProcessorType</a>
</td>
<td align="left" width="63%">
<p>Returns the executing processor type for the processor for which the last event occurred.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546675">GetExecutionStatus</a>
</td>
<td align="left" width="63%">
<p>Returns information about the execution status of the debugger engine.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546717">GetExtensionByPath</a>
</td>
<td align="left" width="63%">
<p>Returns the handle for an already loaded extension library.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546733">GetExtensionFunction</a>
</td>
<td align="left" width="63%">
<p>Returns a pointer to an extension function from an extension library.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546944">GetInterrupt</a>
</td>
<td align="left" width="63%">
<p>Checks whether a user interrupt was issued.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546955">GetInterruptTimeout</a>
</td>
<td align="left" width="63%">
<p>Returns the number of seconds that the engine will wait when requesting a break into the debugger.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546982">GetLastEventInformation</a>
</td>
<td align="left" width="63%">
<p>Returns information about the last event that occurred in a target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547016">GetLogFile</a>
</td>
<td align="left" width="63%">
<p>Returns the name of the currently open log file.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547066">GetLogMask</a>
</td>
<td align="left" width="63%">
<p>Returns the output mask for the currently open log file.

HRESULT

</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547197">GetNearInstruction</a>
</td>
<td align="left" width="63%">
<p>Returns the location of a processor instruction relative to a given location.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547876">GetNotifyEventHandle</a>
</td>
<td align="left" width="63%">
<p>Receives the handle of the event that will be signaled after the next exception in a target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547880">GetNumberBreakpoints</a>
</td>
<td align="left" width="63%">
<p>Returns the number of breakpoints for the current process.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547899">GetNumberEventFilters</a>
</td>
<td align="left" width="63%">
<p>Returns the number of event filters currently used by the engine.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547939">GetNumberPossibleExecutingProcessorTypes</a>
</td>
<td align="left" width="63%">
<p>Returns the number of processor types that are supported by the computer running the current target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547950">GetNumberProcessors</a>
</td>
<td align="left" width="63%">
<p>Returns the number of processors on the computer running the current target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547966">GetNumberSupportedProcessorTypes</a>
</td>
<td align="left" width="63%">
<p>Returns the number of processor types supported by the engine.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548086">GetPageSize</a>
</td>
<td align="left" width="63%">
<p>Returns the page size for the effective processor mode.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548130">GetPossibleExecutingProcessorTypes</a>
</td>
<td align="left" width="63%">
<p>Returns the processor types that are supported by the computer running the current target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548169">GetProcessorTypeNames</a>
</td>
<td align="left" width="63%">
<p>Returns the full name and abbreviated name of the specified processor type.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548180">GetPromptText</a>
</td>
<td align="left" width="63%">
<p>Returns the standard prompt text that will be prepended to the formatted output specified in the <b>OutputPrompt</b> and <b>OutputPromptVaList</b> methods.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548218">GetRadix</a>
</td>
<td align="left" width="63%">
<p>Returns the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548237">GetReturnOffset</a>
</td>
<td align="left" width="63%">
<p> Returns the return address for the current function.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548386">GetSpecificFilterArgument</a>
</td>
<td align="left" width="63%">
<p>Returns the value of filter argument for thespecific filters that have an argument.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548398">GetSpecificFilterParameters</a>
</td>
<td align="left" width="63%">
<p>Returns the parameters for specific event filters.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548425">GetStackTrace</a>
</td>
<td align="left" width="63%">
<p>Returns the frames at the top of the specified call stack.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548438">GetSupportedProcessorTypes</a>
</td>
<td align="left" width="63%">
<p>Returns the processor types supported by the debugger engine. 
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549215">GetSystemErrorControl</a>
</td>
<td align="left" width="63%">
<p>Returns the control values for handling system errors.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549234">GetSystemVersion</a>
</td>
<td align="left" width="63%">
<p>Returns information that identifies the operating system on the computer that is running the current target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549270">GetTextMacro</a>
</td>
<td align="left" width="63%">
<p>Returns the value of a fixed-name alias.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetWindbgExtensionApis32</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549510">GetWindbgExtensionApis64</a>
</td>
<td align="left" width="63%">
<p>returns a structure that facilitates using the WdbgExts API.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550962">Input</a>
</td>
<td align="left" width="63%">
<p>Requests an input string from the debugger engine.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551092">IsPointer64Bit</a>
</td>
<td align="left" width="63%">
<p>Determines if the effective processor uses 64-bit pointers.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553154">OpenLogFile</a>
</td>
<td align="left" width="63%">
<p>Opens a log file that will receive output from the client objects.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553183">Output</a>
</td>
<td align="left" width="63%">
<p>Formats a string and sends the result to output callbacks that have been registered with the engine's clients.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553206">OutputCurrentState</a>
</td>
<td align="left" width="63%">
<p>Prints the current state of the current target to the debugger console.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553211">OutputDisassembly</a>
</td>
<td align="left" width="63%">
<p>Disassembles a processor instruction and sends the disassembly to the output callbacks.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553216">OutputDisassemblyLines</a>
</td>
<td align="left" width="63%">
<p>Disassembles several processor instructions and sends the resulting assembly instructions to the output callbacks.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553227">OutputPrompt</a>
</td>
<td align="left" width="63%">
<p> Formats and sends a user prompt to the output callback objects.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553231">OutputPromptVaList</a>
</td>
<td align="left" width="63%">
<p>Formats and sends a user prompt to the output callback objects.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553252">OutputStackTrace</a>
</td>
<td align="left" width="63%">
<p>Outputs either the supplied stack frame or the current stack frames.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553280">OutputVaList</a>
</td>
<td align="left" width="63%">
<p> Formats a string and sends the result to the output callbacks that are registered with the engine's clients.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553288">OutputVersionInformation</a>
</td>
<td align="left" width="63%">
<p>Prints version information about the debugger engine to the debugger console.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553517">ReadBugCheckData</a>
</td>
<td align="left" width="63%">
<p>Reads the kernel bug check code and related parameters.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554487">RemoveBreakpoint</a>
</td>
<td align="left" width="63%">
<p>Removes a breakpoint.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554491">RemoveEngineOptions</a>
</td>
<td align="left" width="63%">
<p>Turns off some of the engine's options.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554497">RemoveExtension</a>
</td>
<td align="left" width="63%">
<p>Unloads an extension library.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554600">ReturnInput</a>
</td>
<td align="left" width="63%">
<p>This method is used by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550785">IDebugInputCallbacks</a> objects to send an input string to the engine following a request for input.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556629">SetCodeLevel</a>
</td>
<td align="left" width="63%">
<p>Sets the current code level and is mainly used when stepping through code.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556657">SetEffectiveProcessorType</a>
</td>
<td align="left" width="63%">
<p>Sets the effective processor type of the processor of the computer that is running the target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556670">SetEngineOptions</a>
</td>
<td align="left" width="63%">
<p>Changes the engine's options.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556678">SetEventFilterCommand</a>
</td>
<td align="left" width="63%">
<p>Sets a debugger command for the engine to execute when a specified event occurs.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556683">SetExceptionFilterParameters</a>
</td>
<td align="left" width="63%">
<p>Changes the break status and handling status for some exception filters.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556687">SetExceptionFilterSecondCommand</a>
</td>
<td align="left" width="63%">
<p>Sets the command that will be executed by the debugger engine on the second chance of a specified exception.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556693">SetExecutionStatus</a>
</td>
<td align="left" width="63%">
<p>Requests that the debugger engine enter an executable state. Actual execution will not occur until the next time <b>WaitForEvent</b> is called.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556722">SetInterrupt</a>
</td>
<td align="left" width="63%">
<p>Registers a user interrupt or breaks into the debugger.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556725">SetInterruptTimeout</a>
</td>
<td align="left" width="63%">
<p>Sets the number of seconds that the debugger engine should wait when requesting a break into the debugger.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556734">SetLogMask</a>
</td>
<td align="left" width="63%">
<p>Sets the output mask for the currently open log file.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556739">SetNotifyEventHandle</a>
</td>
<td align="left" width="63%">
<p>Sets the event that will be signaled after the next exception in a target.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556770">SetRadix</a>
</td>
<td align="left" width="63%">
<p>Sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556791">SetSpecificFilterArgument</a>
</td>
<td align="left" width="63%">
<p>Sets the value of filter argument for the specific filters that can have an argument.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556795">SetSpecificFilterParameters</a>
</td>
<td align="left" width="63%">
<p>Changes the break status and handling status for some specific event filters.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556806">SetSystemErrorControl</a>
</td>
<td align="left" width="63%">
<p>Sets the control values for handling system errors.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556809">SetTextMacro</a>
</td>
<td align="left" width="63%">
<p>Sets the value of a fixed-name alias.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561229">WaitForEvent</a>
</td>
<td align="left" width="63%">
<p>Waits for an event that breaks into the debugger engine application.
</p>
</td>
</tr>
</table><p>Creates a new breakpoint for the current target.
</p>

<p> Turns on some of the debugger engine's options.</p>

<p>Loads an extension library into the debugger engine.
</p>

<p>Assembles a single processor instruction. The assembled instruction is placed in the target's memory.</p>

<p>Calls a debugger extension.</p>

<p>Closes the currently-open log file.</p>

<p>Converts a value of one type into a value of another type.
</p>

<p>Converts an array of values into an array of values of different types.</p>

<p>Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.
</p>

<p>Formats a string and sends the result to output callbacks that were registered with some of the engine's clients.
</p>

<p>Disassembles a processor instruction in the target's memory.
</p>

<p>Evaluates an expression, returning the result.</p>

<p>Executes the specified debugger commands.
</p>

<p>Opens the specified file and executes the debugger commands that are contained within.
</p>

<p>Returns the processor type of the physical processor of the computer that is running the target.
</p>

<p>Returns the breakpoint with the specified breakpoint ID.
</p>

<p>Returns the breakpoint located at the specified index.
</p>

<p>Returns the parameters of one or more breakpoints.
</p>

<p>Returns the current code level and is mainly used when stepping through code.
</p>

<p>Describes the nature of the current target.
</p>

<p>Returns the address of the last instruction disassembled using Disassemble.
</p>

<p>Returns the effective processor type of the processor of the computer that is running the target.
</p>

<p>Returns the engine's options.</p>

<p>Returns the debugger command that the engine will execute when a specified event occurs.
</p>

<p>Returns a short description of an event for a specific filter.
</p>

<p>Returns the parameters for exception filters specified by exception codes or by index.
</p>

<p>Returns the command that will be executed by the debugger engine upon the second chance of a specified exception.
</p>

<p>Returns the executing processor type for the processor for which the last event occurred.
</p>

<p>Returns information about the execution status of the debugger engine.
</p>

<p>Returns the handle for an already loaded extension library.
</p>

<p>Returns a pointer to an extension function from an extension library.
</p>

<p>Checks whether a user interrupt was issued.</p>

<p>Returns the number of seconds that the engine will wait when requesting a break into the debugger.</p>

<p>Returns information about the last event that occurred in a target.
</p>

<p>Returns the name of the currently open log file.</p>

<p>Returns the output mask for the currently open log file.

HRESULT

</p>

<p>Returns the location of a processor instruction relative to a given location.
</p>

<p>Receives the handle of the event that will be signaled after the next exception in a target.
</p>

<p>Returns the number of breakpoints for the current process.
</p>

<p>Returns the number of event filters currently used by the engine.
</p>

<p>Returns the number of processor types that are supported by the computer running the current target.</p>

<p>Returns the number of processors on the computer running the current target.
</p>

<p>Returns the number of processor types supported by the engine.
</p>

<p>Returns the page size for the effective processor mode.</p>

<p>Returns the processor types that are supported by the computer running the current target.
</p>

<p>Returns the full name and abbreviated name of the specified processor type.
</p>

<p>Returns the standard prompt text that will be prepended to the formatted output specified in the <b>OutputPrompt</b> and <b>OutputPromptVaList</b> methods.</p>

<p>Returns the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information.</p>

<p> Returns the return address for the current function.</p>

<p>Returns the value of filter argument for thespecific filters that have an argument.
</p>

<p>Returns the parameters for specific event filters.
</p>

<p>Returns the frames at the top of the specified call stack.</p>

<p>Returns the processor types supported by the debugger engine. 
</p>

<p>Returns the control values for handling system errors.
</p>

<p>Returns information that identifies the operating system on the computer that is running the current target.</p>

<p>Returns the value of a fixed-name alias.</p>

<p></p>

<p>returns a structure that facilitates using the WdbgExts API.
</p>

<p>Requests an input string from the debugger engine.
</p>

<p>Determines if the effective processor uses 64-bit pointers.</p>

<p>Opens a log file that will receive output from the client objects.</p>

<p>Formats a string and sends the result to output callbacks that have been registered with the engine's clients.</p>

<p>Prints the current state of the current target to the debugger console.
</p>

<p>Disassembles a processor instruction and sends the disassembly to the output callbacks.
</p>

<p>Disassembles several processor instructions and sends the resulting assembly instructions to the output callbacks.</p>

<p> Formats and sends a user prompt to the output callback objects.
</p>

<p>Formats and sends a user prompt to the output callback objects.
</p>

<p>Outputs either the supplied stack frame or the current stack frames.
</p>

<p> Formats a string and sends the result to the output callbacks that are registered with the engine's clients.
</p>

<p>Prints version information about the debugger engine to the debugger console.
</p>

<p>Reads the kernel bug check code and related parameters.
</p>

<p>Removes a breakpoint.
</p>

<p>Turns off some of the engine's options.
</p>

<p>Unloads an extension library.</p>

<p>This method is used by <a href="https://msdn.microsoft.com/library/windows/hardware/ff550785">IDebugInputCallbacks</a> objects to send an input string to the engine following a request for input.
</p>

<p>Sets the current code level and is mainly used when stepping through code.
</p>

<p>Sets the effective processor type of the processor of the computer that is running the target.
</p>

<p>Changes the engine's options.
</p>

<p>Sets a debugger command for the engine to execute when a specified event occurs.
</p>

<p>Changes the break status and handling status for some exception filters.
</p>

<p>Sets the command that will be executed by the debugger engine on the second chance of a specified exception.</p>

<p>Requests that the debugger engine enter an executable state. Actual execution will not occur until the next time <b>WaitForEvent</b> is called.
</p>

<p>Registers a user interrupt or breaks into the debugger.</p>

<p>Sets the number of seconds that the debugger engine should wait when requesting a break into the debugger.</p>

<p>Sets the output mask for the currently open log file.
</p>

<p>Sets the event that will be signaled after the next exception in a target.
</p>

<p>Sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information.</p>

<p>Sets the value of filter argument for the specific filters that can have an argument.
</p>

<p>Changes the break status and handling status for some specific event filters.
</p>

<p>Sets the control values for handling system errors.</p>

<p>Sets the value of a fixed-name alias.</p>

<p>Waits for an event that breaks into the debugger engine application.
</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550526">IDebugControl4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl interface%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
