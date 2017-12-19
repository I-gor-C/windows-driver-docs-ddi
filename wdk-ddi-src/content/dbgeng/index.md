---
UID: NA:
---

# Dbgeng.h header

## -description

This header is used by Debugger. For more information, see
- [Debugger](../_Debugger/index.md)

Dbgeng.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [DebugCommandException function](nf-dbgeng-debugcommandexception.md) | Specifies a debug command exception. |
| [DebugConnect function](nf-dbgeng-debugconnect.md) | The DebugConnect and DebugConnectWide functions create a new client object and return an interface pointer to it. The client object will be connected to a remote host. |
| [DebugConnectWide function](nf-dbgeng-debugconnectwide.md) | The DebugConnect and DebugConnectWide functions create a new client object and return an interface pointer to it. The client object will be connected to a remote host. |
| [DebugCreate function](nf-dbgeng-debugcreate.md) | The DebugCreate function creates a new client object and returns an interface pointer to it. |
| [DebugCreateEx function](nf-dbgeng-debugcreateex.md) | The DebugCreateEx function creates a new client object and returns an interface pointer to it. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PDEBUG_EXTENSION_CALL callback](nc-dbgeng-pdebug_extension_call.md) | Callback functions of the type PDEBUG_EXTENSION_CALL are called by the engine to execute extension commands. You can give these functions any name you want, as long as it contains no uppercase letters. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_DEBUG_BREAKPOINT_PARAMETERS structure](ns-dbgeng-_debug_breakpoint_parameters.md) | The DEBUG_BREAKPOINT_PARAMETERS structure contains most of the parameters for describing a breakpoint. |
| [_DEBUG_CACHED_SYMBOL_INFO structure](ns-dbgeng-_debug_cached_symbol_info.md) | Defines information about cached symbols. |
| [_DEBUG_CLIENT_CONTEXT structure](ns-dbgeng-_debug_client_context.md) | Contains a debug client constant to provide to the IDebugClient7 |
| [_DEBUG_CREATE_PROCESS_OPTIONS structure](ns-dbgeng-_debug_create_process_options.md) | The DEBUG_CREATE_PROCESS_OPTIONS structure specifies the process creation options to use when creating a new process. |
| [_DEBUG_EVENT_CONTEXT structure](ns-dbgeng-_debug_event_context.md) | Defines context information about an event. |
| [_DEBUG_EXCEPTION_FILTER_PARAMETERS structure](ns-dbgeng-_debug_exception_filter_parameters.md) | The DEBUG_EXCEPTION_FILTER_PARAMETERS structure contains the parameters for an exception filter. |
| [_DEBUG_GET_TEXT_COMPLETIONS_IN structure](ns-dbgeng-_debug_get_text_completions_in.md) | Defines information about text completions to get. |
| [_DEBUG_GET_TEXT_COMPLETIONS_OUT structure](ns-dbgeng-_debug_get_text_completions_out.md) | Defines information about text completions to get. |
| [_DEBUG_HANDLE_DATA_BASIC structure](ns-dbgeng-_debug_handle_data_basic.md) | The DEBUG_HANDLE_DATA_BASIC structure contains handle-related information about a system object. |
| [_DEBUG_LAST_EVENT_INFO_BREAKPOINT structure](ns-dbgeng-_debug_last_event_info_breakpoint.md) | Describes the breakpoint of the last event. |
| [_DEBUG_LAST_EVENT_INFO_EXCEPTION structure](ns-dbgeng-_debug_last_event_info_exception.md) | Describes the exception of the last event. |
| [_DEBUG_LAST_EVENT_INFO_EXIT_PROCESS structure](ns-dbgeng-_debug_last_event_info_exit_process.md) | Describes the exit process of the last event. |
| [_DEBUG_LAST_EVENT_INFO_EXIT_THREAD structure](ns-dbgeng-_debug_last_event_info_exit_thread.md) | Describes the exit thread of the last event. |
| [_DEBUG_LAST_EVENT_INFO_LOAD_MODULE structure](ns-dbgeng-_debug_last_event_info_load_module.md) | Describes the load module of the last event. |
| [_DEBUG_LAST_EVENT_INFO_SYSTEM_ERROR structure](ns-dbgeng-_debug_last_event_info_system_error.md) | Describes the system error of the last event. |
| [_DEBUG_LAST_EVENT_INFO_UNLOAD_MODULE structure](ns-dbgeng-_debug_last_event_info_unload_module.md) | Describes the unload module of the last event. |
| [_DEBUG_MODULE_AND_ID structure](ns-dbgeng-_debug_module_and_id.md) | The DEBUG_MODULE_AND_ID structure describes a symbol within a module. |
| [_DEBUG_MODULE_PARAMETERS structure](ns-dbgeng-_debug_module_parameters.md) | The DEBUG_MODULE_PARAMETERS structure contains most of the parameters for describing a module. |
| [_DEBUG_OFFSET_REGION structure](ns-dbgeng-_debug_offset_region.md) | Defines a debug offset region. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_ALL structure](ns-dbgeng-_debug_processor_identification_all.md) | This union contains relevant information for a processor the supported processors. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_ALPHA structure](ns-dbgeng-_debug_processor_identification_alpha.md) | Identifies an Alpha processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_AMD64 structure](ns-dbgeng-_debug_processor_identification_amd64.md) | Identifies an AMD64 processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_ARM structure](ns-dbgeng-_debug_processor_identification_arm.md) | Identifies an ARM processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_ARM64 structure](ns-dbgeng-_debug_processor_identification_arm64.md) | Identifies an ARM64 processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_IA64 structure](ns-dbgeng-_debug_processor_identification_ia64.md) | Identifies an Intel Itanium architecture (IA64) processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_X86 structure](ns-dbgeng-_debug_processor_identification_x86.md) | Identifies an x86 processor. |
| [_DEBUG_READ_USER_MINIDUMP_STREAM structure](ns-dbgeng-_debug_read_user_minidump_stream.md) | Describes a user minidump to read. |
| [_DEBUG_REGISTER_DESCRIPTION structure](ns-dbgeng-_debug_register_description.md) | The DEBUG_REGISTER_DESCRIPTION structure is returned by GetDescription to describe a processor's register. |
| [_DEBUG_SPECIFIC_FILTER_PARAMETERS structure](ns-dbgeng-_debug_specific_filter_parameters.md) | The DEBUG_SPECIFIC_FILTER_PARAMETERS structure contains the parameters for a specific event filter. |
| [_DEBUG_STACK_FRAME structure](ns-dbgeng-_debug_stack_frame.md) | The DEBUG_STACK_FRAME structure describes a stack frame and the address of the current instruction for the stack frame. |
| [_DEBUG_STACK_FRAME_EX structure](ns-dbgeng-_debug_stack_frame_ex.md) | The DEBUG_STACK_FRAME_EX structure describes a stack frame and the address of the current instruction for the stack frame. |
| [_DEBUG_SYMBOL_ENTRY structure](ns-dbgeng-_debug_symbol_entry.md) | The DEBUG_SYMBOL_ENTRY structure describes a symbol in a symbol group. |
| [_DEBUG_SYMBOL_PARAMETERS structure](ns-dbgeng-_debug_symbol_parameters.md) | The DEBUG_SYMBOL_PARAMETERS structure describes a symbol in a symbol group. |
| [_DEBUG_SYMBOL_SOURCE_ENTRY structure](ns-dbgeng-_debug_symbol_source_entry.md) | The DEBUG_SYMBOL_SOURCE_ENTRY structure describes a section of the source code and a corresponding region of the target's memory. |
| [_DEBUG_THREAD_BASIC_INFORMATION structure](ns-dbgeng-_debug_thread_basic_information.md) | The DEBUG_THREAD_BASIC_INFORMATION structure describes an operating system thread. |
| [_DEBUG_VALUE structure](ns-dbgeng-_debug_value.md) | The DEBUG_VALUE structure holds register and expression values. |
| [_INLINE_FRAME_CONTEXT structure](ns-dbgeng-_inline_frame_context.md) | Describes inline frame context. |
| [_STACK_SRC_INFO structure](ns-dbgeng-_stack_src_info.md) | Defines stack source information. |
| [_STACK_SYM_FRAME_INFO structure](ns-dbgeng-_stack_sym_frame_info.md) | Defines stack source information for an extended stack frame. |
| [_SYMBOL_INFO_EX structure](ns-dbgeng-_symbol_info_ex.md) | The SYMBOL_INFO_EX structure describes the extended line symbol information. |

## Methods

