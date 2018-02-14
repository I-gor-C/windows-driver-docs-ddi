---
UID: NN:dbgeng.IDebugControl
title: IDebugControl
author: windows-driver-content
description: IDebugControl interface
old-location: debugger\idebugcontrol.htm
old-project: debugger
ms.assetid: 6ff5b9ff-d2b8-4ade-8b8b-20284efdf266
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugcontrol, IDebugControl interface [Windows Debugging], IDebugControl interface [Windows Debugging], described, IDebugControl, dbgeng/IDebugControl, IDebugControl_ce0030b2-73a7-49a8-9d21-942922a69184.xml
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
req.lib: dbgeng.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	dbgeng.h
apiname:
-	IDebugControl
-	IDebugControl.GetWindbgExtensionApis32
product: Windows
targetos: Windows
req.typenames: "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---

# IDebugControl interface



## Methods

<p>The <b>IDebugControl</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugControl.AddBreakpoint](nf-dbgeng-idebugcontrol-addbreakpoint.md) | The AddBreakpoint method creates a new breakpoint for the current target. |
| [dbgeng.IDebugControl.AddEngineOptions](nf-dbgeng-idebugcontrol-addengineoptions.md) | The AddEngineOptions method turns on some of the debugger engine's options. |
| [dbgeng.IDebugControl.AddExtension](nf-dbgeng-idebugcontrol-addextension.md) | The AddExtension method loads an extension library into the debugger engine. |
| [dbgeng.IDebugControl.Assemble](nf-dbgeng-idebugcontrol-assemble.md) | The Assemble method assembles a single processor instruction. The assembled instruction is placed in the target's memory. |
| [dbgeng.IDebugControl.CallExtension](nf-dbgeng-idebugcontrol-callextension.md) | The CallExtension method calls a debugger extension. |
| [dbgeng.IDebugControl.CloseLogFile](nf-dbgeng-idebugcontrol-closelogfile.md) | The CloseLogFile method closes the currently-open log file. |
| [dbgeng.IDebugControl.CoerceValue](nf-dbgeng-idebugcontrol-coercevalue.md) | The CoerceValue method converts a value of one type into a value of another type. |
| [dbgeng.IDebugControl.CoerceValues](nf-dbgeng-idebugcontrol-coercevalues.md) | The CoerceValues method converts an array of values into an array of values of different types. |
| [dbgeng.IDebugControl.ControlledOutput](nf-dbgeng-idebugcontrol-controlledoutput.md) | The ControlledOutput method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [dbgeng.IDebugControl.ControlledOutputVaList](nf-dbgeng-idebugcontrol-controlledoutputvalist.md) | The ControlledOutputVaList method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [dbgeng.IDebugControl.Disassemble](nf-dbgeng-idebugcontrol-disassemble.md) | The Disassemble method disassembles a processor instruction in the target's memory. |
| [dbgeng.IDebugControl.Evaluate](nf-dbgeng-idebugcontrol-evaluate.md) | The Evaluate method evaluates an expression, returning the result. |
| [dbgeng.IDebugControl.Execute](nf-dbgeng-idebugcontrol-execute.md) | The Execute method executes the specified debugger commands. |
| [dbgeng.IDebugControl.ExecuteCommandFile](nf-dbgeng-idebugcontrol-executecommandfile.md) | The ExecuteCommandFile method opens the specified file and executes the debugger commands that are contained within. |
| [dbgeng.IDebugControl.GetActualProcessorType](nf-dbgeng-idebugcontrol-getactualprocessortype.md) | The GetActualProcessorType method returns the processor type of the physical processor of the computer that is running the target. |
| [dbgeng.IDebugControl.GetBreakpointById](nf-dbgeng-idebugcontrol-getbreakpointbyid.md) | The GetBreakpointById method returns the breakpoint with the specified breakpoint ID. |
| [dbgeng.IDebugControl.GetBreakpointByIndex](nf-dbgeng-idebugcontrol-getbreakpointbyindex.md) | The GetBreakpointByIndex method returns the breakpoint located at the specified index. |
| [dbgeng.IDebugControl.GetBreakpointParameters](nf-dbgeng-idebugcontrol-getbreakpointparameters.md) | The GetBreakpointParameters method returns the parameters of one or more breakpoints. |
| [dbgeng.IDebugControl.GetCodeLevel](nf-dbgeng-idebugcontrol-getcodelevel.md) | The GetCodeLevel method returns the current code level and is mainly used when stepping through code. |
| [dbgeng.IDebugControl.GetDebuggeeType](nf-dbgeng-idebugcontrol-getdebuggeetype.md) | The GetDebuggeeType method describes the nature of the current target. |
| [dbgeng.IDebugControl.GetDisassembleEffectiveOffset](nf-dbgeng-idebugcontrol-getdisassembleeffectiveoffset.md) | The GetDisassembleEffectiveOffset method returns the address of the last instruction disassembled using Disassemble. |
| [dbgeng.IDebugControl.GetEffectiveProcessorType](nf-dbgeng-idebugcontrol-geteffectiveprocessortype.md) | The GetEffectiveProcessorType method returns the effective processor type of the processor of the computer that is running the target. |
| [dbgeng.IDebugControl.GetEngineOptions](nf-dbgeng-idebugcontrol-getengineoptions.md) | The GetEngineOptions method returns the engine's options. |
| [dbgeng.IDebugControl.GetEventFilterCommand](nf-dbgeng-idebugcontrol-geteventfiltercommand.md) | The GetEventFilterCommand method returns the debugger command that the engine will execute when a specified event occurs. |
| [dbgeng.IDebugControl.GetEventFilterText](nf-dbgeng-idebugcontrol-geteventfiltertext.md) | The GetEventFilterText method returns a short description of an event for a specific filter. |
| [dbgeng.IDebugControl.GetExceptionFilterParameters](nf-dbgeng-idebugcontrol-getexceptionfilterparameters.md) | The GetExceptionFilterParameters method returns the parameters for exception filters specified by exception codes or by index. |
| [dbgeng.IDebugControl.GetExceptionFilterSecondCommand](nf-dbgeng-idebugcontrol-getexceptionfiltersecondcommand.md) | The GetExceptionFilterSecondCommand method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [dbgeng.IDebugControl.GetExecutingProcessorType](nf-dbgeng-idebugcontrol-getexecutingprocessortype.md) | The GetExecutingProcessorType method returns the executing processor type for the processor for which the last event occurred. |
| [dbgeng.IDebugControl.GetExecutionStatus](nf-dbgeng-idebugcontrol-getexecutionstatus.md) | The GetExecutionStatus method returns information about the execution status of the debugger engine. |
| [dbgeng.IDebugControl.GetExtensionByPath](nf-dbgeng-idebugcontrol-getextensionbypath.md) | The GetExtensionByPath method returns the handle for an already loaded extension library. |
| [dbgeng.IDebugControl.GetExtensionFunction](nf-dbgeng-idebugcontrol-getextensionfunction.md) | The GetExtensionFunction method returns a pointer to an extension function from an extension library. |
| [dbgeng.IDebugControl.GetInterrupt](nf-dbgeng-idebugcontrol-getinterrupt.md) | The GetInterrupt method checks whether a user interrupt was issued. |
| [dbgeng.IDebugControl.GetInterruptTimeout](nf-dbgeng-idebugcontrol-getinterrupttimeout.md) | The GetInterruptTimeout method returns the number of seconds that the engine will wait when requesting a break into the debugger. |
| [dbgeng.IDebugControl.GetLastEventInformation](nf-dbgeng-idebugcontrol-getlasteventinformation.md) | The GetLastEventInformation method returns information about the last event that occurred in a target. |
| [dbgeng.IDebugControl.GetLogFile](nf-dbgeng-idebugcontrol-getlogfile.md) | The GetLogFile method returns the name of the currently open log file. |
| [dbgeng.IDebugControl.GetLogMask](nf-dbgeng-idebugcontrol-getlogmask.md) | The GetLogMask method returns the output mask for the currently open log file. |
| [dbgeng.IDebugControl.GetNearInstruction](nf-dbgeng-idebugcontrol-getnearinstruction.md) | The GetNearInstruction method returns the location of a processor instruction relative to a given location. |
| [dbgeng.IDebugControl.GetNotifyEventHandle](nf-dbgeng-idebugcontrol-getnotifyeventhandle.md) | The GetNotifyEventHandle method receives the handle of the event that will be signaled after the next exception in a target. |
| [dbgeng.IDebugControl.GetNumberBreakpoints](nf-dbgeng-idebugcontrol-getnumberbreakpoints.md) | The GetNumberBreakpoints method returns the number of breakpoints for the current process. |
| [dbgeng.IDebugControl.GetNumberEventFilters](nf-dbgeng-idebugcontrol-getnumbereventfilters.md) | The GetNumberEventFilters method returns the number of event filters currently used by the engine. |
| [dbgeng.IDebugControl.GetNumberPossibleExecutingProcessorTypes](nf-dbgeng-idebugcontrol-getnumberpossibleexecutingprocessortypes.md) | The GetNumberPossibleExecutingProcessorTypes method returns the number of processor types that are supported by the computer running the current target. |
| [dbgeng.IDebugControl.GetNumberProcessors](nf-dbgeng-idebugcontrol-getnumberprocessors.md) | The GetNumberProcessors method returns the number of processors on the computer running the current target. |
| [dbgeng.IDebugControl.GetNumberSupportedProcessorTypes](nf-dbgeng-idebugcontrol-getnumbersupportedprocessortypes.md) | The GetNumberSupportedProcessorTypes method returns the number of processor types supported by the engine. |
| [dbgeng.IDebugControl.GetPageSize](nf-dbgeng-idebugcontrol-getpagesize.md) | The GetPageSize method returns the page size for the effective processor mode. |
| [dbgeng.IDebugControl.GetPossibleExecutingProcessorTypes](nf-dbgeng-idebugcontrol-getpossibleexecutingprocessortypes.md) | The GetPossibleExecutingProcessorTypes method returns the processor types that are supported by the computer running the current target. |
| [dbgeng.IDebugControl.GetProcessorTypeNames](nf-dbgeng-idebugcontrol-getprocessortypenames.md) | The GetProcessorTypeNames method returns the full name and abbreviated name of the specified processor type. |
| [dbgeng.IDebugControl.GetPromptText](nf-dbgeng-idebugcontrol-getprompttext.md) | The GetPromptText method returns the standard prompt text that will be prepended to the formatted output specified in the OutputPrompt and OutputPromptVaList methods. |
| [dbgeng.IDebugControl.GetRadix](nf-dbgeng-idebugcontrol-getradix.md) | The GetRadix method returns the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [dbgeng.IDebugControl.GetReturnOffset](nf-dbgeng-idebugcontrol-getreturnoffset.md) | The GetReturnOffset method returns the return address for the current function. |
| [dbgeng.IDebugControl.GetSpecificFilterArgument](nf-dbgeng-idebugcontrol-getspecificfilterargument.md) | The GetSpecificFilterArgument method returns the value of filter argument for thespecific filters that have an argument. |
| [dbgeng.IDebugControl.GetSpecificFilterParameters](nf-dbgeng-idebugcontrol-getspecificfilterparameters.md) | The GetSpecificFilterParameters method returns the parameters for specific event filters. |
| [dbgeng.IDebugControl.GetStackTrace](nf-dbgeng-idebugcontrol-getstacktrace.md) | The GetStackTrace method returns the frames at the top of the specified call stack. |
| [dbgeng.IDebugControl.GetSupportedProcessorTypes](nf-dbgeng-idebugcontrol-getsupportedprocessortypes.md) | The GetSupportedProcessorTypes method returns the processor types supported by the debugger engine. |
| [dbgeng.IDebugControl.GetSystemErrorControl](nf-dbgeng-idebugcontrol-getsystemerrorcontrol.md) | The GetSystemErrorControl method returns the control values for handling system errors. |
| [dbgeng.IDebugControl.GetSystemVersion](nf-dbgeng-idebugcontrol-getsystemversion.md) | The GetSystemVersion method returns information that identifies the operating system on the computer that is running the current target. |
| [dbgeng.IDebugControl.GetTextMacro](nf-dbgeng-idebugcontrol-gettextmacro.md) | The GetTextMacro method returns the value of a fixed-name alias. |
| [dbgeng.IDebugControl.GetWindbgExtensionApis32](nf-dbgeng-idebugcontrol-getwindbgextensionapis32.md) | The GetWindbgExtensionApis32 method returns a structure that facilitates using the WdbgExts API. |
| [dbgeng.IDebugControl.GetWindbgExtensionApis64](nf-dbgeng-idebugcontrol-getwindbgextensionapis64.md) | The GetWindbgExtensionApis64 method returns a structure that facilitates using the WdbgExts API. |
| [dbgeng.IDebugControl.Input](nf-dbgeng-idebugcontrol-input.md) | The Input method requests an input string from the debugger engine. |
| [dbgeng.IDebugControl.IsPointer64Bit](nf-dbgeng-idebugcontrol-ispointer64bit.md) | The IsPointer64Bit method determines if the effective processor uses 64-bit pointers. |
| [dbgeng.IDebugControl.OpenLogFile](nf-dbgeng-idebugcontrol-openlogfile.md) | The OpenLogFile method opens a log file that will receive output from the client objects. |
| [dbgeng.IDebugControl.Output](nf-dbgeng-idebugcontrol-output.md) | The Output method formats a string and send the result to output callbacks that have been registered with the engine's clients. |
| [dbgeng.IDebugControl.OutputCurrentState](nf-dbgeng-idebugcontrol-outputcurrentstate.md) | The OutputCurrentState method prints the current state of the current target to the debugger console. |
| [dbgeng.IDebugControl.OutputDisassembly](nf-dbgeng-idebugcontrol-outputdisassembly.md) | The OutputDisassembly method disassembles a processor instruction and sends the disassembly to the output callbacks. |
| [dbgeng.IDebugControl.OutputDisassemblyLines](nf-dbgeng-idebugcontrol-outputdisassemblylines.md) | The OutputDisassemblyLines method disassembles several processor instructions and sends the resulting assembly instructions to the output callbacks. |
| [dbgeng.IDebugControl.OutputPrompt](nf-dbgeng-idebugcontrol-outputprompt.md) | The OutputPrompt method formats and sends a user prompt to the output callback objects. |
| [dbgeng.IDebugControl.OutputPromptVaList](nf-dbgeng-idebugcontrol-outputpromptvalist.md) | The OutputPromptVaList method formats and sends a user prompt to the output callback objects. |
| [dbgeng.IDebugControl.OutputStackTrace](nf-dbgeng-idebugcontrol-outputstacktrace.md) | The OutputStackTrace method outputs either the supplied stack frame or the current stack frames. |
| [dbgeng.IDebugControl.OutputVaList](nf-dbgeng-idebugcontrol-outputvalist.md) | The OutputVaList method formats a string and sends the result to the output callbacks that are registered with the engine's clients. |
| [dbgeng.IDebugControl.OutputVersionInformation](nf-dbgeng-idebugcontrol-outputversioninformation.md) | The OutputVersionInformation method prints version information about the debugger engine to the debugger console. |
| [dbgeng.IDebugControl.ReadBugCheckData](nf-dbgeng-idebugcontrol-readbugcheckdata.md) | The ReadBugCheckData method reads the kernel bug check code and related parameters. |
| [dbgeng.IDebugControl.RemoveBreakpoint](nf-dbgeng-idebugcontrol-removebreakpoint.md) | The RemoveBreakpoint method removes a breakpoint. |
| [dbgeng.IDebugControl.RemoveEngineOptions](nf-dbgeng-idebugcontrol-removeengineoptions.md) | The RemoveEngineOptions method turns off some of the engine's options. |
| [dbgeng.IDebugControl.RemoveExtension](nf-dbgeng-idebugcontrol-removeextension.md) | The RemoveExtension method unloads an extension library. |
| [dbgeng.IDebugControl.ReturnInput](nf-dbgeng-idebugcontrol-returninput.md) | The ReturnInput method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input. |
| [dbgeng.IDebugControl.SetCodeLevel](nf-dbgeng-idebugcontrol-setcodelevel.md) | The SetCodeLevel method sets the current code level and is mainly used when stepping through code. |
| [dbgeng.IDebugControl.SetEffectiveProcessorType](nf-dbgeng-idebugcontrol-seteffectiveprocessortype.md) | The SetEffectiveProcessorType method sets the effective processor type of the processor of the computer that is running the target. |
| [dbgeng.IDebugControl.SetEngineOptions](nf-dbgeng-idebugcontrol-setengineoptions.md) | The SetEngineOptions method changes the engine's options. |
| [dbgeng.IDebugControl.SetEventFilterCommand](nf-dbgeng-idebugcontrol-seteventfiltercommand.md) | The SetEventFilterCommand method sets a debugger command for the engine to execute when a specified event occurs. |
| [dbgeng.IDebugControl.SetExceptionFilterParameters](nf-dbgeng-idebugcontrol-setexceptionfilterparameters.md) | The SetExceptionFilterParameters method changes the break status and handling status for some exception filters. |
| [dbgeng.IDebugControl.SetExceptionFilterSecondCommand](nf-dbgeng-idebugcontrol-setexceptionfiltersecondcommand.md) | The SetExceptionFilterSecondCommand method sets the command that will be executed by the debugger engine on the second chance of a specified exception. |
| [dbgeng.IDebugControl.SetExecutionStatus](nf-dbgeng-idebugcontrol-setexecutionstatus.md) | The SetExecutionStatus method requests that the debugger engine enter an executable state. Actual execution will not occur until the next time WaitForEvent is called. |
| [dbgeng.IDebugControl.SetInterrupt](nf-dbgeng-idebugcontrol-setinterrupt.md) | The SetInterrupt method registers a user interrupt or breaks into the debugger. |
| [dbgeng.IDebugControl.SetInterruptTimeout](nf-dbgeng-idebugcontrol-setinterrupttimeout.md) | The SetInterruptTimeout method sets the number of seconds that the debugger engine should wait when requesting a break into the debugger. |
| [dbgeng.IDebugControl.SetLogMask](nf-dbgeng-idebugcontrol-setlogmask.md) | The SetLogMask method sets the output mask for the currently open log file. |
| [dbgeng.IDebugControl.SetNotifyEventHandle](nf-dbgeng-idebugcontrol-setnotifyeventhandle.md) | The SetNotifyEventHandle method sets the event that will be signaled after the next exception in a target. |
| [dbgeng.IDebugControl.SetRadix](nf-dbgeng-idebugcontrol-setradix.md) | The SetRadix method sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [dbgeng.IDebugControl.SetSpecificFilterArgument](nf-dbgeng-idebugcontrol-setspecificfilterargument.md) | The SetSpecificFilterArgument method sets the value of filter argument for the specific filters that can have an argument. |
| [dbgeng.IDebugControl.SetSpecificFilterParameters](nf-dbgeng-idebugcontrol-setspecificfilterparameters.md) | The SetSpecificFilterParameters method changes the break status and handling status for some specific event filters. |
| [dbgeng.IDebugControl.SetSystemErrorControl](nf-dbgeng-idebugcontrol-setsystemerrorcontrol.md) | The SetSystemErrorControl method sets the control values for handling system errors. |
| [dbgeng.IDebugControl.SetTextMacro](nf-dbgeng-idebugcontrol-settextmacro.md) | The SetTextMacro method sets the value of a fixed-name alias. |
| [dbgeng.IDebugControl.WaitForEvent](nf-dbgeng-idebugcontrol-waitforevent.md) | The WaitForEvent method waits for an event that breaks into the debugger engine application. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>



<a href="..\dbgeng\nn-dbgeng-idebugcontrol4.md">IDebugControl4</a>



<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>