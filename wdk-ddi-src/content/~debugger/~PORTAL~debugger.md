# Declarations in the debugger technology
This technology  contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [IDebugSymbols3::GetSourceEntryBySourceEntry method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentrybysourceentry.md) | Allows navigation within the source entries. |
| [IDebugSymbols3::GetSourceFileLineOffsets method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcefilelineoffsets.md) | The GetSourceFileLineOffsets method maps each line in a source file to a location in the target's memory. |
| [IDebugSystemObjects4::GetProcessIdsByIndex method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidsbyindex.md) | The GetProcessIdsByIndex method returns the engine process ID and system process ID for the specified processes in the current target. |
| [IDebugPlmClient3::EnablePlmPackageDebugWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-enableplmpackagedebugwide.md) | Enables a Process Lifecycle Management (PLM) package debug. |
| [IDebugControl3::Evaluate method](..\dbgeng\nf-dbgeng-idebugcontrol3-evaluate.md) | The Evaluate method evaluates an expression, returning the result. |
| [IDebugClient::GetOutputLinePrefix method](..\dbgeng\nf-dbgeng-idebugclient-getoutputlineprefix.md) | Gets the prefix used for multiple lines of output. |
| [IDebugClient5::SetQuitLockStringWide method](..\dbgeng\nf-dbgeng-idebugclient5-setquitlockstringwide.md) | Sets a quit lock Unicode character string. |
| [IDebugSymbols3::FindSourceFile method](..\dbgeng\nf-dbgeng-idebugsymbols3-findsourcefile.md) | The FindSourceFile method searches the source path for a specified source file. |
| [IDebugRegisters2::GetPseudoIndexByName method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudoindexbyname.md) | The GetPseudoIndexByName method returns the index of a pseudo-register. |
| [IDebugClient5::StartServerWide method](..\dbgeng\nf-dbgeng-idebugclient5-startserverwide.md) | The StartServerWide method starts a debugging server. |
| [IDebugClient5::GetRunningProcessSystemIdByExecutableName method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocesssystemidbyexecutablename.md) | The GetRunningProcessSystemIdByExecutableName method searches for a process with a given executable file name and return its process ID. |
| [IDebugControl3::ReturnInput method](..\dbgeng\nf-dbgeng-idebugcontrol3-returninput.md) | The ReturnInput method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input. |
| [IDebugControl4::SetEventFilterCommandWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-seteventfiltercommandwide.md) | The SetEventFilterCommandWide method sets a debugger command for the engine to execute when a specified event occurs. |
| [IDebugSystemObjects4::SetCurrentProcessId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setcurrentprocessid.md) | The SetCurrentProcessId method makes the specified process the current process. |
| [IDebugSymbolGroup2::GetSymbolRegister method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolregister.md) | The GetSymbolRegister method returns the register that contains the value or a pointer to the value of a symbol in a symbol group. |
| [IDebugSymbols3::GetOffsetByNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsetbynamewide.md) | The GetOffsetByNameWide method returns the location of a symbol identified by name. |
| [IDebugSymbolGroup2::RemoveSymbolByName method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-removesymbolbyname.md) | The RemoveSymbolByName method removes the specified symbol from a symbol group. |
| [IDebugBreakpoint2::GetAdder method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getadder.md) | The GetAdder method returns the client that owns the breakpoint. |
| [IDebugSymbols3::GetSourceEntryString method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentrystring.md) | Queries symbol information and returns locations in the target's memory. |
| [IDebugSystemObjects4::GetCurrentThreadSystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreadsystemid.md) | The GetCurrentThreadSystemId method returns the system thread ID of the current thread. |
| [IDebugRegisters2::GetNumberPseudoRegisters method](..\dbgeng\nf-dbgeng-idebugregisters2-getnumberpseudoregisters.md) | The GetNumberPseudoRegisters method returns the number of pseudo-registers that are maintained by the debugger engine. |
| [IDebugControl4::GetManagedStatus method](..\dbgeng\nf-dbgeng-idebugcontrol4-getmanagedstatus.md) | Provides feedback on the engine's use of the runtime debugging APIs provided by the common language runtime (CLR). |
| [IDebugDataSpaces4::GetNextDifferentlyValidOffsetVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getnextdifferentlyvalidoffsetvirtual.md) | The GetNextDifferentlyValidOffsetVirtual method returns the offset of the next address whose validity might be different from the validity of the specified address. |
| [IDebugClient5::SetOtherOutputMask method](..\dbgeng\nf-dbgeng-idebugclient5-setotheroutputmask.md) | The SetOtherOutputMask method sets the output mask for another client. |
| [IDebugSymbols3::EndSymbolMatch method](..\dbgeng\nf-dbgeng-idebugsymbols3-endsymbolmatch.md) | The EndSymbolMatch method releases the resources used by a symbol search. |
| [IDebugControl3::ControlledOutputVaList method](..\dbgeng\nf-dbgeng-idebugcontrol3-controlledoutputvalist.md) | The ControlledOutputVaList method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugClient5::GetKernelConnectionOptionsWide method](..\dbgeng\nf-dbgeng-idebugclient5-getkernelconnectionoptionswide.md) | The GetKernelConnectionOptionsWide method returns the connection options for the current kernel target. |
| [IDebugSystemObjects4::SetCurrentThreadId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setcurrentthreadid.md) | The SetCurrentThreadId method makes the specified thread the current thread. |
| [IDebugInputCallbacks::EndInput method](..\dbgeng\nf-dbgeng-idebuginputcallbacks-endinput.md) | The EndInput callback method is called by the engine to indicate that it is no longer waiting for input. |
| [IDebugControl4::AddExtensionWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-addextensionwide.md) | The AddExtensionWide method loads an extension library into the debugger engine. |
| [IDebugControl3::GetExtensionFunction method](..\dbgeng\nf-dbgeng-idebugcontrol3-getextensionfunction.md) | The GetExtensionFunction method returns a pointer to an extension function from an extension library. |
| [IDebugEventCallbacksWide::ExitThread method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-exitthread.md) | The ExitThread callback method is called by the engine when an exit-threaddebugging event occurs in the target. |
| [IDebugControl3::SetSpecificFilterArgument method](..\dbgeng\nf-dbgeng-idebugcontrol3-setspecificfilterargument.md) | The SetSpecificFilterArgument method sets the value of filter argument for the specific filters that can have an argument. |
| [IDebugControl3::GetNumberEventFilters method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumbereventfilters.md) | The GetNumberEventFilters method returns the number of event filters currently used by the engine. |
| [IDebugControl4::SetTextReplacementWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-settextreplacementwide.md) | The SetTextReplacementWide method sets the value of a user-named alias. |
| [IDebugEventCallbacksWide::SystemError method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-systemerror.md) | The SystemError callback method is called by the engine when a system error occurs in the target. |
| [IDebugControl3::SetEffectiveProcessorType method](..\dbgeng\nf-dbgeng-idebugcontrol3-seteffectiveprocessortype.md) | The SetEffectiveProcessorType method sets the effective processor type of the processor of the computer that is running the target. |
| [IDebugDataSpaces4::WriteVirtualUncached method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writevirtualuncached.md) | The WriteVirtualUncached method writes data to the target's virtual address space. |
| [IDebugControl4::GetPromptTextWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getprompttextwide.md) | The GetPromptTextWide method returns the standard prompt text that will be prepended to the formatted output specified in the OutputPrompt and OutputPromptVaList methods. |
| [IDebugControl3::GetBreakpointByIndex method](..\dbgeng\nf-dbgeng-idebugcontrol3-getbreakpointbyindex.md) | The GetBreakpointByIndex method returns the breakpoint located at the specified index. |
| [IDebugControl3::SetRadix method](..\dbgeng\nf-dbgeng-idebugcontrol3-setradix.md) | The SetRadix method sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [IDebugSymbols3::GetScopeSymbolGroup method](..\dbgeng\nf-dbgeng-idebugsymbols3-getscopesymbolgroup.md) | The GetScopeSymbolGroup method returns a symbol group containing the symbols in the current target's scope. |
| [IDebugBreakpoint2::GetPassCount method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getpasscount.md) | The GetPassCount method returns the number of times that the target was originally required to reach the breakpoint location before the breakpoint is triggered. |
| [IDebugSymbols3::GetTypeIdWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypeidwide.md) | The GetTypeIdWide method looks up the specified type and return its type ID. |
| [IDebugControl3::SetExpressionSyntax method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexpressionsyntax.md) | The SetExpressionSyntax method sets the syntax that the engine will use to evaluate expressions. |
| [IDebugSymbols3::SetScopeFrameByIndex method](..\dbgeng\nf-dbgeng-idebugsymbols3-setscopeframebyindex.md) | The SetScopeFrameByIndex method sets the current scope to the scope of one of the frames on the call stack. |
| [IDebugControl3::GetNumberEvents method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberevents.md) | The GetNumberEvents method returns the number of events for the current target, if the number of events is fixed. |
| [IDebugSymbols3::GetSourceEntriesByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentriesbyoffset.md) | Queries symbol information and returns locations in the target's memory by using an offset. |
| [IDebugSymbols3::AppendSymbolPathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendsymbolpathwide.md) | The AppendSymbolPathWide method appends directories to the symbol path. |
| [IDebugEventCallbacks::ExitThread method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-exitthread.md) | The ExitThread callback method is called by the engine when an exit-threaddebugging event occurs in the target. |
| [IDebugClient5::SetEventCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-seteventcallbacks.md) | The SetEventCallbacks method registers an event callbacks object with this client. |
| [IDebugSymbols3::ResetScope method](..\dbgeng\nf-dbgeng-idebugsymbols3-resetscope.md) | The ResetScope method resets the current scope to the default scope of the current thread. |
| [IDebugSymbols3::AppendSymbolPath method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendsymbolpath.md) | The AppendSymbolPath method appends directories to the symbol path. |
| [IDebugSymbols3::AddSymbolOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsymboloptions.md) | The AddSymbolOptions method turns on some of the engine's global symbol options. |
| [IDebugEventCallbacks::ExitProcess method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-exitprocess.md) | The ExitProcess callback method is called by the engine when an exit-processdebugging event occurs in the target. |
| [IDebugRegisters2::GetStackOffset method](..\dbgeng\nf-dbgeng-idebugregisters2-getstackoffset.md) | The GetStackOffset method returns the current thread's current stack location. |
| [IDebugControl3::CoerceValues method](..\dbgeng\nf-dbgeng-idebugcontrol3-coercevalues.md) | The CoerceValues method converts an array of values into an array of values of different types. |
| [IDebugSymbols3::GetFieldTypeAndOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldtypeandoffsetwide.md) | The GetFieldTypeAndOffsetWide method returns the type of a field and its offset within a container. |
| [IDebugClient5::CreateProcess2Wide method](..\dbgeng\nf-dbgeng-idebugclient5-createprocess2wide.md) | The CreateProcess2Wide method executes the specified command to create a new process. |
| [IDebugControl4::SetTextMacroWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-settextmacrowide.md) | The SetTextMacroWide method sets the value of a fixed-name alias. |
| [IDebugSymbols3::GetSourceEntriesByLineWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentriesbylinewide.md) | The GetSourceEntriesByLineWide method queries symbol information and returns locations in the target's memory that correspond to lines in a source file. |
| [IDebugBreakpoint2::GetCommand method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getcommand.md) | The GetCommand method returns the command string that is executed when a breakpoint is triggered. |
| [IDebugClient5::CreateProcess method](..\dbgeng\nf-dbgeng-idebugclient5-createprocess.md) | The CreateProcess method creates a process from the specified command line. |
| [IDebugSymbols3::GetSymbolEntryStringWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentrystringwide.md) | The GetSymbolEntryStringWide method returns string information for the specified symbol. |
| [IDebugRegisters2::SetPseudoValues method](..\dbgeng\nf-dbgeng-idebugregisters2-setpseudovalues.md) | The SetPseudoValues method sets the value of several pseudo-registers. |
| [IDebugEventCallbacks::SystemError method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-systemerror.md) | The SystemError callback method is called by the engine when a system error occurs in the target. |
| [IDebugDataSpaces4::WritePhysical method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writephysical.md) | The WritePhysical method writes data to the specified physical address in the target's memory. |
| [IDebugClient5::PopOutputLinePrefix method](..\dbgeng\nf-dbgeng-idebugclient5-popoutputlineprefix.md) | Restores a previously saved output line prefix. |
| [IDebugSymbols3::GetSymbolEntryByToken method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentrybytoken.md) | Looks up a symbol by using a managed metadata token. |
| [IDebugRegisters2::GetStackOffset2 method](..\dbgeng\nf-dbgeng-idebugregisters2-getstackoffset2.md) | The GetStackOffset2 method returns the current thread's current stack location. |
| [IDebugPlmClient2::LaunchPlmBgTaskForDebugWide method](..\dbgeng\nf-dbgeng-idebugplmclient2-launchplmbgtaskfordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) background task. |
| [IDebugEventCallbacksWide::LoadModule method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-loadmodule.md) | The LoadModule callback method is called by the engine when a module-load debugging event occurs in the target. |
| [IDebugSymbols3::FindSourceFileWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-findsourcefilewide.md) | The FindSourceFileWide method searches the source path for a specified source file. |
| [IDebugSystemObjects4::GetCurrentProcessExecutableName method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessexecutablename.md) | The GetCurrentProcessExecutableName method returns the name of executable file loaded in the current process. |
| [IDebugSymbols3::GetTypeName method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypename.md) | The GetTypeName method returns the name of the type symbol specified by its type ID and module. |
| [IDebugBreakpoint2::SetCommand method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setcommand.md) | The SetCommand method sets the command that is executed when a breakpoint is triggered. |
| [IDebugBreakpoint2::GetOffset method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getoffset.md) | The GetOffset method returns the location that triggers a breakpoint. |
| [IDebugAdvanced3::GetSourceFileInformationWide method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsourcefileinformationwide.md) | The GetSourceFileInformationWide method returns specified information about a source file. |
| [IDebugClient5::DisconnectProcessServer method](..\dbgeng\nf-dbgeng-idebugclient5-disconnectprocessserver.md) | The DisconnectProcessServer method disconnects the debugger engine from a process server. |
| [IDebugControl3::GetProcessorTypeNames method](..\dbgeng\nf-dbgeng-idebugcontrol3-getprocessortypenames.md) | The GetProcessorTypeNames method returns the full name and abbreviated name of the specified processor type. |
| [IDebugControl3::GetExecutionStatus method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexecutionstatus.md) | The GetExecutionStatus method returns information about the execution status of the debugger engine. |
| [IDebugSymbolGroup2::GetNumberSymbols method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getnumbersymbols.md) | The GetNumberSymbols method returns the number of symbols that are contained in a symbol group. |
| [IDebugSymbols3::GetNearNameByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnearnamebyoffset.md) | The GetNearNameByOffset method returns the name of a symbol that is located near the specified location. |
| [IDebugSymbols3::GetSymbolTypeIdWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymboltypeidwide.md) | The GetSymbolTypeIdWide method returns the type ID and module of the specified symbol. |
| [IDebugPlmClient3::ActivateAndDebugPlmBgTaskWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-activateanddebugplmbgtaskwide.md) | Launches and attaches to a Process Lifecycle Management (PLM) background task. |
| [IDebugClient5::GetRunningProcessSystemIds method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocesssystemids.md) | The GetRunningProcessSystemIds method returns the process IDs for each running process. |
| [IDebugSymbols3::AddSyntheticModule method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsyntheticmodule.md) | The AddSyntheticModule method adds a synthetic module to the module list the debugger maintains for the current process. |
| [IDebugSymbols3::GetFieldTypeAndOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldtypeandoffset.md) | The GetFieldTypeAndOffset method returns the type of a field and its offset within a container. |
| [IDebugClient5::FlushCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-flushcallbacks.md) | The FlushCallbacks method forces any remaining buffered output to be delivered to the IDebugOutputCallbacks object registered with this client. |
| [IDebugPlmClient3::TerminatePlmPackageWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-terminateplmpackagewide.md) | Ends a Process Lifecycle Management (PLM) package. |
| [IDebugClient::GetOutputWidth method](..\dbgeng\nf-dbgeng-idebugclient-getoutputwidth.md) | Gets the width of an output line for commands that produce formatted output. |
| [IDebugControl4::OutputVaListWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputvalistwide.md) | The OutputVaListWide method formats a string and sends the result to the output callbacks that are registered with the engine's clients. |
| [IDebugClient5::GetKernelConnectionOptions method](..\dbgeng\nf-dbgeng-idebugclient5-getkernelconnectionoptions.md) | The GetKernelConnectionOptions method returns the connection options for the current kernel target. |
| [IDebugSymbolGroup2::GetSymbolValueTextWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolvaluetextwide.md) | The GetSymbolValueTextWide method returns a string that represents the value of a symbol. |
| [IDebugClient5::ConnectProcessServerWide method](..\dbgeng\nf-dbgeng-idebugclient5-connectprocessserverwide.md) | The ConnectProcessServerWide method connects to a process server. |
| [IDebugControl3::ControlledOutput method](..\dbgeng\nf-dbgeng-idebugcontrol3-controlledoutput.md) | The ControlledOutput method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugSystemObjects4::GetThreadIdByTeb method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbyteb.md) | The GetThreadIdByTeb method returns the engine thread ID of the specified thread. The thread is specified by its thread environment block (TEB). |
| [IDebugSystemObjects4::GetEventThread method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-geteventthread.md) | The GetEventThread method returns the engine thread ID for the thread on which the last event occurred. |
| [IDebugPlmClient3::SuspendPlmPackageWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-suspendplmpackagewide.md) | Suspends a Process Lifecycle Management (PLM) package. |
| [IDebugSystemObjects4::GetEventSystem method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-geteventsystem.md) | The GetEventSystem method returns the engine target ID for the target in which the last event occurred. |
| [IDebugBreakpoint2::GetOffsetExpressionWide method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getoffsetexpressionwide.md) | The GetOffsetExpressionWide method returns the expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugSymbols3::AddSyntheticModuleWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsyntheticmodulewide.md) | The AddSyntheticModuleWide method adds a synthetic module to the module list the debugger maintains for the current process. |
| [IDebugRegisters2::GetFrameOffset2 method](..\dbgeng\nf-dbgeng-idebugregisters2-getframeoffset2.md) | The GetFrameOffset2 method returns the location of the stack frame for the current function. |
| [IDebugSymbols3::RemoveTypeOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-removetypeoptions.md) | The RemoveTypeOptions method turns off some type formatting options for output generated by the engine. |
| [IDebugControl3::OutputPrompt method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputprompt.md) | The OutputPrompt method formats and sends a user prompt to the output callback objects. |
| [IDebugControl4::GetExceptionFilterSecondCommand method](..\dbgeng\nf-dbgeng-idebugcontrol4-getexceptionfiltersecondcommand.md) | The GetExceptionFilterSecondCommandWide method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [IDebugDataSpaces4::ReadBusData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readbusdata.md) | The ReadBusData method reads data from a system bus. |
| [IDebugSymbols4::GetScopeEx method](..\dbgeng\nf-dbgeng-idebugsymbols4-getscopeex.md) | Gets the scope as an extended frame structure. |
| [IDebugControl3::GetSpecificFilterArgument method](..\dbgeng\nf-dbgeng-idebugcontrol3-getspecificfilterargument.md) | The GetSpecificFilterArgument method returns the value of filter argument for thespecific filters that have an argument. |
| [IDebugOutputCallbacks2::Output method](..\dbgeng\nf-dbgeng-idebugoutputcallbacks2-output.md) | This method is not used. |
| [IDebugSymbols3::AddSyntheticSymbolWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsyntheticsymbolwide.md) | The AddSyntheticSymbolWide method adds a synthetic symbol to a module in the current process. |
| [IDebugRegisters2::GetValues method](..\dbgeng\nf-dbgeng-idebugregisters2-getvalues.md) | The GetValues method gets the value of several of the target's registers. |
| [IDebugPlmClient3::QueryPlmPackageList method](..\dbgeng\nf-dbgeng-idebugplmclient3-queryplmpackagelist.md) | Query a Process Lifecycle Management (PLM) package list. |
| [IDebugEventCallbacks::ChangeDebuggeeState method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-changedebuggeestate.md) | The ChangeDebuggeeState callback method is called by the engine when it makes or detects changes to the target. |
| [IDebugSymbols3::GetSourcePathElement method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcepathelement.md) | The GetSourcePathElement method returns an element from the source path. |
| [IDebugSystemObjects4::GetThreadIdByDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbydataoffset.md) | The GetThreadIdByDataOffset method returns the engine thread ID for the specified thread. The thread is specified by its system data structure. |
| [DebugConnect function](..\dbgeng\nf-dbgeng-debugconnect.md) | The DebugConnect and DebugConnectWide functions create a new client object and return an interface pointer to it. The client object will be connected to a remote host. |
| [IDebugClient5::PushOutputLinePrefix method](..\dbgeng\nf-dbgeng-idebugclient5-pushoutputlineprefix.md) | Saves an output line prefix. |
| [IDebugClient5::GetNumberDumpFiles method](..\dbgeng\nf-dbgeng-idebugclient5-getnumberdumpfiles.md) | The GetNumberDumpFiles method returns the number of files containing supporting information that were used when opening the current dump target. |
| [IDebugSystemObjects4::GetImplicitProcessDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getimplicitprocessdataoffset.md) | The GetImplicitProcessDataOffset method returns the implicit process for the current target. |
| [IDebugControl5::OutputStackTraceEx method](..\dbgeng\nf-dbgeng-idebugcontrol5-outputstacktraceex.md) | The OutputStackTraceEx method outputs either the supplied stack frame or the current stack frames. |
| [IDebugDataSpaces4::GetOffsetInformation method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getoffsetinformation.md) | The GetOffsetInformation method provides general information about an address in a process's data space. |
| [IDebugSystemObjects4::GetCurrentThreadTeb method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreadteb.md) | The GetCurrentThreadTeb method returns the location of the thread environment block (TEB) for the current thread. |
| [IDebugClient5::WriteDumpFileWide method](..\dbgeng\nf-dbgeng-idebugclient5-writedumpfilewide.md) | The WriteDumpFileWide method creates a user-mode or kernel-modecrash dump file. |
| [IDebugRegisters2::GetIndexByName method](..\dbgeng\nf-dbgeng-idebugregisters2-getindexbyname.md) | The GetIndexByName method returns the index of the named register. |
| [IDebugSystemObjects4::GetThreadIdBySystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbysystemid.md) | The GetThreadIdBySystemId method returns the engine thread ID for the specified thread. The thread is specified by its system thread ID. |
| [IDebugControl4::GetExtensionFunctionWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getextensionfunctionwide.md) | The GetExtensionFunctionWide method returns a pointer to an extension function from an extension library. |
| [IDebugControl3::GetEventIndexDescription method](..\dbgeng\nf-dbgeng-idebugcontrol3-geteventindexdescription.md) | The GetEventIndexDescription method describes the specified event in a static list of events for the current target. |
| [DebugCreate function](..\dbgeng\nf-dbgeng-debugcreate.md) | The DebugCreate function creates a new client object and returns an interface pointer to it. |
| [IDebugBreakpoint2::SetMatchThreadId method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setmatchthreadid.md) | The SetMatchThreadId method sets the engine thread ID of the thread that can trigger a breakpoint. |
| [IDebugControl3::GetExpressionSyntax method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexpressionsyntax.md) | The GetExpressionSyntax method returns the current syntax that the engine is using for evaluating expressions. |
| [IDebugSymbols4::GetNameByInlineContextWide method](..\dbgeng\nf-dbgeng-idebugsymbols4-getnamebyinlinecontextwide.md) | Gets a name by inline context. |
| [IDebugControl3::GetExceptionFilterSecondCommand method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexceptionfiltersecondcommand.md) | The GetExceptionFilterSecondCommand method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [IDebugControl3::GetCurrentSystemUpTime method](..\dbgeng\nf-dbgeng-idebugcontrol3-getcurrentsystemuptime.md) | The GetCurrentSystemUpTime method returns the number of seconds the current target's computer has been running since it was last started. |
| [IDebugControl3::GetDebuggeeType method](..\dbgeng\nf-dbgeng-idebugcontrol3-getdebuggeetype.md) | The GetDebuggeeType method describes the nature of the current target. |
| [IDebugClient5::SetEventCallbacksWide method](..\dbgeng\nf-dbgeng-idebugclient5-seteventcallbackswide.md) | The SetEventCallbacksWide method registers an event callbacks object with this client. |
| [IDebugClient5::OutputServersWide method](..\dbgeng\nf-dbgeng-idebugclient5-outputserverswide.md) | The OutputServersWide method lists the servers running on a given computer. |
| [IDebugDataSpaces4::ReadPhysical method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readphysical.md) | The ReadPhysical method reads the target's memory from the specified physical address. |
| [IDebugEventCallbacksWide::Breakpoint method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-breakpoint.md) | The Breakpoint callback method is called by the engine when the target issues a breakpointexception. |
| [IDebugDataSpaces4::ReadImageNtHeaders method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readimagentheaders.md) | The ReadImageNtHeaders method returns the NT headers for the specified image loaded in the target. |
| [IDebugSymbolGroup2::GetSymbolName method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolname.md) | The GetSymbolName method returns the name of a symbol in a symbol group. |
| [IDebugDataSpaces4::GetValidRegionVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getvalidregionvirtual.md) | The GetValidRegionVirtual method locates the first valid region of memory in a specified memory range. |
| [IDebugSystemObjects4::GetTotalNumberThreads method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-gettotalnumberthreads.md) | The GetTotalNumberThreads method returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target. |
| [IDebugEventCallbacks::SessionStatus method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-sessionstatus.md) | The SessionStatus callback method is called by the engine when a change occurs in the debugger session. |
| [IDebugEventCallbacksWide::SessionStatus method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-sessionstatus.md) | The SessionStatus callback method is called by the engine when a change occurs in the debugger session. |
| [IDebugControl3::SetAssemblyOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-setassemblyoptions.md) | The SetAssemblyOptions method sets the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target. |
| [IDebugSymbols3::GetConstantNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getconstantnamewide.md) | The GetConstantNameWide method returns the name of the specified constant. |
| [IDebugControl3::GetWindbgExtensionApis64 method](..\dbgeng\nf-dbgeng-idebugcontrol3-getwindbgextensionapis64.md) | The GetWindbgExtensionApis64 method returns a structure that facilitates using the WdbgExts API. |
| [IDebugAdvanced3::FindSourceFileAndTokenWide method](..\dbgeng\nf-dbgeng-idebugadvanced3-findsourcefileandtokenwide.md) | The FindSourceFileAndTokenWide method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [IDebugSymbols3::GetSourceEntriesByLine method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentriesbyline.md) | The GetSourceEntriesByLine method queries symbol information and returns locations in the target's memory that correspond to lines in a source file. |
| [IDebugSymbols3::AppendSourcePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendsourcepath.md) | The AppendSourcePath method appends directories to the source path. |
| [IDebugClient5::AttachKernel method](..\dbgeng\nf-dbgeng-idebugclient5-attachkernel.md) | The AttachKernel methods connect the debugger engine to a kernel target. |
| [IDebugControl3::RemoveAssemblyOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-removeassemblyoptions.md) | The RemoveAssemblyOptions method turns off some of the assembly and disassembly options. |
| [IDebugSymbolGroup2::GetSymbolSize method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolsize.md) | The GetSymbolSize method returns the size of a symbol's value. |
| [IDebugClient5::EndSession method](..\dbgeng\nf-dbgeng-idebugclient5-endsession.md) | The EndSession method ends the current debugger session. |
| [IDebugControl3::GetLogFile method](..\dbgeng\nf-dbgeng-idebugcontrol3-getlogfile.md) | The GetLogFile method returns the name of the currently open log file. |
| [IDebugClient5::OutputServers method](..\dbgeng\nf-dbgeng-idebugclient5-outputservers.md) | The OutputServers method lists the servers running on a given computer. |
| [IDebugControl4::GetBreakpointByIndex2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-getbreakpointbyindex2.md) | The GetBreakpointByIndex2 method returns the breakpoint located at the specified index. |
| [IDebugAdvanced3::GetSourceFileInformation method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsourcefileinformation.md) | The GetSourceFileInformation method returns specified information about a source file. |
| [IDebugClient::SetOutputLinePrefix method](..\dbgeng\nf-dbgeng-idebugclient-setoutputlineprefix.md) | Sets a prefix for multiple lines of output. |
| [IDebugSymbolGroup2::RemoveSymbolByIndex method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-removesymbolbyindex.md) | The RemoveSymbolByIndex method removes the specified symbol from a symbol group. |
| [IDebugControl3::GetExecutingProcessorType method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexecutingprocessortype.md) | The GetExecutingProcessorType method returns the executing processor type for the processor for which the last event occurred. |
| [IDebugControl3::SetInterrupt method](..\dbgeng\nf-dbgeng-idebugcontrol3-setinterrupt.md) | The SetInterrupt method registers a user interrupt or breaks into the debugger. |
| [IDebugControl4::GetSystemVersionStringWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getsystemversionstringwide.md) | The GetSystemVersionStringWide method returns a string that describes the target's operating system version. |
| [IDebugClient5::GetIdentity method](..\dbgeng\nf-dbgeng-idebugclient5-getidentity.md) | The GetIdentity method returns a string describing the computer and user this client represents. |
| [IDebugSymbols3::GetFieldOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldoffset.md) | The GetFieldOffset method returns the offset of a field from the base address of an instance of a type. |
| [IDebugControl3::SetEngineOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-setengineoptions.md) | The SetEngineOptions method changes the engine's options. |
| [IDebugClient5::WriteDumpFile method](..\dbgeng\nf-dbgeng-idebugclient5-writedumpfile.md) | The WriteDumpFile method creates a user-mode or kernel-modecrash dump file. |
| [IDebugPlmClient::LaunchPlmPackageForDebugWide method](..\dbgeng\nf-dbgeng-idebugplmclient-launchplmpackagefordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) application. |
| [IDebugSymbols3::RemoveSymbolOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-removesymboloptions.md) | The RemoveSymbolOptions method turns off some of the engine's global symbol options. |
| [IDebugControl3::OutputVaList method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputvalist.md) | The OutputVaList method formats a string and sends the result to the output callbacks that are registered with the engine's clients. |
| [IDebugSymbols3::StartSymbolMatch method](..\dbgeng\nf-dbgeng-idebugsymbols3-startsymbolmatch.md) | The StartSymbolMatch method initializes a search for symbols whose names match a given pattern. |
| [IDebugSymbols3::GetNumberModules method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnumbermodules.md) | The GetNumberModules method returns the number of modules in the current process's module list. |
| [IDebugClient5::TerminateCurrentProcess method](..\dbgeng\nf-dbgeng-idebugclient5-terminatecurrentprocess.md) | The TerminateCurrentProcess method attempts to terminate the current process. |
| [IDebugEventCallbacks::LoadModule method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-loadmodule.md) | The LoadModule callback method is called by the engine when a module-load debugging event occurs in the target. |
| [IDebugBreakpoint2::SetCommandWide method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setcommandwide.md) | The SetCommandWide method sets the command that is executed when a breakpoint is triggered. |
| [IDebugClient5::GetRunningProcessSystemIdByExecutableNameWide method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocesssystemidbyexecutablenamewide.md) | The GetRunningProcessSystemIdByExecutableNameWide method searches for a process with a given executable file name and return its process ID. |
| [IDebugClient5::EndProcessServer method](..\dbgeng\nf-dbgeng-idebugclient5-endprocessserver.md) | The EndProcessServer method requests that a process server be shut down. |
| [IDebugControl4::OpenLogFile2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-openlogfile2.md) | The OpenLogFile2 method opens a log file that will receive output from the client objects. |
| [IDebugRegisters2::GetInstructionOffset method](..\dbgeng\nf-dbgeng-idebugregisters2-getinstructionoffset.md) | The GetInstructionOffset method returns the location of the current thread's current instruction. |
| [IDebugControl3::OutputCurrentState method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputcurrentstate.md) | The OutputCurrentState method prints the current state of the current target to the debugger console. |
| [IDebugClient6::SetEventContextCallbacks method](..\dbgeng\nf-dbgeng-idebugclient6-seteventcontextcallbacks.md) | Registers an event callbacks object with this client. |
| [IDebugSymbols3::GetLineByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getlinebyoffset.md) | The GetLineByOffset method returns the source filename and the line number within the source file of an instruction in the target. |
| [IDebugSystemObjects4::GetCurrentProcessExecutableNameWide method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessexecutablenamewide.md) | The GetCurrentProcessExecutableNameWide method returns the name of executable file loaded in the current process. |
| [IDebugSymbols3::SetSymbolOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsymboloptions.md) | The SetSymbolOptions method changes the engine's global symbol options. |
| [IDebugDataSpaces4::SearchVirtual2 method](..\dbgeng\nf-dbgeng-idebugdataspaces4-searchvirtual2.md) | The SearchVirtual2 method searches the process's virtual memory for a specified pattern of bytes. |
| [IDebugSymbols3::GetFieldOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldoffsetwide.md) | The GetFieldOffsetWide method returns the offset of a field from the base address of an instance of a type. |
| [IDebugControl3::GetExceptionFilterParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexceptionfilterparameters.md) | The GetExceptionFilterParameters method returns the parameters for exception filters specified by exception codes or by index. |
| [IDebugClient5::SetOutputLinePrefixWide method](..\dbgeng\nf-dbgeng-idebugclient5-setoutputlineprefixwide.md) | Sets a wide string prefix for output lines. |
| [IDebugControl4::AssembleWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-assemblewide.md) | The AssembleWide method assembles a single processor instruction. The assembled instruction is placed in the target's memory. |
| [IDebugSymbols3::GetConstantName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getconstantname.md) | The GetConstantName method returns the name of the specified constant. |
| [IDebugSymbols3::AppendImagePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendimagepathwide.md) | The AppendImagePathWide method appends directories to the executable image path. |
| [IDebugControl3::GetEventFilterText method](..\dbgeng\nf-dbgeng-idebugcontrol3-geteventfiltertext.md) | The GetEventFilterText method returns a short description of an event for a specific filter. |
| [IDebugSymbols4::GetNameByInlineContext method](..\dbgeng\nf-dbgeng-idebugsymbols4-getnamebyinlinecontext.md) | Gets a name by inline context. |
| [IDebugSymbols3::GetSymbolEntryOffsetRegions method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentryoffsetregions.md) | Returns all the memory regions known to be associated with a symbol. |
| [IDebugDataSpaces4::VirtualToPhysical method](..\dbgeng\nf-dbgeng-idebugdataspaces4-virtualtophysical.md) | The VirtualToPhysical method translates a location in the target's virtual address space into a physical memory address. |
| [IDebugSystemObjects4::GetCurrentThreadHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreadhandle.md) | The GetCurrentThreadHandle method returns the system handle for the current thread. |
| [IDebugControl3::GetNumberExpressionSyntaxes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberexpressionsyntaxes.md) | The GetNumberExpressionSyntaxes method returns the number of expression syntaxes that are supported by the engine. |
| [IDebugSymbols3::GetSourceFileLineOffsetsWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcefilelineoffsetswide.md) | The GetSourceFileLineOffsetsWide method maps each line in a source file to a location in the target's memory. |
| [IDebugSymbolGroup2::GetSymbolOffset method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymboloffset.md) | The GetSymbolOffset method retrieves the location in the process's virtual address space of a symbol in a symbol group, if the symbol has an absolute address. |
| [IDebugSymbols3::GetSourcePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcepath.md) | The GetSourcePath method returns the source path. |
| [IDebugSymbols3::AddSyntheticSymbol method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsyntheticsymbol.md) | The AddSyntheticSymbol method adds a synthetic symbol to a module in the current process. |
| [IDebugControl4::OpenLogFileWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-openlogfilewide.md) | The OpenLogFileWide method opens a log file that will receive output from the client objects. |
| [IDebugSymbols3::GetModuleNameString method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulenamestring.md) | The GetModuleNameString method returns the name of the specified module. |
| [IDebugControl3::GetSystemErrorControl method](..\dbgeng\nf-dbgeng-idebugcontrol3-getsystemerrorcontrol.md) | The GetSystemErrorControl method returns the control values for handling system errors. |
| [IDebugControl3::GetCodeLevel method](..\dbgeng\nf-dbgeng-idebugcontrol3-getcodelevel.md) | The GetCodeLevel method returns the current code level and is mainly used when stepping through code. |
| [IDebugSymbols3::GetModuleNameStringWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulenamestringwide.md) | The GetModuleNameStringWide method returns the name of the specified module. |
| [IDebugClient5::RemoveProcessOptions method](..\dbgeng\nf-dbgeng-idebugclient5-removeprocessoptions.md) | The RemoveProcessOptions method removes process options from those options that affect the current process. |
| [IDebugBreakpoint2::SetPassCount method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setpasscount.md) | The SetPassCount method sets the number of times that the target must reach the breakpoint location before the breakpoint is triggered. |
| [IDebugSymbols3::SetSymbolPath method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsymbolpath.md) | The SetSymbolPath method sets the symbol path. |
| [IDebugSymbolGroup2::WriteSymbol method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-writesymbol.md) | The WriteSymbol methods set the value of the specified symbol. |
| [IDebugControl3::Execute method](..\dbgeng\nf-dbgeng-idebugcontrol3-execute.md) | The Execute method executes the specified debugger commands. |
| [IDebugEventCallbacks::CreateThread method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-createthread.md) | The CreateThread callback method is called by the engine when a create-threaddebugging event occurs in the target. |
| [IDebugControl3::ReadBugCheckData method](..\dbgeng\nf-dbgeng-idebugcontrol3-readbugcheckdata.md) | The ReadBugCheckData method reads the kernel bug check code and related parameters. |
| [IDebugSymbols3::OutputSymbolByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-outputsymbolbyoffset.md) | The OutputSymbolByOffset method looks up a symbol by address and prints the symbol name and other symbol information to the debugger console. |
| [IDebugSystemObjects4::GetNumberThreads method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getnumberthreads.md) | The GetNumberThreads method returns the number of threads in the current process. |
| [IDebugAdvanced3::GetThreadContext method](..\dbgeng\nf-dbgeng-idebugadvanced3-getthreadcontext.md) | The GetThreadContext method returns the current thread context. |
| [IDebugControl3::AddEngineOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-addengineoptions.md) | The AddEngineOptions method turns on some of the debugger engine's options. |
| [IDebugClient5::GetNumberInputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getnumberinputcallbacks.md) | The GetNumberInputCallbacks method returns the number of input callbacks registered over all clients. |
| [IDebugSymbols3::GetCurrentScopeFrameIndex method](..\dbgeng\nf-dbgeng-idebugsymbols3-getcurrentscopeframeindex.md) | The GetCurrentScopeFrameIndex method returns the index of the current stack frame in the call stack. |
| [IDebugRegisters2::OutputRegisters method](..\dbgeng\nf-dbgeng-idebugregisters2-outputregisters.md) | The OutputRegisters method formats and sends the target's registers to the clients as output. |
| [IDebugSymbols3::Reload method](..\dbgeng\nf-dbgeng-idebugsymbols3-reload.md) | The Reload method deletes the engine's symbol information for the specified module and reload these symbols as needed. |
| [IDebugClient5::GetOutputCallbacksWide method](..\dbgeng\nf-dbgeng-idebugclient5-getoutputcallbackswide.md) | The GetOutputCallbacksWide method returns the output callbacks object registered with the client. |
| [IDebugControl3::GetCurrentTimeDate method](..\dbgeng\nf-dbgeng-idebugcontrol3-getcurrenttimedate.md) | The GetCurrentTimeDate method returns the time of the current target. |
| [IDebugSymbols3::GetNextSymbolMatch method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnextsymbolmatch.md) | The GetNextSymbolMatch method returns the next symbol found in a symbol search. |
| [IDebugControl4::ResetManagedStatus method](..\dbgeng\nf-dbgeng-idebugcontrol4-resetmanagedstatus.md) | Clears and reinitializes the engine's managed code debugging support of the runtime debugging APIs provided by the common language runtime (CLR). |
| [IDebugSymbols3::GetSymbolPath method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolpath.md) | The GetSymbolPath method returns the symbol path. |
| [IDebugDataSpaces4::ReadProcessorSystemData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readprocessorsystemdata.md) | The ReadProcessorSystemData method returns data about the specified processor. |
| [IDebugControl4::DisassembleWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-disassemblewide.md) | The DisassembleWide method disassembles a processor instruction in the target's memory. |
| [IDebugOutputCallbacks2::Output2 method](..\dbgeng\nf-dbgeng-idebugoutputcallbacks2-output2.md) | Returns notifications for the IDebugOutputCallbacks2 interface. |
| [IDebugBreakpoint2::GetParameters method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getparameters.md) | The GetParameters method returns the parameters for a breakpoint. |
| [IDebugSystemObjects4::GetCurrentProcessId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessid.md) | The GetCurrentProcessId method returns the engine process ID for the current process. |
| [IDebugEventCallbacks::Exception method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-exception.md) | The Exception callback method is called by the engine when an exceptiondebugging event occurs in the target. |
| [IDebugClient5::GetDumpFileWide method](..\dbgeng\nf-dbgeng-idebugclient5-getdumpfilewide.md) | The GetDumpFileWide method describes the files containing supporting information that were used when opening the current dump target. |
| [IDebugSystemObjects4::GetProcessIdByPeb method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidbypeb.md) | The GetProcessIdByPeb method returns the engine process ID for the specified process. The process is specified by its process environment block (PEB). |
| [IDebugBreakpoint2::GetId method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getid.md) | The GetId method returns a breakpoint ID, which is the engine's unique identifier for a breakpoint. |
| [IDebugClient5::ConnectSession method](..\dbgeng\nf-dbgeng-idebugclient5-connectsession.md) | The ConnectSession method joins the client to an existing debugger session. |
| [IDebugControl4::GetEventFilterCommandWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-geteventfiltercommandwide.md) | The GetEventFilterCommandWide method returns the debugger command that the engine will execute when a specified event occurs. |
| [IDebugInputCallbacks::StartInput method](..\dbgeng\nf-dbgeng-idebuginputcallbacks-startinput.md) | The StartInput callback method is called by the engine to indicate that it is waiting for a line of input. |
| [IDebugSymbols3::GetSymbolEntriesByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentriesbyoffset.md) | The GetSymbolEntriesByOffset method returns the symbols which are located at a specified address. |
| [IDebugControl3::SetExecutionStatus method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexecutionstatus.md) | The SetExecutionStatus method requests that the debugger engine enter an executable state. Actual execution will not occur until the next time WaitForEvent is called. |
| [IDebugDataSpaces4::ReadUnicodeStringVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readunicodestringvirtual.md) | The ReadUnicodeStringVirtual method reads a null-terminated, Unicode string from the target and converts it to a multibyte string. |
| [IDebugSymbols3::GetFieldNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldnamewide.md) | The GetFieldNameWide method returns the name of a field within a structure. |
| [IDebugControl4::OpenLogFile2Wide method](..\dbgeng\nf-dbgeng-idebugcontrol4-openlogfile2wide.md) | The OpenLogFile2Wide method opens a log file that will receive output from the client objects. |
| [IDebugDataSpaces4::ReadMultiByteStringVirtualWide method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readmultibytestringvirtualwide.md) | The ReadMultiByteStringVirtualWide method reads a null-terminated, multibyte string from the target and converts it to Unicode. |
| [IDebugClient5::ConnectProcessServer method](..\dbgeng\nf-dbgeng-idebugclient5-connectprocessserver.md) | The ConnectProcessServer methods connect to a process server. |
| [IDebugPlmClient3::DisablePlmPackageDebugWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-disableplmpackagedebugwide.md) | Disables a Process Lifecycle Management (PLM) package debug. |
| [IDebugSymbols3::SetImagePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-setimagepath.md) | The SetImagePath method sets the executable image path. |
| [IDebugControl3::CoerceValue method](..\dbgeng\nf-dbgeng-idebugcontrol3-coercevalue.md) | The CoerceValue method converts a value of one type into a value of another type. |
| [IDebugControl4::GetSystemVersionString method](..\dbgeng\nf-dbgeng-idebugcontrol4-getsystemversionstring.md) | The GetSystemVersionString method returns a string that describes the target's operating system version. |
| [IDebugControl4::GetContextStackTrace method](..\dbgeng\nf-dbgeng-idebugcontrol4-getcontextstacktrace.md) | The GetContextStackTrace method returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame. |
| [IDebugClient5::CreateClient method](..\dbgeng\nf-dbgeng-idebugclient5-createclient.md) | The CreateClient method creates a new client object for the current thread. |
| [IDebugClient5::SetOutputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-setoutputcallbacks.md) | The SetOutputCallbacks method registers an output callbacks object with this client. |
| [IDebugBreakpoint3::GetGuid method](..\dbgeng\nf-dbgeng-idebugbreakpoint3-getguid.md) | Returns a GUID for the breakpoint. |
| [IDebugDataSpaces4::ReadDebuggerData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readdebuggerdata.md) | The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session. |
| [IDebugBreakpoint2::GetCurrentPassCount method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getcurrentpasscount.md) | The GetCurrentPassCount method returns the remaining number of times that the target must reach the breakpoint location before the breakpoint is triggered. |
| [IDebugControl3::GetRadix method](..\dbgeng\nf-dbgeng-idebugcontrol3-getradix.md) | The GetRadix method returns the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [IDebugSystemObjects4::GetProcessIdBySystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidbysystemid.md) | The GetProcessIdBySystemId method returns the engine process ID for a process specified by its system process ID. |
| [IDebugControl3::Disassemble method](..\dbgeng\nf-dbgeng-idebugcontrol3-disassemble.md) | The Disassemble method disassembles a processor instruction in the target's memory. |
| [IDebugControl4::ControlledOutputWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-controlledoutputwide.md) | The ControlledOutputWide method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugDataSpaces4::ReadPointersVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readpointersvirtual.md) | The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space. |
| [IDebugControl4::SetSpecificFilterArgumentWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-setspecificfilterargumentwide.md) | The SetSpecificFilterArgumentWide method sets the value of filter argument for the specific filters that can have an argument. |
| [IDebugAdvanced3::GetSystemObjectInformation method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsystemobjectinformation.md) | The GetSystemObjectInformation method returns information about operating system objects on the target. |
| [IDebugControl3::SetTextMacro method](..\dbgeng\nf-dbgeng-idebugcontrol3-settextmacro.md) | The SetTextMacro method sets the value of a fixed-name alias. |
| [IDebugSymbols3::SetTypeOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-settypeoptions.md) | The SetTypeOptions method changes the type formatting options for output generated by the engine. |
| [IDebugSymbolGroup2::AddSymbol method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-addsymbol.md) | The AddSymbol method adds a symbol to a symbol group. |
| [IDebugRegisters2::GetPseudoDescriptionWide method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudodescriptionwide.md) | The GetPseudoDescriptionWide method returns a description of a pseudo-register, including its name and type. |
| [IDebugControl4::GetManagedStatusWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getmanagedstatuswide.md) | Provides feedback as a Unicode character string on the engine's use of the runtime debugging APIs provided by the common language runtime (CLR). |
| [IDebugSymbols3::CreateSymbolGroup method](..\dbgeng\nf-dbgeng-idebugsymbols3-createsymbolgroup.md) | The CreateSymbolGroup method creates a new symbol group. |
| [IDebugControl3::GetDumpFormatFlags method](..\dbgeng\nf-dbgeng-idebugcontrol3-getdumpformatflags.md) | The GetDumpFormatFlags method returns the flags that describe what information is available in a dump file target. |
| [IDebugControl3::AddAssemblyOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-addassemblyoptions.md) | The AddAssemblyOptions method turns on some of the assembly and disassembly options. |
| [IDebugClient5::GetRunningProcessDescriptionWide method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocessdescriptionwide.md) | The GetRunningProcessDescriptionWide method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [IDebugControl5::GetContextStackTraceEx method](..\dbgeng\nf-dbgeng-idebugcontrol5-getcontextstacktraceex.md) | The GetContextStackTraceEx method returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame. |
| [IDebugSystemObjects4::GetCurrentSystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentsystemid.md) | The GetCurrentSystemId method returns the engine target ID for the current process. |
| [IDebugDataSpaces4::ReadPhysical2 method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readphysical2.md) | The ReadPhysical2 method reads the target's memory from the specified physical address. |
| [IDebugDataSpaces4::ReadVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readvirtual.md) | The ReadVirtual method reads memory from the target's virtual address space. |
| [IDebugSymbols3::GetTypeOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypeoptions.md) | The GetTypeOptions method returns the type formatting options for output generated by the engine. |
| [IDebugSymbols3::RemoveSyntheticModule method](..\dbgeng\nf-dbgeng-idebugsymbols3-removesyntheticmodule.md) | The RemoveSyntheticModule method removes a synthetic module from the module list the debugger maintains for the current process. |
| [IDebugSymbolGroup2::OutputAsTypeWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-outputastypewide.md) | The OutputAsTypeWide method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. |
| [IDebugSymbolGroup2::OutputAsType method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-outputastype.md) | The OutputAsType method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. |
| [IDebugControl3::GetNumberPossibleExecutingProcessorTypes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberpossibleexecutingprocessortypes.md) | The GetNumberPossibleExecutingProcessorTypes method returns the number of processor types that are supported by the computer running the current target. |
| [IDebugControl4::GetLogFileWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getlogfilewide.md) | The GetLogFileWide method returns the name of the currently open log file. |
| [IDebugSymbols3::GetModuleByOffset2 method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebyoffset2.md) | The GetModuleByOffset2 method searches through the process's modules for one whose memory allocation includes the specified location. |
| [IDebugControl4::GetTextReplacementWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-gettextreplacementwide.md) | The GetTextReplacementWide method returns the value of a user-named alias or an automatic alias. |
| [IDebugClient5::SetKernelConnectionOptions method](..\dbgeng\nf-dbgeng-idebugclient5-setkernelconnectionoptions.md) | The SetKernelConnectionOptions method updates some of the connection options for a live kernel target. |
| [IDebugSymbols3::GetOffsetByName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsetbyname.md) | The GetOffsetByName method returns the location of a symbol identified by name. |
| [IDebugClient5::GetDumpFile method](..\dbgeng\nf-dbgeng-idebugclient5-getdumpfile.md) | The GetDumpFile method describes the files containing supporting information that were used when opening the current dump target. |
| [IDebugClient5::DispatchCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-dispatchcallbacks.md) | The DispatchCallbacks method lets the debugger engine use the current thread for callbacks. |
| [IDebugAdvanced3::GetSymbolInformation method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsymbolinformation.md) | The GetSymbolInformation method returns specified information about a symbol. |
| [IDebugClient5::ExitDispatch method](..\dbgeng\nf-dbgeng-idebugclient5-exitdispatch.md) | The ExitDispatch method causes the DispatchCallbacks method to return. |
| [IDebugControl3::GetInterruptTimeout method](..\dbgeng\nf-dbgeng-idebugcontrol3-getinterrupttimeout.md) | The GetInterruptTimeout method returns the number of seconds that the engine will wait when requesting a break into the debugger. |
| [IDebugControl3::GetEventFilterCommand method](..\dbgeng\nf-dbgeng-idebugcontrol3-geteventfiltercommand.md) | The GetEventFilterCommand method returns the debugger command that the engine will execute when a specified event occurs. |
| [IDebugSymbols3::ReadTypedDataVirtual method](..\dbgeng\nf-dbgeng-idebugsymbols3-readtypeddatavirtual.md) | The ReadTypedDataVirtual method reads the value of a variable in the target's virtual memory. |
| [IDebugSymbols3::CreateSymbolGroup2 method](..\dbgeng\nf-dbgeng-idebugsymbols3-createsymbolgroup2.md) | The CreateSymbolGroup2 method creates a new symbol group. |
| [IDebugClient5::IsKernelDebuggerEnabled method](..\dbgeng\nf-dbgeng-idebugclient5-iskerneldebuggerenabled.md) | The IsKernelDebuggerEnabled method checks whether kernel debugging is enabled for the local kernel. |
| [IDebugControl3::CallExtension method](..\dbgeng\nf-dbgeng-idebugcontrol3-callextension.md) | The CallExtension method calls a debugger extension. |
| [IDebugSystemObjects4::SetImplicitProcessDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setimplicitprocessdataoffset.md) | The SetImplicitProcessDataOffset method sets the implicit process for the current target. |
| [IDebugSystemObjects4::SetImplicitThreadDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setimplicitthreaddataoffset.md) | The SetImplicitThreadDataOffset method sets the implicit thread for the current process. |
| [IDebugControl3::AddBreakpoint method](..\dbgeng\nf-dbgeng-idebugcontrol3-addbreakpoint.md) | The AddBreakpoint method creates a new breakpoint for the current target. |
| [IDebugClient5::CreateProcessAndAttach2Wide method](..\dbgeng\nf-dbgeng-idebugclient5-createprocessandattach2wide.md) | The CreateProcessAndAttach2Wide method creates a process from a specified command line, then attach to that process or another user-mode process. |
| [IDebugSystemObjects4::GetSystemIdsByIndex method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getsystemidsbyindex.md) | The GetSystemIdsByIndex method returns the engine target IDs for the specified targets. |
| [IDebugDataSpaces4::ReadVirtualUncached method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readvirtualuncached.md) | The ReadVirtualUncached method reads memory from the target's virtual address space. |
| [IDebugSymbols3::GetSourcePathElementWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcepathelementwide.md) | The GetSourcePathElementWide method returns an element from the source path. |
| [IDebugControl3::GetSystemVersion method](..\dbgeng\nf-dbgeng-idebugcontrol3-getsystemversion.md) | The GetSystemVersion method returns information that identifies the operating system on the computer that is running the current target. |
| [IDebugDataSpaces4::SearchVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-searchvirtual.md) | The SearchVirtual method searches the target's virtual memory for a specified pattern of bytes. |
| [IDebugControl3::SetNextEventIndex method](..\dbgeng\nf-dbgeng-idebugcontrol3-setnexteventindex.md) | The SetNextEventIndex method sets the next event for the current target by selecting the event from the static list of events for the target, if such a list exists. |
| [IDebugSystemObjects4::GetCurrentProcessSystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocesssystemid.md) | The GetCurrentProcessSystemId method returns the system process ID of the current process. |
| [IDebugSymbols3::GetSymbolModuleWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolmodulewide.md) | The GetSymbolModuleWide method returns the base address of module which contains the specified symbol. |
| [IDebugSymbolGroup2::GetSymbolTypeName method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymboltypename.md) | The GetSymbolTypeName methods return the name of the specified symbol's type. |
| [IDebugSymbols3::GetModuleByIndex method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebyindex.md) | The GetModuleByIndex method returns the location of the module with the specified index. |
| [IDebugClient5::StartProcessServerWide method](..\dbgeng\nf-dbgeng-idebugclient5-startprocessserverwide.md) | The StartProcessServerWide method starts a process server. |
| [IDebugSymbols3::SetSourcePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsourcepathwide.md) | The SetSourcePathWide method sets the source path. |
| [IDebugSystemObjects4::GetThreadIdByHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbyhandle.md) | The GetThreadIdByHandle method returns the engine thread ID for the specified thread. The thread is specified by its system handle. |
| [DebugCommandException function](..\dbgeng\nf-dbgeng-debugcommandexception.md) | Specifies a debug command exception. |
| [IDebugControl3::GetTextMacro method](..\dbgeng\nf-dbgeng-idebugcontrol3-gettextmacro.md) | The GetTextMacro method returns the value of a fixed-name alias. |
| [IDebugClient5::AttachProcess method](..\dbgeng\nf-dbgeng-idebugclient5-attachprocess.md) | The AttachProcess method connects the debugger engine to a user-modeprocess. |
| [IDebugSymbols3::GetLineByOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getlinebyoffsetwide.md) | The GetLineByOffsetWide method returns the source filename and the line number within the source file of an instruction in the target. |
| [IDebugBreakpoint2::SetOffset method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setoffset.md) | The SetOffset method sets the location that triggers a breakpoint. |
| [IDebugDataSpaces4::StartEnumTagged method](..\dbgeng\nf-dbgeng-idebugdataspaces4-startenumtagged.md) | The StartEnumTagged method initializes a enumeration over the tagged data associated with a debugger session. |
| [IDebugControl3::SetExceptionFilterParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexceptionfilterparameters.md) | The SetExceptionFilterParameters method changes the break status and handling status for some exception filters. |
| [IDebugSymbols4::SetScopeEx method](..\dbgeng\nf-dbgeng-idebugsymbols4-setscopeex.md) | Sets the scope as an extended frame structure. |
| [IDebugBreakpoint2::GetOffsetExpression method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getoffsetexpression.md) | The GetOffsetExpression methods return the expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugClient5::OpenDumpFileWide method](..\dbgeng\nf-dbgeng-idebugclient5-opendumpfilewide.md) | The OpenDumpFileWide method opens a dump file as a debugger target. |
| [IDebugDataSpaces4::ReadUnicodeStringVirtualWide method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readunicodestringvirtualwide.md) | The ReadUnicodeStringVirtualWide method reads a null-terminated, Unicode string from the target. |
| [IDebugRegisters2::GetFrameOffset method](..\dbgeng\nf-dbgeng-idebugregisters2-getframeoffset.md) | The GetFrameOffset method returns the location of the stack frame for the current function. |
| [IDebugControl3::OutputStackTrace method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputstacktrace.md) | The OutputStackTrace method outputs either the supplied stack frame or the current stack frames. |
| [IDebugControl4::GetSpecificFilterArgumentWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getspecificfilterargumentwide.md) | The GetSpecificFilterArgumentWide method returns the value of filter argument for thespecific filters that have an argument. |
| [IDebugRegisters2::GetNumberRegisters method](..\dbgeng\nf-dbgeng-idebugregisters2-getnumberregisters.md) | The GetNumberRegisters method returns the number of registers on the target computer. |
| [IDebugDataSpaces4::CheckLowMemory method](..\dbgeng\nf-dbgeng-idebugdataspaces4-checklowmemory.md) | The CheckLowMemory method checks for memory corruption in the low 4 GB of memory. |
| [IDebugControl3::SetInterruptTimeout method](..\dbgeng\nf-dbgeng-idebugcontrol3-setinterrupttimeout.md) | The SetInterruptTimeout method sets the number of seconds that the debugger engine should wait when requesting a break into the debugger. |
| [IDebugClient5::StartServer method](..\dbgeng\nf-dbgeng-idebugclient5-startserver.md) | The StartServer method starts a debugging server. |
| [IDebugControl4::OutputPromptVaListWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputpromptvalistwide.md) | The OutputPromptVaListWide method formats and sends a user prompt to the output callback objects. |
| [IDebugPlmClient3::ResumePlmPackageWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-resumeplmpackagewide.md) | Resumes a Process Lifecycle Management (PLM) package. |
| [IDebugControl3::SetNotifyEventHandle method](..\dbgeng\nf-dbgeng-idebugcontrol3-setnotifyeventhandle.md) | The SetNotifyEventHandle method sets the event that will be signaled after the next exception in a target. |
| [IDebugAdvanced3::GetSymbolInformationWide method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsymbolinformationwide.md) | The SetSymbolInformationWide method returns specified information about a symbol. |
| [IDebugControl4::GetExpressionSyntaxNamesWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getexpressionsyntaxnameswide.md) | The GetExpressionSyntaxNamesWide method returns the full and abbreviated names of an expression syntax. |
| [IDebugEventCallbacksWide::ChangeDebuggeeState method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-changedebuggeestate.md) | The ChangeDebuggeeState callback method is called by the engine when it makes or detects changes to the target. |
| [IDebugControl3::SetEventFilterCommand method](..\dbgeng\nf-dbgeng-idebugcontrol3-seteventfiltercommand.md) | The SetEventFilterCommand method sets a debugger command for the engine to execute when a specified event occurs. |
| [IDebugControl4::EvaluateWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-evaluatewide.md) | The EvaluateWide method evaluates an expression, returning the result. |
| [IDebugBreakpoint2::GetType method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-gettype.md) | The GetType method returns the type of the breakpoint and the type of the processor that a breakpoint is set for. |
| [IDebugClient5::GetEventCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-geteventcallbacks.md) | The GetEventCallbacks method returns the event callbacks object registered with this client. |
| [IDebugDataSpaces4::GetNextTagged method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getnexttagged.md) | The GetNextTagged method returns the GUID for the next block of tagged data in the enumeration. |
| [IDebugSystemObjects4::GetThreadIdByProcessor method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbyprocessor.md) | The GetThreadIdByProcessor method returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor. |
| [IDebugClient5::DetachCurrentProcess method](..\dbgeng\nf-dbgeng-idebugclient5-detachcurrentprocess.md) | The DetachCurrentProcess method detaches the debugger engine from the current process, resuming all its threads. |
| [IDebugControl4::GetLogFile2Wide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getlogfile2wide.md) | The GetLogFile2Wide method returns the name of the currently open log file. |
| [IDebugClient5::WaitForProcessServerEnd method](..\dbgeng\nf-dbgeng-idebugclient5-waitforprocessserverend.md) | The WaitForProcessServerEnd method waits for a local process server to exit. |
| [IDebugSymbols3::OutputTypedDataVirtual method](..\dbgeng\nf-dbgeng-idebugsymbols3-outputtypeddatavirtual.md) | The OutputTypedDataVirtual method formats the contents of a variable in the target's virtual memory, and then sends this to the output callbacks. |
| [IDebugOutputCallbacks::Output method](..\dbgeng\nf-dbgeng-idebugoutputcallbacks-output.md) | The Output callback method is called by the engine to send output from the client to the IDebugOutputCallbacks object that is registered with the client. |
| [IDebugControl4::InputWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-inputwide.md) | The InputWide method requests an input string from the debugger engine. |
| [IDebugControl4::ReturnInputWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-returninputwide.md) | The ReturnInputWide method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input. |
| [IDebugSymbols3::GetSourceEntryOffsetRegions method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentryoffsetregions.md) | Returns all memory regions known to be associated with a source entry. |
| [IDebugSymbols3::OutputTypedDataPhysical method](..\dbgeng\nf-dbgeng-idebugsymbols3-outputtypeddataphysical.md) | The OutputTypedDataPhysical method formats the contents of a variable in the target computer's physical memory, and then sends this to the output callbacks. |
| [IDebugClient5::GetProcessOptions method](..\dbgeng\nf-dbgeng-idebugclient5-getprocessoptions.md) | The GetProcessOptions method retrieves the process options affecting the current process. |
| [IDebugControl4::GetLogFile2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-getlogfile2.md) | The GetLogFile2 method returns the name of the currently open log file. |
| [IDebugSymbols3::GetNameByOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnamebyoffsetwide.md) | The GetNameByOffsetWide method returns the name of the symbol at the specified location in the target's virtual address space. |
| [IDebugSystemObjects4::GetCurrentProcessPeb method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocesspeb.md) | The GetCurrentProcessPeb method returns the process environment block (PEB) of the current process. |
| [IDebugSymbols4::GetLineByInlineContextWide method](..\dbgeng\nf-dbgeng-idebugsymbols4-getlinebyinlinecontextwide.md) | Gets a line by inline context. |
| [IDebugAdvanced4::GetSymbolInformationWideEx method](..\dbgeng\nf-dbgeng-idebugadvanced4-getsymbolinformationwideex.md) | The GetSymbolInformationWideEx method returns specified information about a symbol. |
| [IDebugSymbols3::GetModuleByModuleName2Wide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebymodulename2wide.md) | The GetModuleByModuleName2Wide method searches through the process's modules for one with the specified name. |
| [IDebugRegisters2::GetPseudoValues method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudovalues.md) | The GetPseudoValues method returns the values of a number of pseudo-registers. |
| [IDebugBreakpoint2::AddFlags method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-addflags.md) | The AddFlags method adds flags to a breakpoint. |
| [IDebugControl3::GetReturnOffset method](..\dbgeng\nf-dbgeng-idebugcontrol3-getreturnoffset.md) | The GetReturnOffset method returns the return address for the current function. |
| [IDebugControl4::OutputWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputwide.md) | The OutputWide method formats a string and send the result to output callbacks that have been registered with the engine's clients. |
| [IDebugDataSpaces4::ReadMsr method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readmsr.md) | The ReadMsr method reads a specified Model-Specific Register (MSR). |
| [IDebugDataSpaces4::FillVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-fillvirtual.md) | The FillVirtual method writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled. |
| [IDebugClient5::AbandonCurrentProcess method](..\dbgeng\nf-dbgeng-idebugclient5-abandoncurrentprocess.md) | The AbandonCurrentProcess method removes the current process from the debugger engine's process list without detaching or terminating the process. |
| [IDebugControl4::ExecuteWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-executewide.md) | The ExecuteWide method executes the specified debugger commands. |
| [IDebugEventCallbacks::ChangeEngineState method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-changeenginestate.md) | The ChangeEngineState callback method is called by the engine when its state has changed. |
| [IDebugBreakpoint2::SetOffsetExpression method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setoffsetexpression.md) | The SetOffsetExpression methods set an expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugControl3::GetNumberBreakpoints method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberbreakpoints.md) | The GetNumberBreakpoints method returns the number of breakpoints for the current process. |
| [IDebugEventCallbacks::CreateProcess method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-createprocess.md) | The CreateProcess callback method is called by the engine when a create-processdebugging event occurs in the target. |
| [IDebugSymbols3::AppendSourcePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendsourcepathwide.md) | The AppendSourcePathWide method appends directories to the source path. |
| [IDebugControl3::OutputTextReplacements method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputtextreplacements.md) | The OutputTextReplacements method prints all the currently defined user-named aliases to the debugger's output stream. |
| [IDebugControl3::Output method](..\dbgeng\nf-dbgeng-idebugcontrol3-output.md) | The Output method formats a string and send the result to output callbacks that have been registered with the engine's clients. |
| [IDebugSymbols3::GetImagePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getimagepathwide.md) | The GetImagePathWide method returns the executable image path. |
| [IDebugDataSpaces4::WriteControl method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writecontrol.md) | The WriteControl method writes implementation-specific system data. |
| [IDebugDataSpaces4::WritePhysical2 method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writephysical2.md) | The WritePhysical2 method writes data to the specified physical address in the target's memory. |
| [IDebugControl3::GetLastEventInformation method](..\dbgeng\nf-dbgeng-idebugcontrol3-getlasteventinformation.md) | The GetLastEventInformation method returns information about the last event that occurred in a target. |
| [IDebugSymbols3::GetSymbolEntryBySymbolEntry method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentrybysymbolentry.md) | Allows navigation within the symbol entry hierarchy. |
| [IDebugClient5::GetEventCallbacksWide method](..\dbgeng\nf-dbgeng-idebugclient5-geteventcallbackswide.md) | The GetEventCallbacksWide method returns the event callbacks object registered with this client. |
| [IDebugClient5::GetOutputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getoutputcallbacks.md) | The GetOutputCallbacks method returns the output callbacks object registered with the client. |
| [IDebugSymbols3::GetTypeId method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypeid.md) | The GetTypeId method looks up the specified type and return its type ID. |
| [IDebugClient5::CreateProcess2 method](..\dbgeng\nf-dbgeng-idebugclient5-createprocess2.md) | The CreateProcess2 method executes the given command to create a new process. |
| [IDebugClient5::OutputIdentity method](..\dbgeng\nf-dbgeng-idebugclient5-outputidentity.md) | The OutputIdentity method formats and outputs a string describing the computer and user this client represents. |
| [IDebugDataSpaces4::ReadMultiByteStringVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readmultibytestringvirtual.md) | The ReadMultiByteStringVirtual method reads a null-terminated, multibyte string from the target. |
| [IDebugSymbols5::GetCurrentScopeFrameIndexEx method](..\dbgeng\nf-dbgeng-idebugsymbols5-getcurrentscopeframeindexex.md) | Gets the index of the current frame. |
| [IDebugSymbols3::WriteTypedDataVirtual method](..\dbgeng\nf-dbgeng-idebugsymbols3-writetypeddatavirtual.md) | The WriteTypedDataVirtual method writes data to the target's virtual address space. The number of bytes written is the size of the specified type. |
| [IDebugControl3::OutputVersionInformation method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputversioninformation.md) | The OutputVersionInformation method prints version information about the debugger engine to the debugger console. |
| [IDebugSymbols3::GetSymbolEntriesByName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentriesbyname.md) | The GetSymbolEntriesByName method returns the symbols whose names match a given pattern. |
| [IDebugControl4::ControlledOutputVaListWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-controlledoutputvalistwide.md) | The ControlledOutputVaListWide method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugControl3::GetStackTrace method](..\dbgeng\nf-dbgeng-idebugcontrol3-getstacktrace.md) | The GetStackTrace method returns the frames at the top of the specified call stack. |
| [IDebugClient5::SetOutputCallbacksWide method](..\dbgeng\nf-dbgeng-idebugclient5-setoutputcallbackswide.md) | The SetOutputCallbacksWide method registers an output callbacks object with this client. |
| [IDebugEventCallbacksWide::ChangeEngineState method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-changeenginestate.md) | The ChangeEngineState callback method is called by the engine when its state has changed. |
| [IDebugControl3::RemoveExtension method](..\dbgeng\nf-dbgeng-idebugcontrol3-removeextension.md) | The RemoveExtension method unloads an extension library. |
| [IDebugControl3::GetPossibleExecutingProcessorTypes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getpossibleexecutingprocessortypes.md) | The GetPossibleExecutingProcessorTypes method returns the processor types that are supported by the computer running the current target. |
| [IDebugControl3::OutputDisassemblyLines method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputdisassemblylines.md) | The OutputDisassemblyLines method disassembles several processor instructions and sends the resulting assembly instructions to the output callbacks. |
| [IDebugClient5::GetRunningProcessDescription method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocessdescription.md) | The GetRunningProcessDescription method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [IDebugEventCallbacks::Breakpoint method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-breakpoint.md) | The Breakpoint callback method is called by the engine when the target issues a breakpointexception. |
| [IDebugControl3::GetSpecificFilterParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-getspecificfilterparameters.md) | The GetSpecificFilterParameters method returns the parameters for specific event filters. |
| [IDebugClient5::GetOtherOutputMask method](..\dbgeng\nf-dbgeng-idebugclient5-getotheroutputmask.md) | The GetOtherOutputMask method returns the output mask for another client. |
| [IDebugDataSpaces4::WriteVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writevirtual.md) | The WriteVirtual method writes data to the target's virtual address space. |
| [IDebugDataSpaces4::WritePointersVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writepointersvirtual.md) | The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space. |
| [IDebugDataSpaces4::ReadHandleData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readhandledata.md) | The ReadHandleData method retrieves information about a system object specified by a system handle. |
| [IDebugClient5::SetKernelConnectionOptionsWide method](..\dbgeng\nf-dbgeng-idebugclient5-setkernelconnectionoptionswide.md) | The SetKernelConnectionOptionsWide method updates some of the connection options for a live kernel target. |
| [IDebugSymbolGroup2::GetSymbolEntryInformation method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolentryinformation.md) | The GetSymbolEntryInformation method returns information about a symbol in a symbol group. |
| [IDebugSymbols3::GetSymbolTypeId method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymboltypeid.md) | The GetSymbolTypeId method returns the type ID and module of the specified symbol. |
| [IDebugClient5::GetOutputLinePrefixWide method](..\dbgeng\nf-dbgeng-idebugclient5-getoutputlineprefixwide.md) | Gets a Unicode character string prefix for output lines. |
| [IDebugSymbols3::GetModuleNames method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulenames.md) | The GetModuleNames method returns the names of the specified module. |
| [IDebugAdvanced3::FindSourceFileAndToken method](..\dbgeng\nf-dbgeng-idebugadvanced3-findsourcefileandtoken.md) | The FindSourceFileAndToken method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [IDebugClient5::GetQuitLockStringWide method](..\dbgeng\nf-dbgeng-idebugclient5-getquitlockstringwide.md) | Gets a Unicode character quit lock string. |
| [IDebugControl4::SetExceptionFilterSecondCommandWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-setexceptionfiltersecondcommandwide.md) | The SetExceptionFilterSecondCommandWide method sets the command that will be executed by the debugger engine on the second chance of a specified exception. |
| [IDebugSymbolGroup2::GetSymbolValueText method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolvaluetext.md) | The GetSymbolValueText method returns a string that represents the value of a symbol. |
| [IDebugControl4::GetEventIndexDescriptionWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-geteventindexdescriptionwide.md) | The GetEventIndexDescriptionWide method describes the specified event in a static list of events for the current target. |
| [IDebugClient5::CreateProcessWide method](..\dbgeng\nf-dbgeng-idebugclient5-createprocesswide.md) | The CreateProcessWide method creates a process from the specified command line. |
| [IDebugControl3::SetExpressionSyntaxByName method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexpressionsyntaxbyname.md) | The SetExpressionSyntaxByName method sets the syntax that the engine will use to evaluate expressions. |
| [IDebugRegisters2::GetPseudoIndexByNameWide method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudoindexbynamewide.md) | The GetPseudoIndexByNameWide method returns the index of a pseudo-register. |
| [IDebugSymbols3::SetSymbolPathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsymbolpathwide.md) | The SetSymbolPathWide method sets the symbol path. |
| [IDebugControl3::OutputDisassembly method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputdisassembly.md) | The OutputDisassembly method disassembles a processor instruction and sends the disassembly to the output callbacks. |
| [IDebugSymbols4::OutputSymbolByInlineContext method](..\dbgeng\nf-dbgeng-idebugsymbols4-outputsymbolbyinlinecontext.md) | Specifies an output symbol by using an inline context. |
| [IDebugAdvanced3::Request method](..\dbgeng\nf-dbgeng-idebugadvanced3-request.md) | The Request method performs a variety of different operations. |
| [IDebugSymbols3::GetModuleByModuleName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebymodulename.md) | The GetModuleByModuleName method searches through the target's modules for one with the specified name. |
| [IDebugClient7::SetClientContext method](..\dbgeng\nf-dbgeng-idebugclient7-setclientcontext.md) | The SetClientContext method is reserved for internal use. |
| [DebugConnectWide function](..\dbgeng\nf-dbgeng-debugconnectwide.md) | The DebugConnect and DebugConnectWide functions create a new client object and return an interface pointer to it. The client object will be connected to a remote host. |
| [IDebugOutputCallbacks2::GetInterestMask method](..\dbgeng\nf-dbgeng-idebugoutputcallbacks2-getinterestmask.md) | Allows the callback object to describe which kinds of output notifications it wants to receive. |
| [IDebugRegisters2::GetPseudoDescription method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudodescription.md) | The GetPseudoDescription method returns a description of a pseudo-register, including its name and type. |
| [IDebugSymbols3::SetScope method](..\dbgeng\nf-dbgeng-idebugsymbols3-setscope.md) | The SetScope method sets the current scope. |
| [IDebugRegisters2::GetValue method](..\dbgeng\nf-dbgeng-idebugregisters2-getvalue.md) | The GetValue method gets the value of one of the target's registers. |
| [IDebugBreakpoint2::SetDataParameters method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setdataparameters.md) | The SetDataParameters method sets the parameters for a processor breakpoint. |
| [IDebugSystemObjects4::GetCurrentProcessUpTime method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessuptime.md) | The GetCurrentProcessUpTime method returns the length of time the current process has been running. |
| [IDebugEventCallbacks::ChangeSymbolState method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-changesymbolstate.md) | The ChangeSymbolState callback method is called by the engine when the symbol state changes. |
| [IDebugControl3::GetLogMask method](..\dbgeng\nf-dbgeng-idebugcontrol3-getlogmask.md) | The GetLogMask method returns the output mask for the currently open log file. |
| [IDebugSystemObjects4::GetCurrentThreadDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreaddataoffset.md) | The GetCurrentThreadDataOffset method returns the location of the system data structure for the current thread. |
| [IDebugClient5::CreateProcessAndAttach2 method](..\dbgeng\nf-dbgeng-idebugclient5-createprocessandattach2.md) | The CreateProcessAndAttach2 method creates a process from a specified command line, then attaches to that process or another user-mode process. |
| [IDebugSymbols3::GetSymbolModule method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolmodule.md) | The GetSymbolModule method returns the base address of module which contains the specified symbol. |
| [IDebugRegisters2::GetIndexByNameWide method](..\dbgeng\nf-dbgeng-idebugregisters2-getindexbynamewide.md) | The GetIndexByNameWide method returns the index of the named register. |
| [IDebugSymbols3::GetImagePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-getimagepath.md) | The GetImagePath method returns the executable image path. |
| [IDebugControl4::AddBreakpoint2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-addbreakpoint2.md) | The AddBreakpoint2 method creates a new breakpoint for the current target. |
| [IDebugClient5::GetExitCode method](..\dbgeng\nf-dbgeng-idebugclient5-getexitcode.md) | The GetExitCode method returns the exit code of the current process if that process has already run through to completion. |
| [IDebugSymbols3::GetSymbolEntriesByNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentriesbynamewide.md) | The GetSymbolEntriesByNameWide method returns the symbols whose names match a given pattern. |
| [IDebugClient5::AttachKernelWide method](..\dbgeng\nf-dbgeng-idebugclient5-attachkernelwide.md) | The AttachKernelWide method connects the debugger engine to a kernel target. |
| [IDebugSymbols3::IsManagedModule method](..\dbgeng\nf-dbgeng-idebugsymbols3-ismanagedmodule.md) | Checks whether the engine is using managed debugging support when it retrieves information for a module. |
| [IDebugBreakpoint2::GetCommandWide method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getcommandwide.md) | The GetCommand method returns the command string that is executed when a breakpoint is triggered. |
| [IDebugSymbols3::GetFieldName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldname.md) | The GetFieldName method returns the name of a field within a structure. |
| [IDebugControl3::GetBreakpointParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-getbreakpointparameters.md) | The GetBreakpointParameters method returns the parameters of one or more breakpoints. |
| [IDebugControl3::SetExceptionFilterSecondCommand method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexceptionfiltersecondcommand.md) | The SetExceptionFilterSecondCommand method sets the command that will be executed by the debugger engine on the second chance of a specified exception. |
| [IDebugClient5::GetInputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getinputcallbacks.md) | The GetInputCallbacks method returns the input callbacks object registered with this client. |
| [IDebugClient::SetOutputWidth method](..\dbgeng\nf-dbgeng-idebugclient-setoutputwidth.md) | Controls the width of an output line for commands that produce formatted output. |
| [IDebugControl3::GetPromptText method](..\dbgeng\nf-dbgeng-idebugcontrol3-getprompttext.md) | The GetPromptText method returns the standard prompt text that will be prepended to the formatted output specified in the OutputPrompt and OutputPromptVaList methods. |
| [IDebugSystemObjects4::GetEventProcess method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-geteventprocess.md) | The GetEventProcess method returns the engine process ID for the process on which the last event occurred. |
| [IDebugClient5::SetProcessOptions method](..\dbgeng\nf-dbgeng-idebugclient5-setprocessoptions.md) | The SetProcessOptions method sets the process options affecting the current process. |
| [IDebugSystemObjects4::GetProcessIdByDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidbydataoffset.md) | The GetProcessIdByDataOffset method returns the engine process ID for the specified process. The process is specified by its data offset. |
| [IDebugControl4::GetSystemVersionValues method](..\dbgeng\nf-dbgeng-idebugcontrol4-getsystemversionvalues.md) | The GetSystemVersionValues method returns version number information for the current target. |
| [IDebugSymbolGroup2::ExpandSymbol method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-expandsymbol.md) | The ExpandSymbol method adds or removes the children of a symbol from a symbol group. |
| [IDebugSymbols3::GetOffsetByLineWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsetbylinewide.md) | The GetOffsetByLineWide method returns the location of the instruction that corresponds to a specified line in the source code. |
| [IDebugControl3::RemoveTextReplacements method](..\dbgeng\nf-dbgeng-idebugcontrol3-removetextreplacements.md) | The RemoveTextReplacements method removes all user-named aliases. |
| [IDebugSymbols3::GetNearNameByOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnearnamebyoffsetwide.md) | The GetNearNameByOffsetWide method returns the name of a symbol that is located near the specified location. |
| [IDebugControl3::GetNotifyEventHandle method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnotifyeventhandle.md) | The GetNotifyEventHandle method receives the handle of the event that will be signaled after the next exception in a target. |
| [IDebugControl3::SetTextReplacement method](..\dbgeng\nf-dbgeng-idebugcontrol3-settextreplacement.md) | The SetTextReplacement method sets the value of a user-named alias. |
| [IDebugClient5::GetNumberEventCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getnumbereventcallbacks.md) | The GetNumberEventCallbacks method returns the number of event callbacks that are interested in the given events. |
| [IDebugDataSpaces4::WriteBusData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writebusdata.md) | The WriteBusData method writes data to a system bus. |
| [IDebugSystemObjects4::GetImplicitThreadDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getimplicitthreaddataoffset.md) | The GetImplicitThreadDataOffset method returns the implicit thread for the current process. |
| [IDebugSymbolGroup2::GetSymbolNameWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolnamewide.md) | The GetSymbolNameWide method returns the name of a symbol in a symbol group. |
| [IDebugControl3::GetNearInstruction method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnearinstruction.md) | The GetNearInstruction method returns the location of a processor instruction relative to a given location. |
| [IDebugBreakpoint2::RemoveFlags method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-removeflags.md) | The RemoveFlags method removes flags from a breakpoint. |
| [IDebugControl4::GetEventFilterTextWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-geteventfiltertextwide.md) | The GetEventFilterTextWide method returns a short description of an event for a specific filter. |
| [IDebugClient5::AddProcessOptions method](..\dbgeng\nf-dbgeng-idebugclient5-addprocessoptions.md) | The AddProcessOptions method adds the process options to those options that affect the current process. |
| [IDebugControl3::GetExpressionSyntaxNames method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexpressionsyntaxnames.md) | The GetExpressionSyntaxNames method returns the full and abbreviated names of an expression syntax. |
| [IDebugEventCallbacksWide::Exception method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-exception.md) | The Exception callback method is called by the engine when an exceptiondebugging event occurs in the target. |
| [IDebugClient5::CreateProcessAndAttach method](..\dbgeng\nf-dbgeng-idebugclient5-createprocessandattach.md) | The CreateProcessAndAttach method creates a process from a specified command line, then attach to another user-mode process. |
| [IDebugControl3::GetExtensionByPath method](..\dbgeng\nf-dbgeng-idebugcontrol3-getextensionbypath.md) | The GetExtensionByPath method returns the handle for an already loaded extension library. |
| [IDebugControl3::WaitForEvent method](..\dbgeng\nf-dbgeng-idebugcontrol3-waitforevent.md) | The WaitForEvent method waits for an event that breaks into the debugger engine application. |
| [IDebugControl3::GetTextReplacement method](..\dbgeng\nf-dbgeng-idebugcontrol3-gettextreplacement.md) | The GetTextReplacement method returns the value of a user-named alias or an automatic alias. |
| [IDebugOutputCallbacksWide::Output method](..\dbgeng\nf-dbgeng-idebugoutputcallbackswide-output.md) | The Output callback method is called by the engine to send output from the client to the IDebugOutputCallbacksWide object that is registered with the client. |
| [IDebugDataSpaces4::FillPhysical method](..\dbgeng\nf-dbgeng-idebugdataspaces4-fillphysical.md) | The FillPhysical method writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled. |
| [IDebugDataSpaces4::ReadIo method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readio.md) | The ReadIo method reads from the system and bus I/O memory. |
| [IDebugSymbols3::ReloadWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-reloadwide.md) | The ReloadWide method deletes the engine's symbol information for the specified module and reload these symbols as needed. |
| [IDebugControl3::GetNumberTextReplacements method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumbertextreplacements.md) | The GetNumberTextReplacements method returns the number of currently defined user-named and automatic aliases. |
| [IDebugDataSpaces4::EndEnumTagged method](..\dbgeng\nf-dbgeng-idebugdataspaces4-endenumtagged.md) | The EndEnumTagged method releases the resources used by the specified enumeration. |
| [IDebugControl4::ExecuteCommandFileWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-executecommandfilewide.md) | The ExecuteCommandFileWide method opens the specified file and executes the debugger commands that are contained within. |
| [IDebugSymbols3::GetOffsetByLine method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsetbyline.md) | The GetOffsetByLine method returns the location of the instruction that corresponds to a specified line in the source code. |
| [IDebugControl3::Assemble method](..\dbgeng\nf-dbgeng-idebugcontrol3-assemble.md) | The Assemble method assembles a single processor instruction. The assembled instruction is placed in the target's memory. |
| [IDebugRegisters2::SetValues method](..\dbgeng\nf-dbgeng-idebugregisters2-setvalues.md) | The SetValues method sets the value of several of the target's registers. |
| [IDebugSymbols5::SetScopeFrameByIndexEx method](..\dbgeng\nf-dbgeng-idebugsymbols5-setscopeframebyindexex.md) | Sets the current frame by using an index. |
| [IDebugControl4::RemoveBreakpoint2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-removebreakpoint2.md) | The RemoveBreakpoint2 method removes a breakpoint. |
| [IDebugEventCallbacksWide::CreateProcess method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-createprocess.md) | The CreateProcess callback method is called by the engine when a create-processdebugging event occurs in the target. |
| [IDebugSymbols3::GetModuleByModuleNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebymodulenamewide.md) | The GetModuleByModuleNameWide method searches through the target's modules for one with the specified name. |
| [IDebugControl4::GetStoredEventInformation method](..\dbgeng\nf-dbgeng-idebugcontrol4-getstoredeventinformation.md) | The GetStoredEventInformation method retrieves information about an event of interest available in the current target. |
| [IDebugSystemObjects4::GetTotalNumberThreadsAndProcesses method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-gettotalnumberthreadsandprocesses.md) | The GetTotalNumberThreadsAndProcesses method returns the total number of threads and processes in all the targets the engine is attached to, in addition to the largest number of threads and processes in a target. |
| [IDebugClient5::DetachProcesses method](..\dbgeng\nf-dbgeng-idebugclient5-detachprocesses.md) | The DetachProcesses method detaches the debugger engine from all processes in all targets, resuming all their threads. |
| [IDebugEventCallbacks::UnloadModule method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-unloadmodule.md) | The UnloadModule callback method is called by the engine when a module-unload debugging event occurs in the target. |
| [IDebugEventCallbacksWide::GetInterestMask method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-getinterestmask.md) | The GetInterestMask callback method is called to determine which events the IDebugEventCallbacksWide object is interested in. The engine calls GetInterestMask when the object is registered with a client by using SetEventCallbacks. |
| [IDebugSymbolGroup2::AddSymbolWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-addsymbolwide.md) | The AddSymbolWide method adds a symbol to a symbol group. |
| [IDebugSymbols3::SetSourcePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsourcepath.md) | The SetSourcePath method sets the source path. |
| [IDebugClient5::SetOutputMask method](..\dbgeng\nf-dbgeng-idebugclient5-setoutputmask.md) | The SetOutputMask method sets the output mask for the client. |
| [IDebugSystemObjects4::GetNumberProcesses method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getnumberprocesses.md) | The GetNumberProcesses method returns the number of processes for the current target. |
| [IDebugClient5::GetNumberOutputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getnumberoutputcallbacks.md) | The GetNumberOutputCallbacks method returns the number of output callbacks registered over all clients. |
| [IDebugClient5::TerminateProcesses method](..\dbgeng\nf-dbgeng-idebugclient5-terminateprocesses.md) | The TerminateProcesses method attempts to terminate all processes in all targets. |
| [IDebugControl4::SetExpressionSyntaxByNameWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-setexpressionsyntaxbynamewide.md) | The SetExpressionSyntaxByNameWide method sets the syntax that the engine will use to evaluate expressions. |
| [IDebugSymbols3::SetImagePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-setimagepathwide.md) | The SetImagePathWide method sets the executable image path. |
| [IDebugSymbols3::StartSymbolMatchWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-startsymbolmatchwide.md) | The StartSymbolMatchWide method initializes a search for symbols whose names match a given pattern. |
| [IDebugControl3::SetSystemErrorControl method](..\dbgeng\nf-dbgeng-idebugcontrol3-setsystemerrorcontrol.md) | The SetSystemErrorControl method sets the control values for handling system errors. |
| [IDebugSymbols3::GetScope method](..\dbgeng\nf-dbgeng-idebugsymbols3-getscope.md) | The GetScope method returns information about the current scope. |
| [IDebugSymbols3::ReadTypedDataPhysical method](..\dbgeng\nf-dbgeng-idebugsymbols3-readtypeddataphysical.md) | The ReadTypedDataPhysical method reads the value of a variable from the target computer's physical memory. |
| [IDebugControl3::GetActualProcessorType method](..\dbgeng\nf-dbgeng-idebugcontrol3-getactualprocessortype.md) | The GetActualProcessorType method returns the processor type of the physical processor of the computer that is running the target. |
| [IDebugSymbols3::GetSymbolPathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolpathwide.md) | The GetSymbolPathWide method returns the symbol path. |
| [IDebugDataSpaces4::ReadTagged method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readtagged.md) | The ReadTagged method reads the tagged data that might be associated with a debugger session. |
| [IDebugControl4::GetLastEventInformationWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getlasteventinformationwide.md) | The GetLastEventInformationWide method returns information about the last event that occurred in a target. |
| [IDebugEventCallbacksWide::ExitProcess method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-exitprocess.md) | The ExitProcess callback method is called by the engine when an exit-processdebugging event occurs in the target. |
| [IDebugControl3::AddExtension method](..\dbgeng\nf-dbgeng-idebugcontrol3-addextension.md) | The AddExtension method loads an extension library into the debugger engine. |
| [IDebugControl3::SetLogMask method](..\dbgeng\nf-dbgeng-idebugcontrol3-setlogmask.md) | The SetLogMask method sets the output mask for the currently open log file. |
| [IDebugBreakpoint2::GetFlags method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getflags.md) | The GetFlags method returns the flags for a breakpoint. |
| [IDebugControl3::GetAssemblyOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-getassemblyoptions.md) | The GetAssemblyOptions method returns the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target. |
| [IDebugSymbols3::RemoveSyntheticSymbol method](..\dbgeng\nf-dbgeng-idebugsymbols3-removesyntheticsymbol.md) | The RemoveSyntheticSymbol method removes a synthetic symbol from a module in the current process. |
| [IDebugClient5::GetIdentityWide method](..\dbgeng\nf-dbgeng-idebugclient5-getidentitywide.md) | The GetIdentityWide method returns a string describing the computer and user this client represents. |
| [IDebugSymbols3::GetSymbolOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymboloptions.md) | The GetSymbolOptions method returns the engine's global symbol options. |
| [IDebugRegisters2::GetDescription method](..\dbgeng\nf-dbgeng-idebugregisters2-getdescription.md) | The GetDescription method returns the description of a register. |
| [IDebugControl3::RemoveEngineOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-removeengineoptions.md) | The RemoveEngineOptions method turns off some of the engine's options. |
| [IDebugSymbols3::GetTypeSize method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypesize.md) | The GetTypeSize method returns the number of bytes of memory an instance of the specified type requires. |
| [IDebugBreakpoint2::SetOffsetExpressionWide method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setoffsetexpressionwide.md) | The SetOffsetExpressionWide methods set an expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugSymbols3::GetSourceEntryStringWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentrystringwide.md) | Queries symbol information and returns locations in the target's memory. |
| [IDebugSymbolGroup2::GetSymbolTypeNameWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymboltypenamewide.md) | The GetSymbolTypeNameWide method returns the name of the specified symbol's type. |
| [IDebugControl3::CloseLogFile method](..\dbgeng\nf-dbgeng-idebugcontrol3-closelogfile.md) | The CloseLogFile method closes the currently-open log file. |
| [IDebugControl3::GetNumberSupportedProcessorTypes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumbersupportedprocessortypes.md) | The GetNumberSupportedProcessorTypes method returns the number of processor types supported by the engine. |
| [IDebugSymbols3::GetFunctionEntryByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfunctionentrybyoffset.md) | The GetFunctionEntryByOffset method returns the function entry information for a function. |
| [IDebugSymbolGroup2::GetSymbolParameters method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolparameters.md) | The GetSymbolParameters method returns the symbol parameters that describe the specified symbols in a symbol group. |
| [IDebugControl5::GetStackTraceEx method](..\dbgeng\nf-dbgeng-idebugcontrol5-getstacktraceex.md) | The GetStackTraceEx method returns the frames at the top of the specified call stack. The GetStackTraceEx method provides inline frame support. For more information about working with inline functions, see Debugging Optimized Code and Inline Functions. |
| [IDebugControl3::GetBreakpointById method](..\dbgeng\nf-dbgeng-idebugcontrol3-getbreakpointbyid.md) | The GetBreakpointById method returns the breakpoint with the specified breakpoint ID. |
| [IDebugControl3::OpenLogFile method](..\dbgeng\nf-dbgeng-idebugcontrol3-openlogfile.md) | The OpenLogFile method opens a log file that will receive output from the client objects. |
| [DebugCreateEx function](..\dbgeng\nf-dbgeng-debugcreateex.md) | The DebugCreateEx function creates a new client object and returns an interface pointer to it. |
| [IDebugClient5::AddDumpInformationFile method](..\dbgeng\nf-dbgeng-idebugclient5-adddumpinformationfile.md) | The AddDumpInformationFile method registers additional files containing supporting information that will be used when opening a dump file. The Unicode version of this method is AddDumpInformationFileWide. |
| [IDebugControl3::ExecuteCommandFile method](..\dbgeng\nf-dbgeng-idebugcontrol3-executecommandfile.md) | The ExecuteCommandFile method opens the specified file and executes the debugger commands that are contained within. |
| [IDebugSymbols3::SetScopeFromJitDebugInfo method](..\dbgeng\nf-dbgeng-idebugsymbols3-setscopefromjitdebuginfo.md) | Recovers just-in-time (JIT) debugging information and sets current debugger scope context based on that information. |
| [IDebugEventCallbacksWide::ChangeSymbolState method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-changesymbolstate.md) | The ChangeSymbolState callback method is called by the engine when the symbol state changes. |
| [IDebugDataSpaces4::WriteMsr method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writemsr.md) | The WriteMsr method writes a value to the specified Model-Specific Register (MSR). |
| [IDebugRegisters2::GetInstructionOffset2 method](..\dbgeng\nf-dbgeng-idebugregisters2-getinstructionoffset2.md) | The GetInstructionOffset2 method returns the location of the current thread's current instruction. |
| [IDebugDataSpaces2::QueryVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces2-queryvirtual.md) | The QueryVirtual method provides information about the specified pages in the target's virtual address space. |
| [IDebugEventCallbacks::GetInterestMask method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-getinterestmask.md) | The GetInterestMask callback method is called to determine which events the IDebugEventCallbacks object is interested in. The engine calls GetInterestMask when the object is registered with a client by using SetEventCallbacks. |
| [IDebugClient5::SetInputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-setinputcallbacks.md) | The SetInputCallbacks method registers an input callbacks object with the client. |
| [IDebugPlmClient3::QueryPlmPackageWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-queryplmpackagewide.md) | Query a Process Lifecycle Management (PLM) package. |
| [IDebugControl3::GetCurrentEventIndex method](..\dbgeng\nf-dbgeng-idebugcontrol3-getcurrenteventindex.md) | The GetCurrentEventIndex method returns the index of the current event within the current list of events for the current target, if such a list exists. |
| [IDebugRegisters2::OutputRegisters2 method](..\dbgeng\nf-dbgeng-idebugregisters2-outputregisters2.md) | The OutputRegisters2 method formats and outputs the target's registers. |
| [IDebugControl::Input method](..\dbgeng\nf-dbgeng-idebugcontrol-input.md) | The Input method requests an input string from the debugger engine. |
| [IDebugSystemObjects4::GetProcessIdByHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidbyhandle.md) | The GetProcessIdByHandle method returns the engine process ID for the specified process. The process is specified by its system handle. |
| [IDebugAdvanced3::SetThreadContext method](..\dbgeng\nf-dbgeng-idebugadvanced3-setthreadcontext.md) | The SetThreadContext method sets the current thread context. |
| [IDebugControl3::SetSpecificFilterParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-setspecificfilterparameters.md) | The SetSpecificFilterParameters method changes the break status and handling status for some specific event filters. |
| [IDebugRegisters2::GetDescriptionWide method](..\dbgeng\nf-dbgeng-idebugregisters2-getdescriptionwide.md) | The GetDescriptionWide method returns the description of a register. |
| [IDebugControl4::OutputContextStackTrace method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputcontextstacktrace.md) | The OutputContextStackTrace method prints the call stack specified by an array of stack frames and corresponding register contexts. |
| [IDebugControl4::GetBreakpointById2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-getbreakpointbyid2.md) | The GetBreakpointById2 method returns the breakpoint with the specified breakpoint ID. |
| [IDebugSymbols3::GetModuleByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebyoffset.md) | The GetModuleByOffset method searches through the target's modules for one whose memory allocation includes the specified location. |
| [IDebugSymbolGroup2::OutputSymbols method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-outputsymbols.md) | The OutputSymbols method prints the specified symbols to the debugger console. |
| [IDebugSymbols3::GetSymbolEntryString method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentrystring.md) | The GetSymbolEntryString method returns string information for the specified symbol. |
| [IDebugSystemObjects3::GetCurrentSystemServer method](..\dbgeng\nf-dbgeng-idebugsystemobjects3-getcurrentsystemserver.md) | Gets the server for the current process. |
| [IDebugEventCallbacksWide::CreateThread method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-createthread.md) | The CreateThread callback method is called by the engine when a create-threaddebugging event occurs in the target. |
| [IDebugSymbolGroup2::WriteSymbolWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-writesymbolwide.md) | The WriteSymbolWide method sets the value of the specified symbol. |
| [IDebugRegisters2::SetValues2 method](..\dbgeng\nf-dbgeng-idebugregisters2-setvalues2.md) | The SetValues2 method sets the value of several of the target's registers. |
| [IDebugBreakpoint2::SetFlags method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setflags.md) | The SetFlags method sets the flags for a breakpoint. |
| [IDebugControl3::GetInterrupt method](..\dbgeng\nf-dbgeng-idebugcontrol3-getinterrupt.md) | The GetInterrupt method checks whether a user interrupt was issued. |
| [IDebugSymbols3::GetScopeSymbolGroup2 method](..\dbgeng\nf-dbgeng-idebugsymbols3-getscopesymbolgroup2.md) | The GetScopeSymbolGroup2 method returns a symbol group containing the symbols in the current target's scope. |
| [IDebugSystemObjects4::GetCurrentProcessDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessdataoffset.md) | The GetCurrentProcessDataOffset method returns the location of the system data structure describing the current process. |
| [IDebugControl3::GetPageSize method](..\dbgeng\nf-dbgeng-idebugcontrol3-getpagesize.md) | The GetPageSize method returns the page size for the effective processor mode. |
| [IDebugSymbols3::WriteTypedDataPhysical method](..\dbgeng\nf-dbgeng-idebugsymbols3-writetypeddataphysical.md) | The WriteTypedDataPhysical method writes the value of a variable in the target computer's physical memory. |
| [IDebugControl4::GetTextMacroWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-gettextmacrowide.md) | The GetTextMacroWide method returns the value of a fixed-name alias. |
| [IDebugClient5::WriteDumpFile2 method](..\dbgeng\nf-dbgeng-idebugclient5-writedumpfile2.md) | The WriteDumpFile2 method creates a user-mode or kernel-modecrash dump file. |
| [IDebugClient5::PushOutputLinePrefixWide method](..\dbgeng\nf-dbgeng-idebugclient5-pushoutputlineprefixwide.md) | Saves a wide string output line prefix. |
| [IDebugClient5::AddDumpInformationFileWide method](..\dbgeng\nf-dbgeng-idebugclient5-adddumpinformationfilewide.md) | The AddDumpInformationFileWide method registers additional files containing supporting information that will be used when opening a dump file. The ASCII version of this method is AddDumpInformationFile. |
| [IDebugSymbols3::GetSourcePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcepathwide.md) | The GetSourcePathWide method returns the source path. |
| [IDebugSymbols3::GetModuleVersionInformationWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmoduleversioninformationwide.md) | The GetModuleVersionInformationWide method returns version information for the specified module. |
| [IDebugBreakpoint2::GetMatchThreadId method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getmatchthreadid.md) | The GetMatchThreadId method returns the engine thread ID of the thread that can trigger a breakpoint. |
| [IDebugDataSpaces4::GetVirtualTranslationPhysicalOffsets method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getvirtualtranslationphysicaloffsets.md) | The GetVirtualTranslationPhysicalOffsets method returns the physical addresses of the system paging structures at different levels of the paging hierarchy. |
| [IDebugBreakpoint2::GetDataParameters method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getdataparameters.md) | The GetDataParameters method returns the parameters for a processor breakpoint. |
| [IDebugSymbols3::GetNextSymbolMatchWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnextsymbolmatchwide.md) | The GetNextSymbolMatchWide method returns the next symbol found in a symbol search. |
| [IDebugSymbols3::SetScopeFromStoredEvent method](..\dbgeng\nf-dbgeng-idebugsymbols3-setscopefromstoredevent.md) | The SetScopeFromStoredEvent method sets the current scope to the scope of the stored event. |
| [IDebugSymbols3::GetModuleParameters method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmoduleparameters.md) | The GetModuleParameters method returns parameters for modules in the target. |
| [IDebugSystemObjects4::SetCurrentSystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setcurrentsystemid.md) | The SetCurrentSystemId method makes the specified target the current target. |
| [IDebugControl4::GetProcessorTypeNamesWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getprocessortypenameswide.md) | The GetProcessorTypeNamesWide method returns the full name and abbreviated name of the specified processor type. |
| [IDebugControl3::OutputPromptVaList method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputpromptvalist.md) | The OutputPromptVaList method formats and sends a user prompt to the output callback objects. |
| [IDebugEventCallbacksWide::UnloadModule method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-unloadmodule.md) | The UnloadModule callback method is called by the engine when a module-unload debugging event occurs in the target. |
| [IDebugControl3::GetEffectiveProcessorType method](..\dbgeng\nf-dbgeng-idebugcontrol3-geteffectiveprocessortype.md) | The GetEffectiveProcessorType method returns the effective processor type of the processor of the computer that is running the target. |
| [IDebugControl3::RemoveBreakpoint method](..\dbgeng\nf-dbgeng-idebugcontrol3-removebreakpoint.md) | The RemoveBreakpoint method removes a breakpoint. |
| [IDebugSystemObjects4::GetThreadIdsByIndex method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidsbyindex.md) | The GetThreadIdsByIndex method returns the engine and system thread IDs for the specified threads in the current process. |
| [IDebugSymbols3::GetModuleByModuleName2 method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebymodulename2.md) | The GetModuleByModuleName2 method searches through the process's modules for one with the specified name. |
| [IDebugControl3::GetEngineOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-getengineoptions.md) | The GetEngineOptions method returns the engine's options. |
| [IDebugClient5::SetQuitLockString method](..\dbgeng\nf-dbgeng-idebugclient5-setquitlockstring.md) | Sets a quit lock string. |
| [IDebugSymbolGroup2::RemoveSymbolByNameWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-removesymbolbynamewide.md) | The RemoveSymbolByNameWide method removes the specified symbol from a symbol group. |
| [IDebugSystemObjects4::GetNumberSystems method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getnumbersystems.md) | The GetNumberSystems method returns the number of targets to which the engine is currently connected. |
| [IDebugSymbols3::GetTypeNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypenamewide.md) | The GetTypeNameWide method returns the name of the type symbol specified by its type ID and module. |
| [IDebugClient5::OutputIdentityWide method](..\dbgeng\nf-dbgeng-idebugclient5-outputidentitywide.md) | The OutputIdentityWide method formats and outputs a string describing the computer and user this client represents. |
| [IDebugSymbols4::GetLineByInlineContext method](..\dbgeng\nf-dbgeng-idebugsymbols4-getlinebyinlinecontext.md) | Gets a line by inline context. |
| [IDebugClient5::OpenDumpFile method](..\dbgeng\nf-dbgeng-idebugclient5-opendumpfile.md) | The OpenDumpFile method opens a dump file as a debugger target. |
| [IDebugSymbols3::GetOffsetTypeId method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsettypeid.md) | The GetOffsetTypeId method returns the type ID of the symbol closest to the specified memory location. |
| [IDebugSymbols3::GetSymbolEntryInformation method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentryinformation.md) | The GetSymbolEntryInformation method returns the symbol entry information for a symbol. |
| [IDebugSystemObjects4::GetCurrentSystemServerNameWide method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentsystemservernamewide.md) | Gets the server name for the current process. |
| [IDebugControl4::CallExtensionWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-callextensionwide.md) | The CallExtensionWide method calls a debugger extension. |
| [IDebugClient5::GetQuitLockString method](..\dbgeng\nf-dbgeng-idebugclient5-getquitlockstring.md) | Gets a quit lock string. |
| [IDebugSymbols3::GetModuleVersionInformation method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmoduleversioninformation.md) | The GetModuleVersionInformation method returns version information for the specified module. |
| [IDebugSystemObjects3::GetCurrentSystemServerName method](..\dbgeng\nf-dbgeng-idebugsystemobjects3-getcurrentsystemservername.md) | Gets the server name for the current process. |
| [IDebugControl4::OutputPromptWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputpromptwide.md) | The OutputPromptWide method formats and sends a user prompt to the output callback objects. |
| [IDebugSymbols3::AppendImagePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendimagepath.md) | The AppendImagePath method appends directories to the executable image path. |
| [IDebugDataSpaces4::WriteIo method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writeio.md) | The WriteIo method writes to the system and bus I/O memory. |
| [IDebugClient5::GetOutputMask method](..\dbgeng\nf-dbgeng-idebugclient5-getoutputmask.md) | The GetOutputMask method returns the output mask currently set for the client. |
| [IDebugSymbols3::GetNameByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnamebyoffset.md) | The GetNameByOffset method returns the name of the symbol at the specified location in the target's virtual address space. |
| [IDebugPlmClient3::LaunchAndDebugPlmAppWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-launchanddebugplmappwide.md) | Launches and attaches to a Process Lifecycle Management (PLM) application. |
| [IDebugSystemObjects3::GetSystemByServer method](..\dbgeng\nf-dbgeng-idebugsystemobjects3-getsystembyserver.md) | Gets the system for a server. |
| [IDebugControl3::GetSupportedProcessorTypes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getsupportedprocessortypes.md) | The GetSupportedProcessorTypes method returns the processor types supported by the debugger engine. |
| [IDebugSystemObjects4::GetCurrentProcessHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocesshandle.md) | The GetCurrentProcessHandle method returns the system handle for the current process. |
| [IDebugControl4::GetExtensionByPathWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getextensionbypathwide.md) | The GetExtensionByPathWide method returns the handle for an already loaded extension library. |
| [IDebugClient5::StartProcessServer method](..\dbgeng\nf-dbgeng-idebugclient5-startprocessserver.md) | The StartProcessServer method starts a process server. |
| [IDebugControl3::GetNumberProcessors method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberprocessors.md) | The GetNumberProcessors method returns the number of processors on the computer running the current target. |
| [IDebugRegisters2::GetValues2 method](..\dbgeng\nf-dbgeng-idebugregisters2-getvalues2.md) | The GetValues2 method fetches the value of several of the target's registers. |
| [IDebugSystemObjects4::GetCurrentThreadId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreadid.md) | The GetCurrentThreadId method returns the engine thread ID for the current thread. |
| [IDebugControl3::GetDisassembleEffectiveOffset method](..\dbgeng\nf-dbgeng-idebugcontrol3-getdisassembleeffectiveoffset.md) | The GetDisassembleEffectiveOffset method returns the address of the last instruction disassembled using Disassemble. |
| [IDebugRegisters2::SetValue method](..\dbgeng\nf-dbgeng-idebugregisters2-setvalue.md) | The SetValue method sets the value of one of the target's registers. |
| [IDebugSymbols3::AddTypeOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-addtypeoptions.md) | The AddTypeOptions method turns on some type formatting options for output generated by the engine. |
| [IDebugDataSpaces4::ReadControl method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readcontrol.md) | The ReadControl method reads implementation-specific system data. |
| [IDebugControl3::SetCodeLevel method](..\dbgeng\nf-dbgeng-idebugcontrol3-setcodelevel.md) | The SetCodeLevel method sets the current code level and is mainly used when stepping through code. |
| [IDebugClient5::CreateProcessAndAttachWide method](..\dbgeng\nf-dbgeng-idebugclient5-createprocessandattachwide.md) | The CreateProcessAndAttachWide method creates a process from a specified command line, then attach to another user-mode process. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [DEBUG_SYMBOL_ENTRY structure](..\dbgeng\ns-dbgeng--debug-symbol-entry.md) | The DEBUG_SYMBOL_ENTRY structure describes a symbol in a symbol group. |
| [DEBUG_VALUE structure](..\dbgeng\ns-dbgeng--debug-value.md) | The DEBUG_VALUE structure holds register and expression values. |
| [DEBUG_LAST_EVENT_INFO_LOAD_MODULE structure](..\dbgeng\ns-dbgeng--debug-last-event-info-load-module.md) | Describes the load module of the last event. |
| [DEBUG_READ_USER_MINIDUMP_STREAM structure](..\dbgeng\ns-dbgeng--debug-read-user-minidump-stream.md) | Describes a user minidump to read. |
| [DEBUG_CREATE_PROCESS_OPTIONS structure](..\dbgeng\ns-dbgeng--debug-create-process-options.md) | The DEBUG_CREATE_PROCESS_OPTIONS structure specifies the process creation options to use when creating a new process. |
| [INLINE_FRAME_CONTEXT structure](..\dbgeng\ns-dbgeng--inline-frame-context.md) | Describes inline frame context. |
| [DEBUG_SPECIFIC_FILTER_PARAMETERS structure](..\dbgeng\ns-dbgeng--debug-specific-filter-parameters.md) | The DEBUG_SPECIFIC_FILTER_PARAMETERS structure contains the parameters for a specific event filter. |
| [DEBUG_PROCESSOR_IDENTIFICATION_ALPHA structure](..\dbgeng\ns-dbgeng--debug-processor-identification-alpha.md) | Identifies an Alpha processor. |
| [STACK_SYM_FRAME_INFO structure](..\dbgeng\ns-dbgeng--stack-sym-frame-info.md) | Defines stack source information for an extended stack frame. |
| [DEBUG_GET_TEXT_COMPLETIONS_OUT structure](..\dbgeng\ns-dbgeng--debug-get-text-completions-out.md) | Defines information about text completions to get. |
| [DEBUG_CACHED_SYMBOL_INFO structure](..\dbgeng\ns-dbgeng--debug-cached-symbol-info.md) | Defines information about cached symbols. |
| [DEBUG_PROCESSOR_IDENTIFICATION_ALL structure](..\dbgeng\ns-dbgeng--debug-processor-identification-all.md) | This union contains relevant information for a processor the supported processors. |
| [DEBUG_LAST_EVENT_INFO_EXIT_THREAD structure](..\dbgeng\ns-dbgeng--debug-last-event-info-exit-thread.md) | Describes the exit thread of the last event. |
| [DEBUG_THREAD_BASIC_INFORMATION structure](..\dbgeng\ns-dbgeng--debug-thread-basic-information.md) | The DEBUG_THREAD_BASIC_INFORMATION structure describes an operating system thread. |
| [DEBUG_PROCESSOR_IDENTIFICATION_ARM64 structure](..\dbgeng\ns-dbgeng--debug-processor-identification-arm64.md) | Identifies an ARM64 processor. |
| [DEBUG_OFFSET_REGION structure](..\dbgeng\ns-dbgeng--debug-offset-region.md) | Defines a debug offset region. |
| [DEBUG_LAST_EVENT_INFO_SYSTEM_ERROR structure](..\dbgeng\ns-dbgeng--debug-last-event-info-system-error.md) | Describes the system error of the last event. |
| [DEBUG_SYMBOL_PARAMETERS structure](..\dbgeng\ns-dbgeng--debug-symbol-parameters.md) | The DEBUG_SYMBOL_PARAMETERS structure describes a symbol in a symbol group. |
| [DEBUG_PROCESSOR_IDENTIFICATION_AMD64 structure](..\dbgeng\ns-dbgeng--debug-processor-identification-amd64.md) | Identifies an AMD64 processor. |
| [DEBUG_BREAKPOINT_PARAMETERS structure](..\dbgeng\ns-dbgeng--debug-breakpoint-parameters.md) | The DEBUG_BREAKPOINT_PARAMETERS structure contains most of the parameters for describing a breakpoint. |
| [DEBUG_CLIENT_CONTEXT structure](..\dbgeng\ns-dbgeng--debug-client-context.md) | Contains a debug client constant to provide to the IDebugClient7 |
| [DEBUG_GET_TEXT_COMPLETIONS_IN structure](..\dbgeng\ns-dbgeng--debug-get-text-completions-in.md) | Defines information about text completions to get. |
| [STACK_SRC_INFO structure](..\dbgeng\ns-dbgeng--stack-src-info.md) | Defines stack source information. |
| [DEBUG_MODULE_AND_ID structure](..\dbgeng\ns-dbgeng--debug-module-and-id.md) | The DEBUG_MODULE_AND_ID structure describes a symbol within a module. |
| [DEBUG_MODULE_PARAMETERS structure](..\dbgeng\ns-dbgeng--debug-module-parameters.md) | The DEBUG_MODULE_PARAMETERS structure contains most of the parameters for describing a module. |
| [DEBUG_STACK_FRAME_EX structure](..\dbgeng\ns-dbgeng--debug-stack-frame-ex.md) | The DEBUG_STACK_FRAME_EX structure describes a stack frame and the address of the current instruction for the stack frame. |
| [DEBUG_SYMBOL_SOURCE_ENTRY structure](..\dbgeng\ns-dbgeng--debug-symbol-source-entry.md) | The DEBUG_SYMBOL_SOURCE_ENTRY structure describes a section of the source code and a corresponding region of the target's memory. |
| [DEBUG_HANDLE_DATA_BASIC structure](..\dbgeng\ns-dbgeng--debug-handle-data-basic.md) | The DEBUG_HANDLE_DATA_BASIC structure contains handle-related information about a system object. |
| [DEBUG_LAST_EVENT_INFO_EXIT_PROCESS structure](..\dbgeng\ns-dbgeng--debug-last-event-info-exit-process.md) | Describes the exit process of the last event. |
| [DEBUG_STACK_FRAME structure](..\dbgeng\ns-dbgeng--debug-stack-frame.md) | The DEBUG_STACK_FRAME structure describes a stack frame and the address of the current instruction for the stack frame. |
| [SYMBOL_INFO_EX structure](..\dbgeng\ns-dbgeng--symbol-info-ex.md) | The SYMBOL_INFO_EX structure describes the extended line symbol information. |
| [DEBUG_EXCEPTION_FILTER_PARAMETERS structure](..\dbgeng\ns-dbgeng--debug-exception-filter-parameters.md) | The DEBUG_EXCEPTION_FILTER_PARAMETERS structure contains the parameters for an exception filter. |
| [DEBUG_LAST_EVENT_INFO_EXCEPTION structure](..\dbgeng\ns-dbgeng--debug-last-event-info-exception.md) | Describes the exception of the last event. |
| [DEBUG_EVENT_CONTEXT structure](..\dbgeng\ns-dbgeng--debug-event-context.md) | Defines context information about an event. |
| [DEBUG_PROCESSOR_IDENTIFICATION_ARM structure](..\dbgeng\ns-dbgeng--debug-processor-identification-arm.md) | Identifies an ARM processor. |
| [DEBUG_REGISTER_DESCRIPTION structure](..\dbgeng\ns-dbgeng--debug-register-description.md) | The DEBUG_REGISTER_DESCRIPTION structure is returned by GetDescription to describe a processor's register. |
| [DEBUG_LAST_EVENT_INFO_BREAKPOINT structure](..\dbgeng\ns-dbgeng--debug-last-event-info-breakpoint.md) | Describes the breakpoint of the last event. |
| [DEBUG_LAST_EVENT_INFO_UNLOAD_MODULE structure](..\dbgeng\ns-dbgeng--debug-last-event-info-unload-module.md) | Describes the unload module of the last event. |
| [DEBUG_PROCESSOR_IDENTIFICATION_X86 structure](..\dbgeng\ns-dbgeng--debug-processor-identification-x86.md) | Identifies an x86 processor. |
| [DEBUG_PROCESSOR_IDENTIFICATION_IA64 structure](..\dbgeng\ns-dbgeng--debug-processor-identification-ia64.md) | Identifies an Intel Itanium architecture (IA64) processor. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IDebugInputCallbacks interface](..\dbgeng\nn-dbgeng-idebuginputcallbacks.md) | IDebugInputCallbacks interface |
| [IDebugEventContextCallbacks interface](..\dbgeng\nn-dbgeng-idebugeventcontextcallbacks.md) | This interface supports event context callbacks and replaces the use of the IDebugClient |
| [IDebugClient4 interface](..\dbgeng\nn-dbgeng-idebugclient4.md) | IDebugClient4 interface |
| [IDebugControl7 interface](..\dbgeng\nn-dbgeng-idebugcontrol7.md) | . |
| [IDebugDataSpaces3 interface](..\dbgeng\nn-dbgeng-idebugdataspaces3.md) | IDebugDataSpaces3 interface |
| [DebugBaseEventCallbacksWide interface](..\dbgeng\nl-dbgeng-debugbaseeventcallbackswide.md) | The DebugBaseEventCallbacksWide class provides a base implementation of the IDebugEventCallbacksWide interface. |
| [IDebugSymbols2 interface](..\dbgeng\nn-dbgeng-idebugsymbols2.md) | IDebugSymbols2 interface |
| [IDebugClient2 interface](..\dbgeng\nn-dbgeng-idebugclient2.md) | IDebugClient2 interface |
| [IDebugDataSpaces2 interface](..\dbgeng\nn-dbgeng-idebugdataspaces2.md) | IDebugDataSpaces2 interface |
| [IDebugSymbols5 interface](..\dbgeng\nn-dbgeng-idebugsymbols5.md) | This interface supports using index values for the current frame. |
| [IDebugSystemObjects4 interface](..\dbgeng\nn-dbgeng-idebugsystemobjects4.md) | IDebugSystemObjects4 interface |
| [IDebugControl5 interface](..\dbgeng\nn-dbgeng-idebugcontrol5.md) | . |
| [IDebugOutputCallbacksWide interface](..\dbgeng\nn-dbgeng-idebugoutputcallbackswide.md) | IDebugOutputCallbacksWide interface |
| [IDebugDataSpaces interface](..\dbgeng\nn-dbgeng-idebugdataspaces.md) | IDebugDataSpaces interface |
| [IDebugBreakpoint2 interface](..\dbgeng\nn-dbgeng-idebugbreakpoint2.md) | IDebugBreakpoint2 interface |
| [IDebugAdvanced2 interface](..\dbgeng\nn-dbgeng-idebugadvanced2.md) | IDebugAdvanced2 interface |
| [IDebugPlmClient2 interface](..\dbgeng\nn-dbgeng-idebugplmclient2.md) | This interface supports Process Lifecycle Management (PLM) for the debug client. |
| [IDebugRegisters2 interface](..\dbgeng\nn-dbgeng-idebugregisters2.md) | IDebugRegisters2 interface |
| [IDebugAdvanced3 interface](..\dbgeng\nn-dbgeng-idebugadvanced3.md) | IDebugAdvanced3 interface |
| [IDebugBreakpoint3 interface](..\dbgeng\nn-dbgeng-idebugbreakpoint3.md) | . |
| [IDebugOutputCallbacks interface](..\dbgeng\nn-dbgeng-idebugoutputcallbacks.md) | IDebugOutputCallbacks interface |
| [IDebugSymbols3 interface](..\dbgeng\nn-dbgeng-idebugsymbols3.md) | IDebugSymbols3 interface |
| [IDebugSymbols4 interface](..\dbgeng\nn-dbgeng-idebugsymbols4.md) | This interface supports determination of the symbol of an inline frame. |
| [IDebugPlmClient3 interface](..\dbgeng\nn-dbgeng-idebugplmclient3.md) | This interface supports Process Lifecycle Management (PLM) for the debug client. |
| [IDebugControl4 interface](..\dbgeng\nn-dbgeng-idebugcontrol4.md) | IDebugControl4 interface |
| [IDebugOutputStream interface](..\dbgeng\nn-dbgeng-idebugoutputstream.md) | Supports the debug output stream. |
| [IDebugSystemObjects3 interface](..\dbgeng\nn-dbgeng-idebugsystemobjects3.md) | IDebugSystemObjects3 interface |
| [IDebugPlmClient interface](..\dbgeng\nn-dbgeng-idebugplmclient.md) | This interface supports Process Lifecycle Management (PLM) for the debug client. |
| [IDebugSymbolGroup2 interface](..\dbgeng\nn-dbgeng-idebugsymbolgroup2.md) | IDebugSymbolGroup2 interface |
| [IDebugClient interface](..\dbgeng\nn-dbgeng-idebugclient.md) | IDebugClient interface |
| [IDebugEventCallbacksWide interface](..\dbgeng\nn-dbgeng-idebugeventcallbackswide.md) | IDebugEventCallbacksWide interface |
| [IDebugSystemObjects2 interface](..\dbgeng\nn-dbgeng-idebugsystemobjects2.md) | IDebugSystemObjects2 interface |
| [IDebugDataSpaces4 interface](..\dbgeng\nn-dbgeng-idebugdataspaces4.md) | IDebugDataSpaces4 interface |
| [IDebugClient3 interface](..\dbgeng\nn-dbgeng-idebugclient3.md) | IDebugClient3 interface |
| [DebugBaseEventCallbacks interface](..\dbgeng\nl-dbgeng-debugbaseeventcallbacks.md) | The DebugBaseEventCallbacks class provides a base implementation of the IDebugEventCallbacks interface. |
| [IDebugControl3 interface](..\dbgeng\nn-dbgeng-idebugcontrol3.md) | IDebugControl3 interface |
| [IDebugClient6 interface](..\dbgeng\nn-dbgeng-idebugclient6.md) | This interface supports event context callbacks. |
| [IDebugControl2 interface](..\dbgeng\nn-dbgeng-idebugcontrol2.md) | IDebugControl2 interface |
| [IDebugEventCallbacks interface](..\dbgeng\nn-dbgeng-idebugeventcallbacks.md) | IDebugEventCallbacks interface |
| [IDebugControl6 interface](..\dbgeng\nn-dbgeng-idebugcontrol6.md) | . |
| [IDebugOutputCallbacks2 interface](..\dbgeng\nn-dbgeng-idebugoutputcallbacks2.md) | The IDebugOutputCallbacks2 interface allows clients to receive full debugger markup language (DML) content for presentation. |
| [IDebugSymbols interface](..\dbgeng\nn-dbgeng-idebugsymbols.md) | IDebugSymbols interface |
| [IDebugRegisters interface](..\dbgeng\nn-dbgeng-idebugregisters.md) | IDebugRegisters interface |
| [IDebugSystemObjects interface](..\dbgeng\nn-dbgeng-idebugsystemobjects.md) | IDebugSystemObjects interface |
| [IDebugSymbolGroup interface](..\dbgeng\nn-dbgeng-idebugsymbolgroup.md) | IDebugSymbolGroup interface |
| [IDebugClient5 interface](..\dbgeng\nn-dbgeng-idebugclient5.md) | IDebugClient5 interface |
| [IDebugControl interface](..\dbgeng\nn-dbgeng-idebugcontrol.md) | IDebugControl interface |
| [IDebugAdvanced interface](..\dbgeng\nn-dbgeng-idebugadvanced.md) | IDebugAdvanced interface |
| [IDebugAdvanced4 interface](..\dbgeng\nn-dbgeng-idebugadvanced4.md) | IDebugAdvanced4 interface |
| [IDebugClient7 interface](..\dbgeng\nn-dbgeng-idebugclient7.md) | The IDebugClient7 interface is reserved for internal use. |
| [IDebugBreakpoint interface](..\dbgeng\nn-dbgeng-idebugbreakpoint.md) | IDebugBreakpoint interface |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PDEBUG_EXTENSION_CALL callback](..\dbgeng\nc-dbgeng-pdebug-extension-call.md) | Callback functions of the type PDEBUG_EXTENSION_CALL are called by the engine to execute extension commands. You can give these functions any name you want, as long as it contains no uppercase letters. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [ExtRemoteData::Set method](..\engextcpp\nf-engextcpp-extremotedata-set~r1.md) | The Set method sets the region of the target's memory represented by the ExtRemoteData object. |
| [ExtRemoteTyped::Dereference method](..\engextcpp\nf-engextcpp-extremotetyped-dereference.md) | The Dereference method returns the typed data that is pointed to by the typed data represented by this object. |
| [ExtRemoteList::StartTail method](..\engextcpp\nf-engextcpp-extremotelist-starttail.md) | The StartTail method initializes the list for iterating backward, starting at the head. |
| [ExtRemoteData::WriteBuffer method](..\engextcpp\nf-engextcpp-extremotedata-writebuffer.md) | The WriteBuffer method writes data to the target's memory. The data is located in the beginning of the region represented by the ExtRemoteData object. However, the size of the data can be different. |
| [ExtRemoteData::ExtRemoteData method](..\engextcpp\nf-engextcpp-extremotedata-extremotedata~r1.md) | The ExtRemoteData constructor creates a new instance of the ExtRemoteData class. |
| [ExtRemoteTyped::GetTypeSize method](..\engextcpp\nf-engextcpp-extremotetyped-gettypesize.md) | The GetTypeSize method returns the size of the type represented by this object. |
| [ExtRemoteTypedList::SetTypeAndLink method](..\engextcpp\nf-engextcpp-extremotetypedlist-settypeandlink.md) | The SetTypeAndLink method sets the type information for the typed list. |
| [ExtRemoteTyped::OutSimpleValue method](..\engextcpp\nf-engextcpp-extremotetyped-outsimplevalue.md) | The OutSimpleValue method prints the value of the typed data represented by this object. |
| [ExtRemoteData::ExtRemoteData method](..\engextcpp\nf-engextcpp-extremotedata-extremotedata.md) | The ExtRemoteData constructor creates a new instance of the ExtRemoteData class. |
| [ExtRemoteData::Read method](..\engextcpp\nf-engextcpp-extremotedata-read.md) | The Read method reads the contents of the target's memory, represented by the ExtRemoteData object, and then caches the data. |
| [ExtRemoteData::GetChar method](..\engextcpp\nf-engextcpp-extremotedata-getchar.md) | The GetChar method returns a CHAR version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::Field method](..\engextcpp\nf-engextcpp-extremotetyped-field.md) | The Field method returns the typed data for a member in the typed data that is represented by this object. |
| [ExtRemoteData::GetStdBool method](..\engextcpp\nf-engextcpp-extremotedata-getstdbool.md) | The GetStdBool method returns a bool version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [EXT_COMMAND_METHOD function](..\engextcpp\nf-engextcpp-ext-command-method.md) | The EXT_COMMAND_METHOD macro declares an extension command from inside the definition of the EXT_CLASS class. |
| [ExtRemoteList::GetNodeOffset method](..\engextcpp\nf-engextcpp-extremotelist-getnodeoffset.md) | The GetNodeOffset method returns the address of the current list item. |
| [ExtRemoteData::GetString method](..\engextcpp\nf-engextcpp-extremotedata-getstring~r2.md) | The GetString method reads a null-terminated string from the target's memory. The string is located in the beginning of the region represented by the ExtRemoteData object. |
| [ExtRemoteList::StartHead method](..\engextcpp\nf-engextcpp-extremotelist-starthead.md) | The StartHead method initializes the list for iterating forward starting at the head. |
| [ExtRemoteList::Next method](..\engextcpp\nf-engextcpp-extremotelist-next.md) | The Next method changes the current item to the next item in the list. |
| [ExtRemoteTyped::GetTypeName method](..\engextcpp\nf-engextcpp-extremotetyped-gettypename.md) | The GetTypeName method returns the type name of the typed data represented by this object. |
| [ExtRemoteTyped::HasField method](..\engextcpp\nf-engextcpp-extremotetyped-hasfield.md) | The HasField method determines if the type of the data represented by this object contains the specified member. |
| [ExtRemoteTyped::SetPrint method](..\engextcpp\nf-engextcpp-extremotetyped-setprint.md) | The SetPrint method sets the typed data represented by the ExtRemoteTyped object by formatting an expression and then evaluating that expression. |
| [ExtRemoteData::GetUshort method](..\engextcpp\nf-engextcpp-extremotedata-getushort.md) | The GetUshort method returns a USHORT version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteData::Set method](..\engextcpp\nf-engextcpp-extremotedata-set.md) | The Set method sets the region of the target's memory represented by the ExtRemoteData object. |
| [ExtRemoteData::GetShort method](..\engextcpp\nf-engextcpp-extremotedata-getshort.md) | The GetShort method returns a SHORT version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::GetFieldOffset method](..\engextcpp\nf-engextcpp-extremotetyped-getfieldoffset.md) | The GetFieldOffset method returns the offset of a member from the base address of an instance of the type that is represented by this object. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r4.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::GetString method](..\engextcpp\nf-engextcpp-extremotedata-getstring.md) | The GetString method reads a null-terminated string from the target's memory. The string is located in the beginning of the region represented by the ExtRemoteData object. |
| [ExtRemoteData::GetDouble method](..\engextcpp\nf-engextcpp-extremotedata-getdouble.md) | The GetDouble method returns a double version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r1.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::ExtRemoteData method](..\engextcpp\nf-engextcpp-extremotedata-extremotedata~r2.md) | The ExtRemoteData constructor creates a new instance of the ExtRemoteData class. |
| [ExtRemoteData::GetLong method](..\engextcpp\nf-engextcpp-extremotedata-getlong.md) | The GetLong method returns a LONG version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [EXT_COMMAND function](..\engextcpp\nf-engextcpp-ext-command.md) | The EXT_COMMAND macro is used to define an extension command that was declared by using the EXT_COMMAND_METHOD macro.An extension command is defined as follows |
| [ExtRemoteTyped::GetTypeFieldOffset method](..\engextcpp\nf-engextcpp-extremotetyped-gettypefieldoffset.md) | The GetTypeFieldOffset static method returns the offset of a member within a structure. |
| [ExtRemoteTyped::GetPointerTo method](..\engextcpp\nf-engextcpp-extremotetyped-getpointerto.md) | The GetPointerTo method returns typed data that is a pointer to the typed data represented by this object. |
| [ExtRemoteTyped::OutTypeName method](..\engextcpp\nf-engextcpp-extremotetyped-outtypename.md) | The OutTypeName method prints the type name of the typed data represented by this object. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r5.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::GetFloat method](..\engextcpp\nf-engextcpp-extremotedata-getfloat.md) | The GetFloat method returns a float version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteData::GetUlong64 method](..\engextcpp\nf-engextcpp-extremotedata-getulong64.md) | The GetUlong64 method returns a ULONG64 version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::GetPtr method](..\engextcpp\nf-engextcpp-extremotedata-getptr.md) | The GetPtr method returns a pointer from the target's memory version of the ExtRemoteData object, which represents the contents of the target's memory. The size of the unsigned integer from the target is the same size as a pointer on the target. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r3.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::GetLongPtr method](..\engextcpp\nf-engextcpp-extremotedata-getlongptr.md) | The GetLongPtr method returns a signed integer version (extended to LONG64) of the ExtRemoteData object, which represents the contents of the target's memory. The size of the unsigned integer from the target is the same size as a pointer on the target. |
| [ExtRemoteData::GetBoolean method](..\engextcpp\nf-engextcpp-extremotedata-getboolean.md) | The GetBoolean method returns a Boolean version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteList::HasNode method](..\engextcpp\nf-engextcpp-extremotelist-hasnode.md) | The HasNode method determines if there is a current item in the list iteration. |
| [ExtRemoteData::GetString method](..\engextcpp\nf-engextcpp-extremotedata-getstring~r1.md) | The GetString method reads a null-terminated string from the target's memory. The string is located in the beginning of the region represented by the ExtRemoteData object. |
| [ExtRemoteData::GetLong64 method](..\engextcpp\nf-engextcpp-extremotedata-getlong64.md) | The GetLong64 method returns a LONG64 version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteData::GetString method](..\engextcpp\nf-engextcpp-extremotedata-getstring~r3.md) | The GetString method reads a null-terminated string from the target's memory. The string is located in the beginning of the region represented by the ExtRemoteData object. |
| [ExtRemoteData::ReadBuffer method](..\engextcpp\nf-engextcpp-extremotedata-readbuffer.md) | The ReadBuffer method reads data from the target's memory. The data is located in the beginning of the region represented by the ExtRemoteData object. However, the size of the data can be different. |
| [ExtRemoteData::GetUchar method](..\engextcpp\nf-engextcpp-extremotedata-getuchar.md) | The GetUChar method returns a UCHAR version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteData::GetUlongPtr method](..\engextcpp\nf-engextcpp-extremotedata-getulongptr.md) | The GetUlongPtr method returns an unsigned integer version (extended to ULONG64) of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::OutFullValue method](..\engextcpp\nf-engextcpp-extremotetyped-outfullvalue.md) | The OutFullValue method prints the type and value of the typed data represented by this object. |
| [ExtRemoteData::Write method](..\engextcpp\nf-engextcpp-extremotedata-write.md) | The Write method writes the data cached by the ExtRemoteData object to the region of memory on the target, represented by this object. |
| [ExtRemoteTyped::ArrayElement method](..\engextcpp\nf-engextcpp-extremotetyped-arrayelement.md) | The ArrayElement method returns the typed data in the specified array element of the typed data represented by the ExtRemoteTyped object. |
| [ExtRemoteList::Prev method](..\engextcpp\nf-engextcpp-extremotelist-prev.md) | The Prev method changes the current item to the previous item in the list. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r2.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteTyped::operator* method](..\engextcpp\nf-engextcpp-extremotetyped-operator.md) | The operator* overloaded operator returns the typed data that is pointed to by the typed data represented by this object. |
| [ExtRemoteTypedList::GetTypedNodePtr method](..\engextcpp\nf-engextcpp-extremotetypedlist-gettypednodeptr.md) | The GetTypedNodePtr method returns a pointer to the current list item. |
| [ExtRemoteTyped::Release method](..\engextcpp\nf-engextcpp-extremotetyped-release.md) | The Release method releases any resources held by this object. |
| [ExtRemoteData::GetW32Bool method](..\engextcpp\nf-engextcpp-extremotedata-getw32bool.md) | The GetW32Bool method returns a BOOL version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::Eval method](..\engextcpp\nf-engextcpp-extremotetyped-eval.md) | The Eval method returns typed data that is the result of evaluating an expression. |
| [ExtRemoteData::GetData method](..\engextcpp\nf-engextcpp-extremotedata-getdata.md) | The GetData method returns the contents of the target's memory, represented by the ExtRemoteData object. |
| [ExtRemoteTyped::OutTypeDefinition method](..\engextcpp\nf-engextcpp-extremotetyped-outtypedefinition.md) | The OutTypeDefinition method prints the type of the typed data represented by this object. |
| [ExtRemoteData::GetUlong method](..\engextcpp\nf-engextcpp-extremotedata-getulong.md) | The GetUlong method returns a ULONG version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTypedList::GetTypedNode method](..\engextcpp\nf-engextcpp-extremotetypedlist-gettypednode.md) | The GetTypedNode method returns the current list item. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [ExtRemoteList interface](..\engextcpp\nl-engextcpp-extremotelist.md) | The ExtRemoteList class provides a wrapper around a singly-linked or doubly-linked list. The class contains methods that can be used to move both forward and backward through the list. |
| [ExtRemoteData interface](..\engextcpp\nl-engextcpp-extremotedata.md) | The ExtRemoteData class provides a wrapper around a small section of a target's memory. ExtRemoteData automatically retrieves the memory and provides a number of convenience methods. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [ExtRemoteData::Set method](..\engextcpp\nf-engextcpp-extremotedata-set~r1.md) | The Set method sets the region of the target's memory represented by the ExtRemoteData object. |
| [ExtRemoteTyped::Dereference method](..\engextcpp\nf-engextcpp-extremotetyped-dereference.md) | The Dereference method returns the typed data that is pointed to by the typed data represented by this object. |
| [ExtRemoteList::StartTail method](..\engextcpp\nf-engextcpp-extremotelist-starttail.md) | The StartTail method initializes the list for iterating backward, starting at the head. |
| [ExtRemoteData::WriteBuffer method](..\engextcpp\nf-engextcpp-extremotedata-writebuffer.md) | The WriteBuffer method writes data to the target's memory. The data is located in the beginning of the region represented by the ExtRemoteData object. However, the size of the data can be different. |
| [ExtRemoteData::ExtRemoteData method](..\engextcpp\nf-engextcpp-extremotedata-extremotedata~r1.md) | The ExtRemoteData constructor creates a new instance of the ExtRemoteData class. |
| [ExtRemoteTyped::GetTypeSize method](..\engextcpp\nf-engextcpp-extremotetyped-gettypesize.md) | The GetTypeSize method returns the size of the type represented by this object. |
| [ExtRemoteTypedList::SetTypeAndLink method](..\engextcpp\nf-engextcpp-extremotetypedlist-settypeandlink.md) | The SetTypeAndLink method sets the type information for the typed list. |
| [ExtRemoteTyped::OutSimpleValue method](..\engextcpp\nf-engextcpp-extremotetyped-outsimplevalue.md) | The OutSimpleValue method prints the value of the typed data represented by this object. |
| [ExtRemoteData::ExtRemoteData method](..\engextcpp\nf-engextcpp-extremotedata-extremotedata.md) | The ExtRemoteData constructor creates a new instance of the ExtRemoteData class. |
| [ExtRemoteData::Read method](..\engextcpp\nf-engextcpp-extremotedata-read.md) | The Read method reads the contents of the target's memory, represented by the ExtRemoteData object, and then caches the data. |
| [ExtRemoteData::GetChar method](..\engextcpp\nf-engextcpp-extremotedata-getchar.md) | The GetChar method returns a CHAR version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::Field method](..\engextcpp\nf-engextcpp-extremotetyped-field.md) | The Field method returns the typed data for a member in the typed data that is represented by this object. |
| [ExtRemoteData::GetStdBool method](..\engextcpp\nf-engextcpp-extremotedata-getstdbool.md) | The GetStdBool method returns a bool version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [EXT_COMMAND_METHOD function](..\engextcpp\nf-engextcpp-ext-command-method.md) | The EXT_COMMAND_METHOD macro declares an extension command from inside the definition of the EXT_CLASS class. |
| [ExtRemoteList::GetNodeOffset method](..\engextcpp\nf-engextcpp-extremotelist-getnodeoffset.md) | The GetNodeOffset method returns the address of the current list item. |
| [ExtRemoteData::GetString method](..\engextcpp\nf-engextcpp-extremotedata-getstring~r2.md) | The GetString method reads a null-terminated string from the target's memory. The string is located in the beginning of the region represented by the ExtRemoteData object. |
| [ExtRemoteList::StartHead method](..\engextcpp\nf-engextcpp-extremotelist-starthead.md) | The StartHead method initializes the list for iterating forward starting at the head. |
| [ExtRemoteList::Next method](..\engextcpp\nf-engextcpp-extremotelist-next.md) | The Next method changes the current item to the next item in the list. |
| [ExtRemoteTyped::GetTypeName method](..\engextcpp\nf-engextcpp-extremotetyped-gettypename.md) | The GetTypeName method returns the type name of the typed data represented by this object. |
| [ExtRemoteTyped::HasField method](..\engextcpp\nf-engextcpp-extremotetyped-hasfield.md) | The HasField method determines if the type of the data represented by this object contains the specified member. |
| [ExtRemoteTyped::SetPrint method](..\engextcpp\nf-engextcpp-extremotetyped-setprint.md) | The SetPrint method sets the typed data represented by the ExtRemoteTyped object by formatting an expression and then evaluating that expression. |
| [ExtRemoteData::GetUshort method](..\engextcpp\nf-engextcpp-extremotedata-getushort.md) | The GetUshort method returns a USHORT version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteData::Set method](..\engextcpp\nf-engextcpp-extremotedata-set.md) | The Set method sets the region of the target's memory represented by the ExtRemoteData object. |
| [ExtRemoteData::GetShort method](..\engextcpp\nf-engextcpp-extremotedata-getshort.md) | The GetShort method returns a SHORT version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::GetFieldOffset method](..\engextcpp\nf-engextcpp-extremotetyped-getfieldoffset.md) | The GetFieldOffset method returns the offset of a member from the base address of an instance of the type that is represented by this object. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r4.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::GetString method](..\engextcpp\nf-engextcpp-extremotedata-getstring.md) | The GetString method reads a null-terminated string from the target's memory. The string is located in the beginning of the region represented by the ExtRemoteData object. |
| [ExtRemoteData::GetDouble method](..\engextcpp\nf-engextcpp-extremotedata-getdouble.md) | The GetDouble method returns a double version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r1.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::ExtRemoteData method](..\engextcpp\nf-engextcpp-extremotedata-extremotedata~r2.md) | The ExtRemoteData constructor creates a new instance of the ExtRemoteData class. |
| [ExtRemoteData::GetLong method](..\engextcpp\nf-engextcpp-extremotedata-getlong.md) | The GetLong method returns a LONG version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [EXT_COMMAND function](..\engextcpp\nf-engextcpp-ext-command.md) | The EXT_COMMAND macro is used to define an extension command that was declared by using the EXT_COMMAND_METHOD macro.An extension command is defined as follows |
| [ExtRemoteTyped::GetTypeFieldOffset method](..\engextcpp\nf-engextcpp-extremotetyped-gettypefieldoffset.md) | The GetTypeFieldOffset static method returns the offset of a member within a structure. |
| [ExtRemoteTyped::GetPointerTo method](..\engextcpp\nf-engextcpp-extremotetyped-getpointerto.md) | The GetPointerTo method returns typed data that is a pointer to the typed data represented by this object. |
| [ExtRemoteTyped::OutTypeName method](..\engextcpp\nf-engextcpp-extremotetyped-outtypename.md) | The OutTypeName method prints the type name of the typed data represented by this object. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r5.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::GetFloat method](..\engextcpp\nf-engextcpp-extremotedata-getfloat.md) | The GetFloat method returns a float version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteData::GetUlong64 method](..\engextcpp\nf-engextcpp-extremotedata-getulong64.md) | The GetUlong64 method returns a ULONG64 version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::GetPtr method](..\engextcpp\nf-engextcpp-extremotedata-getptr.md) | The GetPtr method returns a pointer from the target's memory version of the ExtRemoteData object, which represents the contents of the target's memory. The size of the unsigned integer from the target is the same size as a pointer on the target. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r3.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteData::GetLongPtr method](..\engextcpp\nf-engextcpp-extremotedata-getlongptr.md) | The GetLongPtr method returns a signed integer version (extended to LONG64) of the ExtRemoteData object, which represents the contents of the target's memory. The size of the unsigned integer from the target is the same size as a pointer on the target. |
| [ExtRemoteData::GetBoolean method](..\engextcpp\nf-engextcpp-extremotedata-getboolean.md) | The GetBoolean method returns a Boolean version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteList::HasNode method](..\engextcpp\nf-engextcpp-extremotelist-hasnode.md) | The HasNode method determines if there is a current item in the list iteration. |
| [ExtRemoteData::GetString method](..\engextcpp\nf-engextcpp-extremotedata-getstring~r1.md) | The GetString method reads a null-terminated string from the target's memory. The string is located in the beginning of the region represented by the ExtRemoteData object. |
| [ExtRemoteData::GetLong64 method](..\engextcpp\nf-engextcpp-extremotedata-getlong64.md) | The GetLong64 method returns a LONG64 version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteData::GetString method](..\engextcpp\nf-engextcpp-extremotedata-getstring~r3.md) | The GetString method reads a null-terminated string from the target's memory. The string is located in the beginning of the region represented by the ExtRemoteData object. |
| [ExtRemoteData::ReadBuffer method](..\engextcpp\nf-engextcpp-extremotedata-readbuffer.md) | The ReadBuffer method reads data from the target's memory. The data is located in the beginning of the region represented by the ExtRemoteData object. However, the size of the data can be different. |
| [ExtRemoteData::GetUchar method](..\engextcpp\nf-engextcpp-extremotedata-getuchar.md) | The GetUChar method returns a UCHAR version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteData::GetUlongPtr method](..\engextcpp\nf-engextcpp-extremotedata-getulongptr.md) | The GetUlongPtr method returns an unsigned integer version (extended to ULONG64) of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::OutFullValue method](..\engextcpp\nf-engextcpp-extremotetyped-outfullvalue.md) | The OutFullValue method prints the type and value of the typed data represented by this object. |
| [ExtRemoteData::Write method](..\engextcpp\nf-engextcpp-extremotedata-write.md) | The Write method writes the data cached by the ExtRemoteData object to the region of memory on the target, represented by this object. |
| [ExtRemoteTyped::ArrayElement method](..\engextcpp\nf-engextcpp-extremotetyped-arrayelement.md) | The ArrayElement method returns the typed data in the specified array element of the typed data represented by the ExtRemoteTyped object. |
| [ExtRemoteList::Prev method](..\engextcpp\nf-engextcpp-extremotelist-prev.md) | The Prev method changes the current item to the previous item in the list. |
| [ExtRemoteTyped::ExtRemoteTyped method](..\engextcpp\nf-engextcpp-extremotetyped-extremotetyped~r2.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteTyped::operator* method](..\engextcpp\nf-engextcpp-extremotetyped-operator.md) | The operator* overloaded operator returns the typed data that is pointed to by the typed data represented by this object. |
| [ExtRemoteTypedList::GetTypedNodePtr method](..\engextcpp\nf-engextcpp-extremotetypedlist-gettypednodeptr.md) | The GetTypedNodePtr method returns a pointer to the current list item. |
| [ExtRemoteTyped::Release method](..\engextcpp\nf-engextcpp-extremotetyped-release.md) | The Release method releases any resources held by this object. |
| [ExtRemoteData::GetW32Bool method](..\engextcpp\nf-engextcpp-extremotedata-getw32bool.md) | The GetW32Bool method returns a BOOL version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTyped::Eval method](..\engextcpp\nf-engextcpp-extremotetyped-eval.md) | The Eval method returns typed data that is the result of evaluating an expression. |
| [ExtRemoteData::GetData method](..\engextcpp\nf-engextcpp-extremotedata-getdata.md) | The GetData method returns the contents of the target's memory, represented by the ExtRemoteData object. |
| [ExtRemoteTyped::OutTypeDefinition method](..\engextcpp\nf-engextcpp-extremotetyped-outtypedefinition.md) | The OutTypeDefinition method prints the type of the typed data represented by this object. |
| [ExtRemoteData::GetUlong method](..\engextcpp\nf-engextcpp-extremotedata-getulong.md) | The GetUlong method returns a ULONG version of the ExtRemoteData object, which represents the contents of the target's memory. |
| [ExtRemoteTypedList::GetTypedNode method](..\engextcpp\nf-engextcpp-extremotetypedlist-gettypednode.md) | The GetTypedNode method returns the current list item. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [ExtRemoteList interface](..\engextcpp\nl-engextcpp-extremotelist.md) | The ExtRemoteList class provides a wrapper around a singly-linked or doubly-linked list. The class contains methods that can be used to move both forward and backward through the list. |
| [ExtRemoteData interface](..\engextcpp\nl-engextcpp-extremotedata.md) | The ExtRemoteData class provides a wrapper around a small section of a target's memory. ExtRemoteData automatically retrieves the memory and provides a number of convenience methods. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IDebugFailureAnalysis2::AddUlong64 method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addulong64.md) | The AddUlong64 method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified 64-bit value. |
| [IDebugFailureAnalysis2::SetUlong64 method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setulong64.md) | The SetUlong64 method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it sets (overwrites) the data block of the FA entry to a specified ULONG64 value. |
| [IDebugFailureAnalysis2::GetString method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getstring.md) | The GetString method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the ANSI string value from the entry's data block. |
| [IDebugFailureAnalysis2::GetFailureCode method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getfailurecode.md) | The GetFailureCode method gets the bug check code or exception code of a DebugFailureAnalysis object. |
| [IDebugFailureAnalysis2::NextEntry method](..\extsfns\nf-extsfns-idebugfailureanalysis2-nextentry.md) | The NextEntry method gets the next FA entry, after a given FA entry, in a DebugFailureAnalysis object. |
| [IDebugFAEntryTags::GetProperties method](..\extsfns\nf-extsfns-idebugfaentrytags-getproperties.md) | The GetProperties method gets the name or description (or both) of a tag in a DebugFailureAnalysisTags object. |
| [IDebugFailureAnalysis2::GetNext method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getnext.md) | The GetNext method searches a DebugFailureAnalysis object for the next FA entry, after a given FA entry, that satisfies conditions specified by the Tag and TagMask parameters. |
| [IDebugFAEntryTags::GetType method](..\extsfns\nf-extsfns-idebugfaentrytags-gettype.md) | The GetType method gets the data type that is associated with a tag in a DebugFailureAnalysisTags object. |
| [IDebugFAEntryTags::SetProperties method](..\extsfns\nf-extsfns-idebugfaentrytags-setproperties.md) | The SetProperties method sets the name or description (or both) of a tag in a DebugFailureAnalysisTags object. |
| [IDebugFailureAnalysis2::GetBuffer method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getbuffer.md) | The GetBuffer method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the entry's data block. |
| [IDebugFailureAnalysis2::AddBuffer method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addbuffer.md) | The AddBuffer method adds a new FA entry to a DebugFailureAnalysis object, and writes the bytes from a specified buffer to the data block of the new FA entry. |
| [IDebugFailureAnalysis2::GetDebugFATagControl method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getdebugfatagcontrol.md) | The GetDebugFATagControl method gets a pointer to an IDebugFAEntryTags interface, which provides access to the tags in a DebugFailureAnalysisTags object. |
| [IDebugFailureAnalysis2::SetUlong method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setulong.md) | The SetUlong method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it sets (overwrites) the data block of the FA entry to a specified ULONG value. |
| [IDebugFAEntryTags::IsValidTagToSet method](..\extsfns\nf-extsfns-idebugfaentrytags-isvalidtagtoset.md) | The IsValidTagToSet method determines whether it is OK to set the data of a specified tag. |
| [IDebugFailureAnalysis2::SetExtensionCommand method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setextensioncommand.md) | The SetExtensionCommand method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. |
| [IDebugFAEntryTags::GetTagByName method](..\extsfns\nf-extsfns-idebugfaentrytags-gettagbyname.md) | The GetTagByName method searches for a tag that has a specified name. |
| [IDebugFailureAnalysis2::GetFailureClass method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getfailureclass.md) | The GetFailureClass method gets the failure class of a DebugFailureAnalysis object. The failure class indicates whether the debugging session that created the DebugFailureAnalysis object is a kernel mode session or a user mode session. |
| [IDebugFailureAnalysis2::GetUlong method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getulong.md) | The GetUlong method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the ULONG value from the entry's data block. |
| [IDebugFailureAnalysis2::SetBuffer method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setbuffer.md) | The SetBuffer method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it overwrites the data block of the FA entry with the bytes in a specified buffer. |
| [IDebugFailureAnalysis2::SetString method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setstring.md) | The SetString method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it sets (overwrites) the data block of the FA entry to a specified string value. |
| [IDebugFAEntryTags::SetType method](..\extsfns\nf-extsfns-idebugfaentrytags-settype.md) | The SetType method sets the data type that is associated with a tag in a DebugFailureAnalysisTags object. |
| [IDebugFailureAnalysis2::AddUlong method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addulong.md) | The AddUlong method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified ULONG value. |
| [IDebugFailureAnalysis2::GetFailureType method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getfailuretype.md) | The GetFailureType method gets the failure type of a DebugFailureAnalysis object. The failure type indicates whether the code being analyzed was running in kernel mode or user mode. |
| [IDebugFailureAnalysis2::Get method](..\extsfns\nf-extsfns-idebugfailureanalysis2-get.md) | The Get method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. |
| [IDebugFailureAnalysis2::GetUlong64 method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getulong64.md) | The GetUlong64 method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the ULONG64 value from the entry's data block. |
| [IDebugFailureAnalysis2::AddString method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addstring.md) | The AddString method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified string. |
| [IDebugFailureAnalysis2::AddExtensionCommand method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addextensioncommand.md) | The AddExtensionCommand method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified debugger command. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [DEBUG_FLR_PARAM_TYPE enumeration](..\extsfns\ne-extsfns--debug-flr-param-type.md) | The values of DEBUG_FLR_PARAM_TYPE enumeration are tags that indicate the kind of information that is stored in failure analysis entry. |
| [DEBUG_FAILURE_TYPE enumeration](..\extsfns\ne-extsfns--debug-failure-type.md) | The values in the DEBUG_FAILURE_TYPE enumeration indicate the type of a failure. |
| [FA_ENTRY_TYPE enumeration](..\extsfns\ne-extsfns--fa-entry-type.md) | A DebugFailureAnalysis object has a collection of failure analysis entries (FA entries). |
| [FA_EXTENSION_PLUGIN_PHASE enumeration](..\extsfns\ne-extsfns--fa-extension-plugin-phase.md) | A value in the FA_EXTENSION_PLUGIN_PHASE enumeration is passed to the _EFN_Analyze function to specify which phase of the analysis is currently in progress. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [FA_ENTRY structure](..\extsfns\ns-extsfns--fa-entry.md) | A DebugFailureAnalysis object has a collection of failure analysis entries (FA entries). Each FA entry is represented by an FA_ENTRY structure. For more information, see Failure Analysis Entries, Tags, and Data Types. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IDebugFailureAnalysis2 interface](..\extsfns\nn-extsfns-idebugfailureanalysis2.md) | When the !analyze debugger command runs, the analysis engine can load and run extension analysis plug-ins. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [ReadIoSpace64 function](..\wdbgexts\nf-wdbgexts-readiospace64.md) | The ReadIoSpace64 function reads from the system I/O locations. |
| [WritePhysical function](..\wdbgexts\nf-wdbgexts-writephysical.md) | The WritePhysical function writes to physical memory. |
| [GetSetSympath function](..\wdbgexts\nf-wdbgexts-getsetsympath.md) | The GetSetSympath function can be used to either get or set the symbol search path. |
| [GetFieldOffset function](..\wdbgexts\nf-wdbgexts-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [GetPebAddress function](..\wdbgexts\nf-wdbgexts-getpebaddress.md) | The GetPebAddress function returns the address of the process environment block (PEB) for a system process. |
| [GetTebAddress function](..\wdbgexts\nf-wdbgexts-gettebaddress.md) | The GetTebAddress function returns the address of the thread environment block (TEB) for the current operating system thread. |
| [GetDebuggerData function](..\wdbgexts\nf-wdbgexts-getdebuggerdata.md) | The GetDebuggerData function retrieves information stored in a data block. |
| [WritePointer function](..\wdbgexts\nf-wdbgexts-writepointer.md) | The WritePointer function writes a pointer to the target. |
| [ReadControlSpace64 function](..\wdbgexts\nf-wdbgexts-readcontrolspace64.md) | The ReadControlSpace64 function reads the processor-specific control space into the array pointed to by buf. |
| [GetFieldValue function](..\wdbgexts\nf-wdbgexts-getfieldvalue.md) | The GetFieldValue macro is a thin wrapper around the GetFieldData function. It is provided as a convenience for reading the value of a member in a structure. |
| [WriteControlSpace function](..\wdbgexts\nf-wdbgexts-writecontrolspace.md) | The WriteControlSpace function writes to the processor-specific control space of the current target. |
| [ListType function](..\wdbgexts\nf-wdbgexts-listtype.md) | The ListType function calls a specified callback function for every element in a linked list. |
| [GetTypeSize function](..\wdbgexts\nf-wdbgexts-gettypesize.md) | The GetTypeSize function returns the size in the target's memory of an instance of the specified type. |
| [GetKdContext function](..\wdbgexts\nf-wdbgexts-getkdcontext.md) | The GetKdContext function returns the total number of processors and the number of the current processor in the structure ppi points to. |
| [GetExpressionEx function](..\wdbgexts\nf-wdbgexts-getexpressionex.md) | The GetExpressionEx function evaluates an expression. The expression is evaluated using the MASM evaluator, and can contain aliases. |
| [GetFieldData function](..\wdbgexts\nf-wdbgexts-getfielddata.md) | The GetFieldData function returns the value of a member in a structure. |
| [ReadMsr function](..\wdbgexts\nf-wdbgexts-readmsr.md) | The ReadMsr function reads the contents of a Model-Specific Register (MSR). |
| [GetShortField function](..\wdbgexts\nf-wdbgexts-getshortfield.md) | The GetShortField function reads the value of a member in a structure if its size is less than or equal to 8 bytes, or initializes a structure so it can be read later. |
| [ReadPhysical function](..\wdbgexts\nf-wdbgexts-readphysical.md) | The ReadPhysical function reads from physical memory. |
| [GetInputLine function](..\wdbgexts\nf-wdbgexts-getinputline.md) | The GetInputLine function requests an input string from the debugger. |
| [ReadPhysicalWithFlags function](..\wdbgexts\nf-wdbgexts-readphysicalwithflags.md) | The ReadPhysicalWithFlags function reads from physical memory. |
| [ReloadSymbols function](..\wdbgexts\nf-wdbgexts-reloadsymbols.md) | The ReloadSymbols function deletes symbol information from the debugger so that it can be reloaded as needed. This function behaves the same way as the debugger command .reload. |
| [WriteIoSpaceEx64 function](..\wdbgexts\nf-wdbgexts-writeiospaceex64.md) | The WriteIoSpaceEx64 function is an extended version of WriteIoSpace64. |
| [SetThreadForOperation function](..\wdbgexts\nf-wdbgexts-setthreadforoperation.md) | The SetThreadForOperation function sets the thread to use for the next StackTrace call. |
| [GetCurrentThreadAddr function](..\wdbgexts\nf-wdbgexts-getcurrentthreadaddr.md) | The GetCurrentThreadAddr function returns the location of the system data that describes the current thread. |
| [GetCurrentProcessAddr function](..\wdbgexts\nf-wdbgexts-getcurrentprocessaddr.md) | The GetCurrentProcessAddr function returns the location of the system data that describes the current process. |
| [ReadPointer function](..\wdbgexts\nf-wdbgexts-readpointer.md) | The ReadPointer function reads a pointer from the target. |
| [WritePhysicalWithFlags function](..\wdbgexts\nf-wdbgexts-writephysicalwithflags.md) | The WritePhysicalWithFlags function writes to physical memory. |
| [ReadControlSpace function](..\wdbgexts\nf-wdbgexts-readcontrolspace.md) | The ReadControlSpace function reads the processor-specific control space into the array pointed to by buf. |
| [TranslateVirtualToPhysical function](..\wdbgexts\nf-wdbgexts-translatevirtualtophysical.md) | The TranslateVirtualToPhysical function translates a virtual memory address into a physical memory address. |
| [SearchMemory function](..\wdbgexts\nf-wdbgexts-searchmemory.md) | The SearchMemory function searches the target's virtual memory for a specified pattern of bytes. |
| [IsPtr64 function](..\wdbgexts\nf-wdbgexts-isptr64.md) | The IsPtr64 function determines if the target uses 64-bit pointers. |
| [GetDebuggerCacheSize function](..\wdbgexts\nf-wdbgexts-getdebuggercachesize.md) | The GetDebuggerCacheSize function returns the size of the cache that is used by the debugger to hold data that was obtained from the target. |
| [WriteIoSpace function](..\wdbgexts\nf-wdbgexts-writeiospace.md) | The WriteIoSpace function writes to the system I/O locations. |
| [WriteMsr function](..\wdbgexts\nf-wdbgexts-writemsr.md) | The WriteMsr function writes to a Model-Specific Register (MSR). |
| [ReadListEntry function](..\wdbgexts\nf-wdbgexts-readlistentry.md) | The ReadListEntry function reads a doubly-linked list entry from the target's memory. |
| [ReadPtr function](..\wdbgexts\nf-wdbgexts-readptr.md) | The ReadPtr function reads a pointer from the target. ReadPointer should be used instead of this function as the return value of ReadPointer is more consistent with the rest of the WdbgExts API. |
| [ReadIoSpace function](..\wdbgexts\nf-wdbgexts-readiospace.md) | The ReadIoSpace function reads from the system I/O locations. |
| [WriteIoSpaceEx function](..\wdbgexts\nf-wdbgexts-writeiospaceex.md) | The WriteIoSpaceEx function is an extended version of WriteIoSpace. |
| [ReadIoSpaceEx64 function](..\wdbgexts\nf-wdbgexts-readiospaceex64.md) | The ReadIoSpaceEx64 function is an extended version of ReadIoSpace64. |
| [WriteIoSpace64 function](..\wdbgexts\nf-wdbgexts-writeiospace64.md) | The WriteIoSpace64 function writes to the system I/O locations. |
| [ReadIoSpaceEx function](..\wdbgexts\nf-wdbgexts-readiospaceex.md) | The ReadIoSpaceEx function is an extended version of ReadIoSpace. |
| [GetCurrentProcessHandle function](..\wdbgexts\nf-wdbgexts-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
| [SetThreadForOperation64 function](..\wdbgexts\nf-wdbgexts-setthreadforoperation64.md) | The SetThreadForOperation64 function sets the thread to use for the next StackTrace call. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [DBGKD_GET_VERSION64 structure](..\wdbgexts\ns-wdbgexts--dbgkd-get-version64.md) | The IG_GET_KERNEL_VERSION Ioctl operation receives information related to the operating system version of the target. |
| [EXT_TYPED_DATA structure](..\wdbgexts\ns-wdbgexts--ext-typed-data.md) | The EXT_TYPED_DATA structure is passed to and returned from the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation. It contains the input and output parameters for the operation as well as specifying which particular suboperation to perform. |
| [GETSETBUSDATA structure](..\wdbgexts\ns-wdbgexts--getsetbusdata.md) | The IG_GET_BUS_DATA Ioctl operation reads data from a system bus and the IG_SET_BUS_DATA Ioctl operation writes data to a system bus. |
| [POINTER_SEARCH_PHYSICAL structure](..\wdbgexts\ns-wdbgexts--pointer-search-physical.md) | The IG_POINTER_SEARCH_PHYSICAL Ioctl operation searches the target's physical memory for pointers lying within a specified range. |
| [DEBUG_TYPED_DATA structure](..\wdbgexts\ns-wdbgexts--debug-typed-data.md) | The DEBUG_TYPED_DATA structure describes typed data in the memory of the target. |
| [WDBGEXTS_THREAD_OS_INFO structure](..\wdbgexts\ns-wdbgexts--wdbgexts-thread-os-info.md) | The IG_GET_THREAD_OS_INFO Ioctl operation returns information about an operating system thread in the target. When calling Ioctl with IoctlType set to IG_GET_THREAD_OS_INFO, IpvData should contain an instance of the WDBGEXTS_THREAD_OS_INFO structure. |
| [SYM_DUMP_PARAM structure](..\wdbgexts\ns-wdbgexts--sym-dump-param.md) | The IG_DUMP_SYMBOL_INFO Ioctl operation provides information about the type of a symbol. |
| [FIELD_INFO structure](..\wdbgexts\ns-wdbgexts--field-info.md) | The FIELD_INFO structure is used by the IG_DUMP_SYMBOL_INFOIoctl operation to provide information about a member in a structure. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PSYM_DUMP_FIELD_CALLBACK callback](..\wdbgexts\nc-wdbgexts-psym-dump-field-callback.md) | The PSYM_DUMP_FIELD_CALLBACK callback function is called by the debugger engine during the IG_DUMP_SYMBOL_INFO Ioctl operation with information about a member in the specified symbol. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [EXT_TDOP enumeration](..\wdbgexts\ne-wdbgexts--ext-tdop.md) | The EXT_TDOP enumeration is used in the Operation member of the EXT_TYPED_DATA structure to specify which suboperation the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation will perform. |


This technology is in the following headers:


| Header        | 

| [dbgeng](..\dbgeng\~PORTAL~dbgeng.md) | 

| [engextcpp](..\engextcpp\~PORTAL~engextcpp.md) | 

| [engextcpp](..\engextcpp\~PORTAL~engextcpp.md) | 

| [extsfns](..\extsfns\~PORTAL~extsfns.md) | 

| [ksdebug](..\ksdebug\~PORTAL~ksdebug.md) | 

| [wdbgexts](..\wdbgexts\~PORTAL~wdbgexts.md) | 
