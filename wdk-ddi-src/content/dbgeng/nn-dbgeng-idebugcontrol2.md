---
UID: NN:dbgeng.IDebugControl2
title: IDebugControl2
author: windows-driver-content
description: IDebugControl2 interface
old-location: debugger\idebugcontrol2.htm
old-project: debugger
ms.assetid: c8371bbc-cbd1-4ff4-a055-99cc6cd6f8c6
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IDebugControl2, IDebugControl2 interface [Windows Debugging], IDebugControl2 interface [Windows Debugging], described, dbgeng/IDebugControl2, debugger.idebugcontrol2
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugControl2
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugControl2 interface



## Methods

<p>The <b>IDebugControl2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugControl2::AddBreakpoint](nf-dbgeng-idebugcontrol2-addbreakpoint.md) | The AddBreakpoint method creates a new breakpoint for the current target. |
| [IDebugControl2::AddEngineOptions](nf-dbgeng-idebugcontrol2-addengineoptions.md) | The AddEngineOptions method turns on some of the debugger engine's options. |
| [IDebugControl2::AddExtension](nf-dbgeng-idebugcontrol2-addextension.md) | The AddExtension method loads an extension library into the debugger engine. |
| [IDebugControl2::Assemble](nf-dbgeng-idebugcontrol2-assemble.md) | The Assemble method assembles a single processor instruction. The assembled instruction is placed in the target's memory. |
| [IDebugControl2::CallExtension](nf-dbgeng-idebugcontrol2-callextension.md) | The CallExtension method calls a debugger extension. |
| [IDebugControl2::CloseLogFile](nf-dbgeng-idebugcontrol2-closelogfile.md) | The CloseLogFile method closes the currently-open log file. |
| [IDebugControl2::CoerceValue](nf-dbgeng-idebugcontrol2-coercevalue.md) | The CoerceValue method converts a value of one type into a value of another type. |
| [IDebugControl2::CoerceValues](nf-dbgeng-idebugcontrol2-coercevalues.md) | The CoerceValues method converts an array of values into an array of values of different types. |
| [IDebugControl2::ControlledOutput](nf-dbgeng-idebugcontrol2-controlledoutput.md) | The ControlledOutput method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugControl2::ControlledOutputVaList](nf-dbgeng-idebugcontrol2-controlledoutputvalist.md) | The ControlledOutputVaList method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugControl2::Disassemble](nf-dbgeng-idebugcontrol2-disassemble.md) | The Disassemble method disassembles a processor instruction in the target's memory. |
| [IDebugControl2::Evaluate](nf-dbgeng-idebugcontrol2-evaluate.md) | The Evaluate method evaluates an expression, returning the result. |
| [IDebugControl2::Execute](nf-dbgeng-idebugcontrol2-execute.md) | The Execute method executes the specified debugger commands. |
| [IDebugControl2::ExecuteCommandFile](nf-dbgeng-idebugcontrol2-executecommandfile.md) | The ExecuteCommandFile method opens the specified file and executes the debugger commands that are contained within. |
| [IDebugControl2::GetActualProcessorType](nf-dbgeng-idebugcontrol2-getactualprocessortype.md) | The GetActualProcessorType method returns the processor type of the physical processor of the computer that is running the target. |
| [IDebugControl2::GetBreakpointById](nf-dbgeng-idebugcontrol2-getbreakpointbyid.md) | The GetBreakpointById method returns the breakpoint with the specified breakpoint ID. |
| [IDebugControl2::GetBreakpointByIndex](nf-dbgeng-idebugcontrol2-getbreakpointbyindex.md) | The GetBreakpointByIndex method returns the breakpoint located at the specified index. |
| [IDebugControl2::GetBreakpointParameters](nf-dbgeng-idebugcontrol2-getbreakpointparameters.md) | The GetBreakpointParameters method returns the parameters of one or more breakpoints. |
| [IDebugControl2::GetCodeLevel](nf-dbgeng-idebugcontrol2-getcodelevel.md) | The GetCodeLevel method returns the current code level and is mainly used when stepping through code. |
| [IDebugControl2::GetCurrentSystemUpTime](nf-dbgeng-idebugcontrol2-getcurrentsystemuptime.md) | The GetCurrentSystemUpTime method returns the number of seconds the current target's computer has been running since it was last started. |
| [IDebugControl2::GetCurrentTimeDate](nf-dbgeng-idebugcontrol2-getcurrenttimedate.md) | The GetCurrentTimeDate method returns the time of the current target. |
| [IDebugControl2::GetDebuggeeType](nf-dbgeng-idebugcontrol2-getdebuggeetype.md) | The GetDebuggeeType method describes the nature of the current target. |
| [IDebugControl2::GetDisassembleEffectiveOffset](nf-dbgeng-idebugcontrol2-getdisassembleeffectiveoffset.md) | The GetDisassembleEffectiveOffset method returns the address of the last instruction disassembled using Disassemble. |
| [IDebugControl2::GetDumpFormatFlags](nf-dbgeng-idebugcontrol2-getdumpformatflags.md) | The GetDumpFormatFlags method returns the flags that describe what information is available in a dump file target. |
| [IDebugControl2::GetEffectiveProcessorType](nf-dbgeng-idebugcontrol2-geteffectiveprocessortype.md) | The GetEffectiveProcessorType method returns the effective processor type of the processor of the computer that is running the target. |
| [IDebugControl2::GetEngineOptions](nf-dbgeng-idebugcontrol2-getengineoptions.md) | The GetEngineOptions method returns the engine's options. |
| [IDebugControl2::GetEventFilterCommand](nf-dbgeng-idebugcontrol2-geteventfiltercommand.md) | The GetEventFilterCommand method returns the debugger command that the engine will execute when a specified event occurs. |
| [IDebugControl2::GetEventFilterText](nf-dbgeng-idebugcontrol2-geteventfiltertext.md) | The GetEventFilterText method returns a short description of an event for a specific filter. |
| [IDebugControl2::GetExceptionFilterParameters](nf-dbgeng-idebugcontrol2-getexceptionfilterparameters.md) | The GetExceptionFilterParameters method returns the parameters for exception filters specified by exception codes or by index. |
| [IDebugControl2::GetExceptionFilterSecondCommand](nf-dbgeng-idebugcontrol2-getexceptionfiltersecondcommand.md) | The GetExceptionFilterSecondCommand method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [IDebugControl2::GetExecutingProcessorType](nf-dbgeng-idebugcontrol2-getexecutingprocessortype.md) | The GetExecutingProcessorType method returns the executing processor type for the processor for which the last event occurred. |
| [IDebugControl2::GetExecutionStatus](nf-dbgeng-idebugcontrol2-getexecutionstatus.md) | The GetExecutionStatus method returns information about the execution status of the debugger engine. |
| [IDebugControl2::GetExtensionByPath](nf-dbgeng-idebugcontrol2-getextensionbypath.md) | The GetExtensionByPath method returns the handle for an already loaded extension library. |
| [IDebugControl2::GetExtensionFunction](nf-dbgeng-idebugcontrol2-getextensionfunction.md) | The GetExtensionFunction method returns a pointer to an extension function from an extension library. |
| [IDebugControl2::GetInterrupt](nf-dbgeng-idebugcontrol2-getinterrupt.md) | The GetInterrupt method checks whether a user interrupt was issued. |
| [IDebugControl2::GetInterruptTimeout](nf-dbgeng-idebugcontrol2-getinterrupttimeout.md) | The GetInterruptTimeout method returns the number of seconds that the engine will wait when requesting a break into the debugger. |
| [IDebugControl2::GetLastEventInformation](nf-dbgeng-idebugcontrol2-getlasteventinformation.md) | The GetLastEventInformation method returns information about the last event that occurred in a target. |
| [IDebugControl2::GetLogFile](nf-dbgeng-idebugcontrol2-getlogfile.md) | The GetLogFile method returns the name of the currently open log file. |
| [IDebugControl2::GetLogMask](nf-dbgeng-idebugcontrol2-getlogmask.md) | The GetLogMask method returns the output mask for the currently open log file. |
| [IDebugControl2::GetNearInstruction](nf-dbgeng-idebugcontrol2-getnearinstruction.md) | The GetNearInstruction method returns the location of a processor instruction relative to a given location. |
| [IDebugControl2::GetNotifyEventHandle](nf-dbgeng-idebugcontrol2-getnotifyeventhandle.md) | The GetNotifyEventHandle method receives the handle of the event that will be signaled after the next exception in a target. |
| [IDebugControl2::GetNumberBreakpoints](nf-dbgeng-idebugcontrol2-getnumberbreakpoints.md) | The GetNumberBreakpoints method returns the number of breakpoints for the current process. |
| [IDebugControl2::GetNumberEventFilters](nf-dbgeng-idebugcontrol2-getnumbereventfilters.md) | The GetNumberEventFilters method returns the number of event filters currently used by the engine. |
| [IDebugControl2::GetNumberPossibleExecutingProcessorTypes](nf-dbgeng-idebugcontrol2-getnumberpossibleexecutingprocessortypes.md) | The GetNumberPossibleExecutingProcessorTypes method returns the number of processor types that are supported by the computer running the current target. |
| [IDebugControl2::GetNumberProcessors](nf-dbgeng-idebugcontrol2-getnumberprocessors.md) | The GetNumberProcessors method returns the number of processors on the computer running the current target. |
| [IDebugControl2::GetNumberSupportedProcessorTypes](nf-dbgeng-idebugcontrol2-getnumbersupportedprocessortypes.md) | The GetNumberSupportedProcessorTypes method returns the number of processor types supported by the engine. |
| [IDebugControl2::GetNumberTextReplacements](nf-dbgeng-idebugcontrol2-getnumbertextreplacements.md) | The GetNumberTextReplacements method returns the number of currently defined user-named and automatic aliases. |
| [IDebugControl2::GetPageSize](nf-dbgeng-idebugcontrol2-getpagesize.md) | The GetPageSize method returns the page size for the effective processor mode. |
| [IDebugControl2::GetPossibleExecutingProcessorTypes](nf-dbgeng-idebugcontrol2-getpossibleexecutingprocessortypes.md) | The GetPossibleExecutingProcessorTypes method returns the processor types that are supported by the computer running the current target. |
| [IDebugControl2::GetProcessorTypeNames](nf-dbgeng-idebugcontrol2-getprocessortypenames.md) | The GetProcessorTypeNames method returns the full name and abbreviated name of the specified processor type. |
| [IDebugControl2::GetPromptText](nf-dbgeng-idebugcontrol2-getprompttext.md) | The GetPromptText method returns the standard prompt text that will be prepended to the formatted output specified in the OutputPrompt and OutputPromptVaList methods. |
| [IDebugControl2::GetRadix](nf-dbgeng-idebugcontrol2-getradix.md) | The GetRadix method returns the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [IDebugControl2::GetReturnOffset](nf-dbgeng-idebugcontrol2-getreturnoffset.md) | The GetReturnOffset method returns the return address for the current function. |
| [IDebugControl2::GetSpecificFilterArgument](nf-dbgeng-idebugcontrol2-getspecificfilterargument.md) | The GetSpecificFilterArgument method returns the value of filter argument for thespecific filters that have an argument. |
| [IDebugControl2::GetSpecificFilterParameters](nf-dbgeng-idebugcontrol2-getspecificfilterparameters.md) | The GetSpecificFilterParameters method returns the parameters for specific event filters. |
| [IDebugControl2::GetStackTrace](nf-dbgeng-idebugcontrol2-getstacktrace.md) | The GetStackTrace method returns the frames at the top of the specified call stack. |
| [IDebugControl2::GetSupportedProcessorTypes](nf-dbgeng-idebugcontrol2-getsupportedprocessortypes.md) | The GetSupportedProcessorTypes method returns the processor types supported by the debugger engine. |
| [IDebugControl2::GetSystemErrorControl](nf-dbgeng-idebugcontrol2-getsystemerrorcontrol.md) | The GetSystemErrorControl method returns the control values for handling system errors. |
| [IDebugControl2::GetSystemVersion](nf-dbgeng-idebugcontrol2-getsystemversion.md) | The GetSystemVersion method returns information that identifies the operating system on the computer that is running the current target. |
| [IDebugControl2::GetTextMacro](nf-dbgeng-idebugcontrol2-gettextmacro.md) | The GetTextMacro method returns the value of a fixed-name alias. |
| [IDebugControl2::GetTextReplacement](nf-dbgeng-idebugcontrol2-gettextreplacement.md) | The GetTextReplacement method returns the value of a user-named alias or an automatic alias. |
| [IDebugControl2::GetWindbgExtensionApis32](nf-dbgeng-idebugcontrol2-getwindbgextensionapis32.md) | The GetWindbgExtensionApis32 method returns a structure that facilitates using the WdbgExts API. |
| [IDebugControl2::GetWindbgExtensionApis64](nf-dbgeng-idebugcontrol2-getwindbgextensionapis64.md) | The GetWindbgExtensionApis64 method returns a structure that facilitates using the WdbgExts API. |
| [IDebugControl2::IsPointer64Bit](nf-dbgeng-idebugcontrol2-ispointer64bit.md) | The IsPointer64Bit method determines if the effective processor uses 64-bit pointers. |
| [IDebugControl2::OpenLogFile](nf-dbgeng-idebugcontrol2-openlogfile.md) | The OpenLogFile method opens a log file that will receive output from the client objects. |
| [IDebugControl2::Output](nf-dbgeng-idebugcontrol2-output.md) | The Output method formats a string and send the result to output callbacks that have been registered with the engine's clients. |
| [IDebugControl2::OutputCurrentState](nf-dbgeng-idebugcontrol2-outputcurrentstate.md) | The OutputCurrentState method prints the current state of the current target to the debugger console. |
| [IDebugControl2::OutputDisassembly](nf-dbgeng-idebugcontrol2-outputdisassembly.md) | The OutputDisassembly method disassembles a processor instruction and sends the disassembly to the output callbacks. |
| [IDebugControl2::OutputDisassemblyLines](nf-dbgeng-idebugcontrol2-outputdisassemblylines.md) | The OutputDisassemblyLines method disassembles several processor instructions and sends the resulting assembly instructions to the output callbacks. |
| [IDebugControl2::OutputPrompt](nf-dbgeng-idebugcontrol2-outputprompt.md) | The OutputPrompt method formats and sends a user prompt to the output callback objects. |
| [IDebugControl2::OutputPromptVaList](nf-dbgeng-idebugcontrol2-outputpromptvalist.md) | The OutputPromptVaList method formats and sends a user prompt to the output callback objects. |
| [IDebugControl2::OutputStackTrace](nf-dbgeng-idebugcontrol2-outputstacktrace.md) | The OutputStackTrace method outputs either the supplied stack frame or the current stack frames. |
| [IDebugControl2::OutputTextReplacements](nf-dbgeng-idebugcontrol2-outputtextreplacements.md) | The OutputTextReplacements method prints all the currently defined user-named aliases to the debugger's output stream. |
| [IDebugControl2::OutputVaList](nf-dbgeng-idebugcontrol2-outputvalist.md) | The OutputVaList method formats a string and sends the result to the output callbacks that are registered with the engine's clients. |
| [IDebugControl2::OutputVersionInformation](nf-dbgeng-idebugcontrol2-outputversioninformation.md) | The OutputVersionInformation method prints version information about the debugger engine to the debugger console. |
| [IDebugControl2::ReadBugCheckData](nf-dbgeng-idebugcontrol2-readbugcheckdata.md) | The ReadBugCheckData method reads the kernel bug check code and related parameters. |
| [IDebugControl2::RemoveBreakpoint](nf-dbgeng-idebugcontrol2-removebreakpoint.md) | The RemoveBreakpoint method removes a breakpoint. |
| [IDebugControl2::RemoveEngineOptions](nf-dbgeng-idebugcontrol2-removeengineoptions.md) | The RemoveEngineOptions method turns off some of the engine's options. |
| [IDebugControl2::RemoveExtension](nf-dbgeng-idebugcontrol2-removeextension.md) | The RemoveExtension method unloads an extension library. |
| [IDebugControl2::RemoveTextReplacements](nf-dbgeng-idebugcontrol2-removetextreplacements.md) | The RemoveTextReplacements method removes all user-named aliases. |
| [IDebugControl2::ReturnInput](nf-dbgeng-idebugcontrol2-returninput.md) | The ReturnInput method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input. |
| [IDebugControl2::SetCodeLevel](nf-dbgeng-idebugcontrol2-setcodelevel.md) | The SetCodeLevel method sets the current code level and is mainly used when stepping through code. |
| [IDebugControl2::SetEffectiveProcessorType](nf-dbgeng-idebugcontrol2-seteffectiveprocessortype.md) | The SetEffectiveProcessorType method sets the effective processor type of the processor of the computer that is running the target. |
| [IDebugControl2::SetEngineOptions](nf-dbgeng-idebugcontrol2-setengineoptions.md) | The SetEngineOptions method changes the engine's options. |
| [IDebugControl2::SetEventFilterCommand](nf-dbgeng-idebugcontrol2-seteventfiltercommand.md) | The SetEventFilterCommand method sets a debugger command for the engine to execute when a specified event occurs. |
| [IDebugControl2::SetExceptionFilterParameters](nf-dbgeng-idebugcontrol2-setexceptionfilterparameters.md) | The SetExceptionFilterParameters method changes the break status and handling status for some exception filters. |
| [IDebugControl2::SetExceptionFilterSecondCommand](nf-dbgeng-idebugcontrol2-setexceptionfiltersecondcommand.md) | The SetExceptionFilterSecondCommand method sets the command that will be executed by the debugger engine on the second chance of a specified exception. |
| [IDebugControl2::SetExecutionStatus](nf-dbgeng-idebugcontrol2-setexecutionstatus.md) | The SetExecutionStatus method requests that the debugger engine enter an executable state. Actual execution will not occur until the next time WaitForEvent is called. |
| [IDebugControl2::SetInterrupt](nf-dbgeng-idebugcontrol2-setinterrupt.md) | The SetInterrupt method registers a user interrupt or breaks into the debugger. |
| [IDebugControl2::SetInterruptTimeout](nf-dbgeng-idebugcontrol2-setinterrupttimeout.md) | The SetInterruptTimeout method sets the number of seconds that the debugger engine should wait when requesting a break into the debugger. |
| [IDebugControl2::SetLogMask](nf-dbgeng-idebugcontrol2-setlogmask.md) | The SetLogMask method sets the output mask for the currently open log file. |
| [IDebugControl2::SetNotifyEventHandle](nf-dbgeng-idebugcontrol2-setnotifyeventhandle.md) | The SetNotifyEventHandle method sets the event that will be signaled after the next exception in a target. |
| [IDebugControl2::SetRadix](nf-dbgeng-idebugcontrol2-setradix.md) | The SetRadix method sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [IDebugControl2::SetSpecificFilterArgument](nf-dbgeng-idebugcontrol2-setspecificfilterargument.md) | The SetSpecificFilterArgument method sets the value of filter argument for the specific filters that can have an argument. |
| [IDebugControl2::SetSpecificFilterParameters](nf-dbgeng-idebugcontrol2-setspecificfilterparameters.md) | The SetSpecificFilterParameters method changes the break status and handling status for some specific event filters. |
| [IDebugControl2::SetSystemErrorControl](nf-dbgeng-idebugcontrol2-setsystemerrorcontrol.md) | The SetSystemErrorControl method sets the control values for handling system errors. |
| [IDebugControl2::SetTextMacro](nf-dbgeng-idebugcontrol2-settextmacro.md) | The SetTextMacro method sets the value of a fixed-name alias. |
| [IDebugControl2::SetTextReplacement](nf-dbgeng-idebugcontrol2-settextreplacement.md) | The SetTextReplacement method sets the value of a user-named alias. |
| [IDebugControl2::WaitForEvent](nf-dbgeng-idebugcontrol2-waitforevent.md) | The WaitForEvent method waits for an event that breaks into the debugger engine application. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>



<a href="..\dbgeng\nn-dbgeng-idebugcontrol4.md">IDebugControl4</a>



<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>