| Title   | Description   |
| ---- |:---- |
| [IDebugAdvanced3::FindSourceFileAndToken method](nf-dbgeng-idebugadvanced3-findsourcefileandtoken.md) | The FindSourceFileAndToken method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [IDebugAdvanced3::FindSourceFileAndTokenWide method](nf-dbgeng-idebugadvanced3-findsourcefileandtokenwide.md) | The FindSourceFileAndTokenWide method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [IDebugAdvanced3::GetSourceFileInformation method](nf-dbgeng-idebugadvanced3-getsourcefileinformation.md) | The GetSourceFileInformation method returns specified information about a source file. |
| [IDebugAdvanced3::GetSourceFileInformationWide method](nf-dbgeng-idebugadvanced3-getsourcefileinformationwide.md) | The GetSourceFileInformationWide method returns specified information about a source file. |
| [IDebugAdvanced3::GetSymbolInformation method](nf-dbgeng-idebugadvanced3-getsymbolinformation.md) | The GetSymbolInformation method returns specified information about a symbol. |
| [IDebugAdvanced3::GetSymbolInformationWide method](nf-dbgeng-idebugadvanced3-getsymbolinformationwide.md) | The SetSymbolInformationWide method returns specified information about a symbol. |
| [IDebugAdvanced3::GetSystemObjectInformation method](nf-dbgeng-idebugadvanced3-getsystemobjectinformation.md) | The GetSystemObjectInformation method returns information about operating system objects on the target. |
| [IDebugAdvanced3::GetThreadContext method](nf-dbgeng-idebugadvanced3-getthreadcontext.md) | The GetThreadContext method returns the current thread context. |
| [IDebugAdvanced3::Request method](nf-dbgeng-idebugadvanced3-request.md) | The Request method performs a variety of different operations. |
| [IDebugAdvanced3::SetThreadContext method](nf-dbgeng-idebugadvanced3-setthreadcontext.md) | The SetThreadContext method sets the current thread context. |
| [IDebugAdvanced4::GetSymbolInformationWideEx method](nf-dbgeng-idebugadvanced4-getsymbolinformationwideex.md) | The GetSymbolInformationWideEx method returns specified information about a symbol. |
| [IDebugBreakpoint2::AddFlags method](nf-dbgeng-idebugbreakpoint2-addflags.md) | The AddFlags method adds flags to a breakpoint. |
| [IDebugBreakpoint2::GetAdder method](nf-dbgeng-idebugbreakpoint2-getadder.md) | The GetAdder method returns the client that owns the breakpoint. |
| [IDebugBreakpoint2::GetCommand method](nf-dbgeng-idebugbreakpoint2-getcommand.md) | The GetCommand method returns the command string that is executed when a breakpoint is triggered. |
| [IDebugBreakpoint2::GetCommandWide method](nf-dbgeng-idebugbreakpoint2-getcommandwide.md) | The GetCommand method returns the command string that is executed when a breakpoint is triggered. |
| [IDebugBreakpoint2::GetCurrentPassCount method](nf-dbgeng-idebugbreakpoint2-getcurrentpasscount.md) | The GetCurrentPassCount method returns the remaining number of times that the target must reach the breakpoint location before the breakpoint is triggered. |
| [IDebugBreakpoint2::GetDataParameters method](nf-dbgeng-idebugbreakpoint2-getdataparameters.md) | The GetDataParameters method returns the parameters for a processor breakpoint. |
| [IDebugBreakpoint2::GetFlags method](nf-dbgeng-idebugbreakpoint2-getflags.md) | The GetFlags method returns the flags for a breakpoint. |
| [IDebugBreakpoint2::GetId method](nf-dbgeng-idebugbreakpoint2-getid.md) | The GetId method returns a breakpoint ID, which is the engine's unique identifier for a breakpoint. |
| [IDebugBreakpoint2::GetMatchThreadId method](nf-dbgeng-idebugbreakpoint2-getmatchthreadid.md) | The GetMatchThreadId method returns the engine thread ID of the thread that can trigger a breakpoint. |
| [IDebugBreakpoint2::GetOffset method](nf-dbgeng-idebugbreakpoint2-getoffset.md) | The GetOffset method returns the location that triggers a breakpoint. |
| [IDebugBreakpoint2::GetOffsetExpression method](nf-dbgeng-idebugbreakpoint2-getoffsetexpression.md) | The GetOffsetExpression methods return the expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugBreakpoint2::GetOffsetExpressionWide method](nf-dbgeng-idebugbreakpoint2-getoffsetexpressionwide.md) | The GetOffsetExpressionWide method returns the expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugBreakpoint2::GetParameters method](nf-dbgeng-idebugbreakpoint2-getparameters.md) | The GetParameters method returns the parameters for a breakpoint. |
| [IDebugBreakpoint2::GetPassCount method](nf-dbgeng-idebugbreakpoint2-getpasscount.md) | The GetPassCount method returns the number of times that the target was originally required to reach the breakpoint location before the breakpoint is triggered. |
| [IDebugBreakpoint2::GetType method](nf-dbgeng-idebugbreakpoint2-gettype.md) | The GetType method returns the type of the breakpoint and the type of the processor that a breakpoint is set for. |
| [IDebugBreakpoint2::RemoveFlags method](nf-dbgeng-idebugbreakpoint2-removeflags.md) | The RemoveFlags method removes flags from a breakpoint. |
| [IDebugBreakpoint2::SetCommand method](nf-dbgeng-idebugbreakpoint2-setcommand.md) | The SetCommand method sets the command that is executed when a breakpoint is triggered. |
| [IDebugBreakpoint2::SetCommandWide method](nf-dbgeng-idebugbreakpoint2-setcommandwide.md) | The SetCommandWide method sets the command that is executed when a breakpoint is triggered. |
| [IDebugBreakpoint2::SetDataParameters method](nf-dbgeng-idebugbreakpoint2-setdataparameters.md) | The SetDataParameters method sets the parameters for a processor breakpoint. |
| [IDebugBreakpoint2::SetFlags method](nf-dbgeng-idebugbreakpoint2-setflags.md) | The SetFlags method sets the flags for a breakpoint. |
| [IDebugBreakpoint2::SetMatchThreadId method](nf-dbgeng-idebugbreakpoint2-setmatchthreadid.md) | The SetMatchThreadId method sets the engine thread ID of the thread that can trigger a breakpoint. |
| [IDebugBreakpoint2::SetOffset method](nf-dbgeng-idebugbreakpoint2-setoffset.md) | The SetOffset method sets the location that triggers a breakpoint. |
| [IDebugBreakpoint2::SetOffsetExpression method](nf-dbgeng-idebugbreakpoint2-setoffsetexpression.md) | The SetOffsetExpression methods set an expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugBreakpoint2::SetOffsetExpressionWide method](nf-dbgeng-idebugbreakpoint2-setoffsetexpressionwide.md) | The SetOffsetExpressionWide methods set an expression string that evaluates to the location that triggers a breakpoint. |
| [IDebugBreakpoint2::SetPassCount method](nf-dbgeng-idebugbreakpoint2-setpasscount.md) | The SetPassCount method sets the number of times that the target must reach the breakpoint location before the breakpoint is triggered. |
| [IDebugBreakpoint3::GetGuid method](nf-dbgeng-idebugbreakpoint3-getguid.md) | Returns a GUID for the breakpoint. |
| [IDebugClient5::AbandonCurrentProcess method](nf-dbgeng-idebugclient5-abandoncurrentprocess.md) | The AbandonCurrentProcess method removes the current process from the debugger engine's process list without detaching or terminating the process. |
| [IDebugClient5::AddDumpInformationFile method](nf-dbgeng-idebugclient5-adddumpinformationfile.md) | The AddDumpInformationFile method registers additional files containing supporting information that will be used when opening a dump file. The Unicode version of this method is AddDumpInformationFileWide. |
| [IDebugClient5::AddDumpInformationFileWide method](nf-dbgeng-idebugclient5-adddumpinformationfilewide.md) | The AddDumpInformationFileWide method registers additional files containing supporting information that will be used when opening a dump file. The ASCII version of this method is AddDumpInformationFile. |
| [IDebugClient5::AddProcessOptions method](nf-dbgeng-idebugclient5-addprocessoptions.md) | The AddProcessOptions method adds the process options to those options that affect the current process. |
| [IDebugClient5::AttachKernel method](nf-dbgeng-idebugclient5-attachkernel.md) | The AttachKernel methods connect the debugger engine to a kernel target. |
| [IDebugClient5::AttachKernelWide method](nf-dbgeng-idebugclient5-attachkernelwide.md) | The AttachKernelWide method connects the debugger engine to a kernel target. |
| [IDebugClient5::AttachProcess method](nf-dbgeng-idebugclient5-attachprocess.md) | The AttachProcess method connects the debugger engine to a user-modeprocess. |
| [IDebugClient5::ConnectProcessServer method](nf-dbgeng-idebugclient5-connectprocessserver.md) | The ConnectProcessServer methods connect to a process server. |
| [IDebugClient5::ConnectProcessServerWide method](nf-dbgeng-idebugclient5-connectprocessserverwide.md) | The ConnectProcessServerWide method connects to a process server. |
| [IDebugClient5::ConnectSession method](nf-dbgeng-idebugclient5-connectsession.md) | The ConnectSession method joins the client to an existing debugger session. |
| [IDebugClient5::CreateClient method](nf-dbgeng-idebugclient5-createclient.md) | The CreateClient method creates a new client object for the current thread. |
| [IDebugClient5::CreateProcess method](nf-dbgeng-idebugclient5-createprocess.md) | The CreateProcess method creates a process from the specified command line. |
| [IDebugClient5::CreateProcess2 method](nf-dbgeng-idebugclient5-createprocess2.md) | The CreateProcess2 method executes the given command to create a new process. |
| [IDebugClient5::CreateProcess2Wide method](nf-dbgeng-idebugclient5-createprocess2wide.md) | The CreateProcess2Wide method executes the specified command to create a new process. |
| [IDebugClient5::CreateProcessAndAttach method](nf-dbgeng-idebugclient5-createprocessandattach.md) | The CreateProcessAndAttach method creates a process from a specified command line, then attach to another user-mode process. |
| [IDebugClient5::CreateProcessAndAttach2 method](nf-dbgeng-idebugclient5-createprocessandattach2.md) | The CreateProcessAndAttach2 method creates a process from a specified command line, then attaches to that process or another user-mode process. |
| [IDebugClient5::CreateProcessAndAttach2Wide method](nf-dbgeng-idebugclient5-createprocessandattach2wide.md) | The CreateProcessAndAttach2Wide method creates a process from a specified command line, then attach to that process or another user-mode process. |
| [IDebugClient5::CreateProcessAndAttachWide method](nf-dbgeng-idebugclient5-createprocessandattachwide.md) | The CreateProcessAndAttachWide method creates a process from a specified command line, then attach to another user-mode process. |
| [IDebugClient5::CreateProcessWide method](nf-dbgeng-idebugclient5-createprocesswide.md) | The CreateProcessWide method creates a process from the specified command line. |
| [IDebugClient5::DetachCurrentProcess method](nf-dbgeng-idebugclient5-detachcurrentprocess.md) | The DetachCurrentProcess method detaches the debugger engine from the current process, resuming all its threads. |
| [IDebugClient5::DetachProcesses method](nf-dbgeng-idebugclient5-detachprocesses.md) | The DetachProcesses method detaches the debugger engine from all processes in all targets, resuming all their threads. |
| [IDebugClient5::DisconnectProcessServer method](nf-dbgeng-idebugclient5-disconnectprocessserver.md) | The DisconnectProcessServer method disconnects the debugger engine from a process server. |
| [IDebugClient5::DispatchCallbacks method](nf-dbgeng-idebugclient5-dispatchcallbacks.md) | The DispatchCallbacks method lets the debugger engine use the current thread for callbacks. |
| [IDebugClient5::EndProcessServer method](nf-dbgeng-idebugclient5-endprocessserver.md) | The EndProcessServer method requests that a process server be shut down. |
| [IDebugClient5::EndSession method](nf-dbgeng-idebugclient5-endsession.md) | The EndSession method ends the current debugger session. |
| [IDebugClient5::ExitDispatch method](nf-dbgeng-idebugclient5-exitdispatch.md) | The ExitDispatch method causes the DispatchCallbacks method to return. |
| [IDebugClient5::FlushCallbacks method](nf-dbgeng-idebugclient5-flushcallbacks.md) | The FlushCallbacks method forces any remaining buffered output to be delivered to the IDebugOutputCallbacks object registered with this client. |
| [IDebugClient5::GetDumpFile method](nf-dbgeng-idebugclient5-getdumpfile.md) | The GetDumpFile method describes the files containing supporting information that were used when opening the current dump target. |
| [IDebugClient5::GetDumpFileWide method](nf-dbgeng-idebugclient5-getdumpfilewide.md) | The GetDumpFileWide method describes the files containing supporting information that were used when opening the current dump target. |
| [IDebugClient5::GetEventCallbacks method](nf-dbgeng-idebugclient5-geteventcallbacks.md) | The GetEventCallbacks method returns the event callbacks object registered with this client. |
| [IDebugClient5::GetEventCallbacksWide method](nf-dbgeng-idebugclient5-geteventcallbackswide.md) | The GetEventCallbacksWide method returns the event callbacks object registered with this client. |
| [IDebugClient5::GetExitCode method](nf-dbgeng-idebugclient5-getexitcode.md) | The GetExitCode method returns the exit code of the current process if that process has already run through to completion. |
| [IDebugClient5::GetIdentity method](nf-dbgeng-idebugclient5-getidentity.md) | The GetIdentity method returns a string describing the computer and user this client represents. |
| [IDebugClient5::GetIdentityWide method](nf-dbgeng-idebugclient5-getidentitywide.md) | The GetIdentityWide method returns a string describing the computer and user this client represents. |
| [IDebugClient5::GetInputCallbacks method](nf-dbgeng-idebugclient5-getinputcallbacks.md) | The GetInputCallbacks method returns the input callbacks object registered with this client. |
| [IDebugClient5::GetKernelConnectionOptions method](nf-dbgeng-idebugclient5-getkernelconnectionoptions.md) | The GetKernelConnectionOptions method returns the connection options for the current kernel target. |
| [IDebugClient5::GetKernelConnectionOptionsWide method](nf-dbgeng-idebugclient5-getkernelconnectionoptionswide.md) | The GetKernelConnectionOptionsWide method returns the connection options for the current kernel target. |
| [IDebugClient5::GetNumberDumpFiles method](nf-dbgeng-idebugclient5-getnumberdumpfiles.md) | The GetNumberDumpFiles method returns the number of files containing supporting information that were used when opening the current dump target. |
| [IDebugClient5::GetNumberEventCallbacks method](nf-dbgeng-idebugclient5-getnumbereventcallbacks.md) | The GetNumberEventCallbacks method returns the number of event callbacks that are interested in the given events. |
| [IDebugClient5::GetNumberInputCallbacks method](nf-dbgeng-idebugclient5-getnumberinputcallbacks.md) | The GetNumberInputCallbacks method returns the number of input callbacks registered over all clients. |
| [IDebugClient5::GetNumberOutputCallbacks method](nf-dbgeng-idebugclient5-getnumberoutputcallbacks.md) | The GetNumberOutputCallbacks method returns the number of output callbacks registered over all clients. |
| [IDebugClient5::GetOtherOutputMask method](nf-dbgeng-idebugclient5-getotheroutputmask.md) | The GetOtherOutputMask method returns the output mask for another client. |
| [IDebugClient5::GetOutputCallbacks method](nf-dbgeng-idebugclient5-getoutputcallbacks.md) | The GetOutputCallbacks method returns the output callbacks object registered with the client. |
| [IDebugClient5::GetOutputCallbacksWide method](nf-dbgeng-idebugclient5-getoutputcallbackswide.md) | The GetOutputCallbacksWide method returns the output callbacks object registered with the client. |
| [IDebugClient5::GetOutputLinePrefixWide method](nf-dbgeng-idebugclient5-getoutputlineprefixwide.md) | Gets a Unicode character string prefix for output lines. |
| [IDebugClient5::GetOutputMask method](nf-dbgeng-idebugclient5-getoutputmask.md) | The GetOutputMask method returns the output mask currently set for the client. |
| [IDebugClient5::GetProcessOptions method](nf-dbgeng-idebugclient5-getprocessoptions.md) | The GetProcessOptions method retrieves the process options affecting the current process. |
| [IDebugClient5::GetQuitLockString method](nf-dbgeng-idebugclient5-getquitlockstring.md) | Gets a quit lock string. |
| [IDebugClient5::GetQuitLockStringWide method](nf-dbgeng-idebugclient5-getquitlockstringwide.md) | Gets a Unicode character quit lock string. |
| [IDebugClient5::GetRunningProcessDescription method](nf-dbgeng-idebugclient5-getrunningprocessdescription.md) | The GetRunningProcessDescription method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [IDebugClient5::GetRunningProcessDescriptionWide method](nf-dbgeng-idebugclient5-getrunningprocessdescriptionwide.md) | The GetRunningProcessDescriptionWide method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [IDebugClient5::GetRunningProcessSystemIdByExecutableName method](nf-dbgeng-idebugclient5-getrunningprocesssystemidbyexecutablename.md) | The GetRunningProcessSystemIdByExecutableName method searches for a process with a given executable file name and return its process ID. |
| [IDebugClient5::GetRunningProcessSystemIdByExecutableNameWide method](nf-dbgeng-idebugclient5-getrunningprocesssystemidbyexecutablenamewide.md) | The GetRunningProcessSystemIdByExecutableNameWide method searches for a process with a given executable file name and return its process ID. |
| [IDebugClient5::GetRunningProcessSystemIds method](nf-dbgeng-idebugclient5-getrunningprocesssystemids.md) | The GetRunningProcessSystemIds method returns the process IDs for each running process. |
| [IDebugClient5::IsKernelDebuggerEnabled method](nf-dbgeng-idebugclient5-iskerneldebuggerenabled.md) | The IsKernelDebuggerEnabled method checks whether kernel debugging is enabled for the local kernel. |
| [IDebugClient5::OpenDumpFile method](nf-dbgeng-idebugclient5-opendumpfile.md) | The OpenDumpFile method opens a dump file as a debugger target. |
| [IDebugClient5::OpenDumpFileWide method](nf-dbgeng-idebugclient5-opendumpfilewide.md) | The OpenDumpFileWide method opens a dump file as a debugger target. |
| [IDebugClient5::OutputIdentity method](nf-dbgeng-idebugclient5-outputidentity.md) | The OutputIdentity method formats and outputs a string describing the computer and user this client represents. |
| [IDebugClient5::OutputIdentityWide method](nf-dbgeng-idebugclient5-outputidentitywide.md) | The OutputIdentityWide method formats and outputs a string describing the computer and user this client represents. |
| [IDebugClient5::OutputServers method](nf-dbgeng-idebugclient5-outputservers.md) | The OutputServers method lists the servers running on a given computer. |
| [IDebugClient5::OutputServersWide method](nf-dbgeng-idebugclient5-outputserverswide.md) | The OutputServersWide method lists the servers running on a given computer. |
| [IDebugClient5::PopOutputLinePrefix method](nf-dbgeng-idebugclient5-popoutputlineprefix.md) | Restores a previously saved output line prefix. |
| [IDebugClient5::PushOutputLinePrefix method](nf-dbgeng-idebugclient5-pushoutputlineprefix.md) | Saves an output line prefix. |
| [IDebugClient5::PushOutputLinePrefixWide method](nf-dbgeng-idebugclient5-pushoutputlineprefixwide.md) | Saves a wide string output line prefix. |
| [IDebugClient5::RemoveProcessOptions method](nf-dbgeng-idebugclient5-removeprocessoptions.md) | The RemoveProcessOptions method removes process options from those options that affect the current process. |
| [IDebugClient5::SetEventCallbacks method](nf-dbgeng-idebugclient5-seteventcallbacks.md) | The SetEventCallbacks method registers an event callbacks object with this client. |
| [IDebugClient5::SetEventCallbacksWide method](nf-dbgeng-idebugclient5-seteventcallbackswide.md) | The SetEventCallbacksWide method registers an event callbacks object with this client. |
| [IDebugClient5::SetInputCallbacks method](nf-dbgeng-idebugclient5-setinputcallbacks.md) | The SetInputCallbacks method registers an input callbacks object with the client. |
| [IDebugClient5::SetKernelConnectionOptions method](nf-dbgeng-idebugclient5-setkernelconnectionoptions.md) | The SetKernelConnectionOptions method updates some of the connection options for a live kernel target. |
| [IDebugClient5::SetKernelConnectionOptionsWide method](nf-dbgeng-idebugclient5-setkernelconnectionoptionswide.md) | The SetKernelConnectionOptionsWide method updates some of the connection options for a live kernel target. |
| [IDebugClient5::SetOtherOutputMask method](nf-dbgeng-idebugclient5-setotheroutputmask.md) | The SetOtherOutputMask method sets the output mask for another client. |
| [IDebugClient5::SetOutputCallbacks method](nf-dbgeng-idebugclient5-setoutputcallbacks.md) | The SetOutputCallbacks method registers an output callbacks object with this client. |
| [IDebugClient5::SetOutputCallbacksWide method](nf-dbgeng-idebugclient5-setoutputcallbackswide.md) | The SetOutputCallbacksWide method registers an output callbacks object with this client. |
| [IDebugClient5::SetOutputLinePrefixWide method](nf-dbgeng-idebugclient5-setoutputlineprefixwide.md) | Sets a wide string prefix for output lines. |
| [IDebugClient5::SetOutputMask method](nf-dbgeng-idebugclient5-setoutputmask.md) | The SetOutputMask method sets the output mask for the client. |
| [IDebugClient5::SetProcessOptions method](nf-dbgeng-idebugclient5-setprocessoptions.md) | The SetProcessOptions method sets the process options affecting the current process. |
| [IDebugClient5::SetQuitLockString method](nf-dbgeng-idebugclient5-setquitlockstring.md) | Sets a quit lock string. |
| [IDebugClient5::SetQuitLockStringWide method](nf-dbgeng-idebugclient5-setquitlockstringwide.md) | Sets a quit lock Unicode character string. |
| [IDebugClient5::StartProcessServer method](nf-dbgeng-idebugclient5-startprocessserver.md) | The StartProcessServer method starts a process server. |
| [IDebugClient5::StartProcessServerWide method](nf-dbgeng-idebugclient5-startprocessserverwide.md) | The StartProcessServerWide method starts a process server. |
| [IDebugClient5::StartServer method](nf-dbgeng-idebugclient5-startserver.md) | The StartServer method starts a debugging server. |
| [IDebugClient5::StartServerWide method](nf-dbgeng-idebugclient5-startserverwide.md) | The StartServerWide method starts a debugging server. |
| [IDebugClient5::TerminateCurrentProcess method](nf-dbgeng-idebugclient5-terminatecurrentprocess.md) | The TerminateCurrentProcess method attempts to terminate the current process. |
| [IDebugClient5::TerminateProcesses method](nf-dbgeng-idebugclient5-terminateprocesses.md) | The TerminateProcesses method attempts to terminate all processes in all targets. |
| [IDebugClient5::WaitForProcessServerEnd method](nf-dbgeng-idebugclient5-waitforprocessserverend.md) | The WaitForProcessServerEnd method waits for a local process server to exit. |
| [IDebugClient5::WriteDumpFile method](nf-dbgeng-idebugclient5-writedumpfile.md) | The WriteDumpFile method creates a user-mode or kernel-modecrash dump file. |
| [IDebugClient5::WriteDumpFile2 method](nf-dbgeng-idebugclient5-writedumpfile2.md) | The WriteDumpFile2 method creates a user-mode or kernel-modecrash dump file. |
| [IDebugClient5::WriteDumpFileWide method](nf-dbgeng-idebugclient5-writedumpfilewide.md) | The WriteDumpFileWide method creates a user-mode or kernel-modecrash dump file. |
| [IDebugClient6::SetEventContextCallbacks method](nf-dbgeng-idebugclient6-seteventcontextcallbacks.md) | Registers an event callbacks object with this client. |
| [IDebugClient7::SetClientContext method](nf-dbgeng-idebugclient7-setclientcontext.md) | The SetClientContext method is reserved for internal use. |
| [IDebugClient::GetOutputLinePrefix method](nf-dbgeng-idebugclient-getoutputlineprefix.md) | Gets the prefix used for multiple lines of output. |
| [IDebugClient::GetOutputWidth method](nf-dbgeng-idebugclient-getoutputwidth.md) | Gets the width of an output line for commands that produce formatted output. |
| [IDebugClient::SetOutputLinePrefix method](nf-dbgeng-idebugclient-setoutputlineprefix.md) | Sets a prefix for multiple lines of output. |
| [IDebugClient::SetOutputWidth method](nf-dbgeng-idebugclient-setoutputwidth.md) | Controls the width of an output line for commands that produce formatted output. |
| [IDebugControl3::AddAssemblyOptions method](nf-dbgeng-idebugcontrol3-addassemblyoptions.md) | The AddAssemblyOptions method turns on some of the assembly and disassembly options. |
| [IDebugControl3::AddBreakpoint method](nf-dbgeng-idebugcontrol3-addbreakpoint.md) | The AddBreakpoint method creates a new breakpoint for the current target. |
| [IDebugControl3::AddEngineOptions method](nf-dbgeng-idebugcontrol3-addengineoptions.md) | The AddEngineOptions method turns on some of the debugger engine's options. |
| [IDebugControl3::AddExtension method](nf-dbgeng-idebugcontrol3-addextension.md) | The AddExtension method loads an extension library into the debugger engine. |
| [IDebugControl3::Assemble method](nf-dbgeng-idebugcontrol3-assemble.md) | The Assemble method assembles a single processor instruction. The assembled instruction is placed in the target's memory. |
| [IDebugControl3::CallExtension method](nf-dbgeng-idebugcontrol3-callextension.md) | The CallExtension method calls a debugger extension. |
| [IDebugControl3::CloseLogFile method](nf-dbgeng-idebugcontrol3-closelogfile.md) | The CloseLogFile method closes the currently-open log file. |
| [IDebugControl3::CoerceValue method](nf-dbgeng-idebugcontrol3-coercevalue.md) | The CoerceValue method converts a value of one type into a value of another type. |
| [IDebugControl3::CoerceValues method](nf-dbgeng-idebugcontrol3-coercevalues.md) | The CoerceValues method converts an array of values into an array of values of different types. |
| [IDebugControl3::ControlledOutput method](nf-dbgeng-idebugcontrol3-controlledoutput.md) | The ControlledOutput method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugControl3::ControlledOutputVaList method](nf-dbgeng-idebugcontrol3-controlledoutputvalist.md) | The ControlledOutputVaList method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugControl3::Disassemble method](nf-dbgeng-idebugcontrol3-disassemble.md) | The Disassemble method disassembles a processor instruction in the target's memory. |
| [IDebugControl3::Evaluate method](nf-dbgeng-idebugcontrol3-evaluate.md) | The Evaluate method evaluates an expression, returning the result. |
| [IDebugControl3::Execute method](nf-dbgeng-idebugcontrol3-execute.md) | The Execute method executes the specified debugger commands. |
| [IDebugControl3::ExecuteCommandFile method](nf-dbgeng-idebugcontrol3-executecommandfile.md) | The ExecuteCommandFile method opens the specified file and executes the debugger commands that are contained within. |
| [IDebugControl3::GetActualProcessorType method](nf-dbgeng-idebugcontrol3-getactualprocessortype.md) | The GetActualProcessorType method returns the processor type of the physical processor of the computer that is running the target. |
| [IDebugControl3::GetAssemblyOptions method](nf-dbgeng-idebugcontrol3-getassemblyoptions.md) | The GetAssemblyOptions method returns the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target. |
| [IDebugControl3::GetBreakpointById method](nf-dbgeng-idebugcontrol3-getbreakpointbyid.md) | The GetBreakpointById method returns the breakpoint with the specified breakpoint ID. |
| [IDebugControl3::GetBreakpointByIndex method](nf-dbgeng-idebugcontrol3-getbreakpointbyindex.md) | The GetBreakpointByIndex method returns the breakpoint located at the specified index. |
| [IDebugControl3::GetBreakpointParameters method](nf-dbgeng-idebugcontrol3-getbreakpointparameters.md) | The GetBreakpointParameters method returns the parameters of one or more breakpoints. |
| [IDebugControl3::GetCodeLevel method](nf-dbgeng-idebugcontrol3-getcodelevel.md) | The GetCodeLevel method returns the current code level and is mainly used when stepping through code. |
| [IDebugControl3::GetCurrentEventIndex method](nf-dbgeng-idebugcontrol3-getcurrenteventindex.md) | The GetCurrentEventIndex method returns the index of the current event within the current list of events for the current target, if such a list exists. |
| [IDebugControl3::GetCurrentSystemUpTime method](nf-dbgeng-idebugcontrol3-getcurrentsystemuptime.md) | The GetCurrentSystemUpTime method returns the number of seconds the current target's computer has been running since it was last started. |
| [IDebugControl3::GetCurrentTimeDate method](nf-dbgeng-idebugcontrol3-getcurrenttimedate.md) | The GetCurrentTimeDate method returns the time of the current target. |
| [IDebugControl3::GetDebuggeeType method](nf-dbgeng-idebugcontrol3-getdebuggeetype.md) | The GetDebuggeeType method describes the nature of the current target. |
| [IDebugControl3::GetDisassembleEffectiveOffset method](nf-dbgeng-idebugcontrol3-getdisassembleeffectiveoffset.md) | The GetDisassembleEffectiveOffset method returns the address of the last instruction disassembled using Disassemble. |
| [IDebugControl3::GetDumpFormatFlags method](nf-dbgeng-idebugcontrol3-getdumpformatflags.md) | The GetDumpFormatFlags method returns the flags that describe what information is available in a dump file target. |
| [IDebugControl3::GetEffectiveProcessorType method](nf-dbgeng-idebugcontrol3-geteffectiveprocessortype.md) | The GetEffectiveProcessorType method returns the effective processor type of the processor of the computer that is running the target. |
| [IDebugControl3::GetEngineOptions method](nf-dbgeng-idebugcontrol3-getengineoptions.md) | The GetEngineOptions method returns the engine's options. |
| [IDebugControl3::GetEventFilterCommand method](nf-dbgeng-idebugcontrol3-geteventfiltercommand.md) | The GetEventFilterCommand method returns the debugger command that the engine will execute when a specified event occurs. |
| [IDebugControl3::GetEventFilterText method](nf-dbgeng-idebugcontrol3-geteventfiltertext.md) | The GetEventFilterText method returns a short description of an event for a specific filter. |
| [IDebugControl3::GetEventIndexDescription method](nf-dbgeng-idebugcontrol3-geteventindexdescription.md) | The GetEventIndexDescription method describes the specified event in a static list of events for the current target. |
| [IDebugControl3::GetExceptionFilterParameters method](nf-dbgeng-idebugcontrol3-getexceptionfilterparameters.md) | The GetExceptionFilterParameters method returns the parameters for exception filters specified by exception codes or by index. |
| [IDebugControl3::GetExceptionFilterSecondCommand method](nf-dbgeng-idebugcontrol3-getexceptionfiltersecondcommand.md) | The GetExceptionFilterSecondCommand method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [IDebugControl3::GetExecutingProcessorType method](nf-dbgeng-idebugcontrol3-getexecutingprocessortype.md) | The GetExecutingProcessorType method returns the executing processor type for the processor for which the last event occurred. |
| [IDebugControl3::GetExecutionStatus method](nf-dbgeng-idebugcontrol3-getexecutionstatus.md) | The GetExecutionStatus method returns information about the execution status of the debugger engine. |
| [IDebugControl3::GetExpressionSyntax method](nf-dbgeng-idebugcontrol3-getexpressionsyntax.md) | The GetExpressionSyntax method returns the current syntax that the engine is using for evaluating expressions. |
| [IDebugControl3::GetExpressionSyntaxNames method](nf-dbgeng-idebugcontrol3-getexpressionsyntaxnames.md) | The GetExpressionSyntaxNames method returns the full and abbreviated names of an expression syntax. |
| [IDebugControl3::GetExtensionByPath method](nf-dbgeng-idebugcontrol3-getextensionbypath.md) | The GetExtensionByPath method returns the handle for an already loaded extension library. |
| [IDebugControl3::GetExtensionFunction method](nf-dbgeng-idebugcontrol3-getextensionfunction.md) | The GetExtensionFunction method returns a pointer to an extension function from an extension library. |
| [IDebugControl3::GetInterrupt method](nf-dbgeng-idebugcontrol3-getinterrupt.md) | The GetInterrupt method checks whether a user interrupt was issued. |
| [IDebugControl3::GetInterruptTimeout method](nf-dbgeng-idebugcontrol3-getinterrupttimeout.md) | The GetInterruptTimeout method returns the number of seconds that the engine will wait when requesting a break into the debugger. |
| [IDebugControl3::GetLastEventInformation method](nf-dbgeng-idebugcontrol3-getlasteventinformation.md) | The GetLastEventInformation method returns information about the last event that occurred in a target. |
| [IDebugControl3::GetLogFile method](nf-dbgeng-idebugcontrol3-getlogfile.md) | The GetLogFile method returns the name of the currently open log file. |
| [IDebugControl3::GetLogMask method](nf-dbgeng-idebugcontrol3-getlogmask.md) | The GetLogMask method returns the output mask for the currently open log file. |
| [IDebugControl3::GetNearInstruction method](nf-dbgeng-idebugcontrol3-getnearinstruction.md) | The GetNearInstruction method returns the location of a processor instruction relative to a given location. |
| [IDebugControl3::GetNotifyEventHandle method](nf-dbgeng-idebugcontrol3-getnotifyeventhandle.md) | The GetNotifyEventHandle method receives the handle of the event that will be signaled after the next exception in a target. |
| [IDebugControl3::GetNumberBreakpoints method](nf-dbgeng-idebugcontrol3-getnumberbreakpoints.md) | The GetNumberBreakpoints method returns the number of breakpoints for the current process. |
| [IDebugControl3::GetNumberEventFilters method](nf-dbgeng-idebugcontrol3-getnumbereventfilters.md) | The GetNumberEventFilters method returns the number of event filters currently used by the engine. |
| [IDebugControl3::GetNumberEvents method](nf-dbgeng-idebugcontrol3-getnumberevents.md) | The GetNumberEvents method returns the number of events for the current target, if the number of events is fixed. |
| [IDebugControl3::GetNumberExpressionSyntaxes method](nf-dbgeng-idebugcontrol3-getnumberexpressionsyntaxes.md) | The GetNumberExpressionSyntaxes method returns the number of expression syntaxes that are supported by the engine. |
| [IDebugControl3::GetNumberPossibleExecutingProcessorTypes method](nf-dbgeng-idebugcontrol3-getnumberpossibleexecutingprocessortypes.md) | The GetNumberPossibleExecutingProcessorTypes method returns the number of processor types that are supported by the computer running the current target. |
| [IDebugControl3::GetNumberProcessors method](nf-dbgeng-idebugcontrol3-getnumberprocessors.md) | The GetNumberProcessors method returns the number of processors on the computer running the current target. |
| [IDebugControl3::GetNumberSupportedProcessorTypes method](nf-dbgeng-idebugcontrol3-getnumbersupportedprocessortypes.md) | The GetNumberSupportedProcessorTypes method returns the number of processor types supported by the engine. |
| [IDebugControl3::GetNumberTextReplacements method](nf-dbgeng-idebugcontrol3-getnumbertextreplacements.md) | The GetNumberTextReplacements method returns the number of currently defined user-named and automatic aliases. |
| [IDebugControl3::GetPageSize method](nf-dbgeng-idebugcontrol3-getpagesize.md) | The GetPageSize method returns the page size for the effective processor mode. |
| [IDebugControl3::GetPossibleExecutingProcessorTypes method](nf-dbgeng-idebugcontrol3-getpossibleexecutingprocessortypes.md) | The GetPossibleExecutingProcessorTypes method returns the processor types that are supported by the computer running the current target. |
| [IDebugControl3::GetProcessorTypeNames method](nf-dbgeng-idebugcontrol3-getprocessortypenames.md) | The GetProcessorTypeNames method returns the full name and abbreviated name of the specified processor type. |
| [IDebugControl3::GetPromptText method](nf-dbgeng-idebugcontrol3-getprompttext.md) | The GetPromptText method returns the standard prompt text that will be prepended to the formatted output specified in the OutputPrompt and OutputPromptVaList methods. |
| [IDebugControl3::GetRadix method](nf-dbgeng-idebugcontrol3-getradix.md) | The GetRadix method returns the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [IDebugControl3::GetReturnOffset method](nf-dbgeng-idebugcontrol3-getreturnoffset.md) | The GetReturnOffset method returns the return address for the current function. |
| [IDebugControl3::GetSpecificFilterArgument method](nf-dbgeng-idebugcontrol3-getspecificfilterargument.md) | The GetSpecificFilterArgument method returns the value of filter argument for thespecific filters that have an argument. |
| [IDebugControl3::GetSpecificFilterParameters method](nf-dbgeng-idebugcontrol3-getspecificfilterparameters.md) | The GetSpecificFilterParameters method returns the parameters for specific event filters. |
| [IDebugControl3::GetStackTrace method](nf-dbgeng-idebugcontrol3-getstacktrace.md) | The GetStackTrace method returns the frames at the top of the specified call stack. |
| [IDebugControl3::GetSupportedProcessorTypes method](nf-dbgeng-idebugcontrol3-getsupportedprocessortypes.md) | The GetSupportedProcessorTypes method returns the processor types supported by the debugger engine. |
| [IDebugControl3::GetSystemErrorControl method](nf-dbgeng-idebugcontrol3-getsystemerrorcontrol.md) | The GetSystemErrorControl method returns the control values for handling system errors. |
| [IDebugControl3::GetSystemVersion method](nf-dbgeng-idebugcontrol3-getsystemversion.md) | The GetSystemVersion method returns information that identifies the operating system on the computer that is running the current target. |
| [IDebugControl3::GetTextMacro method](nf-dbgeng-idebugcontrol3-gettextmacro.md) | The GetTextMacro method returns the value of a fixed-name alias. |
| [IDebugControl3::GetTextReplacement method](nf-dbgeng-idebugcontrol3-gettextreplacement.md) | The GetTextReplacement method returns the value of a user-named alias or an automatic alias. |
| [IDebugControl3::GetWindbgExtensionApis32 method](nf-dbgeng-idebugcontrol3-getwindbgextensionapis32.md) | The GetWindbgExtensionApis32 method returns a structure that facilitates using the WdbgExts API. |
| [IDebugControl3::GetWindbgExtensionApis64 method](nf-dbgeng-idebugcontrol3-getwindbgextensionapis64.md) | The GetWindbgExtensionApis64 method returns a structure that facilitates using the WdbgExts API. |
| [IDebugControl3::IsPointer64Bit method](nf-dbgeng-idebugcontrol3-ispointer64bit.md) | The IsPointer64Bit method determines if the effective processor uses 64-bit pointers. |
| [IDebugControl3::OpenLogFile method](nf-dbgeng-idebugcontrol3-openlogfile.md) | The OpenLogFile method opens a log file that will receive output from the client objects. |
| [IDebugControl3::Output method](nf-dbgeng-idebugcontrol3-output.md) | The Output method formats a string and send the result to output callbacks that have been registered with the engine's clients. |
| [IDebugControl3::OutputCurrentState method](nf-dbgeng-idebugcontrol3-outputcurrentstate.md) | The OutputCurrentState method prints the current state of the current target to the debugger console. |
| [IDebugControl3::OutputDisassembly method](nf-dbgeng-idebugcontrol3-outputdisassembly.md) | The OutputDisassembly method disassembles a processor instruction and sends the disassembly to the output callbacks. |
| [IDebugControl3::OutputDisassemblyLines method](nf-dbgeng-idebugcontrol3-outputdisassemblylines.md) | The OutputDisassemblyLines method disassembles several processor instructions and sends the resulting assembly instructions to the output callbacks. |
| [IDebugControl3::OutputPrompt method](nf-dbgeng-idebugcontrol3-outputprompt.md) | The OutputPrompt method formats and sends a user prompt to the output callback objects. |
| [IDebugControl3::OutputPromptVaList method](nf-dbgeng-idebugcontrol3-outputpromptvalist.md) | The OutputPromptVaList method formats and sends a user prompt to the output callback objects. |
| [IDebugControl3::OutputStackTrace method](nf-dbgeng-idebugcontrol3-outputstacktrace.md) | The OutputStackTrace method outputs either the supplied stack frame or the current stack frames. |
| [IDebugControl3::OutputTextReplacements method](nf-dbgeng-idebugcontrol3-outputtextreplacements.md) | The OutputTextReplacements method prints all the currently defined user-named aliases to the debugger's output stream. |
| [IDebugControl3::OutputVaList method](nf-dbgeng-idebugcontrol3-outputvalist.md) | The OutputVaList method formats a string and sends the result to the output callbacks that are registered with the engine's clients. |
| [IDebugControl3::OutputVersionInformation method](nf-dbgeng-idebugcontrol3-outputversioninformation.md) | The OutputVersionInformation method prints version information about the debugger engine to the debugger console. |
| [IDebugControl3::ReadBugCheckData method](nf-dbgeng-idebugcontrol3-readbugcheckdata.md) | The ReadBugCheckData method reads the kernel bug check code and related parameters. |
| [IDebugControl3::RemoveAssemblyOptions method](nf-dbgeng-idebugcontrol3-removeassemblyoptions.md) | The RemoveAssemblyOptions method turns off some of the assembly and disassembly options. |
| [IDebugControl3::RemoveBreakpoint method](nf-dbgeng-idebugcontrol3-removebreakpoint.md) | The RemoveBreakpoint method removes a breakpoint. |
| [IDebugControl3::RemoveEngineOptions method](nf-dbgeng-idebugcontrol3-removeengineoptions.md) | The RemoveEngineOptions method turns off some of the engine's options. |
| [IDebugControl3::RemoveExtension method](nf-dbgeng-idebugcontrol3-removeextension.md) | The RemoveExtension method unloads an extension library. |
| [IDebugControl3::RemoveTextReplacements method](nf-dbgeng-idebugcontrol3-removetextreplacements.md) | The RemoveTextReplacements method removes all user-named aliases. |
| [IDebugControl3::ReturnInput method](nf-dbgeng-idebugcontrol3-returninput.md) | The ReturnInput method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input. |
| [IDebugControl3::SetAssemblyOptions method](nf-dbgeng-idebugcontrol3-setassemblyoptions.md) | The SetAssemblyOptions method sets the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target. |
| [IDebugControl3::SetCodeLevel method](nf-dbgeng-idebugcontrol3-setcodelevel.md) | The SetCodeLevel method sets the current code level and is mainly used when stepping through code. |
| [IDebugControl3::SetEffectiveProcessorType method](nf-dbgeng-idebugcontrol3-seteffectiveprocessortype.md) | The SetEffectiveProcessorType method sets the effective processor type of the processor of the computer that is running the target. |
| [IDebugControl3::SetEngineOptions method](nf-dbgeng-idebugcontrol3-setengineoptions.md) | The SetEngineOptions method changes the engine's options. |
| [IDebugControl3::SetEventFilterCommand method](nf-dbgeng-idebugcontrol3-seteventfiltercommand.md) | The SetEventFilterCommand method sets a debugger command for the engine to execute when a specified event occurs. |
| [IDebugControl3::SetExceptionFilterParameters method](nf-dbgeng-idebugcontrol3-setexceptionfilterparameters.md) | The SetExceptionFilterParameters method changes the break status and handling status for some exception filters. |
| [IDebugControl3::SetExceptionFilterSecondCommand method](nf-dbgeng-idebugcontrol3-setexceptionfiltersecondcommand.md) | The SetExceptionFilterSecondCommand method sets the command that will be executed by the debugger engine on the second chance of a specified exception. |
| [IDebugControl3::SetExecutionStatus method](nf-dbgeng-idebugcontrol3-setexecutionstatus.md) | The SetExecutionStatus method requests that the debugger engine enter an executable state. Actual execution will not occur until the next time WaitForEvent is called. |
| [IDebugControl3::SetExpressionSyntax method](nf-dbgeng-idebugcontrol3-setexpressionsyntax.md) | The SetExpressionSyntax method sets the syntax that the engine will use to evaluate expressions. |
| [IDebugControl3::SetExpressionSyntaxByName method](nf-dbgeng-idebugcontrol3-setexpressionsyntaxbyname.md) | The SetExpressionSyntaxByName method sets the syntax that the engine will use to evaluate expressions. |
| [IDebugControl3::SetInterrupt method](nf-dbgeng-idebugcontrol3-setinterrupt.md) | The SetInterrupt method registers a user interrupt or breaks into the debugger. |
| [IDebugControl3::SetInterruptTimeout method](nf-dbgeng-idebugcontrol3-setinterrupttimeout.md) | The SetInterruptTimeout method sets the number of seconds that the debugger engine should wait when requesting a break into the debugger. |
| [IDebugControl3::SetLogMask method](nf-dbgeng-idebugcontrol3-setlogmask.md) | The SetLogMask method sets the output mask for the currently open log file. |
| [IDebugControl3::SetNextEventIndex method](nf-dbgeng-idebugcontrol3-setnexteventindex.md) | The SetNextEventIndex method sets the next event for the current target by selecting the event from the static list of events for the target, if such a list exists. |
| [IDebugControl3::SetNotifyEventHandle method](nf-dbgeng-idebugcontrol3-setnotifyeventhandle.md) | The SetNotifyEventHandle method sets the event that will be signaled after the next exception in a target. |
| [IDebugControl3::SetRadix method](nf-dbgeng-idebugcontrol3-setradix.md) | The SetRadix method sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [IDebugControl3::SetSpecificFilterArgument method](nf-dbgeng-idebugcontrol3-setspecificfilterargument.md) | The SetSpecificFilterArgument method sets the value of filter argument for the specific filters that can have an argument. |
| [IDebugControl3::SetSpecificFilterParameters method](nf-dbgeng-idebugcontrol3-setspecificfilterparameters.md) | The SetSpecificFilterParameters method changes the break status and handling status for some specific event filters. |
| [IDebugControl3::SetSystemErrorControl method](nf-dbgeng-idebugcontrol3-setsystemerrorcontrol.md) | The SetSystemErrorControl method sets the control values for handling system errors. |
| [IDebugControl3::SetTextMacro method](nf-dbgeng-idebugcontrol3-settextmacro.md) | The SetTextMacro method sets the value of a fixed-name alias. |
| [IDebugControl3::SetTextReplacement method](nf-dbgeng-idebugcontrol3-settextreplacement.md) | The SetTextReplacement method sets the value of a user-named alias. |
| [IDebugControl3::WaitForEvent method](nf-dbgeng-idebugcontrol3-waitforevent.md) | The WaitForEvent method waits for an event that breaks into the debugger engine application. |
| [IDebugControl4::AddBreakpoint2 method](nf-dbgeng-idebugcontrol4-addbreakpoint2.md) | The AddBreakpoint2 method creates a new breakpoint for the current target. |
| [IDebugControl4::AddExtensionWide method](nf-dbgeng-idebugcontrol4-addextensionwide.md) | The AddExtensionWide method loads an extension library into the debugger engine. |
| [IDebugControl4::AssembleWide method](nf-dbgeng-idebugcontrol4-assemblewide.md) | The AssembleWide method assembles a single processor instruction. The assembled instruction is placed in the target's memory. |
| [IDebugControl4::CallExtensionWide method](nf-dbgeng-idebugcontrol4-callextensionwide.md) | The CallExtensionWide method calls a debugger extension. |
| [IDebugControl4::ControlledOutputVaListWide method](nf-dbgeng-idebugcontrol4-controlledoutputvalistwide.md) | The ControlledOutputVaListWide method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugControl4::ControlledOutputWide method](nf-dbgeng-idebugcontrol4-controlledoutputwide.md) | The ControlledOutputWide method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [IDebugControl4::DisassembleWide method](nf-dbgeng-idebugcontrol4-disassemblewide.md) | The DisassembleWide method disassembles a processor instruction in the target's memory. |
| [IDebugControl4::EvaluateWide method](nf-dbgeng-idebugcontrol4-evaluatewide.md) | The EvaluateWide method evaluates an expression, returning the result. |
| [IDebugControl4::ExecuteCommandFileWide method](nf-dbgeng-idebugcontrol4-executecommandfilewide.md) | The ExecuteCommandFileWide method opens the specified file and executes the debugger commands that are contained within. |
| [IDebugControl4::ExecuteWide method](nf-dbgeng-idebugcontrol4-executewide.md) | The ExecuteWide method executes the specified debugger commands. |
| [IDebugControl4::GetBreakpointById2 method](nf-dbgeng-idebugcontrol4-getbreakpointbyid2.md) | The GetBreakpointById2 method returns the breakpoint with the specified breakpoint ID. |
| [IDebugControl4::GetBreakpointByIndex2 method](nf-dbgeng-idebugcontrol4-getbreakpointbyindex2.md) | The GetBreakpointByIndex2 method returns the breakpoint located at the specified index. |
| [IDebugControl4::GetContextStackTrace method](nf-dbgeng-idebugcontrol4-getcontextstacktrace.md) | The GetContextStackTrace method returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame. |
| [IDebugControl4::GetEventFilterCommandWide method](nf-dbgeng-idebugcontrol4-geteventfiltercommandwide.md) | The GetEventFilterCommandWide method returns the debugger command that the engine will execute when a specified event occurs. |
| [IDebugControl4::GetEventFilterTextWide method](nf-dbgeng-idebugcontrol4-geteventfiltertextwide.md) | The GetEventFilterTextWide method returns a short description of an event for a specific filter. |
| [IDebugControl4::GetEventIndexDescriptionWide method](nf-dbgeng-idebugcontrol4-geteventindexdescriptionwide.md) | The GetEventIndexDescriptionWide method describes the specified event in a static list of events for the current target. |
| [IDebugControl4::GetExceptionFilterSecondCommand method](nf-dbgeng-idebugcontrol4-getexceptionfiltersecondcommand.md) | The GetExceptionFilterSecondCommandWide method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [IDebugControl4::GetExpressionSyntaxNamesWide method](nf-dbgeng-idebugcontrol4-getexpressionsyntaxnameswide.md) | The GetExpressionSyntaxNamesWide method returns the full and abbreviated names of an expression syntax. |
| [IDebugControl4::GetExtensionByPathWide method](nf-dbgeng-idebugcontrol4-getextensionbypathwide.md) | The GetExtensionByPathWide method returns the handle for an already loaded extension library. |
| [IDebugControl4::GetExtensionFunctionWide method](nf-dbgeng-idebugcontrol4-getextensionfunctionwide.md) | The GetExtensionFunctionWide method returns a pointer to an extension function from an extension library. |
| [IDebugControl4::GetLastEventInformationWide method](nf-dbgeng-idebugcontrol4-getlasteventinformationwide.md) | The GetLastEventInformationWide method returns information about the last event that occurred in a target. |
| [IDebugControl4::GetLogFile2 method](nf-dbgeng-idebugcontrol4-getlogfile2.md) | The GetLogFile2 method returns the name of the currently open log file. |
| [IDebugControl4::GetLogFile2Wide method](nf-dbgeng-idebugcontrol4-getlogfile2wide.md) | The GetLogFile2Wide method returns the name of the currently open log file. |
| [IDebugControl4::GetLogFileWide method](nf-dbgeng-idebugcontrol4-getlogfilewide.md) | The GetLogFileWide method returns the name of the currently open log file. |
| [IDebugControl4::GetManagedStatus method](nf-dbgeng-idebugcontrol4-getmanagedstatus.md) | Provides feedback on the engine's use of the runtime debugging APIs provided by the common language runtime (CLR). |
| [IDebugControl4::GetManagedStatusWide method](nf-dbgeng-idebugcontrol4-getmanagedstatuswide.md) | Provides feedback as a Unicode character string on the engine's use of the runtime debugging APIs provided by the common language runtime (CLR). |
| [IDebugControl4::GetProcessorTypeNamesWide method](nf-dbgeng-idebugcontrol4-getprocessortypenameswide.md) | The GetProcessorTypeNamesWide method returns the full name and abbreviated name of the specified processor type. |
| [IDebugControl4::GetPromptTextWide method](nf-dbgeng-idebugcontrol4-getprompttextwide.md) | The GetPromptTextWide method returns the standard prompt text that will be prepended to the formatted output specified in the OutputPrompt and OutputPromptVaList methods. |
| [IDebugControl4::GetSpecificFilterArgumentWide method](nf-dbgeng-idebugcontrol4-getspecificfilterargumentwide.md) | The GetSpecificFilterArgumentWide method returns the value of filter argument for thespecific filters that have an argument. |
| [IDebugControl4::GetStoredEventInformation method](nf-dbgeng-idebugcontrol4-getstoredeventinformation.md) | The GetStoredEventInformation method retrieves information about an event of interest available in the current target. |
| [IDebugControl4::GetSystemVersionString method](nf-dbgeng-idebugcontrol4-getsystemversionstring.md) | The GetSystemVersionString method returns a string that describes the target's operating system version. |
| [IDebugControl4::GetSystemVersionStringWide method](nf-dbgeng-idebugcontrol4-getsystemversionstringwide.md) | The GetSystemVersionStringWide method returns a string that describes the target's operating system version. |
| [IDebugControl4::GetSystemVersionValues method](nf-dbgeng-idebugcontrol4-getsystemversionvalues.md) | The GetSystemVersionValues method returns version number information for the current target. |
| [IDebugControl4::GetTextMacroWide method](nf-dbgeng-idebugcontrol4-gettextmacrowide.md) | The GetTextMacroWide method returns the value of a fixed-name alias. |
| [IDebugControl4::GetTextReplacementWide method](nf-dbgeng-idebugcontrol4-gettextreplacementwide.md) | The GetTextReplacementWide method returns the value of a user-named alias or an automatic alias. |
| [IDebugControl4::InputWide method](nf-dbgeng-idebugcontrol4-inputwide.md) | The InputWide method requests an input string from the debugger engine. |
| [IDebugControl4::OpenLogFile2 method](nf-dbgeng-idebugcontrol4-openlogfile2.md) | The OpenLogFile2 method opens a log file that will receive output from the client objects. |
| [IDebugControl4::OpenLogFile2Wide method](nf-dbgeng-idebugcontrol4-openlogfile2wide.md) | The OpenLogFile2Wide method opens a log file that will receive output from the client objects. |
| [IDebugControl4::OpenLogFileWide method](nf-dbgeng-idebugcontrol4-openlogfilewide.md) | The OpenLogFileWide method opens a log file that will receive output from the client objects. |
| [IDebugControl4::OutputContextStackTrace method](nf-dbgeng-idebugcontrol4-outputcontextstacktrace.md) | The OutputContextStackTrace method prints the call stack specified by an array of stack frames and corresponding register contexts. |
| [IDebugControl4::OutputPromptVaListWide method](nf-dbgeng-idebugcontrol4-outputpromptvalistwide.md) | The OutputPromptVaListWide method formats and sends a user prompt to the output callback objects. |
| [IDebugControl4::OutputPromptWide method](nf-dbgeng-idebugcontrol4-outputpromptwide.md) | The OutputPromptWide method formats and sends a user prompt to the output callback objects. |
| [IDebugControl4::OutputVaListWide method](nf-dbgeng-idebugcontrol4-outputvalistwide.md) | The OutputVaListWide method formats a string and sends the result to the output callbacks that are registered with the engine's clients. |
| [IDebugControl4::OutputWide method](nf-dbgeng-idebugcontrol4-outputwide.md) | The OutputWide method formats a string and send the result to output callbacks that have been registered with the engine's clients. |
| [IDebugControl4::RemoveBreakpoint2 method](nf-dbgeng-idebugcontrol4-removebreakpoint2.md) | The RemoveBreakpoint2 method removes a breakpoint. |
| [IDebugControl4::ResetManagedStatus method](nf-dbgeng-idebugcontrol4-resetmanagedstatus.md) | Clears and reinitializes the engine's managed code debugging support of the runtime debugging APIs provided by the common language runtime (CLR). |
| [IDebugControl4::ReturnInputWide method](nf-dbgeng-idebugcontrol4-returninputwide.md) | The ReturnInputWide method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input. |
| [IDebugControl4::SetEventFilterCommandWide method](nf-dbgeng-idebugcontrol4-seteventfiltercommandwide.md) | The SetEventFilterCommandWide method sets a debugger command for the engine to execute when a specified event occurs. |
| [IDebugControl4::SetExceptionFilterSecondCommandWide method](nf-dbgeng-idebugcontrol4-setexceptionfiltersecondcommandwide.md) | The SetExceptionFilterSecondCommandWide method sets the command that will be executed by the debugger engine on the second chance of a specified exception. |
| [IDebugControl4::SetExpressionSyntaxByNameWide method](nf-dbgeng-idebugcontrol4-setexpressionsyntaxbynamewide.md) | The SetExpressionSyntaxByNameWide method sets the syntax that the engine will use to evaluate expressions. |
| [IDebugControl4::SetSpecificFilterArgumentWide method](nf-dbgeng-idebugcontrol4-setspecificfilterargumentwide.md) | The SetSpecificFilterArgumentWide method sets the value of filter argument for the specific filters that can have an argument. |
| [IDebugControl4::SetTextMacroWide method](nf-dbgeng-idebugcontrol4-settextmacrowide.md) | The SetTextMacroWide method sets the value of a fixed-name alias. |
| [IDebugControl4::SetTextReplacementWide method](nf-dbgeng-idebugcontrol4-settextreplacementwide.md) | The SetTextReplacementWide method sets the value of a user-named alias. |
| [IDebugControl5::GetBreakpointByGuid method](nf-dbgeng-idebugcontrol5-getbreakpointbyguid.md) | The GetBreakpointByGuid method returns the breakpoint with the specified breakpoint GUID. |
| [IDebugControl5::GetContextStackTraceEx method](nf-dbgeng-idebugcontrol5-getcontextstacktraceex.md) | The GetContextStackTraceEx method returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame. |
| [IDebugControl5::GetStackTraceEx method](nf-dbgeng-idebugcontrol5-getstacktraceex.md) | The GetStackTraceEx method returns the frames at the top of the specified call stack. The GetStackTraceEx method provides inline frame support. For more information about working with inline functions, see Debugging Optimized Code and Inline Functions. |
| [IDebugControl5::OutputContextStackTraceEx method](nf-dbgeng-idebugcontrol5-outputcontextstacktraceex.md) | The OutputContextStackTraceEx method prints the call stack specified by an array of stack frames and corresponding register contexts. |
| [IDebugControl5::OutputStackTraceEx method](nf-dbgeng-idebugcontrol5-outputstacktraceex.md) | The OutputStackTraceEx method outputs either the supplied stack frame or the current stack frames. |
| [IDebugControl6::GetExecutionStatusEx method](nf-dbgeng-idebugcontrol6-getexecutionstatusex.md) | The GetExecutionStatusEx method returns information about the execution status of the debugger engine. |
| [IDebugControl6::GetSynchronizationStatus method](nf-dbgeng-idebugcontrol6-getsynchronizationstatus.md) | The GetSynchronizationStatus method returns information about the synchronization status of the debugger engine. |
| [IDebugControl7::GetDebuggeeType2 method](nf-dbgeng-idebugcontrol7-getdebuggeetype2.md) | The GetDebuggeeType2 method describes the nature of the current target. |
| [IDebugControl::Input method](nf-dbgeng-idebugcontrol-input.md) | The Input method requests an input string from the debugger engine. |
| [IDebugDataSpaces2::QueryVirtual method](nf-dbgeng-idebugdataspaces2-queryvirtual.md) | The QueryVirtual method provides information about the specified pages in the target's virtual address space. |
| [IDebugDataSpaces4::CheckLowMemory method](nf-dbgeng-idebugdataspaces4-checklowmemory.md) | The CheckLowMemory method checks for memory corruption in the low 4 GB of memory. |
| [IDebugDataSpaces4::EndEnumTagged method](nf-dbgeng-idebugdataspaces4-endenumtagged.md) | The EndEnumTagged method releases the resources used by the specified enumeration. |
| [IDebugDataSpaces4::FillPhysical method](nf-dbgeng-idebugdataspaces4-fillphysical.md) | The FillPhysical method writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled. |
| [IDebugDataSpaces4::FillVirtual method](nf-dbgeng-idebugdataspaces4-fillvirtual.md) | The FillVirtual method writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled. |
| [IDebugDataSpaces4::GetNextDifferentlyValidOffsetVirtual method](nf-dbgeng-idebugdataspaces4-getnextdifferentlyvalidoffsetvirtual.md) | The GetNextDifferentlyValidOffsetVirtual method returns the offset of the next address whose validity might be different from the validity of the specified address. |
| [IDebugDataSpaces4::GetNextTagged method](nf-dbgeng-idebugdataspaces4-getnexttagged.md) | The GetNextTagged method returns the GUID for the next block of tagged data in the enumeration. |
| [IDebugDataSpaces4::GetOffsetInformation method](nf-dbgeng-idebugdataspaces4-getoffsetinformation.md) | The GetOffsetInformation method provides general information about an address in a process's data space. |
| [IDebugDataSpaces4::GetValidRegionVirtual method](nf-dbgeng-idebugdataspaces4-getvalidregionvirtual.md) | The GetValidRegionVirtual method locates the first valid region of memory in a specified memory range. |
| [IDebugDataSpaces4::GetVirtualTranslationPhysicalOffsets method](nf-dbgeng-idebugdataspaces4-getvirtualtranslationphysicaloffsets.md) | The GetVirtualTranslationPhysicalOffsets method returns the physical addresses of the system paging structures at different levels of the paging hierarchy. |
| [IDebugDataSpaces4::ReadBusData method](nf-dbgeng-idebugdataspaces4-readbusdata.md) | The ReadBusData method reads data from a system bus. |
| [IDebugDataSpaces4::ReadControl method](nf-dbgeng-idebugdataspaces4-readcontrol.md) | The ReadControl method reads implementation-specific system data. |
| [IDebugDataSpaces4::ReadDebuggerData method](nf-dbgeng-idebugdataspaces4-readdebuggerdata.md) | The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session. |
| [IDebugDataSpaces4::ReadHandleData method](nf-dbgeng-idebugdataspaces4-readhandledata.md) | The ReadHandleData method retrieves information about a system object specified by a system handle. |
| [IDebugDataSpaces4::ReadImageNtHeaders method](nf-dbgeng-idebugdataspaces4-readimagentheaders.md) | The ReadImageNtHeaders method returns the NT headers for the specified image loaded in the target. |
| [IDebugDataSpaces4::ReadIo method](nf-dbgeng-idebugdataspaces4-readio.md) | The ReadIo method reads from the system and bus I/O memory. |
| [IDebugDataSpaces4::ReadMsr method](nf-dbgeng-idebugdataspaces4-readmsr.md) | The ReadMsr method reads a specified Model-Specific Register (MSR). |
| [IDebugDataSpaces4::ReadMultiByteStringVirtual method](nf-dbgeng-idebugdataspaces4-readmultibytestringvirtual.md) | The ReadMultiByteStringVirtual method reads a null-terminated, multibyte string from the target. |
| [IDebugDataSpaces4::ReadMultiByteStringVirtualWide method](nf-dbgeng-idebugdataspaces4-readmultibytestringvirtualwide.md) | The ReadMultiByteStringVirtualWide method reads a null-terminated, multibyte string from the target and converts it to Unicode. |
| [IDebugDataSpaces4::ReadPhysical method](nf-dbgeng-idebugdataspaces4-readphysical.md) | The ReadPhysical method reads the target's memory from the specified physical address. |
| [IDebugDataSpaces4::ReadPhysical2 method](nf-dbgeng-idebugdataspaces4-readphysical2.md) | The ReadPhysical2 method reads the target's memory from the specified physical address. |
| [IDebugDataSpaces4::ReadPointersVirtual method](nf-dbgeng-idebugdataspaces4-readpointersvirtual.md) | The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space. |
| [IDebugDataSpaces4::ReadProcessorSystemData method](nf-dbgeng-idebugdataspaces4-readprocessorsystemdata.md) | The ReadProcessorSystemData method returns data about the specified processor. |
| [IDebugDataSpaces4::ReadTagged method](nf-dbgeng-idebugdataspaces4-readtagged.md) | The ReadTagged method reads the tagged data that might be associated with a debugger session. |
| [IDebugDataSpaces4::ReadUnicodeStringVirtual method](nf-dbgeng-idebugdataspaces4-readunicodestringvirtual.md) | The ReadUnicodeStringVirtual method reads a null-terminated, Unicode string from the target and converts it to a multibyte string. |
| [IDebugDataSpaces4::ReadUnicodeStringVirtualWide method](nf-dbgeng-idebugdataspaces4-readunicodestringvirtualwide.md) | The ReadUnicodeStringVirtualWide method reads a null-terminated, Unicode string from the target. |
| [IDebugDataSpaces4::ReadVirtual method](nf-dbgeng-idebugdataspaces4-readvirtual.md) | The ReadVirtual method reads memory from the target's virtual address space. |
| [IDebugDataSpaces4::ReadVirtualUncached method](nf-dbgeng-idebugdataspaces4-readvirtualuncached.md) | The ReadVirtualUncached method reads memory from the target's virtual address space. |
| [IDebugDataSpaces4::SearchVirtual method](nf-dbgeng-idebugdataspaces4-searchvirtual.md) | The SearchVirtual method searches the target's virtual memory for a specified pattern of bytes. |
| [IDebugDataSpaces4::SearchVirtual2 method](nf-dbgeng-idebugdataspaces4-searchvirtual2.md) | The SearchVirtual2 method searches the process's virtual memory for a specified pattern of bytes. |
| [IDebugDataSpaces4::StartEnumTagged method](nf-dbgeng-idebugdataspaces4-startenumtagged.md) | The StartEnumTagged method initializes a enumeration over the tagged data associated with a debugger session. |
| [IDebugDataSpaces4::VirtualToPhysical method](nf-dbgeng-idebugdataspaces4-virtualtophysical.md) | The VirtualToPhysical method translates a location in the target's virtual address space into a physical memory address. |
| [IDebugDataSpaces4::WriteBusData method](nf-dbgeng-idebugdataspaces4-writebusdata.md) | The WriteBusData method writes data to a system bus. |
| [IDebugDataSpaces4::WriteControl method](nf-dbgeng-idebugdataspaces4-writecontrol.md) | The WriteControl method writes implementation-specific system data. |
| [IDebugDataSpaces4::WriteIo method](nf-dbgeng-idebugdataspaces4-writeio.md) | The WriteIo method writes to the system and bus I/O memory. |
| [IDebugDataSpaces4::WriteMsr method](nf-dbgeng-idebugdataspaces4-writemsr.md) | The WriteMsr method writes a value to the specified Model-Specific Register (MSR). |
| [IDebugDataSpaces4::WritePhysical method](nf-dbgeng-idebugdataspaces4-writephysical.md) | The WritePhysical method writes data to the specified physical address in the target's memory. |
| [IDebugDataSpaces4::WritePhysical2 method](nf-dbgeng-idebugdataspaces4-writephysical2.md) | The WritePhysical2 method writes data to the specified physical address in the target's memory. |
| [IDebugDataSpaces4::WritePointersVirtual method](nf-dbgeng-idebugdataspaces4-writepointersvirtual.md) | The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space. |
| [IDebugDataSpaces4::WriteVirtual method](nf-dbgeng-idebugdataspaces4-writevirtual.md) | The WriteVirtual method writes data to the target's virtual address space. |
| [IDebugDataSpaces4::WriteVirtualUncached method](nf-dbgeng-idebugdataspaces4-writevirtualuncached.md) | The WriteVirtualUncached method writes data to the target's virtual address space. |
| [IDebugEventCallbacks::Breakpoint method](nf-dbgeng-idebugeventcallbacks-breakpoint.md) | The Breakpoint callback method is called by the engine when the target issues a breakpointexception. |
| [IDebugEventCallbacks::ChangeDebuggeeState method](nf-dbgeng-idebugeventcallbacks-changedebuggeestate.md) | The ChangeDebuggeeState callback method is called by the engine when it makes or detects changes to the target. |
| [IDebugEventCallbacks::ChangeEngineState method](nf-dbgeng-idebugeventcallbacks-changeenginestate.md) | The ChangeEngineState callback method is called by the engine when its state has changed. |
| [IDebugEventCallbacks::ChangeSymbolState method](nf-dbgeng-idebugeventcallbacks-changesymbolstate.md) | The ChangeSymbolState callback method is called by the engine when the symbol state changes. |
| [IDebugEventCallbacks::CreateProcess method](nf-dbgeng-idebugeventcallbacks-createprocess.md) | The CreateProcess callback method is called by the engine when a create-processdebugging event occurs in the target. |
| [IDebugEventCallbacks::CreateThread method](nf-dbgeng-idebugeventcallbacks-createthread.md) | The CreateThread callback method is called by the engine when a create-threaddebugging event occurs in the target. |
| [IDebugEventCallbacks::Exception method](nf-dbgeng-idebugeventcallbacks-exception.md) | The Exception callback method is called by the engine when an exceptiondebugging event occurs in the target. |
| [IDebugEventCallbacks::ExitProcess method](nf-dbgeng-idebugeventcallbacks-exitprocess.md) | The ExitProcess callback method is called by the engine when an exit-processdebugging event occurs in the target. |
| [IDebugEventCallbacks::ExitThread method](nf-dbgeng-idebugeventcallbacks-exitthread.md) | The ExitThread callback method is called by the engine when an exit-threaddebugging event occurs in the target. |
| [IDebugEventCallbacks::GetInterestMask method](nf-dbgeng-idebugeventcallbacks-getinterestmask.md) | The GetInterestMask callback method is called to determine which events the IDebugEventCallbacks object is interested in. The engine calls GetInterestMask when the object is registered with a client by using SetEventCallbacks. |
| [IDebugEventCallbacks::LoadModule method](nf-dbgeng-idebugeventcallbacks-loadmodule.md) | The LoadModule callback method is called by the engine when a module-load debugging event occurs in the target. |
| [IDebugEventCallbacks::SessionStatus method](nf-dbgeng-idebugeventcallbacks-sessionstatus.md) | The SessionStatus callback method is called by the engine when a change occurs in the debugger session. |
| [IDebugEventCallbacks::SystemError method](nf-dbgeng-idebugeventcallbacks-systemerror.md) | The SystemError callback method is called by the engine when a system error occurs in the target. |
| [IDebugEventCallbacks::UnloadModule method](nf-dbgeng-idebugeventcallbacks-unloadmodule.md) | The UnloadModule callback method is called by the engine when a module-unload debugging event occurs in the target. |
| [IDebugEventCallbacksWide::Breakpoint method](nf-dbgeng-idebugeventcallbackswide-breakpoint.md) | The Breakpoint callback method is called by the engine when the target issues a breakpointexception. |
| [IDebugEventCallbacksWide::ChangeDebuggeeState method](nf-dbgeng-idebugeventcallbackswide-changedebuggeestate.md) | The ChangeDebuggeeState callback method is called by the engine when it makes or detects changes to the target. |
| [IDebugEventCallbacksWide::ChangeEngineState method](nf-dbgeng-idebugeventcallbackswide-changeenginestate.md) | The ChangeEngineState callback method is called by the engine when its state has changed. |
| [IDebugEventCallbacksWide::ChangeSymbolState method](nf-dbgeng-idebugeventcallbackswide-changesymbolstate.md) | The ChangeSymbolState callback method is called by the engine when the symbol state changes. |
| [IDebugEventCallbacksWide::CreateProcess method](nf-dbgeng-idebugeventcallbackswide-createprocess.md) | The CreateProcess callback method is called by the engine when a create-processdebugging event occurs in the target. |
| [IDebugEventCallbacksWide::CreateThread method](nf-dbgeng-idebugeventcallbackswide-createthread.md) | The CreateThread callback method is called by the engine when a create-threaddebugging event occurs in the target. |
| [IDebugEventCallbacksWide::Exception method](nf-dbgeng-idebugeventcallbackswide-exception.md) | The Exception callback method is called by the engine when an exceptiondebugging event occurs in the target. |
| [IDebugEventCallbacksWide::ExitProcess method](nf-dbgeng-idebugeventcallbackswide-exitprocess.md) | The ExitProcess callback method is called by the engine when an exit-processdebugging event occurs in the target. |
| [IDebugEventCallbacksWide::ExitThread method](nf-dbgeng-idebugeventcallbackswide-exitthread.md) | The ExitThread callback method is called by the engine when an exit-threaddebugging event occurs in the target. |
| [IDebugEventCallbacksWide::GetInterestMask method](nf-dbgeng-idebugeventcallbackswide-getinterestmask.md) | The GetInterestMask callback method is called to determine which events the IDebugEventCallbacksWide object is interested in. The engine calls GetInterestMask when the object is registered with a client by using SetEventCallbacks. |
| [IDebugEventCallbacksWide::LoadModule method](nf-dbgeng-idebugeventcallbackswide-loadmodule.md) | The LoadModule callback method is called by the engine when a module-load debugging event occurs in the target. |
| [IDebugEventCallbacksWide::SessionStatus method](nf-dbgeng-idebugeventcallbackswide-sessionstatus.md) | The SessionStatus callback method is called by the engine when a change occurs in the debugger session. |
| [IDebugEventCallbacksWide::SystemError method](nf-dbgeng-idebugeventcallbackswide-systemerror.md) | The SystemError callback method is called by the engine when a system error occurs in the target. |
| [IDebugEventCallbacksWide::UnloadModule method](nf-dbgeng-idebugeventcallbackswide-unloadmodule.md) | The UnloadModule callback method is called by the engine when a module-unload debugging event occurs in the target. |
| [IDebugInputCallbacks::EndInput method](nf-dbgeng-idebuginputcallbacks-endinput.md) | The EndInput callback method is called by the engine to indicate that it is no longer waiting for input. |
| [IDebugInputCallbacks::StartInput method](nf-dbgeng-idebuginputcallbacks-startinput.md) | The StartInput callback method is called by the engine to indicate that it is waiting for a line of input. |
| [IDebugOutputCallbacks2::GetInterestMask method](nf-dbgeng-idebugoutputcallbacks2-getinterestmask.md) | Allows the callback object to describe which kinds of output notifications it wants to receive. |
| [IDebugOutputCallbacks2::Output method](nf-dbgeng-idebugoutputcallbacks2-output.md) | This method is not used. |
| [IDebugOutputCallbacks2::Output2 method](nf-dbgeng-idebugoutputcallbacks2-output2.md) | Returns notifications for the IDebugOutputCallbacks2 interface. |
| [IDebugOutputCallbacks::Output method](nf-dbgeng-idebugoutputcallbacks-output.md) | The Output callback method is called by the engine to send output from the client to the IDebugOutputCallbacks object that is registered with the client. |
| [IDebugOutputCallbacksWide::Output method](nf-dbgeng-idebugoutputcallbackswide-output.md) | The Output callback method is called by the engine to send output from the client to the IDebugOutputCallbacksWide object that is registered with the client. |
| [IDebugOutputStream::Write method](nf-dbgeng-idebugoutputstream-write.md) | Writes to the debug output stream. |
| [IDebugPlmClient2::LaunchPlmBgTaskForDebugWide method](nf-dbgeng-idebugplmclient2-launchplmbgtaskfordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) background task. |
| [IDebugPlmClient3::ActivateAndDebugPlmBgTaskWide method](nf-dbgeng-idebugplmclient3-activateanddebugplmbgtaskwide.md) | Launches and attaches to a Process Lifecycle Management (PLM) background task. |
| [IDebugPlmClient3::DisablePlmPackageDebugWide method](nf-dbgeng-idebugplmclient3-disableplmpackagedebugwide.md) | Disables a Process Lifecycle Management (PLM) package debug. |
| [IDebugPlmClient3::EnablePlmPackageDebugWide method](nf-dbgeng-idebugplmclient3-enableplmpackagedebugwide.md) | Enables a Process Lifecycle Management (PLM) package debug. |
| [IDebugPlmClient3::LaunchAndDebugPlmAppWide method](nf-dbgeng-idebugplmclient3-launchanddebugplmappwide.md) | Launches and attaches to a Process Lifecycle Management (PLM) application. |
| [IDebugPlmClient3::QueryPlmPackageList method](nf-dbgeng-idebugplmclient3-queryplmpackagelist.md) | Query a Process Lifecycle Management (PLM) package list. |
| [IDebugPlmClient3::QueryPlmPackageWide method](nf-dbgeng-idebugplmclient3-queryplmpackagewide.md) | Query a Process Lifecycle Management (PLM) package. |
| [IDebugPlmClient3::ResumePlmPackageWide method](nf-dbgeng-idebugplmclient3-resumeplmpackagewide.md) | Resumes a Process Lifecycle Management (PLM) package. |
| [IDebugPlmClient3::SuspendPlmPackageWide method](nf-dbgeng-idebugplmclient3-suspendplmpackagewide.md) | Suspends a Process Lifecycle Management (PLM) package. |
| [IDebugPlmClient3::TerminatePlmPackageWide method](nf-dbgeng-idebugplmclient3-terminateplmpackagewide.md) | Ends a Process Lifecycle Management (PLM) package. |
| [IDebugPlmClient::LaunchPlmPackageForDebugWide method](nf-dbgeng-idebugplmclient-launchplmpackagefordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) application. |
| [IDebugRegisters2::GetDescription method](nf-dbgeng-idebugregisters2-getdescription.md) | The GetDescription method returns the description of a register. |
| [IDebugRegisters2::GetDescriptionWide method](nf-dbgeng-idebugregisters2-getdescriptionwide.md) | The GetDescriptionWide method returns the description of a register. |
| [IDebugRegisters2::GetFrameOffset method](nf-dbgeng-idebugregisters2-getframeoffset.md) | The GetFrameOffset method returns the location of the stack frame for the current function. |
| [IDebugRegisters2::GetFrameOffset2 method](nf-dbgeng-idebugregisters2-getframeoffset2.md) | The GetFrameOffset2 method returns the location of the stack frame for the current function. |
| [IDebugRegisters2::GetIndexByName method](nf-dbgeng-idebugregisters2-getindexbyname.md) | The GetIndexByName method returns the index of the named register. |
| [IDebugRegisters2::GetIndexByNameWide method](nf-dbgeng-idebugregisters2-getindexbynamewide.md) | The GetIndexByNameWide method returns the index of the named register. |
| [IDebugRegisters2::GetInstructionOffset method](nf-dbgeng-idebugregisters2-getinstructionoffset.md) | The GetInstructionOffset method returns the location of the current thread's current instruction. |
| [IDebugRegisters2::GetInstructionOffset2 method](nf-dbgeng-idebugregisters2-getinstructionoffset2.md) | The GetInstructionOffset2 method returns the location of the current thread's current instruction. |
| [IDebugRegisters2::GetNumberPseudoRegisters method](nf-dbgeng-idebugregisters2-getnumberpseudoregisters.md) | The GetNumberPseudoRegisters method returns the number of pseudo-registers that are maintained by the debugger engine. |
| [IDebugRegisters2::GetNumberRegisters method](nf-dbgeng-idebugregisters2-getnumberregisters.md) | The GetNumberRegisters method returns the number of registers on the target computer. |
| [IDebugRegisters2::GetPseudoDescription method](nf-dbgeng-idebugregisters2-getpseudodescription.md) | The GetPseudoDescription method returns a description of a pseudo-register, including its name and type. |
| [IDebugRegisters2::GetPseudoDescriptionWide method](nf-dbgeng-idebugregisters2-getpseudodescriptionwide.md) | The GetPseudoDescriptionWide method returns a description of a pseudo-register, including its name and type. |
| [IDebugRegisters2::GetPseudoIndexByName method](nf-dbgeng-idebugregisters2-getpseudoindexbyname.md) | The GetPseudoIndexByName method returns the index of a pseudo-register. |
| [IDebugRegisters2::GetPseudoIndexByNameWide method](nf-dbgeng-idebugregisters2-getpseudoindexbynamewide.md) | The GetPseudoIndexByNameWide method returns the index of a pseudo-register. |
| [IDebugRegisters2::GetPseudoValues method](nf-dbgeng-idebugregisters2-getpseudovalues.md) | The GetPseudoValues method returns the values of a number of pseudo-registers. |
| [IDebugRegisters2::GetStackOffset method](nf-dbgeng-idebugregisters2-getstackoffset.md) | The GetStackOffset method returns the current thread's current stack location. |
| [IDebugRegisters2::GetStackOffset2 method](nf-dbgeng-idebugregisters2-getstackoffset2.md) | The GetStackOffset2 method returns the current thread's current stack location. |
| [IDebugRegisters2::GetValue method](nf-dbgeng-idebugregisters2-getvalue.md) | The GetValue method gets the value of one of the target's registers. |
| [IDebugRegisters2::GetValues method](nf-dbgeng-idebugregisters2-getvalues.md) | The GetValues method gets the value of several of the target's registers. |
| [IDebugRegisters2::GetValues2 method](nf-dbgeng-idebugregisters2-getvalues2.md) | The GetValues2 method fetches the value of several of the target's registers. |
| [IDebugRegisters2::OutputRegisters method](nf-dbgeng-idebugregisters2-outputregisters.md) | The OutputRegisters method formats and sends the target's registers to the clients as output. |
| [IDebugRegisters2::OutputRegisters2 method](nf-dbgeng-idebugregisters2-outputregisters2.md) | The OutputRegisters2 method formats and outputs the target's registers. |
| [IDebugRegisters2::SetPseudoValues method](nf-dbgeng-idebugregisters2-setpseudovalues.md) | The SetPseudoValues method sets the value of several pseudo-registers. |
| [IDebugRegisters2::SetValue method](nf-dbgeng-idebugregisters2-setvalue.md) | The SetValue method sets the value of one of the target's registers. |
| [IDebugRegisters2::SetValues method](nf-dbgeng-idebugregisters2-setvalues.md) | The SetValues method sets the value of several of the target's registers. |
| [IDebugRegisters2::SetValues2 method](nf-dbgeng-idebugregisters2-setvalues2.md) | The SetValues2 method sets the value of several of the target's registers. |
| [IDebugSymbolGroup2::AddSymbol method](nf-dbgeng-idebugsymbolgroup2-addsymbol.md) | The AddSymbol method adds a symbol to a symbol group. |
| [IDebugSymbolGroup2::AddSymbolWide method](nf-dbgeng-idebugsymbolgroup2-addsymbolwide.md) | The AddSymbolWide method adds a symbol to a symbol group. |
| [IDebugSymbolGroup2::ExpandSymbol method](nf-dbgeng-idebugsymbolgroup2-expandsymbol.md) | The ExpandSymbol method adds or removes the children of a symbol from a symbol group. |
| [IDebugSymbolGroup2::GetNumberSymbols method](nf-dbgeng-idebugsymbolgroup2-getnumbersymbols.md) | The GetNumberSymbols method returns the number of symbols that are contained in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolEntryInformation method](nf-dbgeng-idebugsymbolgroup2-getsymbolentryinformation.md) | The GetSymbolEntryInformation method returns information about a symbol in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolName method](nf-dbgeng-idebugsymbolgroup2-getsymbolname.md) | The GetSymbolName method returns the name of a symbol in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolNameWide method](nf-dbgeng-idebugsymbolgroup2-getsymbolnamewide.md) | The GetSymbolNameWide method returns the name of a symbol in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolOffset method](nf-dbgeng-idebugsymbolgroup2-getsymboloffset.md) | The GetSymbolOffset method retrieves the location in the process's virtual address space of a symbol in a symbol group, if the symbol has an absolute address. |
| [IDebugSymbolGroup2::GetSymbolParameters method](nf-dbgeng-idebugsymbolgroup2-getsymbolparameters.md) | The GetSymbolParameters method returns the symbol parameters that describe the specified symbols in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolRegister method](nf-dbgeng-idebugsymbolgroup2-getsymbolregister.md) | The GetSymbolRegister method returns the register that contains the value or a pointer to the value of a symbol in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolSize method](nf-dbgeng-idebugsymbolgroup2-getsymbolsize.md) | The GetSymbolSize method returns the size of a symbol's value. |
| [IDebugSymbolGroup2::GetSymbolTypeName method](nf-dbgeng-idebugsymbolgroup2-getsymboltypename.md) | The GetSymbolTypeName methods return the name of the specified symbol's type. |
| [IDebugSymbolGroup2::GetSymbolTypeNameWide method](nf-dbgeng-idebugsymbolgroup2-getsymboltypenamewide.md) | The GetSymbolTypeNameWide method returns the name of the specified symbol's type. |
| [IDebugSymbolGroup2::GetSymbolValueText method](nf-dbgeng-idebugsymbolgroup2-getsymbolvaluetext.md) | The GetSymbolValueText method returns a string that represents the value of a symbol. |
| [IDebugSymbolGroup2::GetSymbolValueTextWide method](nf-dbgeng-idebugsymbolgroup2-getsymbolvaluetextwide.md) | The GetSymbolValueTextWide method returns a string that represents the value of a symbol. |
| [IDebugSymbolGroup2::OutputAsType method](nf-dbgeng-idebugsymbolgroup2-outputastype.md) | The OutputAsType method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. |
| [IDebugSymbolGroup2::OutputAsTypeWide method](nf-dbgeng-idebugsymbolgroup2-outputastypewide.md) | The OutputAsTypeWide method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. |
| [IDebugSymbolGroup2::OutputSymbols method](nf-dbgeng-idebugsymbolgroup2-outputsymbols.md) | The OutputSymbols method prints the specified symbols to the debugger console. |
| [IDebugSymbolGroup2::RemoveSymbolByIndex method](nf-dbgeng-idebugsymbolgroup2-removesymbolbyindex.md) | The RemoveSymbolByIndex method removes the specified symbol from a symbol group. |
| [IDebugSymbolGroup2::RemoveSymbolByName method](nf-dbgeng-idebugsymbolgroup2-removesymbolbyname.md) | The RemoveSymbolByName method removes the specified symbol from a symbol group. |
| [IDebugSymbolGroup2::RemoveSymbolByNameWide method](nf-dbgeng-idebugsymbolgroup2-removesymbolbynamewide.md) | The RemoveSymbolByNameWide method removes the specified symbol from a symbol group. |
| [IDebugSymbolGroup2::WriteSymbol method](nf-dbgeng-idebugsymbolgroup2-writesymbol.md) | The WriteSymbol methods set the value of the specified symbol. |
| [IDebugSymbolGroup2::WriteSymbolWide method](nf-dbgeng-idebugsymbolgroup2-writesymbolwide.md) | The WriteSymbolWide method sets the value of the specified symbol. |
| [IDebugSymbols3::AddSymbolOptions method](nf-dbgeng-idebugsymbols3-addsymboloptions.md) | The AddSymbolOptions method turns on some of the engine's global symbol options. |
| [IDebugSymbols3::AddSyntheticModule method](nf-dbgeng-idebugsymbols3-addsyntheticmodule.md) | The AddSyntheticModule method adds a synthetic module to the module list the debugger maintains for the current process. |
| [IDebugSymbols3::AddSyntheticModuleWide method](nf-dbgeng-idebugsymbols3-addsyntheticmodulewide.md) | The AddSyntheticModuleWide method adds a synthetic module to the module list the debugger maintains for the current process. |
| [IDebugSymbols3::AddSyntheticSymbol method](nf-dbgeng-idebugsymbols3-addsyntheticsymbol.md) | The AddSyntheticSymbol method adds a synthetic symbol to a module in the current process. |
| [IDebugSymbols3::AddSyntheticSymbolWide method](nf-dbgeng-idebugsymbols3-addsyntheticsymbolwide.md) | The AddSyntheticSymbolWide method adds a synthetic symbol to a module in the current process. |
| [IDebugSymbols3::AddTypeOptions method](nf-dbgeng-idebugsymbols3-addtypeoptions.md) | The AddTypeOptions method turns on some type formatting options for output generated by the engine. |
| [IDebugSymbols3::AppendImagePath method](nf-dbgeng-idebugsymbols3-appendimagepath.md) | The AppendImagePath method appends directories to the executable image path. |
| [IDebugSymbols3::AppendImagePathWide method](nf-dbgeng-idebugsymbols3-appendimagepathwide.md) | The AppendImagePathWide method appends directories to the executable image path. |
| [IDebugSymbols3::AppendSourcePath method](nf-dbgeng-idebugsymbols3-appendsourcepath.md) | The AppendSourcePath method appends directories to the source path. |
| [IDebugSymbols3::AppendSourcePathWide method](nf-dbgeng-idebugsymbols3-appendsourcepathwide.md) | The AppendSourcePathWide method appends directories to the source path. |
| [IDebugSymbols3::AppendSymbolPath method](nf-dbgeng-idebugsymbols3-appendsymbolpath.md) | The AppendSymbolPath method appends directories to the symbol path. |
| [IDebugSymbols3::AppendSymbolPathWide method](nf-dbgeng-idebugsymbols3-appendsymbolpathwide.md) | The AppendSymbolPathWide method appends directories to the symbol path. |
| [IDebugSymbols3::CreateSymbolGroup method](nf-dbgeng-idebugsymbols3-createsymbolgroup.md) | The CreateSymbolGroup method creates a new symbol group. |
| [IDebugSymbols3::CreateSymbolGroup2 method](nf-dbgeng-idebugsymbols3-createsymbolgroup2.md) | The CreateSymbolGroup2 method creates a new symbol group. |
| [IDebugSymbols3::EndSymbolMatch method](nf-dbgeng-idebugsymbols3-endsymbolmatch.md) | The EndSymbolMatch method releases the resources used by a symbol search. |
| [IDebugSymbols3::FindSourceFile method](nf-dbgeng-idebugsymbols3-findsourcefile.md) | The FindSourceFile method searches the source path for a specified source file. |
| [IDebugSymbols3::FindSourceFileWide method](nf-dbgeng-idebugsymbols3-findsourcefilewide.md) | The FindSourceFileWide method searches the source path for a specified source file. |
| [IDebugSymbols3::GetConstantName method](nf-dbgeng-idebugsymbols3-getconstantname.md) | The GetConstantName method returns the name of the specified constant. |
| [IDebugSymbols3::GetConstantNameWide method](nf-dbgeng-idebugsymbols3-getconstantnamewide.md) | The GetConstantNameWide method returns the name of the specified constant. |
| [IDebugSymbols3::GetCurrentScopeFrameIndex method](nf-dbgeng-idebugsymbols3-getcurrentscopeframeindex.md) | The GetCurrentScopeFrameIndex method returns the index of the current stack frame in the call stack. |
| [IDebugSymbols3::GetFieldName method](nf-dbgeng-idebugsymbols3-getfieldname.md) | The GetFieldName method returns the name of a field within a structure. |
| [IDebugSymbols3::GetFieldNameWide method](nf-dbgeng-idebugsymbols3-getfieldnamewide.md) | The GetFieldNameWide method returns the name of a field within a structure. |
| [IDebugSymbols3::GetFieldOffset method](nf-dbgeng-idebugsymbols3-getfieldoffset.md) | The GetFieldOffset method returns the offset of a field from the base address of an instance of a type. |
| [IDebugSymbols3::GetFieldOffsetWide method](nf-dbgeng-idebugsymbols3-getfieldoffsetwide.md) | The GetFieldOffsetWide method returns the offset of a field from the base address of an instance of a type. |
| [IDebugSymbols3::GetFieldTypeAndOffset method](nf-dbgeng-idebugsymbols3-getfieldtypeandoffset.md) | The GetFieldTypeAndOffset method returns the type of a field and its offset within a container. |
| [IDebugSymbols3::GetFieldTypeAndOffsetWide method](nf-dbgeng-idebugsymbols3-getfieldtypeandoffsetwide.md) | The GetFieldTypeAndOffsetWide method returns the type of a field and its offset within a container. |
| [IDebugSymbols3::GetFunctionEntryByOffset method](nf-dbgeng-idebugsymbols3-getfunctionentrybyoffset.md) | The GetFunctionEntryByOffset method returns the function entry information for a function. |
| [IDebugSymbols3::GetImagePath method](nf-dbgeng-idebugsymbols3-getimagepath.md) | The GetImagePath method returns the executable image path. |
| [IDebugSymbols3::GetImagePathWide method](nf-dbgeng-idebugsymbols3-getimagepathwide.md) | The GetImagePathWide method returns the executable image path. |
| [IDebugSymbols3::GetLineByOffset method](nf-dbgeng-idebugsymbols3-getlinebyoffset.md) | The GetLineByOffset method returns the source filename and the line number within the source file of an instruction in the target. |
| [IDebugSymbols3::GetLineByOffsetWide method](nf-dbgeng-idebugsymbols3-getlinebyoffsetwide.md) | The GetLineByOffsetWide method returns the source filename and the line number within the source file of an instruction in the target. |
| [IDebugSymbols3::GetModuleByIndex method](nf-dbgeng-idebugsymbols3-getmodulebyindex.md) | The GetModuleByIndex method returns the location of the module with the specified index. |
| [IDebugSymbols3::GetModuleByModuleName method](nf-dbgeng-idebugsymbols3-getmodulebymodulename.md) | The GetModuleByModuleName method searches through the target's modules for one with the specified name. |
| [IDebugSymbols3::GetModuleByModuleName2 method](nf-dbgeng-idebugsymbols3-getmodulebymodulename2.md) | The GetModuleByModuleName2 method searches through the process's modules for one with the specified name. |
| [IDebugSymbols3::GetModuleByModuleName2Wide method](nf-dbgeng-idebugsymbols3-getmodulebymodulename2wide.md) | The GetModuleByModuleName2Wide method searches through the process's modules for one with the specified name. |
| [IDebugSymbols3::GetModuleByModuleNameWide method](nf-dbgeng-idebugsymbols3-getmodulebymodulenamewide.md) | The GetModuleByModuleNameWide method searches through the target's modules for one with the specified name. |
| [IDebugSymbols3::GetModuleByOffset method](nf-dbgeng-idebugsymbols3-getmodulebyoffset.md) | The GetModuleByOffset method searches through the target's modules for one whose memory allocation includes the specified location. |
| [IDebugSymbols3::GetModuleByOffset2 method](nf-dbgeng-idebugsymbols3-getmodulebyoffset2.md) | The GetModuleByOffset2 method searches through the process's modules for one whose memory allocation includes the specified location. |
| [IDebugSymbols3::GetModuleNameString method](nf-dbgeng-idebugsymbols3-getmodulenamestring.md) | The GetModuleNameString method returns the name of the specified module. |
| [IDebugSymbols3::GetModuleNameStringWide method](nf-dbgeng-idebugsymbols3-getmodulenamestringwide.md) | The GetModuleNameStringWide method returns the name of the specified module. |
| [IDebugSymbols3::GetModuleNames method](nf-dbgeng-idebugsymbols3-getmodulenames.md) | The GetModuleNames method returns the names of the specified module. |
| [IDebugSymbols3::GetModuleParameters method](nf-dbgeng-idebugsymbols3-getmoduleparameters.md) | The GetModuleParameters method returns parameters for modules in the target. |
| [IDebugSymbols3::GetModuleVersionInformation method](nf-dbgeng-idebugsymbols3-getmoduleversioninformation.md) | The GetModuleVersionInformation method returns version information for the specified module. |
| [IDebugSymbols3::GetModuleVersionInformationWide method](nf-dbgeng-idebugsymbols3-getmoduleversioninformationwide.md) | The GetModuleVersionInformationWide method returns version information for the specified module. |
| [IDebugSymbols3::GetNameByOffset method](nf-dbgeng-idebugsymbols3-getnamebyoffset.md) | The GetNameByOffset method returns the name of the symbol at the specified location in the target's virtual address space. |
| [IDebugSymbols3::GetNameByOffsetWide method](nf-dbgeng-idebugsymbols3-getnamebyoffsetwide.md) | The GetNameByOffsetWide method returns the name of the symbol at the specified location in the target's virtual address space. |
| [IDebugSymbols3::GetNearNameByOffset method](nf-dbgeng-idebugsymbols3-getnearnamebyoffset.md) | The GetNearNameByOffset method returns the name of a symbol that is located near the specified location. |
| [IDebugSymbols3::GetNearNameByOffsetWide method](nf-dbgeng-idebugsymbols3-getnearnamebyoffsetwide.md) | The GetNearNameByOffsetWide method returns the name of a symbol that is located near the specified location. |
| [IDebugSymbols3::GetNextSymbolMatch method](nf-dbgeng-idebugsymbols3-getnextsymbolmatch.md) | The GetNextSymbolMatch method returns the next symbol found in a symbol search. |
| [IDebugSymbols3::GetNextSymbolMatchWide method](nf-dbgeng-idebugsymbols3-getnextsymbolmatchwide.md) | The GetNextSymbolMatchWide method returns the next symbol found in a symbol search. |
| [IDebugSymbols3::GetNumberModules method](nf-dbgeng-idebugsymbols3-getnumbermodules.md) | The GetNumberModules method returns the number of modules in the current process's module list. |
| [IDebugSymbols3::GetOffsetByLine method](nf-dbgeng-idebugsymbols3-getoffsetbyline.md) | The GetOffsetByLine method returns the location of the instruction that corresponds to a specified line in the source code. |
| [IDebugSymbols3::GetOffsetByLineWide method](nf-dbgeng-idebugsymbols3-getoffsetbylinewide.md) | The GetOffsetByLineWide method returns the location of the instruction that corresponds to a specified line in the source code. |
| [IDebugSymbols3::GetOffsetByName method](nf-dbgeng-idebugsymbols3-getoffsetbyname.md) | The GetOffsetByName method returns the location of a symbol identified by name. |
| [IDebugSymbols3::GetOffsetByNameWide method](nf-dbgeng-idebugsymbols3-getoffsetbynamewide.md) | The GetOffsetByNameWide method returns the location of a symbol identified by name. |
| [IDebugSymbols3::GetOffsetTypeId method](nf-dbgeng-idebugsymbols3-getoffsettypeid.md) | The GetOffsetTypeId method returns the type ID of the symbol closest to the specified memory location. |
| [IDebugSymbols3::GetScope method](nf-dbgeng-idebugsymbols3-getscope.md) | The GetScope method returns information about the current scope. |
| [IDebugSymbols3::GetScopeSymbolGroup method](nf-dbgeng-idebugsymbols3-getscopesymbolgroup.md) | The GetScopeSymbolGroup method returns a symbol group containing the symbols in the current target's scope. |
| [IDebugSymbols3::GetScopeSymbolGroup2 method](nf-dbgeng-idebugsymbols3-getscopesymbolgroup2.md) | The GetScopeSymbolGroup2 method returns a symbol group containing the symbols in the current target's scope. |
| [IDebugSymbols3::GetSourceEntriesByLine method](nf-dbgeng-idebugsymbols3-getsourceentriesbyline.md) | The GetSourceEntriesByLine method queries symbol information and returns locations in the target's memory that correspond to lines in a source file. |
| [IDebugSymbols3::GetSourceEntriesByLineWide method](nf-dbgeng-idebugsymbols3-getsourceentriesbylinewide.md) | The GetSourceEntriesByLineWide method queries symbol information and returns locations in the target's memory that correspond to lines in a source file. |
| [IDebugSymbols3::GetSourceEntriesByOffset method](nf-dbgeng-idebugsymbols3-getsourceentriesbyoffset.md) | Queries symbol information and returns locations in the target's memory by using an offset. |
| [IDebugSymbols3::GetSourceEntryBySourceEntry method](nf-dbgeng-idebugsymbols3-getsourceentrybysourceentry.md) | Allows navigation within the source entries. |
| [IDebugSymbols3::GetSourceEntryOffsetRegions method](nf-dbgeng-idebugsymbols3-getsourceentryoffsetregions.md) | Returns all memory regions known to be associated with a source entry. |
| [IDebugSymbols3::GetSourceEntryString method](nf-dbgeng-idebugsymbols3-getsourceentrystring.md) | Queries symbol information and returns locations in the target's memory. |
| [IDebugSymbols3::GetSourceEntryStringWide method](nf-dbgeng-idebugsymbols3-getsourceentrystringwide.md) | Queries symbol information and returns locations in the target's memory. |
| [IDebugSymbols3::GetSourceFileLineOffsets method](nf-dbgeng-idebugsymbols3-getsourcefilelineoffsets.md) | The GetSourceFileLineOffsets method maps each line in a source file to a location in the target's memory. |
| [IDebugSymbols3::GetSourceFileLineOffsetsWide method](nf-dbgeng-idebugsymbols3-getsourcefilelineoffsetswide.md) | The GetSourceFileLineOffsetsWide method maps each line in a source file to a location in the target's memory. |
| [IDebugSymbols3::GetSourcePath method](nf-dbgeng-idebugsymbols3-getsourcepath.md) | The GetSourcePath method returns the source path. |
| [IDebugSymbols3::GetSourcePathElement method](nf-dbgeng-idebugsymbols3-getsourcepathelement.md) | The GetSourcePathElement method returns an element from the source path. |
| [IDebugSymbols3::GetSourcePathElementWide method](nf-dbgeng-idebugsymbols3-getsourcepathelementwide.md) | The GetSourcePathElementWide method returns an element from the source path. |
| [IDebugSymbols3::GetSourcePathWide method](nf-dbgeng-idebugsymbols3-getsourcepathwide.md) | The GetSourcePathWide method returns the source path. |
| [IDebugSymbols3::GetSymbolEntriesByName method](nf-dbgeng-idebugsymbols3-getsymbolentriesbyname.md) | The GetSymbolEntriesByName method returns the symbols whose names match a given pattern. |
| [IDebugSymbols3::GetSymbolEntriesByNameWide method](nf-dbgeng-idebugsymbols3-getsymbolentriesbynamewide.md) | The GetSymbolEntriesByNameWide method returns the symbols whose names match a given pattern. |
| [IDebugSymbols3::GetSymbolEntriesByOffset method](nf-dbgeng-idebugsymbols3-getsymbolentriesbyoffset.md) | The GetSymbolEntriesByOffset method returns the symbols which are located at a specified address. |
| [IDebugSymbols3::GetSymbolEntryBySymbolEntry method](nf-dbgeng-idebugsymbols3-getsymbolentrybysymbolentry.md) | Allows navigation within the symbol entry hierarchy. |
| [IDebugSymbols3::GetSymbolEntryByToken method](nf-dbgeng-idebugsymbols3-getsymbolentrybytoken.md) | Looks up a symbol by using a managed metadata token. |
| [IDebugSymbols3::GetSymbolEntryInformation method](nf-dbgeng-idebugsymbols3-getsymbolentryinformation.md) | The GetSymbolEntryInformation method returns the symbol entry information for a symbol. |
| [IDebugSymbols3::GetSymbolEntryOffsetRegions method](nf-dbgeng-idebugsymbols3-getsymbolentryoffsetregions.md) | Returns all the memory regions known to be associated with a symbol. |
| [IDebugSymbols3::GetSymbolEntryString method](nf-dbgeng-idebugsymbols3-getsymbolentrystring.md) | The GetSymbolEntryString method returns string information for the specified symbol. |
| [IDebugSymbols3::GetSymbolEntryStringWide method](nf-dbgeng-idebugsymbols3-getsymbolentrystringwide.md) | The GetSymbolEntryStringWide method returns string information for the specified symbol. |
| [IDebugSymbols3::GetSymbolModule method](nf-dbgeng-idebugsymbols3-getsymbolmodule.md) | The GetSymbolModule method returns the base address of module which contains the specified symbol. |
| [IDebugSymbols3::GetSymbolModuleWide method](nf-dbgeng-idebugsymbols3-getsymbolmodulewide.md) | The GetSymbolModuleWide method returns the base address of module which contains the specified symbol. |
| [IDebugSymbols3::GetSymbolOptions method](nf-dbgeng-idebugsymbols3-getsymboloptions.md) | The GetSymbolOptions method returns the engine's global symbol options. |
| [IDebugSymbols3::GetSymbolPath method](nf-dbgeng-idebugsymbols3-getsymbolpath.md) | The GetSymbolPath method returns the symbol path. |
| [IDebugSymbols3::GetSymbolPathWide method](nf-dbgeng-idebugsymbols3-getsymbolpathwide.md) | The GetSymbolPathWide method returns the symbol path. |
| [IDebugSymbols3::GetSymbolTypeId method](nf-dbgeng-idebugsymbols3-getsymboltypeid.md) | The GetSymbolTypeId method returns the type ID and module of the specified symbol. |
| [IDebugSymbols3::GetSymbolTypeIdWide method](nf-dbgeng-idebugsymbols3-getsymboltypeidwide.md) | The GetSymbolTypeIdWide method returns the type ID and module of the specified symbol. |
| [IDebugSymbols3::GetTypeId method](nf-dbgeng-idebugsymbols3-gettypeid.md) | The GetTypeId method looks up the specified type and return its type ID. |
| [IDebugSymbols3::GetTypeIdWide method](nf-dbgeng-idebugsymbols3-gettypeidwide.md) | The GetTypeIdWide method looks up the specified type and return its type ID. |
| [IDebugSymbols3::GetTypeName method](nf-dbgeng-idebugsymbols3-gettypename.md) | The GetTypeName method returns the name of the type symbol specified by its type ID and module. |
| [IDebugSymbols3::GetTypeNameWide method](nf-dbgeng-idebugsymbols3-gettypenamewide.md) | The GetTypeNameWide method returns the name of the type symbol specified by its type ID and module. |
| [IDebugSymbols3::GetTypeOptions method](nf-dbgeng-idebugsymbols3-gettypeoptions.md) | The GetTypeOptions method returns the type formatting options for output generated by the engine. |
| [IDebugSymbols3::GetTypeSize method](nf-dbgeng-idebugsymbols3-gettypesize.md) | The GetTypeSize method returns the number of bytes of memory an instance of the specified type requires. |
| [IDebugSymbols3::IsManagedModule method](nf-dbgeng-idebugsymbols3-ismanagedmodule.md) | Checks whether the engine is using managed debugging support when it retrieves information for a module. |
| [IDebugSymbols3::OutputSymbolByOffset method](nf-dbgeng-idebugsymbols3-outputsymbolbyoffset.md) | The OutputSymbolByOffset method looks up a symbol by address and prints the symbol name and other symbol information to the debugger console. |
| [IDebugSymbols3::OutputTypedDataPhysical method](nf-dbgeng-idebugsymbols3-outputtypeddataphysical.md) | The OutputTypedDataPhysical method formats the contents of a variable in the target computer's physical memory, and then sends this to the output callbacks. |
| [IDebugSymbols3::OutputTypedDataVirtual method](nf-dbgeng-idebugsymbols3-outputtypeddatavirtual.md) | The OutputTypedDataVirtual method formats the contents of a variable in the target's virtual memory, and then sends this to the output callbacks. |
| [IDebugSymbols3::ReadTypedDataPhysical method](nf-dbgeng-idebugsymbols3-readtypeddataphysical.md) | The ReadTypedDataPhysical method reads the value of a variable from the target computer's physical memory. |
| [IDebugSymbols3::ReadTypedDataVirtual method](nf-dbgeng-idebugsymbols3-readtypeddatavirtual.md) | The ReadTypedDataVirtual method reads the value of a variable in the target's virtual memory. |
| [IDebugSymbols3::Reload method](nf-dbgeng-idebugsymbols3-reload.md) | The Reload method deletes the engine's symbol information for the specified module and reload these symbols as needed. |
| [IDebugSymbols3::ReloadWide method](nf-dbgeng-idebugsymbols3-reloadwide.md) | The ReloadWide method deletes the engine's symbol information for the specified module and reload these symbols as needed. |
| [IDebugSymbols3::RemoveSymbolOptions method](nf-dbgeng-idebugsymbols3-removesymboloptions.md) | The RemoveSymbolOptions method turns off some of the engine's global symbol options. |
| [IDebugSymbols3::RemoveSyntheticModule method](nf-dbgeng-idebugsymbols3-removesyntheticmodule.md) | The RemoveSyntheticModule method removes a synthetic module from the module list the debugger maintains for the current process. |
| [IDebugSymbols3::RemoveSyntheticSymbol method](nf-dbgeng-idebugsymbols3-removesyntheticsymbol.md) | The RemoveSyntheticSymbol method removes a synthetic symbol from a module in the current process. |
| [IDebugSymbols3::RemoveTypeOptions method](nf-dbgeng-idebugsymbols3-removetypeoptions.md) | The RemoveTypeOptions method turns off some type formatting options for output generated by the engine. |
| [IDebugSymbols3::ResetScope method](nf-dbgeng-idebugsymbols3-resetscope.md) | The ResetScope method resets the current scope to the default scope of the current thread. |
| [IDebugSymbols3::SetImagePath method](nf-dbgeng-idebugsymbols3-setimagepath.md) | The SetImagePath method sets the executable image path. |
| [IDebugSymbols3::SetImagePathWide method](nf-dbgeng-idebugsymbols3-setimagepathwide.md) | The SetImagePathWide method sets the executable image path. |
| [IDebugSymbols3::SetScope method](nf-dbgeng-idebugsymbols3-setscope.md) | The SetScope method sets the current scope. |
| [IDebugSymbols3::SetScopeFrameByIndex method](nf-dbgeng-idebugsymbols3-setscopeframebyindex.md) | The SetScopeFrameByIndex method sets the current scope to the scope of one of the frames on the call stack. |
| [IDebugSymbols3::SetScopeFromJitDebugInfo method](nf-dbgeng-idebugsymbols3-setscopefromjitdebuginfo.md) | Recovers just-in-time (JIT) debugging information and sets current debugger scope context based on that information. |
| [IDebugSymbols3::SetScopeFromStoredEvent method](nf-dbgeng-idebugsymbols3-setscopefromstoredevent.md) | The SetScopeFromStoredEvent method sets the current scope to the scope of the stored event. |
| [IDebugSymbols3::SetSourcePath method](nf-dbgeng-idebugsymbols3-setsourcepath.md) | The SetSourcePath method sets the source path. |
| [IDebugSymbols3::SetSourcePathWide method](nf-dbgeng-idebugsymbols3-setsourcepathwide.md) | The SetSourcePathWide method sets the source path. |
| [IDebugSymbols3::SetSymbolOptions method](nf-dbgeng-idebugsymbols3-setsymboloptions.md) | The SetSymbolOptions method changes the engine's global symbol options. |
| [IDebugSymbols3::SetSymbolPath method](nf-dbgeng-idebugsymbols3-setsymbolpath.md) | The SetSymbolPath method sets the symbol path. |
| [IDebugSymbols3::SetSymbolPathWide method](nf-dbgeng-idebugsymbols3-setsymbolpathwide.md) | The SetSymbolPathWide method sets the symbol path. |
| [IDebugSymbols3::SetTypeOptions method](nf-dbgeng-idebugsymbols3-settypeoptions.md) | The SetTypeOptions method changes the type formatting options for output generated by the engine. |
| [IDebugSymbols3::StartSymbolMatch method](nf-dbgeng-idebugsymbols3-startsymbolmatch.md) | The StartSymbolMatch method initializes a search for symbols whose names match a given pattern. |
| [IDebugSymbols3::StartSymbolMatchWide method](nf-dbgeng-idebugsymbols3-startsymbolmatchwide.md) | The StartSymbolMatchWide method initializes a search for symbols whose names match a given pattern. |
| [IDebugSymbols3::WriteTypedDataPhysical method](nf-dbgeng-idebugsymbols3-writetypeddataphysical.md) | The WriteTypedDataPhysical method writes the value of a variable in the target computer's physical memory. |
| [IDebugSymbols3::WriteTypedDataVirtual method](nf-dbgeng-idebugsymbols3-writetypeddatavirtual.md) | The WriteTypedDataVirtual method writes data to the target's virtual address space. The number of bytes written is the size of the specified type. |
| [IDebugSymbols4::GetLineByInlineContext method](nf-dbgeng-idebugsymbols4-getlinebyinlinecontext.md) | Gets a line by inline context. |
| [IDebugSymbols4::GetLineByInlineContextWide method](nf-dbgeng-idebugsymbols4-getlinebyinlinecontextwide.md) | Gets a line by inline context. |
| [IDebugSymbols4::GetNameByInlineContext method](nf-dbgeng-idebugsymbols4-getnamebyinlinecontext.md) | Gets a name by inline context. |
| [IDebugSymbols4::GetNameByInlineContextWide method](nf-dbgeng-idebugsymbols4-getnamebyinlinecontextwide.md) | Gets a name by inline context. |
| [IDebugSymbols4::GetScopeEx method](nf-dbgeng-idebugsymbols4-getscopeex.md) | Gets the scope as an extended frame structure. |
| [IDebugSymbols4::OutputSymbolByInlineContext method](nf-dbgeng-idebugsymbols4-outputsymbolbyinlinecontext.md) | Specifies an output symbol by using an inline context. |
| [IDebugSymbols4::SetScopeEx method](nf-dbgeng-idebugsymbols4-setscopeex.md) | Sets the scope as an extended frame structure. |
| [IDebugSymbols5::GetCurrentScopeFrameIndexEx method](nf-dbgeng-idebugsymbols5-getcurrentscopeframeindexex.md) | Gets the index of the current frame. |
| [IDebugSymbols5::GetFieldOffset method](nf-dbgeng-idebugsymbols5-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [IDebugSymbols5::SetScopeFrameByIndexEx method](nf-dbgeng-idebugsymbols5-setscopeframebyindexex.md) | Sets the current frame by using an index. |
| [IDebugSymbols::GetFieldOffset method](nf-dbgeng-idebugsymbols-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [IDebugSystemObjects2::GetCurrentProcessHandle method](nf-dbgeng-idebugsystemobjects2-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
| [IDebugSystemObjects3::GetCurrentProcessHandle method](nf-dbgeng-idebugsystemobjects3-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
| [IDebugSystemObjects3::GetCurrentSystemServer method](nf-dbgeng-idebugsystemobjects3-getcurrentsystemserver.md) | Gets the server for the current process. |
| [IDebugSystemObjects3::GetCurrentSystemServerName method](nf-dbgeng-idebugsystemobjects3-getcurrentsystemservername.md) | Gets the server name for the current process. |
| [IDebugSystemObjects3::GetSystemByServer method](nf-dbgeng-idebugsystemobjects3-getsystembyserver.md) | Gets the system for a server. |
| [IDebugSystemObjects4::GetCurrentProcessDataOffset method](nf-dbgeng-idebugsystemobjects4-getcurrentprocessdataoffset.md) | The GetCurrentProcessDataOffset method returns the location of the system data structure describing the current process. |
| [IDebugSystemObjects4::GetCurrentProcessExecutableName method](nf-dbgeng-idebugsystemobjects4-getcurrentprocessexecutablename.md) | The GetCurrentProcessExecutableName method returns the name of executable file loaded in the current process. |
| [IDebugSystemObjects4::GetCurrentProcessExecutableNameWide method](nf-dbgeng-idebugsystemobjects4-getcurrentprocessexecutablenamewide.md) | The GetCurrentProcessExecutableNameWide method returns the name of executable file loaded in the current process. |
| [IDebugSystemObjects4::GetCurrentProcessHandle method](nf-dbgeng-idebugsystemobjects4-getcurrentprocesshandle.md) | The GetCurrentProcessHandle method returns the system handle for the current process. |
| [IDebugSystemObjects4::GetCurrentProcessId method](nf-dbgeng-idebugsystemobjects4-getcurrentprocessid.md) | The GetCurrentProcessId method returns the engine process ID for the current process. |
| [IDebugSystemObjects4::GetCurrentProcessPeb method](nf-dbgeng-idebugsystemobjects4-getcurrentprocesspeb.md) | The GetCurrentProcessPeb method returns the process environment block (PEB) of the current process. |
| [IDebugSystemObjects4::GetCurrentProcessSystemId method](nf-dbgeng-idebugsystemobjects4-getcurrentprocesssystemid.md) | The GetCurrentProcessSystemId method returns the system process ID of the current process. |
| [IDebugSystemObjects4::GetCurrentProcessUpTime method](nf-dbgeng-idebugsystemobjects4-getcurrentprocessuptime.md) | The GetCurrentProcessUpTime method returns the length of time the current process has been running. |
| [IDebugSystemObjects4::GetCurrentSystemId method](nf-dbgeng-idebugsystemobjects4-getcurrentsystemid.md) | The GetCurrentSystemId method returns the engine target ID for the current process. |
| [IDebugSystemObjects4::GetCurrentSystemServerNameWide method](nf-dbgeng-idebugsystemobjects4-getcurrentsystemservernamewide.md) | Gets the server name for the current process. |
| [IDebugSystemObjects4::GetCurrentThreadDataOffset method](nf-dbgeng-idebugsystemobjects4-getcurrentthreaddataoffset.md) | The GetCurrentThreadDataOffset method returns the location of the system data structure for the current thread. |
| [IDebugSystemObjects4::GetCurrentThreadHandle method](nf-dbgeng-idebugsystemobjects4-getcurrentthreadhandle.md) | The GetCurrentThreadHandle method returns the system handle for the current thread. |
| [IDebugSystemObjects4::GetCurrentThreadId method](nf-dbgeng-idebugsystemobjects4-getcurrentthreadid.md) | The GetCurrentThreadId method returns the engine thread ID for the current thread. |
| [IDebugSystemObjects4::GetCurrentThreadSystemId method](nf-dbgeng-idebugsystemobjects4-getcurrentthreadsystemid.md) | The GetCurrentThreadSystemId method returns the system thread ID of the current thread. |
| [IDebugSystemObjects4::GetCurrentThreadTeb method](nf-dbgeng-idebugsystemobjects4-getcurrentthreadteb.md) | The GetCurrentThreadTeb method returns the location of the thread environment block (TEB) for the current thread. |
| [IDebugSystemObjects4::GetEventProcess method](nf-dbgeng-idebugsystemobjects4-geteventprocess.md) | The GetEventProcess method returns the engine process ID for the process on which the last event occurred. |
| [IDebugSystemObjects4::GetEventSystem method](nf-dbgeng-idebugsystemobjects4-geteventsystem.md) | The GetEventSystem method returns the engine target ID for the target in which the last event occurred. |
| [IDebugSystemObjects4::GetEventThread method](nf-dbgeng-idebugsystemobjects4-geteventthread.md) | The GetEventThread method returns the engine thread ID for the thread on which the last event occurred. |
| [IDebugSystemObjects4::GetImplicitProcessDataOffset method](nf-dbgeng-idebugsystemobjects4-getimplicitprocessdataoffset.md) | The GetImplicitProcessDataOffset method returns the implicit process for the current target. |
| [IDebugSystemObjects4::GetImplicitThreadDataOffset method](nf-dbgeng-idebugsystemobjects4-getimplicitthreaddataoffset.md) | The GetImplicitThreadDataOffset method returns the implicit thread for the current process. |
| [IDebugSystemObjects4::GetNumberProcesses method](nf-dbgeng-idebugsystemobjects4-getnumberprocesses.md) | The GetNumberProcesses method returns the number of processes for the current target. |
| [IDebugSystemObjects4::GetNumberSystems method](nf-dbgeng-idebugsystemobjects4-getnumbersystems.md) | The GetNumberSystems method returns the number of targets to which the engine is currently connected. |
| [IDebugSystemObjects4::GetNumberThreads method](nf-dbgeng-idebugsystemobjects4-getnumberthreads.md) | The GetNumberThreads method returns the number of threads in the current process. |
| [IDebugSystemObjects4::GetProcessIdByDataOffset method](nf-dbgeng-idebugsystemobjects4-getprocessidbydataoffset.md) | The GetProcessIdByDataOffset method returns the engine process ID for the specified process. The process is specified by its data offset. |
| [IDebugSystemObjects4::GetProcessIdByHandle method](nf-dbgeng-idebugsystemobjects4-getprocessidbyhandle.md) | The GetProcessIdByHandle method returns the engine process ID for the specified process. The process is specified by its system handle. |
| [IDebugSystemObjects4::GetProcessIdByPeb method](nf-dbgeng-idebugsystemobjects4-getprocessidbypeb.md) | The GetProcessIdByPeb method returns the engine process ID for the specified process. The process is specified by its process environment block (PEB). |
| [IDebugSystemObjects4::GetProcessIdBySystemId method](nf-dbgeng-idebugsystemobjects4-getprocessidbysystemid.md) | The GetProcessIdBySystemId method returns the engine process ID for a process specified by its system process ID. |
| [IDebugSystemObjects4::GetProcessIdsByIndex method](nf-dbgeng-idebugsystemobjects4-getprocessidsbyindex.md) | The GetProcessIdsByIndex method returns the engine process ID and system process ID for the specified processes in the current target. |
| [IDebugSystemObjects4::GetSystemIdsByIndex method](nf-dbgeng-idebugsystemobjects4-getsystemidsbyindex.md) | The GetSystemIdsByIndex method returns the engine target IDs for the specified targets. |
| [IDebugSystemObjects4::GetThreadIdByDataOffset method](nf-dbgeng-idebugsystemobjects4-getthreadidbydataoffset.md) | The GetThreadIdByDataOffset method returns the engine thread ID for the specified thread. The thread is specified by its system data structure. |
| [IDebugSystemObjects4::GetThreadIdByHandle method](nf-dbgeng-idebugsystemobjects4-getthreadidbyhandle.md) | The GetThreadIdByHandle method returns the engine thread ID for the specified thread. The thread is specified by its system handle. |
| [IDebugSystemObjects4::GetThreadIdByProcessor method](nf-dbgeng-idebugsystemobjects4-getthreadidbyprocessor.md) | The GetThreadIdByProcessor method returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor. |
| [IDebugSystemObjects4::GetThreadIdBySystemId method](nf-dbgeng-idebugsystemobjects4-getthreadidbysystemid.md) | The GetThreadIdBySystemId method returns the engine thread ID for the specified thread. The thread is specified by its system thread ID. |
| [IDebugSystemObjects4::GetThreadIdByTeb method](nf-dbgeng-idebugsystemobjects4-getthreadidbyteb.md) | The GetThreadIdByTeb method returns the engine thread ID of the specified thread. The thread is specified by its thread environment block (TEB). |
| [IDebugSystemObjects4::GetThreadIdsByIndex method](nf-dbgeng-idebugsystemobjects4-getthreadidsbyindex.md) | The GetThreadIdsByIndex method returns the engine and system thread IDs for the specified threads in the current process. |
| [IDebugSystemObjects4::GetTotalNumberThreads method](nf-dbgeng-idebugsystemobjects4-gettotalnumberthreads.md) | The GetTotalNumberThreads method returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target. |
| [IDebugSystemObjects4::GetTotalNumberThreadsAndProcesses method](nf-dbgeng-idebugsystemobjects4-gettotalnumberthreadsandprocesses.md) | The GetTotalNumberThreadsAndProcesses method returns the total number of threads and processes in all the targets the engine is attached to, in addition to the largest number of threads and processes in a target. |
| [IDebugSystemObjects4::SetCurrentProcessId method](nf-dbgeng-idebugsystemobjects4-setcurrentprocessid.md) | The SetCurrentProcessId method makes the specified process the current process. |
| [IDebugSystemObjects4::SetCurrentSystemId method](nf-dbgeng-idebugsystemobjects4-setcurrentsystemid.md) | The SetCurrentSystemId method makes the specified target the current target. |
| [IDebugSystemObjects4::SetCurrentThreadId method](nf-dbgeng-idebugsystemobjects4-setcurrentthreadid.md) | The SetCurrentThreadId method makes the specified thread the current thread. |
| [IDebugSystemObjects4::SetImplicitProcessDataOffset method](nf-dbgeng-idebugsystemobjects4-setimplicitprocessdataoffset.md) | The SetImplicitProcessDataOffset method sets the implicit process for the current target. |
| [IDebugSystemObjects4::SetImplicitThreadDataOffset method](nf-dbgeng-idebugsystemobjects4-setimplicitthreaddataoffset.md) | The SetImplicitThreadDataOffset method sets the implicit thread for the current process. |
| [IDebugSystemObjects::GetCurrentProcessHandle method](nf-dbgeng-idebugsystemobjects-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
