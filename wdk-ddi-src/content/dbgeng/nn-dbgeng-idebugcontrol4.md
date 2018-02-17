---
UID: NN:dbgeng.IDebugControl4
title: IDebugControl4
author: windows-driver-content
description: IDebugControl4 interface
old-location: debugger\idebugcontrol4.htm
old-project: debugger
ms.assetid: 693207c2-70d7-45be-ae22-436555225928
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugcontrol4, IDebugControl4 interface [Windows Debugging], IDebugControl4 interface [Windows Debugging], described, IDebugControl4, dbgeng/IDebugControl4
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
-	IDebugControl4
-	IDebugControl4.GetManagedStatus
-	IDebugControl4.GetManagedStatusWide
-	IDebugControl4.ResetManagedStatus
product: Windows
targetos: Windows
req.typenames: "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---

# IDebugControl4 interface



## Methods

<p>The <b>IDebugControl4</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugControl4.AddBreakpoint2](nf-dbgeng-idebugcontrol4-addbreakpoint2.md) | The AddBreakpoint2 method creates a new breakpoint for the current target. |
| [dbgeng.IDebugControl4.AddExtensionWide](nf-dbgeng-idebugcontrol4-addextensionwide.md) | The AddExtensionWide method loads an extension library into the debugger engine. |
| [dbgeng.IDebugControl4.AssembleWide](nf-dbgeng-idebugcontrol4-assemblewide.md) | The AssembleWide method assembles a single processor instruction. The assembled instruction is placed in the target's memory. |
| [dbgeng.IDebugControl4.CallExtensionWide](nf-dbgeng-idebugcontrol4-callextensionwide.md) | The CallExtensionWide method calls a debugger extension. |
| [dbgeng.IDebugControl4.ControlledOutputVaListWide](nf-dbgeng-idebugcontrol4-controlledoutputvalistwide.md) | The ControlledOutputVaListWide method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [dbgeng.IDebugControl4.ControlledOutputWide](nf-dbgeng-idebugcontrol4-controlledoutputwide.md) | The ControlledOutputWide method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [dbgeng.IDebugControl4.DisassembleWide](nf-dbgeng-idebugcontrol4-disassemblewide.md) | The DisassembleWide method disassembles a processor instruction in the target's memory. |
| [dbgeng.IDebugControl4.EvaluateWide](nf-dbgeng-idebugcontrol4-evaluatewide.md) | The EvaluateWide method evaluates an expression, returning the result. |
| [dbgeng.IDebugControl4.ExecuteCommandFileWide](nf-dbgeng-idebugcontrol4-executecommandfilewide.md) | The ExecuteCommandFileWide method opens the specified file and executes the debugger commands that are contained within. |
| [dbgeng.IDebugControl4.ExecuteWide](nf-dbgeng-idebugcontrol4-executewide.md) | The ExecuteWide method executes the specified debugger commands. |
| [dbgeng.IDebugControl4.GetBreakpointById2](nf-dbgeng-idebugcontrol4-getbreakpointbyid2.md) | The GetBreakpointById2 method returns the breakpoint with the specified breakpoint ID. |
| [dbgeng.IDebugControl4.GetBreakpointByIndex2](nf-dbgeng-idebugcontrol4-getbreakpointbyindex2.md) | The GetBreakpointByIndex2 method returns the breakpoint located at the specified index. |
| [dbgeng.IDebugControl4.GetContextStackTrace](nf-dbgeng-idebugcontrol4-getcontextstacktrace.md) | The GetContextStackTrace method returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame. |
| [dbgeng.IDebugControl4.GetEventFilterCommandWide](nf-dbgeng-idebugcontrol4-geteventfiltercommandwide.md) | The GetEventFilterCommandWide method returns the debugger command that the engine will execute when a specified event occurs. |
| [dbgeng.IDebugControl4.GetEventFilterTextWide](nf-dbgeng-idebugcontrol4-geteventfiltertextwide.md) | The GetEventFilterTextWide method returns a short description of an event for a specific filter. |
| [dbgeng.IDebugControl4.GetEventIndexDescriptionWide](nf-dbgeng-idebugcontrol4-geteventindexdescriptionwide.md) | The GetEventIndexDescriptionWide method describes the specified event in a static list of events for the current target. |
| [dbgeng.IDebugControl4.GetExceptionFilterSecondCommand](nf-dbgeng-idebugcontrol4-getexceptionfiltersecondcommand.md) | The GetExceptionFilterSecondCommandWide method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [dbgeng.IDebugControl4.GetExceptionFilterSecondCommandWide](nf-dbgeng-idebugcontrol4-getexceptionfiltersecondcommandwide.md) | The GetExceptionFilterSecondCommandWide method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [dbgeng.IDebugControl4.GetExpressionSyntaxNamesWide](nf-dbgeng-idebugcontrol4-getexpressionsyntaxnameswide.md) | The GetExpressionSyntaxNamesWide method returns the full and abbreviated names of an expression syntax. |
| [dbgeng.IDebugControl4.GetExtensionByPathWide](nf-dbgeng-idebugcontrol4-getextensionbypathwide.md) | The GetExtensionByPathWide method returns the handle for an already loaded extension library. |
| [dbgeng.IDebugControl4.GetExtensionFunctionWide](nf-dbgeng-idebugcontrol4-getextensionfunctionwide.md) | The GetExtensionFunctionWide method returns a pointer to an extension function from an extension library. |
| [dbgeng.IDebugControl4.GetLastEventInformationWide](nf-dbgeng-idebugcontrol4-getlasteventinformationwide.md) | The GetLastEventInformationWide method returns information about the last event that occurred in a target. |
| [dbgeng.IDebugControl4.GetLogFile2](nf-dbgeng-idebugcontrol4-getlogfile2.md) | The GetLogFile2 method returns the name of the currently open log file. |
| [dbgeng.IDebugControl4.GetLogFile2Wide](nf-dbgeng-idebugcontrol4-getlogfile2wide.md) | The GetLogFile2Wide method returns the name of the currently open log file. |
| [dbgeng.IDebugControl4.GetLogFileWide](nf-dbgeng-idebugcontrol4-getlogfilewide.md) | The GetLogFileWide method returns the name of the currently open log file. |
| [dbgeng.IDebugControl4.GetManagedStatus](nf-dbgeng-idebugcontrol4-getmanagedstatus.md) | Provides feedback on the engine's use of the runtime debugging APIs provided by the common language runtime (CLR). |
| [dbgeng.IDebugControl4.GetManagedStatusWide](nf-dbgeng-idebugcontrol4-getmanagedstatuswide.md) | Provides feedback as a Unicode character string on the engine's use of the runtime debugging APIs provided by the common language runtime (CLR). |
| [dbgeng.IDebugControl4.GetProcessorTypeNamesWide](nf-dbgeng-idebugcontrol4-getprocessortypenameswide.md) | The GetProcessorTypeNamesWide method returns the full name and abbreviated name of the specified processor type. |
| [dbgeng.IDebugControl4.GetPromptTextWide](nf-dbgeng-idebugcontrol4-getprompttextwide.md) | The GetPromptTextWide method returns the standard prompt text that will be prepended to the formatted output specified in the OutputPrompt and OutputPromptVaList methods. |
| [dbgeng.IDebugControl4.GetSpecificFilterArgumentWide](nf-dbgeng-idebugcontrol4-getspecificfilterargumentwide.md) | The GetSpecificFilterArgumentWide method returns the value of filter argument for thespecific filters that have an argument. |
| [dbgeng.IDebugControl4.GetStoredEventInformation](nf-dbgeng-idebugcontrol4-getstoredeventinformation.md) | The GetStoredEventInformation method retrieves information about an event of interest available in the current target. |
| [dbgeng.IDebugControl4.GetSystemVersionString](nf-dbgeng-idebugcontrol4-getsystemversionstring.md) | The GetSystemVersionString method returns a string that describes the target's operating system version. |
| [dbgeng.IDebugControl4.GetSystemVersionStringWide](nf-dbgeng-idebugcontrol4-getsystemversionstringwide.md) | The GetSystemVersionStringWide method returns a string that describes the target's operating system version. |
| [dbgeng.IDebugControl4.GetSystemVersionValues](nf-dbgeng-idebugcontrol4-getsystemversionvalues.md) | The GetSystemVersionValues method returns version number information for the current target. |
| [dbgeng.IDebugControl4.GetTextMacroWide](nf-dbgeng-idebugcontrol4-gettextmacrowide.md) | The GetTextMacroWide method returns the value of a fixed-name alias. |
| [dbgeng.IDebugControl4.GetTextReplacementWide](nf-dbgeng-idebugcontrol4-gettextreplacementwide.md) | The GetTextReplacementWide method returns the value of a user-named alias or an automatic alias. |
| [dbgeng.IDebugControl4.InputWide](nf-dbgeng-idebugcontrol4-inputwide.md) | The InputWide method requests an input string from the debugger engine. |
| [dbgeng.IDebugControl4.OpenLogFile2](nf-dbgeng-idebugcontrol4-openlogfile2.md) | The OpenLogFile2 method opens a log file that will receive output from the client objects. |
| [dbgeng.IDebugControl4.OpenLogFile2Wide](nf-dbgeng-idebugcontrol4-openlogfile2wide.md) | The OpenLogFile2Wide method opens a log file that will receive output from the client objects. |
| [dbgeng.IDebugControl4.OpenLogFileWide](nf-dbgeng-idebugcontrol4-openlogfilewide.md) | The OpenLogFileWide method opens a log file that will receive output from the client objects. |
| [dbgeng.IDebugControl4.OutputContextStackTrace](nf-dbgeng-idebugcontrol4-outputcontextstacktrace.md) | The OutputContextStackTrace method prints the call stack specified by an array of stack frames and corresponding register contexts. |
| [dbgeng.IDebugControl4.OutputPromptVaListWide](nf-dbgeng-idebugcontrol4-outputpromptvalistwide.md) | The OutputPromptVaListWide method formats and sends a user prompt to the output callback objects. |
| [dbgeng.IDebugControl4.OutputPromptWide](nf-dbgeng-idebugcontrol4-outputpromptwide.md) | The OutputPromptWide method formats and sends a user prompt to the output callback objects. |
| [dbgeng.IDebugControl4.OutputVaListWide](nf-dbgeng-idebugcontrol4-outputvalistwide.md) | The OutputVaListWide method formats a string and sends the result to the output callbacks that are registered with the engine's clients. |
| [dbgeng.IDebugControl4.OutputWide](nf-dbgeng-idebugcontrol4-outputwide.md) | The OutputWide method formats a string and send the result to output callbacks that have been registered with the engine's clients. |
| [dbgeng.IDebugControl4.RemoveBreakpoint2](nf-dbgeng-idebugcontrol4-removebreakpoint2.md) | The RemoveBreakpoint2 method removes a breakpoint. |
| [dbgeng.IDebugControl4.ResetManagedStatus](nf-dbgeng-idebugcontrol4-resetmanagedstatus.md) | Clears and reinitializes the engine's managed code debugging support of the runtime debugging APIs provided by the common language runtime (CLR). |
| [dbgeng.IDebugControl4.ReturnInputWide](nf-dbgeng-idebugcontrol4-returninputwide.md) | The ReturnInputWide method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input. |
| [dbgeng.IDebugControl4.SetEventFilterCommandWide](nf-dbgeng-idebugcontrol4-seteventfiltercommandwide.md) | The SetEventFilterCommandWide method sets a debugger command for the engine to execute when a specified event occurs. |
| [dbgeng.IDebugControl4.SetExceptionFilterSecondCommandWide](nf-dbgeng-idebugcontrol4-setexceptionfiltersecondcommandwide.md) | The SetExceptionFilterSecondCommandWide method sets the command that will be executed by the debugger engine on the second chance of a specified exception. |
| [dbgeng.IDebugControl4.SetExpressionSyntaxByNameWide](nf-dbgeng-idebugcontrol4-setexpressionsyntaxbynamewide.md) | The SetExpressionSyntaxByNameWide method sets the syntax that the engine will use to evaluate expressions. |
| [dbgeng.IDebugControl4.SetSpecificFilterArgumentWide](nf-dbgeng-idebugcontrol4-setspecificfilterargumentwide.md) | The SetSpecificFilterArgumentWide method sets the value of filter argument for the specific filters that can have an argument. |
| [dbgeng.IDebugControl4.SetTextMacroWide](nf-dbgeng-idebugcontrol4-settextmacrowide.md) | The SetTextMacroWide method sets the value of a fixed-name alias. |
| [dbgeng.IDebugControl4.SetTextReplacementWide](nf-dbgeng-idebugcontrol4-settextreplacementwide.md) | The SetTextReplacementWide method sets the value of a user-named alias. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>



<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>



<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4 interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>