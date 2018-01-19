---
UID: TP:debugger
ms.assetid: 025d7cc4-309d-33e6-8813-f58445c3acaf
ms.author: windowsdriverdev
ms.date: 01/19/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Debugger


Overview of the Debugger technology.

To develop Debugger, you need these headers:

 * [dbgeng.h](..\dbgeng\index.md)
 * [engextcpp.hpp](..\engextcpp\index.md)
 * [extsfns.h](..\extsfns\index.md)
 * [wdbgexts.h](..\wdbgexts\index.md)

For the programming guide, see [Debugger](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger).

## Functions

| Title   | Description   |
| ---- |:---- |
| [DebugCommandException function](..\dbgeng\nf-dbgeng-debugcommandexception.md) | Specifies a debug command exception. |
| [DebugConnect function](..\dbgeng\nf-dbgeng-debugconnect.md) | The DebugConnect and DebugConnectWide functions create a new client object and return an interface pointer to it. The client object will be connected to a remote host. |
| [DebugConnectWide function](..\dbgeng\nf-dbgeng-debugconnectwide.md) | The DebugConnect and DebugConnectWide functions create a new client object and return an interface pointer to it. The client object will be connected to a remote host. |
| [DebugCreate function](..\dbgeng\nf-dbgeng-debugcreate.md) | The DebugCreate function creates a new client object and returns an interface pointer to it. |
| [DebugCreateEx function](..\dbgeng\nf-dbgeng-debugcreateex.md) | The DebugCreateEx function creates a new client object and returns an interface pointer to it. |
| [GetCurrentProcessAddr function](..\wdbgexts\nf-wdbgexts-getcurrentprocessaddr.md) | The GetCurrentProcessAddr function returns the location of the system data that describes the current process. |
| [GetCurrentProcessHandle function](..\wdbgexts\nf-wdbgexts-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
| [GetCurrentThreadAddr function](..\wdbgexts\nf-wdbgexts-getcurrentthreadaddr.md) | The GetCurrentThreadAddr function returns the location of the system data that describes the current thread. |
| [GetDebuggerCacheSize function](..\wdbgexts\nf-wdbgexts-getdebuggercachesize.md) | The GetDebuggerCacheSize function returns the size of the cache that is used by the debugger to hold data that was obtained from the target. |
| [GetExpressionEx function](..\wdbgexts\nf-wdbgexts-getexpressionex.md) | The GetExpressionEx function evaluates an expression. The expression is evaluated using the MASM evaluator, and can contain aliases. |
| [GetFieldData function](..\wdbgexts\nf-wdbgexts-getfielddata.md) | The GetFieldData function returns the value of a member in a structure. |
| [GetFieldOffset function](..\wdbgexts\nf-wdbgexts-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [GetInputLine function](..\wdbgexts\nf-wdbgexts-getinputline.md) | The GetInputLine function requests an input string from the debugger. |
| [GetPebAddress function](..\wdbgexts\nf-wdbgexts-getpebaddress.md) | The GetPebAddress function returns the address of the process environment block (PEB) for a system process. |
| [GetSetSympath function](..\wdbgexts\nf-wdbgexts-getsetsympath.md) | The GetSetSympath function can be used to either get or set the symbol search path. |
| [GetShortField function](..\wdbgexts\nf-wdbgexts-getshortfield.md) | The GetShortField function reads the value of a member in a structure if its size is less than or equal to 8 bytes, or initializes a structure so it can be read later. |
| [GetTebAddress function](..\wdbgexts\nf-wdbgexts-gettebaddress.md) | The GetTebAddress function returns the address of the thread environment block (TEB) for the current operating system thread. |
| [GetTypeSize function](..\wdbgexts\nf-wdbgexts-gettypesize.md) | The GetTypeSize function returns the size in the target's memory of an instance of the specified type. |
| [IsPtr64 function](..\wdbgexts\nf-wdbgexts-isptr64.md) | The IsPtr64 function determines if the target uses 64-bit pointers. |
| [ListType function](..\wdbgexts\nf-wdbgexts-listtype.md) | The ListType function calls a specified callback function for every element in a linked list. |
| [ReadControlSpace function](..\wdbgexts\nf-wdbgexts-readcontrolspace.md) | The ReadControlSpace function reads the processor-specific control space into the array pointed to by buf. |
| [ReadControlSpace64 function](..\wdbgexts\nf-wdbgexts-readcontrolspace64.md) | The ReadControlSpace64 function reads the processor-specific control space into the array pointed to by buf. |
| [ReadIoSpace function](..\wdbgexts\nf-wdbgexts-readiospace.md) | The ReadIoSpace function reads from the system I/O locations. |
| [ReadIoSpace64 function](..\wdbgexts\nf-wdbgexts-readiospace64.md) | The ReadIoSpace64 function reads from the system I/O locations. |
| [ReadIoSpaceEx function](..\wdbgexts\nf-wdbgexts-readiospaceex.md) | The ReadIoSpaceEx function is an extended version of ReadIoSpace. |
| [ReadIoSpaceEx64 function](..\wdbgexts\nf-wdbgexts-readiospaceex64.md) | The ReadIoSpaceEx64 function is an extended version of ReadIoSpace64. |
| [ReadListEntry function](..\wdbgexts\nf-wdbgexts-readlistentry.md) | The ReadListEntry function reads a doubly-linked list entry from the target's memory. |
| [ReadMsr function](..\wdbgexts\nf-wdbgexts-readmsr.md) | The ReadMsr function reads the contents of a Model-Specific Register (MSR). |
| [ReadPhysical function](..\wdbgexts\nf-wdbgexts-readphysical.md) | The ReadPhysical function reads from physical memory. |
| [ReadPhysicalWithFlags function](..\wdbgexts\nf-wdbgexts-readphysicalwithflags.md) | The ReadPhysicalWithFlags function reads from physical memory. |
| [ReadPointer function](..\wdbgexts\nf-wdbgexts-readpointer.md) | The ReadPointer function reads a pointer from the target. |
| [ReadPtr function](..\wdbgexts\nf-wdbgexts-readptr.md) | The ReadPtr function reads a pointer from the target. ReadPointer should be used instead of this function as the return value of ReadPointer is more consistent with the rest of the WdbgExts API. |
| [ReloadSymbols function](..\wdbgexts\nf-wdbgexts-reloadsymbols.md) | The ReloadSymbols function deletes symbol information from the debugger so that it can be reloaded as needed. This function behaves the same way as the debugger command .reload. |
| [SearchMemory function](..\wdbgexts\nf-wdbgexts-searchmemory.md) | The SearchMemory function searches the target's virtual memory for a specified pattern of bytes. |
| [SetThreadForOperation function](..\wdbgexts\nf-wdbgexts-setthreadforoperation.md) | The SetThreadForOperation function sets the thread to use for the next StackTrace call. |
| [SetThreadForOperation64 function](..\wdbgexts\nf-wdbgexts-setthreadforoperation64.md) | The SetThreadForOperation64 function sets the thread to use for the next StackTrace call. |
| [TranslateVirtualToPhysical function](..\wdbgexts\nf-wdbgexts-translatevirtualtophysical.md) | The TranslateVirtualToPhysical function translates a virtual memory address into a physical memory address. |
| [WriteControlSpace function](..\wdbgexts\nf-wdbgexts-writecontrolspace.md) | The WriteControlSpace function writes to the processor-specific control space of the current target. |
| [WriteIoSpace function](..\wdbgexts\nf-wdbgexts-writeiospace.md) | The WriteIoSpace function writes to the system I/O locations. |
| [WriteIoSpace64 function](..\wdbgexts\nf-wdbgexts-writeiospace64.md) | The WriteIoSpace64 function writes to the system I/O locations. |
| [WriteIoSpaceEx function](..\wdbgexts\nf-wdbgexts-writeiospaceex.md) | The WriteIoSpaceEx function is an extended version of WriteIoSpace. |
| [WriteIoSpaceEx64 function](..\wdbgexts\nf-wdbgexts-writeiospaceex64.md) | The WriteIoSpaceEx64 function is an extended version of WriteIoSpace64. |
| [WriteMsr function](..\wdbgexts\nf-wdbgexts-writemsr.md) | The WriteMsr function writes to a Model-Specific Register (MSR). |
| [WritePhysical function](..\wdbgexts\nf-wdbgexts-writephysical.md) | The WritePhysical function writes to physical memory. |
| [WritePhysicalWithFlags function](..\wdbgexts\nf-wdbgexts-writephysicalwithflags.md) | The WritePhysicalWithFlags function writes to physical memory. |
| [WritePointer function](..\wdbgexts\nf-wdbgexts-writepointer.md) | The WritePointer function writes a pointer to the target. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PDEBUG_EXTENSION_CALL callback function](..\dbgeng\nc-dbgeng-pdebug_extension_call.md) | Callback functions of the type PDEBUG_EXTENSION_CALL are called by the engine to execute extension commands. You can give these functions any name you want, as long as it contains no uppercase letters. |
| [PDEBUG_EXTENSION_CANUNLOAD callback function](..\dbgeng\nc-dbgeng-pdebug_extension_canunload.md) | The DebugExtensionCanUnload callback function checks whether a debug extension can unload after the uninitialization call. |
| [PDEBUG_EXTENSION_INITIALIZE callback function](..\dbgeng\nc-dbgeng-pdebug_extension_initialize.md) | The DebugExtensionInitialize callback function is called by the engine after loading a DbgEng extension DLL.C++ CALLBACK* PDEBUG_EXTENSION_INITIALIZE DebugExtensionInitialize; |
| [PDEBUG_EXTENSION_KNOWN_STRUCT callback function](..\dbgeng\nc-dbgeng-pdebug_extension_known_struct.md) | The engine calls the KnownStructOutput callback function to request information about structures that the extension DLL can format for printing. The engine calls this function for the following reasons. |
| [PDEBUG_EXTENSION_KNOWN_STRUCT_EX callback function](..\dbgeng\nc-dbgeng-pdebug_extension_known_struct_ex.md) | The DebugExtensionKnownStructEx callback function is called by extensions in order to dump structures that are well known to them. |
| [PDEBUG_EXTENSION_NOTIFY callback function](..\dbgeng\nc-dbgeng-pdebug_extension_notify.md) | The engine calls the DebugExtensionNotify callback function to inform the extension DLL when a session changes its active or accessible status.C++ CALLBACK* PDEBUG_EXTENSION_NOTIFY DebugExtensionNotify; |
| [PDEBUG_EXTENSION_PROVIDE_VALUE callback function](..\dbgeng\nc-dbgeng-pdebug_extension_provide_value.md) | The DebugExtensionProvideValue callback function sets pseudo-register values.C++ CALLBACK* PDEBUG_EXTENSION_PROVIDE_VALUE DebugExtensionProvideValue; |
| [PDEBUG_EXTENSION_QUERY_VALUE_NAMES callback function](..\dbgeng\nc-dbgeng-pdebug_extension_query_value_names.md) | The DebugExtensionQueryValueNames callback function recovers pseudo-register values.C++ CALLBACK* PDEBUG_EXTENSION_QUERY_VALUE_NAMES DebugExtensionQueryValueNames; |
| [PDEBUG_EXTENSION_UNINITIALIZE callback function](..\dbgeng\nc-dbgeng-pdebug_extension_uninitialize.md) | The DebugExtensionUninitialize callback function is called by the engine to uninitialize the DbgEng extension DLL before it is unloaded. |
| [PDEBUG_EXTENSION_UNLOAD callback function](..\dbgeng\nc-dbgeng-pdebug_extension_unload.md) | The DebugExtensionUnload callback function unloads the debug extension. |
| [PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION callback function](..\dbgeng\nc-dbgeng-pdebug_stack_provider_beginthreadstackreconstruction.md) | The BeginThreadStackReconstruction callback function causes debugger to pass the stream to the dump stack provider prior to thread enumeration. |
| [PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION callback function](..\dbgeng\nc-dbgeng-pdebug_stack_provider_endthreadstackreconstruction.md) | The EndThreadStackReconstruction callback function may be called after stack reconstruction to clean up state. |
| [PDEBUG_STACK_PROVIDER_FREESTACKSYMFRAMES callback function](..\dbgeng\nc-dbgeng-pdebug_stack_provider_freestacksymframes.md) | The FreeStackSymFrames callback function frees memory from a stack provider. |
| [PDEBUG_STACK_PROVIDER_RECONSTRUCTSTACK callback function](..\dbgeng\nc-dbgeng-pdebug_stack_provider_reconstructstack.md) | The ReconstructStack callback function queries dump stream provider on a per-thread basis. |
| [PSYM_DUMP_FIELD_CALLBACK callback function](..\wdbgexts\nc-wdbgexts-psym_dump_field_callback.md) | The PSYM_DUMP_FIELD_CALLBACK callback function is called by the debugger engine during the IG_DUMP_SYMBOL_INFO Ioctl operation with information about a member in the specified symbol. |
| [PWINDBG_CHECK_VERSION callback function](..\wdbgexts\nc-wdbgexts-pwindbg_check_version.md) | The PWINDBG_CHECK_VERSION (CheckVersion) callback function verifies that the extension module version matches the debugger version, and outputs an warning message if there is a mismatch. |
| [PWINDBG_EXTENSION_API_VERSION callback function](..\wdbgexts\nc-wdbgexts-pwindbg_extension_api_version.md) | The PWINDBG_EXTENSION_API_VERSION (ExtensionApiVersion) callback function returns version information about the extension DLL. |
| [PWINDBG_EXTENSION_DLL_INIT callback function](..\wdbgexts\nc-wdbgexts-pwindbg_extension_dll_init.md) | The PWINDBG_EXTENSION_DLL_INIT ( WinDbgExtensionDllInit) callback function is used to load and initialize the extension module. |
| [PWINDBG_OUTPUT_ROUTINE callback function](..\wdbgexts\nc-wdbgexts-pwindbg_output_routine.md) | The callback function implements the functionality to print a formatted string to the Debugger Command window. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [ExtKnownStruct structure](..\engextcpp\ns-engextcpp-extknownstruct.md) | The ExtKnownStruct structure is used to specify how a target's structure can be formatted for output. |
| [_DBGKD_GET_VERSION64 structure](..\wdbgexts\ns-wdbgexts-_dbgkd_get_version64.md) | The IG_GET_KERNEL_VERSION Ioctl operation receives information related to the operating system version of the target. |
| [_DEBUG_BREAKPOINT_PARAMETERS structure](..\dbgeng\ns-dbgeng-_debug_breakpoint_parameters.md) | The DEBUG_BREAKPOINT_PARAMETERS structure contains most of the parameters for describing a breakpoint. |
| [_DEBUG_CACHED_SYMBOL_INFO structure](..\dbgeng\ns-dbgeng-_debug_cached_symbol_info.md) | Defines information about cached symbols. |
| [_DEBUG_CLIENT_CONTEXT structure](..\dbgeng\ns-dbgeng-_debug_client_context.md) | Contains a debug client constant to provide to the IDebugClient7 |
| [_DEBUG_CREATE_PROCESS_OPTIONS structure](..\dbgeng\ns-dbgeng-_debug_create_process_options.md) | The DEBUG_CREATE_PROCESS_OPTIONS structure specifies the process creation options to use when creating a new process. |
| [_DEBUG_EVENT_CONTEXT structure](..\dbgeng\ns-dbgeng-_debug_event_context.md) | Defines context information about an event. |
| [_DEBUG_EXCEPTION_FILTER_PARAMETERS structure](..\dbgeng\ns-dbgeng-_debug_exception_filter_parameters.md) | The DEBUG_EXCEPTION_FILTER_PARAMETERS structure contains the parameters for an exception filter. |
| [_DEBUG_GET_TEXT_COMPLETIONS_IN structure](..\dbgeng\ns-dbgeng-_debug_get_text_completions_in.md) | Defines information about text completions to get. |
| [_DEBUG_GET_TEXT_COMPLETIONS_OUT structure](..\dbgeng\ns-dbgeng-_debug_get_text_completions_out.md) | Defines information about text completions to get. |
| [_DEBUG_HANDLE_DATA_BASIC structure](..\dbgeng\ns-dbgeng-_debug_handle_data_basic.md) | The DEBUG_HANDLE_DATA_BASIC structure contains handle-related information about a system object. |
| [_DEBUG_LAST_EVENT_INFO_BREAKPOINT structure](..\dbgeng\ns-dbgeng-_debug_last_event_info_breakpoint.md) | Describes the breakpoint of the last event. |
| [_DEBUG_LAST_EVENT_INFO_EXCEPTION structure](..\dbgeng\ns-dbgeng-_debug_last_event_info_exception.md) | Describes the exception of the last event. |
| [_DEBUG_LAST_EVENT_INFO_EXIT_PROCESS structure](..\dbgeng\ns-dbgeng-_debug_last_event_info_exit_process.md) | Describes the exit process of the last event. |
| [_DEBUG_LAST_EVENT_INFO_EXIT_THREAD structure](..\dbgeng\ns-dbgeng-_debug_last_event_info_exit_thread.md) | Describes the exit thread of the last event. |
| [_DEBUG_LAST_EVENT_INFO_LOAD_MODULE structure](..\dbgeng\ns-dbgeng-_debug_last_event_info_load_module.md) | Describes the load module of the last event. |
| [_DEBUG_LAST_EVENT_INFO_SYSTEM_ERROR structure](..\dbgeng\ns-dbgeng-_debug_last_event_info_system_error.md) | Describes the system error of the last event. |
| [_DEBUG_LAST_EVENT_INFO_UNLOAD_MODULE structure](..\dbgeng\ns-dbgeng-_debug_last_event_info_unload_module.md) | Describes the unload module of the last event. |
| [_DEBUG_MODULE_AND_ID structure](..\dbgeng\ns-dbgeng-_debug_module_and_id.md) | The DEBUG_MODULE_AND_ID structure describes a symbol within a module. |
| [_DEBUG_MODULE_PARAMETERS structure](..\dbgeng\ns-dbgeng-_debug_module_parameters.md) | The DEBUG_MODULE_PARAMETERS structure contains most of the parameters for describing a module. |
| [_DEBUG_OFFSET_REGION structure](..\dbgeng\ns-dbgeng-_debug_offset_region.md) | Defines a debug offset region. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_ALL structure](..\dbgeng\ns-dbgeng-_debug_processor_identification_all.md) | This union contains relevant information for a processor the supported processors. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_ALPHA structure](..\dbgeng\ns-dbgeng-_debug_processor_identification_alpha.md) | Identifies an Alpha processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_AMD64 structure](..\dbgeng\ns-dbgeng-_debug_processor_identification_amd64.md) | Identifies an AMD64 processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_ARM structure](..\dbgeng\ns-dbgeng-_debug_processor_identification_arm.md) | Identifies an ARM processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_ARM64 structure](..\dbgeng\ns-dbgeng-_debug_processor_identification_arm64.md) | Identifies an ARM64 processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_IA64 structure](..\dbgeng\ns-dbgeng-_debug_processor_identification_ia64.md) | Identifies an Intel Itanium architecture (IA64) processor. |
| [_DEBUG_PROCESSOR_IDENTIFICATION_X86 structure](..\dbgeng\ns-dbgeng-_debug_processor_identification_x86.md) | Identifies an x86 processor. |
| [_DEBUG_READ_USER_MINIDUMP_STREAM structure](..\dbgeng\ns-dbgeng-_debug_read_user_minidump_stream.md) | Describes a user minidump to read. |
| [_DEBUG_REGISTER_DESCRIPTION structure](..\dbgeng\ns-dbgeng-_debug_register_description.md) | The DEBUG_REGISTER_DESCRIPTION structure is returned by GetDescription to describe a processor's register. |
| [_DEBUG_SPECIFIC_FILTER_PARAMETERS structure](..\dbgeng\ns-dbgeng-_debug_specific_filter_parameters.md) | The DEBUG_SPECIFIC_FILTER_PARAMETERS structure contains the parameters for a specific event filter. |
| [_DEBUG_STACK_FRAME structure](..\dbgeng\ns-dbgeng-_debug_stack_frame.md) | The DEBUG_STACK_FRAME structure describes a stack frame and the address of the current instruction for the stack frame. |
| [_DEBUG_STACK_FRAME_EX structure](..\dbgeng\ns-dbgeng-_debug_stack_frame_ex.md) | The DEBUG_STACK_FRAME_EX structure describes a stack frame and the address of the current instruction for the stack frame. |
| [_DEBUG_SYMBOL_ENTRY structure](..\dbgeng\ns-dbgeng-_debug_symbol_entry.md) | The DEBUG_SYMBOL_ENTRY structure describes a symbol in a symbol group. |
| [_DEBUG_SYMBOL_PARAMETERS structure](..\dbgeng\ns-dbgeng-_debug_symbol_parameters.md) | The DEBUG_SYMBOL_PARAMETERS structure describes a symbol in a symbol group. |
| [_DEBUG_SYMBOL_SOURCE_ENTRY structure](..\dbgeng\ns-dbgeng-_debug_symbol_source_entry.md) | The DEBUG_SYMBOL_SOURCE_ENTRY structure describes a section of the source code and a corresponding region of the target's memory. |
| [_DEBUG_THREAD_BASIC_INFORMATION structure](..\dbgeng\ns-dbgeng-_debug_thread_basic_information.md) | The DEBUG_THREAD_BASIC_INFORMATION structure describes an operating system thread. |
| [_DEBUG_TYPED_DATA structure](..\wdbgexts\ns-wdbgexts-_debug_typed_data.md) | The DEBUG_TYPED_DATA structure describes typed data in the memory of the target. |
| [_DEBUG_VALUE structure](..\dbgeng\ns-dbgeng-_debug_value.md) | The DEBUG_VALUE structure holds register and expression values. |
| [_EXT_TYPED_DATA structure](..\wdbgexts\ns-wdbgexts-_ext_typed_data.md) | The EXT_TYPED_DATA structure is passed to and returned from the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation. It contains the input and output parameters for the operation as well as specifying which particular suboperation to perform. |
| [_FA_ENTRY structure](..\extsfns\ns-extsfns-_fa_entry.md) | A DebugFailureAnalysis object has a collection of failure analysis entries (FA entries). Each FA entry is represented by an FA_ENTRY structure. For more information, see Failure Analysis Entries, Tags, and Data Types. |
| [_FIELD_INFO structure](..\wdbgexts\ns-wdbgexts-_field_info.md) | The FIELD_INFO structure is used by the IG_DUMP_SYMBOL_INFOIoctl operation to provide information about a member in a structure. |
| [_GETSETBUSDATA structure](..\wdbgexts\ns-wdbgexts-_getsetbusdata.md) | The IG_GET_BUS_DATA Ioctl operation reads data from a system bus and the IG_SET_BUS_DATA Ioctl operation writes data to a system bus. |
| [_INLINE_FRAME_CONTEXT structure](..\dbgeng\ns-dbgeng-_inline_frame_context.md) | Describes inline frame context. |
| [_POINTER_SEARCH_PHYSICAL structure](..\wdbgexts\ns-wdbgexts-_pointer_search_physical.md) | The IG_POINTER_SEARCH_PHYSICAL Ioctl operation searches the target's physical memory for pointers lying within a specified range. |
| [_STACK_SRC_INFO structure](..\dbgeng\ns-dbgeng-_stack_src_info.md) | Defines stack source information. |
| [_STACK_SYM_FRAME_INFO structure](..\dbgeng\ns-dbgeng-_stack_sym_frame_info.md) | Defines stack source information for an extended stack frame. |
| [_SYMBOL_INFO_EX structure](..\dbgeng\ns-dbgeng-_symbol_info_ex.md) | The SYMBOL_INFO_EX structure describes the extended line symbol information. |
| [_SYM_DUMP_PARAM structure](..\wdbgexts\ns-wdbgexts-_sym_dump_param.md) | The IG_DUMP_SYMBOL_INFO Ioctl operation provides information about the type of a symbol. |
| [_WDBGEXTS_THREAD_OS_INFO structure](..\wdbgexts\ns-wdbgexts-_wdbgexts_thread_os_info.md) | The IG_GET_THREAD_OS_INFO Ioctl operation returns information about an operating system thread in the target. When calling Ioctl with IoctlType set to IG_GET_THREAD_OS_INFO, IpvData should contain an instance of the WDBGEXTS_THREAD_OS_INFO structure. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_DEBUG_FAILURE_TYPE Enumeration](..\extsfns\ne-extsfns-_debug_failure_type.md) | The values in the DEBUG_FAILURE_TYPE enumeration indicate the type of a failure. |
| [_DEBUG_FLR_PARAM_TYPE Enumeration](..\extsfns\ne-extsfns-_debug_flr_param_type.md) | The values of DEBUG_FLR_PARAM_TYPE enumeration are tags that indicate the kind of information that is stored in failure analysis entry. |
| [_EXT_TDOP Enumeration](..\wdbgexts\ne-wdbgexts-_ext_tdop.md) | The EXT_TDOP enumeration is used in the Operation member of the EXT_TYPED_DATA structure to specify which suboperation the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation will perform. |
| [_FA_ENTRY_TYPE Enumeration](..\extsfns\ne-extsfns-_fa_entry_type.md) | A DebugFailureAnalysis object has a collection of failure analysis entries (FA entries). |
| [_FA_EXTENSION_PLUGIN_PHASE Enumeration](..\extsfns\ne-extsfns-_fa_extension_plugin_phase.md) | A value in the FA_EXTENSION_PLUGIN_PHASE enumeration is passed to the _EFN_Analyze function to specify which phase of the analysis is currently in progress. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IDebugAdvanced interface](..\dbgeng\nn-dbgeng-idebugadvanced.md) | IDebugAdvanced interface |
| [IDebugAdvanced2 interface](..\dbgeng\nn-dbgeng-idebugadvanced2.md) | IDebugAdvanced2 interface |
| [IDebugAdvanced3 interface](..\dbgeng\nn-dbgeng-idebugadvanced3.md) | IDebugAdvanced3 interface |
| [IDebugAdvanced4 interface](..\dbgeng\nn-dbgeng-idebugadvanced4.md) | IDebugAdvanced4 interface |
| [IDebugBreakpoint interface](..\dbgeng\nn-dbgeng-idebugbreakpoint.md) | IDebugBreakpoint interface |
| [IDebugBreakpoint2 interface](..\dbgeng\nn-dbgeng-idebugbreakpoint2.md) | IDebugBreakpoint2 interface |
| [IDebugBreakpoint3 interface](..\dbgeng\nn-dbgeng-idebugbreakpoint3.md) | . |
| [IDebugClient interface](..\dbgeng\nn-dbgeng-idebugclient.md) | IDebugClient interface |
| [IDebugClient2 interface](..\dbgeng\nn-dbgeng-idebugclient2.md) | IDebugClient2 interface |
| [IDebugClient3 interface](..\dbgeng\nn-dbgeng-idebugclient3.md) | IDebugClient3 interface |
| [IDebugClient4 interface](..\dbgeng\nn-dbgeng-idebugclient4.md) | IDebugClient4 interface |
| [IDebugClient5 interface](..\dbgeng\nn-dbgeng-idebugclient5.md) | IDebugClient5 interface |
| [IDebugClient6 interface](..\dbgeng\nn-dbgeng-idebugclient6.md) | This interface supports event context callbacks. |
| [IDebugClient7 interface](..\dbgeng\nn-dbgeng-idebugclient7.md) | The IDebugClient7 interface is reserved for internal use. |
| [IDebugControl interface](..\dbgeng\nn-dbgeng-idebugcontrol.md) | IDebugControl interface |
| [IDebugControl2 interface](..\dbgeng\nn-dbgeng-idebugcontrol2.md) | IDebugControl2 interface |
| [IDebugControl3 interface](..\dbgeng\nn-dbgeng-idebugcontrol3.md) | IDebugControl3 interface |
| [IDebugControl4 interface](..\dbgeng\nn-dbgeng-idebugcontrol4.md) | IDebugControl4 interface |
| [IDebugControl5 interface](..\dbgeng\nn-dbgeng-idebugcontrol5.md) | . |
| [IDebugControl6 interface](..\dbgeng\nn-dbgeng-idebugcontrol6.md) | . |
| [IDebugControl7 interface](..\dbgeng\nn-dbgeng-idebugcontrol7.md) | . |
| [IDebugDataSpaces interface](..\dbgeng\nn-dbgeng-idebugdataspaces.md) | IDebugDataSpaces interface |
| [IDebugDataSpaces2 interface](..\dbgeng\nn-dbgeng-idebugdataspaces2.md) | IDebugDataSpaces2 interface |
| [IDebugDataSpaces3 interface](..\dbgeng\nn-dbgeng-idebugdataspaces3.md) | IDebugDataSpaces3 interface |
| [IDebugDataSpaces4 interface](..\dbgeng\nn-dbgeng-idebugdataspaces4.md) | IDebugDataSpaces4 interface |
| [IDebugEventCallbacks interface](..\dbgeng\nn-dbgeng-idebugeventcallbacks.md) | IDebugEventCallbacks interface |
| [IDebugEventCallbacksWide interface](..\dbgeng\nn-dbgeng-idebugeventcallbackswide.md) | IDebugEventCallbacksWide interface |
| [IDebugEventContextCallbacks interface](..\dbgeng\nn-dbgeng-idebugeventcontextcallbacks.md) | This interface supports event context callbacks and replaces the use of the IDebugClient |
| [IDebugFAEntryTags interface](..\extsfns\nn-extsfns-idebugfaentrytags.md) | When the !analyze debugger command runs, the analysis engine can load and run extension analysis plug-ins. |
| [IDebugFailureAnalysis2 interface](..\extsfns\nn-extsfns-idebugfailureanalysis2.md) | When the !analyze debugger command runs, the analysis engine can load and run extension analysis plug-ins. |
| [IDebugInputCallbacks interface](..\dbgeng\nn-dbgeng-idebuginputcallbacks.md) | IDebugInputCallbacks interface |
| [IDebugOutputCallbacks interface](..\dbgeng\nn-dbgeng-idebugoutputcallbacks.md) | IDebugOutputCallbacks interface |
| [IDebugOutputCallbacks2 interface](..\dbgeng\nn-dbgeng-idebugoutputcallbacks2.md) | The IDebugOutputCallbacks2 interface allows clients to receive full debugger markup language (DML) content for presentation. |
| [IDebugOutputCallbacksWide interface](..\dbgeng\nn-dbgeng-idebugoutputcallbackswide.md) | IDebugOutputCallbacksWide interface |
| [IDebugOutputStream interface](..\dbgeng\nn-dbgeng-idebugoutputstream.md) | Supports the debug output stream. |
| [IDebugPlmClient interface](..\dbgeng\nn-dbgeng-idebugplmclient.md) | This interface supports Process Lifecycle Management (PLM) for the debug client. |
| [IDebugPlmClient2 interface](..\dbgeng\nn-dbgeng-idebugplmclient2.md) | This interface supports Process Lifecycle Management (PLM) for the debug client. |
| [IDebugPlmClient3 interface](..\dbgeng\nn-dbgeng-idebugplmclient3.md) | This interface supports Process Lifecycle Management (PLM) for the debug client. |
| [IDebugRegisters interface](..\dbgeng\nn-dbgeng-idebugregisters.md) | IDebugRegisters interface |
| [IDebugRegisters2 interface](..\dbgeng\nn-dbgeng-idebugregisters2.md) | IDebugRegisters2 interface |
| [IDebugSymbolGroup interface](..\dbgeng\nn-dbgeng-idebugsymbolgroup.md) | IDebugSymbolGroup interface |
| [IDebugSymbolGroup2 interface](..\dbgeng\nn-dbgeng-idebugsymbolgroup2.md) | IDebugSymbolGroup2 interface |
| [IDebugSymbols interface](..\dbgeng\nn-dbgeng-idebugsymbols.md) | IDebugSymbols interface |
| [IDebugSymbols2 interface](..\dbgeng\nn-dbgeng-idebugsymbols2.md) | IDebugSymbols2 interface |
| [IDebugSymbols3 interface](..\dbgeng\nn-dbgeng-idebugsymbols3.md) | IDebugSymbols3 interface |
| [IDebugSymbols4 interface](..\dbgeng\nn-dbgeng-idebugsymbols4.md) | This interface supports determination of the symbol of an inline frame. |
| [IDebugSymbols5 interface](..\dbgeng\nn-dbgeng-idebugsymbols5.md) | This interface supports using index values for the current frame. |
| [IDebugSystemObjects interface](..\dbgeng\nn-dbgeng-idebugsystemobjects.md) | IDebugSystemObjects interface |
| [IDebugSystemObjects2 interface](..\dbgeng\nn-dbgeng-idebugsystemobjects2.md) | IDebugSystemObjects2 interface |
| [IDebugSystemObjects3 interface](..\dbgeng\nn-dbgeng-idebugsystemobjects3.md) | IDebugSystemObjects3 interface |
| [IDebugSystemObjects4 interface](..\dbgeng\nn-dbgeng-idebugsystemobjects4.md) | IDebugSystemObjects4 interface |

## Macros

| Title   | Description   |
| ---- |:---- |
| [EXT_COMMAND function](..\engextcpp\nf-engextcpp-ext_command.md) | The EXT_COMMAND macro is used to define an extension command that was declared by using the EXT_COMMAND_METHOD macro.An extension command is defined as follows |
| [EXT_COMMAND_METHOD function](..\engextcpp\nf-engextcpp-ext_command_method.md) | The EXT_COMMAND_METHOD macro declares an extension command from inside the definition of the EXT_CLASS class. |
| [GetDebuggerData function](..\wdbgexts\nf-wdbgexts-getdebuggerdata.md) | The GetDebuggerData function retrieves information stored in a data block. |
| [GetFieldValue function](..\wdbgexts\nf-wdbgexts-getfieldvalue.md) | The GetFieldValue macro is a thin wrapper around the GetFieldData function. It is provided as a convenience for reading the value of a member in a structure. |
| [GetKdContext function](..\wdbgexts\nf-wdbgexts-getkdcontext.md) | The GetKdContext function returns the total number of processors and the number of the current processor in the structure ppi points to. |

## Methods

| Title   | Description   |
| ---- |:---- |
| [AbandonCurrentProcess method](..\dbgeng\nf-dbgeng-idebugclient5-abandoncurrentprocess.md) | The AbandonCurrentProcess method removes the current process from the debugger engine's process list without detaching or terminating the process. |
| [ActivateAndDebugPlmBgTaskWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-activateanddebugplmbgtaskwide.md) | Launches and attaches to a Process Lifecycle Management (PLM) background task. |
| [AddAssemblyOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-addassemblyoptions.md) | The AddAssemblyOptions method turns on some of the assembly and disassembly options. |
| [AddBreakpoint method](..\dbgeng\nf-dbgeng-idebugcontrol3-addbreakpoint.md) | The AddBreakpoint method creates a new breakpoint for the current target. |
| [AddBreakpoint2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-addbreakpoint2.md) | The AddBreakpoint2 method creates a new breakpoint for the current target. |
| [AddBuffer method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addbuffer.md) | The AddBuffer method adds a new FA entry to a DebugFailureAnalysis object, and writes the bytes from a specified buffer to the data block of the new FA entry. |
| [AddDumpInformationFile method](..\dbgeng\nf-dbgeng-idebugclient5-adddumpinformationfile.md) | The AddDumpInformationFile method registers additional files containing supporting information that will be used when opening a dump file. The Unicode version of this method is AddDumpInformationFileWide. |
| [AddDumpInformationFileWide method](..\dbgeng\nf-dbgeng-idebugclient5-adddumpinformationfilewide.md) | The AddDumpInformationFileWide method registers additional files containing supporting information that will be used when opening a dump file. The ASCII version of this method is AddDumpInformationFile. |
| [AddEngineOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-addengineoptions.md) | The AddEngineOptions method turns on some of the debugger engine's options. |
| [AddExtension method](..\dbgeng\nf-dbgeng-idebugcontrol3-addextension.md) | The AddExtension method loads an extension library into the debugger engine. |
| [AddExtensionCommand method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addextensioncommand.md) | The AddExtensionCommand method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified debugger command. |
| [AddExtensionWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-addextensionwide.md) | The AddExtensionWide method loads an extension library into the debugger engine. |
| [AddFlags method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-addflags.md) | The AddFlags method adds flags to a breakpoint. |
| [AddProcessOptions method](..\dbgeng\nf-dbgeng-idebugclient5-addprocessoptions.md) | The AddProcessOptions method adds the process options to those options that affect the current process. |
| [AddString method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addstring.md) | The AddString method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified string. |
| [AddSymbol method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-addsymbol.md) | The AddSymbol method adds a symbol to a symbol group. |
| [AddSymbolOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsymboloptions.md) | The AddSymbolOptions method turns on some of the engine's global symbol options. |
| [AddSymbolWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-addsymbolwide.md) | The AddSymbolWide method adds a symbol to a symbol group. |
| [AddSyntheticModule method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsyntheticmodule.md) | The AddSyntheticModule method adds a synthetic module to the module list the debugger maintains for the current process. |
| [AddSyntheticModuleWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsyntheticmodulewide.md) | The AddSyntheticModuleWide method adds a synthetic module to the module list the debugger maintains for the current process. |
| [AddSyntheticSymbol method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsyntheticsymbol.md) | The AddSyntheticSymbol method adds a synthetic symbol to a module in the current process. |
| [AddSyntheticSymbolWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-addsyntheticsymbolwide.md) | The AddSyntheticSymbolWide method adds a synthetic symbol to a module in the current process. |
| [AddTypeOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-addtypeoptions.md) | The AddTypeOptions method turns on some type formatting options for output generated by the engine. |
| [AddUlong method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addulong.md) | The AddUlong method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified ULONG value. |
| [AddUlong64 method](..\extsfns\nf-extsfns-idebugfailureanalysis2-addulong64.md) | The AddUlong64 method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified 64-bit value. |
| [AppendImagePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendimagepath.md) | The AppendImagePath method appends directories to the executable image path. |
| [AppendImagePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendimagepathwide.md) | The AppendImagePathWide method appends directories to the executable image path. |
| [AppendSourcePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendsourcepath.md) | The AppendSourcePath method appends directories to the source path. |
| [AppendSourcePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendsourcepathwide.md) | The AppendSourcePathWide method appends directories to the source path. |
| [AppendSymbolPath method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendsymbolpath.md) | The AppendSymbolPath method appends directories to the symbol path. |
| [AppendSymbolPathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-appendsymbolpathwide.md) | The AppendSymbolPathWide method appends directories to the symbol path. |
| [Assemble method](..\dbgeng\nf-dbgeng-idebugcontrol3-assemble.md) | The Assemble method assembles a single processor instruction. The assembled instruction is placed in the target's memory. |
| [AssembleWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-assemblewide.md) | The AssembleWide method assembles a single processor instruction. The assembled instruction is placed in the target's memory. |
| [AttachKernel method](..\dbgeng\nf-dbgeng-idebugclient5-attachkernel.md) | The AttachKernel methods connect the debugger engine to a kernel target. |
| [AttachKernelWide method](..\dbgeng\nf-dbgeng-idebugclient5-attachkernelwide.md) | The AttachKernelWide method connects the debugger engine to a kernel target. |
| [AttachProcess method](..\dbgeng\nf-dbgeng-idebugclient5-attachprocess.md) | The AttachProcess method connects the debugger engine to a user-modeprocess. |
| [Breakpoint method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-breakpoint.md) | The Breakpoint callback method is called by the engine when the target issues a breakpointexception. |
| [Breakpoint method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-breakpoint.md) | The Breakpoint callback method is called by the engine when the target issues a breakpointexception. |
| [CallExtension method](..\dbgeng\nf-dbgeng-idebugcontrol3-callextension.md) | The CallExtension method calls a debugger extension. |
| [CallExtensionWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-callextensionwide.md) | The CallExtensionWide method calls a debugger extension. |
| [ChangeDebuggeeState method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-changedebuggeestate.md) | The ChangeDebuggeeState callback method is called by the engine when it makes or detects changes to the target. |
| [ChangeDebuggeeState method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-changedebuggeestate.md) | The ChangeDebuggeeState callback method is called by the engine when it makes or detects changes to the target. |
| [ChangeEngineState method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-changeenginestate.md) | The ChangeEngineState callback method is called by the engine when its state has changed. |
| [ChangeEngineState method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-changeenginestate.md) | The ChangeEngineState callback method is called by the engine when its state has changed. |
| [ChangeSymbolState method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-changesymbolstate.md) | The ChangeSymbolState callback method is called by the engine when the symbol state changes. |
| [ChangeSymbolState method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-changesymbolstate.md) | The ChangeSymbolState callback method is called by the engine when the symbol state changes. |
| [CheckLowMemory method](..\dbgeng\nf-dbgeng-idebugdataspaces4-checklowmemory.md) | The CheckLowMemory method checks for memory corruption in the low 4 GB of memory. |
| [CloseLogFile method](..\dbgeng\nf-dbgeng-idebugcontrol3-closelogfile.md) | The CloseLogFile method closes the currently-open log file. |
| [CoerceValue method](..\dbgeng\nf-dbgeng-idebugcontrol3-coercevalue.md) | The CoerceValue method converts a value of one type into a value of another type. |
| [CoerceValues method](..\dbgeng\nf-dbgeng-idebugcontrol3-coercevalues.md) | The CoerceValues method converts an array of values into an array of values of different types. |
| [ConnectProcessServer method](..\dbgeng\nf-dbgeng-idebugclient5-connectprocessserver.md) | The ConnectProcessServer methods connect to a process server. |
| [ConnectProcessServerWide method](..\dbgeng\nf-dbgeng-idebugclient5-connectprocessserverwide.md) | The ConnectProcessServerWide method connects to a process server. |
| [ConnectSession method](..\dbgeng\nf-dbgeng-idebugclient5-connectsession.md) | The ConnectSession method joins the client to an existing debugger session. |
| [ControlledOutput method](..\dbgeng\nf-dbgeng-idebugcontrol3-controlledoutput.md) | The ControlledOutput method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [ControlledOutputVaList method](..\dbgeng\nf-dbgeng-idebugcontrol3-controlledoutputvalist.md) | The ControlledOutputVaList method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [ControlledOutputVaListWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-controlledoutputvalistwide.md) | The ControlledOutputVaListWide method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [ControlledOutputWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-controlledoutputwide.md) | The ControlledOutputWide method formats a string and sends the result to output callbacks that were registered with some of the engine's clients. |
| [CreateClient method](..\dbgeng\nf-dbgeng-idebugclient5-createclient.md) | The CreateClient method creates a new client object for the current thread. |
| [CreateProcess method](..\dbgeng\nf-dbgeng-idebugclient5-createprocess.md) | The CreateProcess method creates a process from the specified command line. |
| [CreateProcess method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-createprocess.md) | The CreateProcess callback method is called by the engine when a create-processdebugging event occurs in the target. |
| [CreateProcess method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-createprocess.md) | The CreateProcess callback method is called by the engine when a create-processdebugging event occurs in the target. |
| [CreateProcess2 method](..\dbgeng\nf-dbgeng-idebugclient5-createprocess2.md) | The CreateProcess2 method executes the given command to create a new process. |
| [CreateProcess2Wide method](..\dbgeng\nf-dbgeng-idebugclient5-createprocess2wide.md) | The CreateProcess2Wide method executes the specified command to create a new process. |
| [CreateProcessAndAttach method](..\dbgeng\nf-dbgeng-idebugclient5-createprocessandattach.md) | The CreateProcessAndAttach method creates a process from a specified command line, then attach to another user-mode process. |
| [CreateProcessAndAttach2 method](..\dbgeng\nf-dbgeng-idebugclient5-createprocessandattach2.md) | The CreateProcessAndAttach2 method creates a process from a specified command line, then attaches to that process or another user-mode process. |
| [CreateProcessAndAttach2Wide method](..\dbgeng\nf-dbgeng-idebugclient5-createprocessandattach2wide.md) | The CreateProcessAndAttach2Wide method creates a process from a specified command line, then attach to that process or another user-mode process. |
| [CreateProcessAndAttachWide method](..\dbgeng\nf-dbgeng-idebugclient5-createprocessandattachwide.md) | The CreateProcessAndAttachWide method creates a process from a specified command line, then attach to another user-mode process. |
| [CreateProcessWide method](..\dbgeng\nf-dbgeng-idebugclient5-createprocesswide.md) | The CreateProcessWide method creates a process from the specified command line. |
| [CreateSymbolGroup method](..\dbgeng\nf-dbgeng-idebugsymbols3-createsymbolgroup.md) | The CreateSymbolGroup method creates a new symbol group. |
| [CreateSymbolGroup2 method](..\dbgeng\nf-dbgeng-idebugsymbols3-createsymbolgroup2.md) | The CreateSymbolGroup2 method creates a new symbol group. |
| [CreateThread method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-createthread.md) | The CreateThread callback method is called by the engine when a create-threaddebugging event occurs in the target. |
| [CreateThread method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-createthread.md) | The CreateThread callback method is called by the engine when a create-threaddebugging event occurs in the target. |
| [DetachCurrentProcess method](..\dbgeng\nf-dbgeng-idebugclient5-detachcurrentprocess.md) | The DetachCurrentProcess method detaches the debugger engine from the current process, resuming all its threads. |
| [DetachProcesses method](..\dbgeng\nf-dbgeng-idebugclient5-detachprocesses.md) | The DetachProcesses method detaches the debugger engine from all processes in all targets, resuming all their threads. |
| [DisablePlmPackageDebugWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-disableplmpackagedebugwide.md) | Disables a Process Lifecycle Management (PLM) package debug. |
| [Disassemble method](..\dbgeng\nf-dbgeng-idebugcontrol3-disassemble.md) | The Disassemble method disassembles a processor instruction in the target's memory. |
| [DisassembleWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-disassemblewide.md) | The DisassembleWide method disassembles a processor instruction in the target's memory. |
| [DisconnectProcessServer method](..\dbgeng\nf-dbgeng-idebugclient5-disconnectprocessserver.md) | The DisconnectProcessServer method disconnects the debugger engine from a process server. |
| [DispatchCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-dispatchcallbacks.md) | The DispatchCallbacks method lets the debugger engine use the current thread for callbacks. |
| [EnablePlmPackageDebugWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-enableplmpackagedebugwide.md) | Enables a Process Lifecycle Management (PLM) package debug. |
| [EndEnumTagged method](..\dbgeng\nf-dbgeng-idebugdataspaces4-endenumtagged.md) | The EndEnumTagged method releases the resources used by the specified enumeration. |
| [EndInput method](..\dbgeng\nf-dbgeng-idebuginputcallbacks-endinput.md) | The EndInput callback method is called by the engine to indicate that it is no longer waiting for input. |
| [EndProcessServer method](..\dbgeng\nf-dbgeng-idebugclient5-endprocessserver.md) | The EndProcessServer method requests that a process server be shut down. |
| [EndSession method](..\dbgeng\nf-dbgeng-idebugclient5-endsession.md) | The EndSession method ends the current debugger session. |
| [EndSymbolMatch method](..\dbgeng\nf-dbgeng-idebugsymbols3-endsymbolmatch.md) | The EndSymbolMatch method releases the resources used by a symbol search. |
| [Evaluate method](..\dbgeng\nf-dbgeng-idebugcontrol3-evaluate.md) | The Evaluate method evaluates an expression, returning the result. |
| [EvaluateWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-evaluatewide.md) | The EvaluateWide method evaluates an expression, returning the result. |
| [Exception method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-exception.md) | The Exception callback method is called by the engine when an exceptiondebugging event occurs in the target. |
| [Exception method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-exception.md) | The Exception callback method is called by the engine when an exceptiondebugging event occurs in the target. |
| [Execute method](..\dbgeng\nf-dbgeng-idebugcontrol3-execute.md) | The Execute method executes the specified debugger commands. |
| [ExecuteCommandFile method](..\dbgeng\nf-dbgeng-idebugcontrol3-executecommandfile.md) | The ExecuteCommandFile method opens the specified file and executes the debugger commands that are contained within. |
| [ExecuteCommandFileWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-executecommandfilewide.md) | The ExecuteCommandFileWide method opens the specified file and executes the debugger commands that are contained within. |
| [ExecuteWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-executewide.md) | The ExecuteWide method executes the specified debugger commands. |
| [ExitDispatch method](..\dbgeng\nf-dbgeng-idebugclient5-exitdispatch.md) | The ExitDispatch method causes the DispatchCallbacks method to return. |
| [ExitProcess method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-exitprocess.md) | The ExitProcess callback method is called by the engine when an exit-processdebugging event occurs in the target. |
| [ExitProcess method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-exitprocess.md) | The ExitProcess callback method is called by the engine when an exit-processdebugging event occurs in the target. |
| [ExitThread method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-exitthread.md) | The ExitThread callback method is called by the engine when an exit-threaddebugging event occurs in the target. |
| [ExitThread method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-exitthread.md) | The ExitThread callback method is called by the engine when an exit-threaddebugging event occurs in the target. |
| [ExpandSymbol method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-expandsymbol.md) | The ExpandSymbol method adds or removes the children of a symbol from a symbol group. |
| [FillPhysical method](..\dbgeng\nf-dbgeng-idebugdataspaces4-fillphysical.md) | The FillPhysical method writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled. |
| [FillVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-fillvirtual.md) | The FillVirtual method writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled. |
| [FindSourceFile method](..\dbgeng\nf-dbgeng-idebugsymbols3-findsourcefile.md) | The FindSourceFile method searches the source path for a specified source file. |
| [FindSourceFileAndToken method](..\dbgeng\nf-dbgeng-idebugadvanced3-findsourcefileandtoken.md) | The FindSourceFileAndToken method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [FindSourceFileAndTokenWide method](..\dbgeng\nf-dbgeng-idebugadvanced3-findsourcefileandtokenwide.md) | The FindSourceFileAndTokenWide method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [FindSourceFileWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-findsourcefilewide.md) | The FindSourceFileWide method searches the source path for a specified source file. |
| [FlushCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-flushcallbacks.md) | The FlushCallbacks method forces any remaining buffered output to be delivered to the IDebugOutputCallbacks object registered with this client. |
| [Get method](..\extsfns\nf-extsfns-idebugfailureanalysis2-get.md) | The Get method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. |
| [GetActualProcessorType method](..\dbgeng\nf-dbgeng-idebugcontrol3-getactualprocessortype.md) | The GetActualProcessorType method returns the processor type of the physical processor of the computer that is running the target. |
| [GetAdder method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getadder.md) | The GetAdder method returns the client that owns the breakpoint. |
| [GetAssemblyOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-getassemblyoptions.md) | The GetAssemblyOptions method returns the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target. |
| [GetBreakpointByGuid method](..\dbgeng\nf-dbgeng-idebugcontrol5-getbreakpointbyguid.md) | The GetBreakpointByGuid method returns the breakpoint with the specified breakpoint GUID. |
| [GetBreakpointById method](..\dbgeng\nf-dbgeng-idebugcontrol3-getbreakpointbyid.md) | The GetBreakpointById method returns the breakpoint with the specified breakpoint ID. |
| [GetBreakpointById2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-getbreakpointbyid2.md) | The GetBreakpointById2 method returns the breakpoint with the specified breakpoint ID. |
| [GetBreakpointByIndex method](..\dbgeng\nf-dbgeng-idebugcontrol3-getbreakpointbyindex.md) | The GetBreakpointByIndex method returns the breakpoint located at the specified index. |
| [GetBreakpointByIndex2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-getbreakpointbyindex2.md) | The GetBreakpointByIndex2 method returns the breakpoint located at the specified index. |
| [GetBreakpointParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-getbreakpointparameters.md) | The GetBreakpointParameters method returns the parameters of one or more breakpoints. |
| [GetBuffer method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getbuffer.md) | The GetBuffer method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the entry's data block. |
| [GetCodeLevel method](..\dbgeng\nf-dbgeng-idebugcontrol3-getcodelevel.md) | The GetCodeLevel method returns the current code level and is mainly used when stepping through code. |
| [GetCommand method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getcommand.md) | The GetCommand method returns the command string that is executed when a breakpoint is triggered. |
| [GetCommandWide method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getcommandwide.md) | The GetCommand method returns the command string that is executed when a breakpoint is triggered. |
| [GetConstantName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getconstantname.md) | The GetConstantName method returns the name of the specified constant. |
| [GetConstantNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getconstantnamewide.md) | The GetConstantNameWide method returns the name of the specified constant. |
| [GetContextStackTrace method](..\dbgeng\nf-dbgeng-idebugcontrol4-getcontextstacktrace.md) | The GetContextStackTrace method returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame. |
| [GetContextStackTraceEx method](..\dbgeng\nf-dbgeng-idebugcontrol5-getcontextstacktraceex.md) | The GetContextStackTraceEx method returns the frames at the top of the call stack, starting with an arbitrary register context and returning the reconstructed register context for each stack frame. |
| [GetCurrentEventIndex method](..\dbgeng\nf-dbgeng-idebugcontrol3-getcurrenteventindex.md) | The GetCurrentEventIndex method returns the index of the current event within the current list of events for the current target, if such a list exists. |
| [GetCurrentPassCount method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getcurrentpasscount.md) | The GetCurrentPassCount method returns the remaining number of times that the target must reach the breakpoint location before the breakpoint is triggered. |
| [GetCurrentProcessDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessdataoffset.md) | The GetCurrentProcessDataOffset method returns the location of the system data structure describing the current process. |
| [GetCurrentProcessExecutableName method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessexecutablename.md) | The GetCurrentProcessExecutableName method returns the name of executable file loaded in the current process. |
| [GetCurrentProcessExecutableNameWide method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessexecutablenamewide.md) | The GetCurrentProcessExecutableNameWide method returns the name of executable file loaded in the current process. |
| [GetCurrentProcessHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
| [GetCurrentProcessHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects2-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
| [GetCurrentProcessHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects3-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
| [GetCurrentProcessHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocesshandle.md) | The GetCurrentProcessHandle method returns the system handle for the current process. |
| [GetCurrentProcessId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessid.md) | The GetCurrentProcessId method returns the engine process ID for the current process. |
| [GetCurrentProcessPeb method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocesspeb.md) | The GetCurrentProcessPeb method returns the process environment block (PEB) of the current process. |
| [GetCurrentProcessSystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocesssystemid.md) | The GetCurrentProcessSystemId method returns the system process ID of the current process. |
| [GetCurrentProcessUpTime method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentprocessuptime.md) | The GetCurrentProcessUpTime method returns the length of time the current process has been running. |
| [GetCurrentScopeFrameIndex method](..\dbgeng\nf-dbgeng-idebugsymbols3-getcurrentscopeframeindex.md) | The GetCurrentScopeFrameIndex method returns the index of the current stack frame in the call stack. |
| [GetCurrentScopeFrameIndexEx method](..\dbgeng\nf-dbgeng-idebugsymbols5-getcurrentscopeframeindexex.md) | Gets the index of the current frame. |
| [GetCurrentSystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentsystemid.md) | The GetCurrentSystemId method returns the engine target ID for the current process. |
| [GetCurrentSystemServer method](..\dbgeng\nf-dbgeng-idebugsystemobjects3-getcurrentsystemserver.md) | Gets the server for the current process. |
| [GetCurrentSystemServerName method](..\dbgeng\nf-dbgeng-idebugsystemobjects3-getcurrentsystemservername.md) | Gets the server name for the current process. |
| [GetCurrentSystemServerNameWide method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentsystemservernamewide.md) | Gets the server name for the current process. |
| [GetCurrentSystemUpTime method](..\dbgeng\nf-dbgeng-idebugcontrol3-getcurrentsystemuptime.md) | The GetCurrentSystemUpTime method returns the number of seconds the current target's computer has been running since it was last started. |
| [GetCurrentThreadDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreaddataoffset.md) | The GetCurrentThreadDataOffset method returns the location of the system data structure for the current thread. |
| [GetCurrentThreadHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreadhandle.md) | The GetCurrentThreadHandle method returns the system handle for the current thread. |
| [GetCurrentThreadId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreadid.md) | The GetCurrentThreadId method returns the engine thread ID for the current thread. |
| [GetCurrentThreadSystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreadsystemid.md) | The GetCurrentThreadSystemId method returns the system thread ID of the current thread. |
| [GetCurrentThreadTeb method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getcurrentthreadteb.md) | The GetCurrentThreadTeb method returns the location of the thread environment block (TEB) for the current thread. |
| [GetCurrentTimeDate method](..\dbgeng\nf-dbgeng-idebugcontrol3-getcurrenttimedate.md) | The GetCurrentTimeDate method returns the time of the current target. |
| [GetDataParameters method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getdataparameters.md) | The GetDataParameters method returns the parameters for a processor breakpoint. |
| [GetDebugFATagControl method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getdebugfatagcontrol.md) | The GetDebugFATagControl method gets a pointer to an IDebugFAEntryTags interface, which provides access to the tags in a DebugFailureAnalysisTags object. |
| [GetDebuggeeType method](..\dbgeng\nf-dbgeng-idebugcontrol3-getdebuggeetype.md) | The GetDebuggeeType method describes the nature of the current target. |
| [GetDebuggeeType2 method](..\dbgeng\nf-dbgeng-idebugcontrol7-getdebuggeetype2.md) | The GetDebuggeeType2 method describes the nature of the current target. |
| [GetDescription method](..\dbgeng\nf-dbgeng-idebugregisters2-getdescription.md) | The GetDescription method returns the description of a register. |
| [GetDescriptionWide method](..\dbgeng\nf-dbgeng-idebugregisters2-getdescriptionwide.md) | The GetDescriptionWide method returns the description of a register. |
| [GetDisassembleEffectiveOffset method](..\dbgeng\nf-dbgeng-idebugcontrol3-getdisassembleeffectiveoffset.md) | The GetDisassembleEffectiveOffset method returns the address of the last instruction disassembled using Disassemble. |
| [GetDumpFile method](..\dbgeng\nf-dbgeng-idebugclient5-getdumpfile.md) | The GetDumpFile method describes the files containing supporting information that were used when opening the current dump target. |
| [GetDumpFileWide method](..\dbgeng\nf-dbgeng-idebugclient5-getdumpfilewide.md) | The GetDumpFileWide method describes the files containing supporting information that were used when opening the current dump target. |
| [GetDumpFormatFlags method](..\dbgeng\nf-dbgeng-idebugcontrol3-getdumpformatflags.md) | The GetDumpFormatFlags method returns the flags that describe what information is available in a dump file target. |
| [GetEffectiveProcessorType method](..\dbgeng\nf-dbgeng-idebugcontrol3-geteffectiveprocessortype.md) | The GetEffectiveProcessorType method returns the effective processor type of the processor of the computer that is running the target. |
| [GetEngineOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-getengineoptions.md) | The GetEngineOptions method returns the engine's options. |
| [GetEventCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-geteventcallbacks.md) | The GetEventCallbacks method returns the event callbacks object registered with this client. |
| [GetEventCallbacksWide method](..\dbgeng\nf-dbgeng-idebugclient5-geteventcallbackswide.md) | The GetEventCallbacksWide method returns the event callbacks object registered with this client. |
| [GetEventFilterCommand method](..\dbgeng\nf-dbgeng-idebugcontrol3-geteventfiltercommand.md) | The GetEventFilterCommand method returns the debugger command that the engine will execute when a specified event occurs. |
| [GetEventFilterCommandWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-geteventfiltercommandwide.md) | The GetEventFilterCommandWide method returns the debugger command that the engine will execute when a specified event occurs. |
| [GetEventFilterText method](..\dbgeng\nf-dbgeng-idebugcontrol3-geteventfiltertext.md) | The GetEventFilterText method returns a short description of an event for a specific filter. |
| [GetEventFilterTextWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-geteventfiltertextwide.md) | The GetEventFilterTextWide method returns a short description of an event for a specific filter. |
| [GetEventIndexDescription method](..\dbgeng\nf-dbgeng-idebugcontrol3-geteventindexdescription.md) | The GetEventIndexDescription method describes the specified event in a static list of events for the current target. |
| [GetEventIndexDescriptionWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-geteventindexdescriptionwide.md) | The GetEventIndexDescriptionWide method describes the specified event in a static list of events for the current target. |
| [GetEventProcess method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-geteventprocess.md) | The GetEventProcess method returns the engine process ID for the process on which the last event occurred. |
| [GetEventSystem method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-geteventsystem.md) | The GetEventSystem method returns the engine target ID for the target in which the last event occurred. |
| [GetEventThread method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-geteventthread.md) | The GetEventThread method returns the engine thread ID for the thread on which the last event occurred. |
| [GetExceptionFilterParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexceptionfilterparameters.md) | The GetExceptionFilterParameters method returns the parameters for exception filters specified by exception codes or by index. |
| [GetExceptionFilterSecondCommand method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexceptionfiltersecondcommand.md) | The GetExceptionFilterSecondCommand method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [GetExceptionFilterSecondCommand method](..\dbgeng\nf-dbgeng-idebugcontrol4-getexceptionfiltersecondcommand.md) | The GetExceptionFilterSecondCommandWide method returns the command that will be executed by the debugger engine upon the second chance of a specified exception. |
| [GetExecutingProcessorType method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexecutingprocessortype.md) | The GetExecutingProcessorType method returns the executing processor type for the processor for which the last event occurred. |
| [GetExecutionStatus method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexecutionstatus.md) | The GetExecutionStatus method returns information about the execution status of the debugger engine. |
| [GetExecutionStatusEx method](..\dbgeng\nf-dbgeng-idebugcontrol6-getexecutionstatusex.md) | The GetExecutionStatusEx method returns information about the execution status of the debugger engine. |
| [GetExitCode method](..\dbgeng\nf-dbgeng-idebugclient5-getexitcode.md) | The GetExitCode method returns the exit code of the current process if that process has already run through to completion. |
| [GetExpressionSyntax method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexpressionsyntax.md) | The GetExpressionSyntax method returns the current syntax that the engine is using for evaluating expressions. |
| [GetExpressionSyntaxNames method](..\dbgeng\nf-dbgeng-idebugcontrol3-getexpressionsyntaxnames.md) | The GetExpressionSyntaxNames method returns the full and abbreviated names of an expression syntax. |
| [GetExpressionSyntaxNamesWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getexpressionsyntaxnameswide.md) | The GetExpressionSyntaxNamesWide method returns the full and abbreviated names of an expression syntax. |
| [GetExtensionByPath method](..\dbgeng\nf-dbgeng-idebugcontrol3-getextensionbypath.md) | The GetExtensionByPath method returns the handle for an already loaded extension library. |
| [GetExtensionByPathWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getextensionbypathwide.md) | The GetExtensionByPathWide method returns the handle for an already loaded extension library. |
| [GetExtensionFunction method](..\dbgeng\nf-dbgeng-idebugcontrol3-getextensionfunction.md) | The GetExtensionFunction method returns a pointer to an extension function from an extension library. |
| [GetExtensionFunctionWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getextensionfunctionwide.md) | The GetExtensionFunctionWide method returns a pointer to an extension function from an extension library. |
| [GetFailureClass method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getfailureclass.md) | The GetFailureClass method gets the failure class of a DebugFailureAnalysis object. The failure class indicates whether the debugging session that created the DebugFailureAnalysis object is a kernel mode session or a user mode session. |
| [GetFailureCode method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getfailurecode.md) | The GetFailureCode method gets the bug check code or exception code of a DebugFailureAnalysis object. |
| [GetFailureType method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getfailuretype.md) | The GetFailureType method gets the failure type of a DebugFailureAnalysis object. The failure type indicates whether the code being analyzed was running in kernel mode or user mode. |
| [GetFieldName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldname.md) | The GetFieldName method returns the name of a field within a structure. |
| [GetFieldNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldnamewide.md) | The GetFieldNameWide method returns the name of a field within a structure. |
| [GetFieldOffset method](..\dbgeng\nf-dbgeng-idebugsymbols-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [GetFieldOffset method](..\dbgeng\nf-dbgeng-idebugsymbols2-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [GetFieldOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldoffset.md) | The GetFieldOffset method returns the offset of a field from the base address of an instance of a type. |
| [GetFieldOffset method](..\dbgeng\nf-dbgeng-idebugsymbols4-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [GetFieldOffset method](..\dbgeng\nf-dbgeng-idebugsymbols5-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [GetFieldOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldoffsetwide.md) | The GetFieldOffsetWide method returns the offset of a field from the base address of an instance of a type. |
| [GetFieldTypeAndOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldtypeandoffset.md) | The GetFieldTypeAndOffset method returns the type of a field and its offset within a container. |
| [GetFieldTypeAndOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfieldtypeandoffsetwide.md) | The GetFieldTypeAndOffsetWide method returns the type of a field and its offset within a container. |
| [GetFlags method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getflags.md) | The GetFlags method returns the flags for a breakpoint. |
| [GetFrameOffset method](..\dbgeng\nf-dbgeng-idebugregisters2-getframeoffset.md) | The GetFrameOffset method returns the location of the stack frame for the current function. |
| [GetFrameOffset2 method](..\dbgeng\nf-dbgeng-idebugregisters2-getframeoffset2.md) | The GetFrameOffset2 method returns the location of the stack frame for the current function. |
| [GetFunctionEntryByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getfunctionentrybyoffset.md) | The GetFunctionEntryByOffset method returns the function entry information for a function. |
| [GetGuid method](..\dbgeng\nf-dbgeng-idebugbreakpoint3-getguid.md) | Returns a GUID for the breakpoint. |
| [GetId method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getid.md) | The GetId method returns a breakpoint ID, which is the engine's unique identifier for a breakpoint. |
| [GetIdentity method](..\dbgeng\nf-dbgeng-idebugclient5-getidentity.md) | The GetIdentity method returns a string describing the computer and user this client represents. |
| [GetIdentityWide method](..\dbgeng\nf-dbgeng-idebugclient5-getidentitywide.md) | The GetIdentityWide method returns a string describing the computer and user this client represents. |
| [GetImagePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-getimagepath.md) | The GetImagePath method returns the executable image path. |
| [GetImagePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getimagepathwide.md) | The GetImagePathWide method returns the executable image path. |
| [GetImplicitProcessDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getimplicitprocessdataoffset.md) | The GetImplicitProcessDataOffset method returns the implicit process for the current target. |
| [GetImplicitThreadDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getimplicitthreaddataoffset.md) | The GetImplicitThreadDataOffset method returns the implicit thread for the current process. |
| [GetIndexByName method](..\dbgeng\nf-dbgeng-idebugregisters2-getindexbyname.md) | The GetIndexByName method returns the index of the named register. |
| [GetIndexByNameWide method](..\dbgeng\nf-dbgeng-idebugregisters2-getindexbynamewide.md) | The GetIndexByNameWide method returns the index of the named register. |
| [GetInputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getinputcallbacks.md) | The GetInputCallbacks method returns the input callbacks object registered with this client. |
| [GetInstructionOffset method](..\dbgeng\nf-dbgeng-idebugregisters2-getinstructionoffset.md) | The GetInstructionOffset method returns the location of the current thread's current instruction. |
| [GetInstructionOffset2 method](..\dbgeng\nf-dbgeng-idebugregisters2-getinstructionoffset2.md) | The GetInstructionOffset2 method returns the location of the current thread's current instruction. |
| [GetInterestMask method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-getinterestmask.md) | The GetInterestMask callback method is called to determine which events the IDebugEventCallbacks object is interested in. The engine calls GetInterestMask when the object is registered with a client by using SetEventCallbacks. |
| [GetInterestMask method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-getinterestmask.md) | The GetInterestMask callback method is called to determine which events the IDebugEventCallbacksWide object is interested in. The engine calls GetInterestMask when the object is registered with a client by using SetEventCallbacks. |
| [GetInterestMask method](..\dbgeng\nf-dbgeng-idebugoutputcallbacks2-getinterestmask.md) | Allows the callback object to describe which kinds of output notifications it wants to receive. |
| [GetInterrupt method](..\dbgeng\nf-dbgeng-idebugcontrol3-getinterrupt.md) | The GetInterrupt method checks whether a user interrupt was issued. |
| [GetInterruptTimeout method](..\dbgeng\nf-dbgeng-idebugcontrol3-getinterrupttimeout.md) | The GetInterruptTimeout method returns the number of seconds that the engine will wait when requesting a break into the debugger. |
| [GetKernelConnectionOptions method](..\dbgeng\nf-dbgeng-idebugclient5-getkernelconnectionoptions.md) | The GetKernelConnectionOptions method returns the connection options for the current kernel target. |
| [GetKernelConnectionOptionsWide method](..\dbgeng\nf-dbgeng-idebugclient5-getkernelconnectionoptionswide.md) | The GetKernelConnectionOptionsWide method returns the connection options for the current kernel target. |
| [GetLastEventInformation method](..\dbgeng\nf-dbgeng-idebugcontrol3-getlasteventinformation.md) | The GetLastEventInformation method returns information about the last event that occurred in a target. |
| [GetLastEventInformationWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getlasteventinformationwide.md) | The GetLastEventInformationWide method returns information about the last event that occurred in a target. |
| [GetLineByInlineContext method](..\dbgeng\nf-dbgeng-idebugsymbols4-getlinebyinlinecontext.md) | Gets a line by inline context. |
| [GetLineByInlineContextWide method](..\dbgeng\nf-dbgeng-idebugsymbols4-getlinebyinlinecontextwide.md) | Gets a line by inline context. |
| [GetLineByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getlinebyoffset.md) | The GetLineByOffset method returns the source filename and the line number within the source file of an instruction in the target. |
| [GetLineByOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getlinebyoffsetwide.md) | The GetLineByOffsetWide method returns the source filename and the line number within the source file of an instruction in the target. |
| [GetLogFile method](..\dbgeng\nf-dbgeng-idebugcontrol3-getlogfile.md) | The GetLogFile method returns the name of the currently open log file. |
| [GetLogFile2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-getlogfile2.md) | The GetLogFile2 method returns the name of the currently open log file. |
| [GetLogFile2Wide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getlogfile2wide.md) | The GetLogFile2Wide method returns the name of the currently open log file. |
| [GetLogFileWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getlogfilewide.md) | The GetLogFileWide method returns the name of the currently open log file. |
| [GetLogMask method](..\dbgeng\nf-dbgeng-idebugcontrol3-getlogmask.md) | The GetLogMask method returns the output mask for the currently open log file. |
| [GetManagedStatus method](..\dbgeng\nf-dbgeng-idebugcontrol4-getmanagedstatus.md) | Provides feedback on the engine's use of the runtime debugging APIs provided by the common language runtime (CLR). |
| [GetManagedStatusWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getmanagedstatuswide.md) | Provides feedback as a Unicode character string on the engine's use of the runtime debugging APIs provided by the common language runtime (CLR). |
| [GetMatchThreadId method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getmatchthreadid.md) | The GetMatchThreadId method returns the engine thread ID of the thread that can trigger a breakpoint. |
| [GetModuleByIndex method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebyindex.md) | The GetModuleByIndex method returns the location of the module with the specified index. |
| [GetModuleByModuleName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebymodulename.md) | The GetModuleByModuleName method searches through the target's modules for one with the specified name. |
| [GetModuleByModuleName2 method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebymodulename2.md) | The GetModuleByModuleName2 method searches through the process's modules for one with the specified name. |
| [GetModuleByModuleName2Wide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebymodulename2wide.md) | The GetModuleByModuleName2Wide method searches through the process's modules for one with the specified name. |
| [GetModuleByModuleNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebymodulenamewide.md) | The GetModuleByModuleNameWide method searches through the target's modules for one with the specified name. |
| [GetModuleByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebyoffset.md) | The GetModuleByOffset method searches through the target's modules for one whose memory allocation includes the specified location. |
| [GetModuleByOffset2 method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulebyoffset2.md) | The GetModuleByOffset2 method searches through the process's modules for one whose memory allocation includes the specified location. |
| [GetModuleNameString method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulenamestring.md) | The GetModuleNameString method returns the name of the specified module. |
| [GetModuleNameStringWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulenamestringwide.md) | The GetModuleNameStringWide method returns the name of the specified module. |
| [GetModuleNames method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmodulenames.md) | The GetModuleNames method returns the names of the specified module. |
| [GetModuleParameters method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmoduleparameters.md) | The GetModuleParameters method returns parameters for modules in the target. |
| [GetModuleVersionInformation method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmoduleversioninformation.md) | The GetModuleVersionInformation method returns version information for the specified module. |
| [GetModuleVersionInformationWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getmoduleversioninformationwide.md) | The GetModuleVersionInformationWide method returns version information for the specified module. |
| [GetNameByInlineContext method](..\dbgeng\nf-dbgeng-idebugsymbols4-getnamebyinlinecontext.md) | Gets a name by inline context. |
| [GetNameByInlineContextWide method](..\dbgeng\nf-dbgeng-idebugsymbols4-getnamebyinlinecontextwide.md) | Gets a name by inline context. |
| [GetNameByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnamebyoffset.md) | The GetNameByOffset method returns the name of the symbol at the specified location in the target's virtual address space. |
| [GetNameByOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnamebyoffsetwide.md) | The GetNameByOffsetWide method returns the name of the symbol at the specified location in the target's virtual address space. |
| [GetNearInstruction method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnearinstruction.md) | The GetNearInstruction method returns the location of a processor instruction relative to a given location. |
| [GetNearNameByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnearnamebyoffset.md) | The GetNearNameByOffset method returns the name of a symbol that is located near the specified location. |
| [GetNearNameByOffsetWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnearnamebyoffsetwide.md) | The GetNearNameByOffsetWide method returns the name of a symbol that is located near the specified location. |
| [GetNext method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getnext.md) | The GetNext method searches a DebugFailureAnalysis object for the next FA entry, after a given FA entry, that satisfies conditions specified by the Tag and TagMask parameters. |
| [GetNextDifferentlyValidOffsetVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getnextdifferentlyvalidoffsetvirtual.md) | The GetNextDifferentlyValidOffsetVirtual method returns the offset of the next address whose validity might be different from the validity of the specified address. |
| [GetNextSymbolMatch method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnextsymbolmatch.md) | The GetNextSymbolMatch method returns the next symbol found in a symbol search. |
| [GetNextSymbolMatchWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnextsymbolmatchwide.md) | The GetNextSymbolMatchWide method returns the next symbol found in a symbol search. |
| [GetNextTagged method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getnexttagged.md) | The GetNextTagged method returns the GUID for the next block of tagged data in the enumeration. |
| [GetNotifyEventHandle method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnotifyeventhandle.md) | The GetNotifyEventHandle method receives the handle of the event that will be signaled after the next exception in a target. |
| [GetNumberBreakpoints method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberbreakpoints.md) | The GetNumberBreakpoints method returns the number of breakpoints for the current process. |
| [GetNumberDumpFiles method](..\dbgeng\nf-dbgeng-idebugclient5-getnumberdumpfiles.md) | The GetNumberDumpFiles method returns the number of files containing supporting information that were used when opening the current dump target. |
| [GetNumberEventCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getnumbereventcallbacks.md) | The GetNumberEventCallbacks method returns the number of event callbacks that are interested in the given events. |
| [GetNumberEventFilters method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumbereventfilters.md) | The GetNumberEventFilters method returns the number of event filters currently used by the engine. |
| [GetNumberEvents method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberevents.md) | The GetNumberEvents method returns the number of events for the current target, if the number of events is fixed. |
| [GetNumberExpressionSyntaxes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberexpressionsyntaxes.md) | The GetNumberExpressionSyntaxes method returns the number of expression syntaxes that are supported by the engine. |
| [GetNumberInputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getnumberinputcallbacks.md) | The GetNumberInputCallbacks method returns the number of input callbacks registered over all clients. |
| [GetNumberModules method](..\dbgeng\nf-dbgeng-idebugsymbols3-getnumbermodules.md) | The GetNumberModules method returns the number of modules in the current process's module list. |
| [GetNumberOutputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getnumberoutputcallbacks.md) | The GetNumberOutputCallbacks method returns the number of output callbacks registered over all clients. |
| [GetNumberPossibleExecutingProcessorTypes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberpossibleexecutingprocessortypes.md) | The GetNumberPossibleExecutingProcessorTypes method returns the number of processor types that are supported by the computer running the current target. |
| [GetNumberProcesses method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getnumberprocesses.md) | The GetNumberProcesses method returns the number of processes for the current target. |
| [GetNumberProcessors method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumberprocessors.md) | The GetNumberProcessors method returns the number of processors on the computer running the current target. |
| [GetNumberPseudoRegisters method](..\dbgeng\nf-dbgeng-idebugregisters2-getnumberpseudoregisters.md) | The GetNumberPseudoRegisters method returns the number of pseudo-registers that are maintained by the debugger engine. |
| [GetNumberRegisters method](..\dbgeng\nf-dbgeng-idebugregisters2-getnumberregisters.md) | The GetNumberRegisters method returns the number of registers on the target computer. |
| [GetNumberSupportedProcessorTypes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumbersupportedprocessortypes.md) | The GetNumberSupportedProcessorTypes method returns the number of processor types supported by the engine. |
| [GetNumberSymbols method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getnumbersymbols.md) | The GetNumberSymbols method returns the number of symbols that are contained in a symbol group. |
| [GetNumberSystems method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getnumbersystems.md) | The GetNumberSystems method returns the number of targets to which the engine is currently connected. |
| [GetNumberTextReplacements method](..\dbgeng\nf-dbgeng-idebugcontrol3-getnumbertextreplacements.md) | The GetNumberTextReplacements method returns the number of currently defined user-named and automatic aliases. |
| [GetNumberThreads method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getnumberthreads.md) | The GetNumberThreads method returns the number of threads in the current process. |
| [GetOffset method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getoffset.md) | The GetOffset method returns the location that triggers a breakpoint. |
| [GetOffsetByLine method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsetbyline.md) | The GetOffsetByLine method returns the location of the instruction that corresponds to a specified line in the source code. |
| [GetOffsetByLineWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsetbylinewide.md) | The GetOffsetByLineWide method returns the location of the instruction that corresponds to a specified line in the source code. |
| [GetOffsetByName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsetbyname.md) | The GetOffsetByName method returns the location of a symbol identified by name. |
| [GetOffsetByNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsetbynamewide.md) | The GetOffsetByNameWide method returns the location of a symbol identified by name. |
| [GetOffsetExpression method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getoffsetexpression.md) | The GetOffsetExpression methods return the expression string that evaluates to the location that triggers a breakpoint. |
| [GetOffsetExpressionWide method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getoffsetexpressionwide.md) | The GetOffsetExpressionWide method returns the expression string that evaluates to the location that triggers a breakpoint. |
| [GetOffsetInformation method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getoffsetinformation.md) | The GetOffsetInformation method provides general information about an address in a process's data space. |
| [GetOffsetTypeId method](..\dbgeng\nf-dbgeng-idebugsymbols3-getoffsettypeid.md) | The GetOffsetTypeId method returns the type ID of the symbol closest to the specified memory location. |
| [GetOtherOutputMask method](..\dbgeng\nf-dbgeng-idebugclient5-getotheroutputmask.md) | The GetOtherOutputMask method returns the output mask for another client. |
| [GetOutputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-getoutputcallbacks.md) | The GetOutputCallbacks method returns the output callbacks object registered with the client. |
| [GetOutputCallbacksWide method](..\dbgeng\nf-dbgeng-idebugclient5-getoutputcallbackswide.md) | The GetOutputCallbacksWide method returns the output callbacks object registered with the client. |
| [GetOutputLinePrefix method](..\dbgeng\nf-dbgeng-idebugclient-getoutputlineprefix.md) | Gets the prefix used for multiple lines of output. |
| [GetOutputLinePrefixWide method](..\dbgeng\nf-dbgeng-idebugclient5-getoutputlineprefixwide.md) | Gets a Unicode character string prefix for output lines. |
| [GetOutputMask method](..\dbgeng\nf-dbgeng-idebugclient5-getoutputmask.md) | The GetOutputMask method returns the output mask currently set for the client. |
| [GetOutputWidth method](..\dbgeng\nf-dbgeng-idebugclient-getoutputwidth.md) | Gets the width of an output line for commands that produce formatted output. |
| [GetPageSize method](..\dbgeng\nf-dbgeng-idebugcontrol3-getpagesize.md) | The GetPageSize method returns the page size for the effective processor mode. |
| [GetParameters method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getparameters.md) | The GetParameters method returns the parameters for a breakpoint. |
| [GetPassCount method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-getpasscount.md) | The GetPassCount method returns the number of times that the target was originally required to reach the breakpoint location before the breakpoint is triggered. |
| [GetPossibleExecutingProcessorTypes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getpossibleexecutingprocessortypes.md) | The GetPossibleExecutingProcessorTypes method returns the processor types that are supported by the computer running the current target. |
| [GetProcessIdByDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidbydataoffset.md) | The GetProcessIdByDataOffset method returns the engine process ID for the specified process. The process is specified by its data offset. |
| [GetProcessIdByHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidbyhandle.md) | The GetProcessIdByHandle method returns the engine process ID for the specified process. The process is specified by its system handle. |
| [GetProcessIdByPeb method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidbypeb.md) | The GetProcessIdByPeb method returns the engine process ID for the specified process. The process is specified by its process environment block (PEB). |
| [GetProcessIdBySystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidbysystemid.md) | The GetProcessIdBySystemId method returns the engine process ID for a process specified by its system process ID. |
| [GetProcessIdsByIndex method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getprocessidsbyindex.md) | The GetProcessIdsByIndex method returns the engine process ID and system process ID for the specified processes in the current target. |
| [GetProcessOptions method](..\dbgeng\nf-dbgeng-idebugclient5-getprocessoptions.md) | The GetProcessOptions method retrieves the process options affecting the current process. |
| [GetProcessorTypeNames method](..\dbgeng\nf-dbgeng-idebugcontrol3-getprocessortypenames.md) | The GetProcessorTypeNames method returns the full name and abbreviated name of the specified processor type. |
| [GetProcessorTypeNamesWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getprocessortypenameswide.md) | The GetProcessorTypeNamesWide method returns the full name and abbreviated name of the specified processor type. |
| [GetPromptText method](..\dbgeng\nf-dbgeng-idebugcontrol3-getprompttext.md) | The GetPromptText method returns the standard prompt text that will be prepended to the formatted output specified in the OutputPrompt and OutputPromptVaList methods. |
| [GetPromptTextWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getprompttextwide.md) | The GetPromptTextWide method returns the standard prompt text that will be prepended to the formatted output specified in the OutputPrompt and OutputPromptVaList methods. |
| [GetProperties method](..\extsfns\nf-extsfns-idebugfaentrytags-getproperties.md) | The GetProperties method gets the name or description (or both) of a tag in a DebugFailureAnalysisTags object. |
| [GetPseudoDescription method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudodescription.md) | The GetPseudoDescription method returns a description of a pseudo-register, including its name and type. |
| [GetPseudoDescriptionWide method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudodescriptionwide.md) | The GetPseudoDescriptionWide method returns a description of a pseudo-register, including its name and type. |
| [GetPseudoIndexByName method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudoindexbyname.md) | The GetPseudoIndexByName method returns the index of a pseudo-register. |
| [GetPseudoIndexByNameWide method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudoindexbynamewide.md) | The GetPseudoIndexByNameWide method returns the index of a pseudo-register. |
| [GetPseudoValues method](..\dbgeng\nf-dbgeng-idebugregisters2-getpseudovalues.md) | The GetPseudoValues method returns the values of a number of pseudo-registers. |
| [GetQuitLockString method](..\dbgeng\nf-dbgeng-idebugclient5-getquitlockstring.md) | Gets a quit lock string. |
| [GetQuitLockStringWide method](..\dbgeng\nf-dbgeng-idebugclient5-getquitlockstringwide.md) | Gets a Unicode character quit lock string. |
| [GetRadix method](..\dbgeng\nf-dbgeng-idebugcontrol3-getradix.md) | The GetRadix method returns the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [GetReturnOffset method](..\dbgeng\nf-dbgeng-idebugcontrol3-getreturnoffset.md) | The GetReturnOffset method returns the return address for the current function. |
| [GetRunningProcessDescription method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocessdescription.md) | The GetRunningProcessDescription method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [GetRunningProcessDescriptionWide method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocessdescriptionwide.md) | The GetRunningProcessDescriptionWide method returns a description of the process that includes the executable image name, the service names, the MTS package names, and the command line. |
| [GetRunningProcessSystemIdByExecutableName method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocesssystemidbyexecutablename.md) | The GetRunningProcessSystemIdByExecutableName method searches for a process with a given executable file name and return its process ID. |
| [GetRunningProcessSystemIdByExecutableNameWide method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocesssystemidbyexecutablenamewide.md) | The GetRunningProcessSystemIdByExecutableNameWide method searches for a process with a given executable file name and return its process ID. |
| [GetRunningProcessSystemIds method](..\dbgeng\nf-dbgeng-idebugclient5-getrunningprocesssystemids.md) | The GetRunningProcessSystemIds method returns the process IDs for each running process. |
| [GetScope method](..\dbgeng\nf-dbgeng-idebugsymbols3-getscope.md) | The GetScope method returns information about the current scope. |
| [GetScopeEx method](..\dbgeng\nf-dbgeng-idebugsymbols4-getscopeex.md) | Gets the scope as an extended frame structure. |
| [GetScopeSymbolGroup method](..\dbgeng\nf-dbgeng-idebugsymbols3-getscopesymbolgroup.md) | The GetScopeSymbolGroup method returns a symbol group containing the symbols in the current target's scope. |
| [GetScopeSymbolGroup2 method](..\dbgeng\nf-dbgeng-idebugsymbols3-getscopesymbolgroup2.md) | The GetScopeSymbolGroup2 method returns a symbol group containing the symbols in the current target's scope. |
| [GetSourceEntriesByLine method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentriesbyline.md) | The GetSourceEntriesByLine method queries symbol information and returns locations in the target's memory that correspond to lines in a source file. |
| [GetSourceEntriesByLineWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentriesbylinewide.md) | The GetSourceEntriesByLineWide method queries symbol information and returns locations in the target's memory that correspond to lines in a source file. |
| [GetSourceEntriesByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentriesbyoffset.md) | Queries symbol information and returns locations in the target's memory by using an offset. |
| [GetSourceEntryBySourceEntry method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentrybysourceentry.md) | Allows navigation within the source entries. |
| [GetSourceEntryOffsetRegions method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentryoffsetregions.md) | Returns all memory regions known to be associated with a source entry. |
| [GetSourceEntryString method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentrystring.md) | Queries symbol information and returns locations in the target's memory. |
| [GetSourceEntryStringWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourceentrystringwide.md) | Queries symbol information and returns locations in the target's memory. |
| [GetSourceFileInformation method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsourcefileinformation.md) | The GetSourceFileInformation method returns specified information about a source file. |
| [GetSourceFileInformationWide method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsourcefileinformationwide.md) | The GetSourceFileInformationWide method returns specified information about a source file. |
| [GetSourceFileLineOffsets method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcefilelineoffsets.md) | The GetSourceFileLineOffsets method maps each line in a source file to a location in the target's memory. |
| [GetSourceFileLineOffsetsWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcefilelineoffsetswide.md) | The GetSourceFileLineOffsetsWide method maps each line in a source file to a location in the target's memory. |
| [GetSourcePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcepath.md) | The GetSourcePath method returns the source path. |
| [GetSourcePathElement method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcepathelement.md) | The GetSourcePathElement method returns an element from the source path. |
| [GetSourcePathElementWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcepathelementwide.md) | The GetSourcePathElementWide method returns an element from the source path. |
| [GetSourcePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsourcepathwide.md) | The GetSourcePathWide method returns the source path. |
| [GetSpecificFilterArgument method](..\dbgeng\nf-dbgeng-idebugcontrol3-getspecificfilterargument.md) | The GetSpecificFilterArgument method returns the value of filter argument for thespecific filters that have an argument. |
| [GetSpecificFilterArgumentWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getspecificfilterargumentwide.md) | The GetSpecificFilterArgumentWide method returns the value of filter argument for thespecific filters that have an argument. |
| [GetSpecificFilterParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-getspecificfilterparameters.md) | The GetSpecificFilterParameters method returns the parameters for specific event filters. |
| [GetStackOffset method](..\dbgeng\nf-dbgeng-idebugregisters2-getstackoffset.md) | The GetStackOffset method returns the current thread's current stack location. |
| [GetStackOffset2 method](..\dbgeng\nf-dbgeng-idebugregisters2-getstackoffset2.md) | The GetStackOffset2 method returns the current thread's current stack location. |
| [GetStackTrace method](..\dbgeng\nf-dbgeng-idebugcontrol3-getstacktrace.md) | The GetStackTrace method returns the frames at the top of the specified call stack. |
| [GetStackTraceEx method](..\dbgeng\nf-dbgeng-idebugcontrol5-getstacktraceex.md) | The GetStackTraceEx method returns the frames at the top of the specified call stack. The GetStackTraceEx method provides inline frame support. For more information about working with inline functions, see Debugging Optimized Code and Inline Functions. |
| [GetStoredEventInformation method](..\dbgeng\nf-dbgeng-idebugcontrol4-getstoredeventinformation.md) | The GetStoredEventInformation method retrieves information about an event of interest available in the current target. |
| [GetString method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getstring.md) | The GetString method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the ANSI string value from the entry's data block. |
| [GetSupportedProcessorTypes method](..\dbgeng\nf-dbgeng-idebugcontrol3-getsupportedprocessortypes.md) | The GetSupportedProcessorTypes method returns the processor types supported by the debugger engine. |
| [GetSymbolEntriesByName method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentriesbyname.md) | The GetSymbolEntriesByName method returns the symbols whose names match a given pattern. |
| [GetSymbolEntriesByNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentriesbynamewide.md) | The GetSymbolEntriesByNameWide method returns the symbols whose names match a given pattern. |
| [GetSymbolEntriesByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentriesbyoffset.md) | The GetSymbolEntriesByOffset method returns the symbols which are located at a specified address. |
| [GetSymbolEntryBySymbolEntry method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentrybysymbolentry.md) | Allows navigation within the symbol entry hierarchy. |
| [GetSymbolEntryByToken method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentrybytoken.md) | Looks up a symbol by using a managed metadata token. |
| [GetSymbolEntryInformation method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolentryinformation.md) | The GetSymbolEntryInformation method returns information about a symbol in a symbol group. |
| [GetSymbolEntryInformation method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentryinformation.md) | The GetSymbolEntryInformation method returns the symbol entry information for a symbol. |
| [GetSymbolEntryOffsetRegions method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentryoffsetregions.md) | Returns all the memory regions known to be associated with a symbol. |
| [GetSymbolEntryString method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentrystring.md) | The GetSymbolEntryString method returns string information for the specified symbol. |
| [GetSymbolEntryStringWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolentrystringwide.md) | The GetSymbolEntryStringWide method returns string information for the specified symbol. |
| [GetSymbolInformation method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsymbolinformation.md) | The GetSymbolInformation method returns specified information about a symbol. |
| [GetSymbolInformationWide method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsymbolinformationwide.md) | The SetSymbolInformationWide method returns specified information about a symbol. |
| [GetSymbolInformationWideEx method](..\dbgeng\nf-dbgeng-idebugadvanced4-getsymbolinformationwideex.md) | The GetSymbolInformationWideEx method returns specified information about a symbol. |
| [GetSymbolModule method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolmodule.md) | The GetSymbolModule method returns the base address of module which contains the specified symbol. |
| [GetSymbolModuleWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolmodulewide.md) | The GetSymbolModuleWide method returns the base address of module which contains the specified symbol. |
| [GetSymbolName method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolname.md) | The GetSymbolName method returns the name of a symbol in a symbol group. |
| [GetSymbolNameWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolnamewide.md) | The GetSymbolNameWide method returns the name of a symbol in a symbol group. |
| [GetSymbolOffset method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymboloffset.md) | The GetSymbolOffset method retrieves the location in the process's virtual address space of a symbol in a symbol group, if the symbol has an absolute address. |
| [GetSymbolOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymboloptions.md) | The GetSymbolOptions method returns the engine's global symbol options. |
| [GetSymbolParameters method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolparameters.md) | The GetSymbolParameters method returns the symbol parameters that describe the specified symbols in a symbol group. |
| [GetSymbolPath method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolpath.md) | The GetSymbolPath method returns the symbol path. |
| [GetSymbolPathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymbolpathwide.md) | The GetSymbolPathWide method returns the symbol path. |
| [GetSymbolRegister method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolregister.md) | The GetSymbolRegister method returns the register that contains the value or a pointer to the value of a symbol in a symbol group. |
| [GetSymbolSize method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolsize.md) | The GetSymbolSize method returns the size of a symbol's value. |
| [GetSymbolTypeId method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymboltypeid.md) | The GetSymbolTypeId method returns the type ID and module of the specified symbol. |
| [GetSymbolTypeIdWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-getsymboltypeidwide.md) | The GetSymbolTypeIdWide method returns the type ID and module of the specified symbol. |
| [GetSymbolTypeName method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymboltypename.md) | The GetSymbolTypeName methods return the name of the specified symbol's type. |
| [GetSymbolTypeNameWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymboltypenamewide.md) | The GetSymbolTypeNameWide method returns the name of the specified symbol's type. |
| [GetSymbolValueText method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolvaluetext.md) | The GetSymbolValueText method returns a string that represents the value of a symbol. |
| [GetSymbolValueTextWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-getsymbolvaluetextwide.md) | The GetSymbolValueTextWide method returns a string that represents the value of a symbol. |
| [GetSynchronizationStatus method](..\dbgeng\nf-dbgeng-idebugcontrol6-getsynchronizationstatus.md) | The GetSynchronizationStatus method returns information about the synchronization status of the debugger engine. |
| [GetSystemByServer method](..\dbgeng\nf-dbgeng-idebugsystemobjects3-getsystembyserver.md) | Gets the system for a server. |
| [GetSystemErrorControl method](..\dbgeng\nf-dbgeng-idebugcontrol3-getsystemerrorcontrol.md) | The GetSystemErrorControl method returns the control values for handling system errors. |
| [GetSystemIdsByIndex method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getsystemidsbyindex.md) | The GetSystemIdsByIndex method returns the engine target IDs for the specified targets. |
| [GetSystemObjectInformation method](..\dbgeng\nf-dbgeng-idebugadvanced3-getsystemobjectinformation.md) | The GetSystemObjectInformation method returns information about operating system objects on the target. |
| [GetSystemVersion method](..\dbgeng\nf-dbgeng-idebugcontrol3-getsystemversion.md) | The GetSystemVersion method returns information that identifies the operating system on the computer that is running the current target. |
| [GetSystemVersionString method](..\dbgeng\nf-dbgeng-idebugcontrol4-getsystemversionstring.md) | The GetSystemVersionString method returns a string that describes the target's operating system version. |
| [GetSystemVersionStringWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-getsystemversionstringwide.md) | The GetSystemVersionStringWide method returns a string that describes the target's operating system version. |
| [GetSystemVersionValues method](..\dbgeng\nf-dbgeng-idebugcontrol4-getsystemversionvalues.md) | The GetSystemVersionValues method returns version number information for the current target. |
| [GetTagByName method](..\extsfns\nf-extsfns-idebugfaentrytags-gettagbyname.md) | The GetTagByName method searches for a tag that has a specified name. |
| [GetTextMacro method](..\dbgeng\nf-dbgeng-idebugcontrol3-gettextmacro.md) | The GetTextMacro method returns the value of a fixed-name alias. |
| [GetTextMacroWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-gettextmacrowide.md) | The GetTextMacroWide method returns the value of a fixed-name alias. |
| [GetTextReplacement method](..\dbgeng\nf-dbgeng-idebugcontrol3-gettextreplacement.md) | The GetTextReplacement method returns the value of a user-named alias or an automatic alias. |
| [GetTextReplacementWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-gettextreplacementwide.md) | The GetTextReplacementWide method returns the value of a user-named alias or an automatic alias. |
| [GetThreadContext method](..\dbgeng\nf-dbgeng-idebugadvanced3-getthreadcontext.md) | The GetThreadContext method returns the current thread context. |
| [GetThreadIdByDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbydataoffset.md) | The GetThreadIdByDataOffset method returns the engine thread ID for the specified thread. The thread is specified by its system data structure. |
| [GetThreadIdByHandle method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbyhandle.md) | The GetThreadIdByHandle method returns the engine thread ID for the specified thread. The thread is specified by its system handle. |
| [GetThreadIdByProcessor method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbyprocessor.md) | The GetThreadIdByProcessor method returns the engine thread ID for the kernel-modevirtual thread corresponding to the specified processor. |
| [GetThreadIdBySystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbysystemid.md) | The GetThreadIdBySystemId method returns the engine thread ID for the specified thread. The thread is specified by its system thread ID. |
| [GetThreadIdByTeb method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidbyteb.md) | The GetThreadIdByTeb method returns the engine thread ID of the specified thread. The thread is specified by its thread environment block (TEB). |
| [GetThreadIdsByIndex method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-getthreadidsbyindex.md) | The GetThreadIdsByIndex method returns the engine and system thread IDs for the specified threads in the current process. |
| [GetTotalNumberThreads method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-gettotalnumberthreads.md) | The GetTotalNumberThreads method returns the total number of threads for all the processes in the current target, in addition to the largest number of threads in any process for the current target. |
| [GetTotalNumberThreadsAndProcesses method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-gettotalnumberthreadsandprocesses.md) | The GetTotalNumberThreadsAndProcesses method returns the total number of threads and processes in all the targets the engine is attached to, in addition to the largest number of threads and processes in a target. |
| [GetType method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-gettype.md) | The GetType method returns the type of the breakpoint and the type of the processor that a breakpoint is set for. |
| [GetType method](..\extsfns\nf-extsfns-idebugfaentrytags-gettype.md) | The GetType method gets the data type that is associated with a tag in a DebugFailureAnalysisTags object. |
| [GetTypeId method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypeid.md) | The GetTypeId method looks up the specified type and return its type ID. |
| [GetTypeIdWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypeidwide.md) | The GetTypeIdWide method looks up the specified type and return its type ID. |
| [GetTypeName method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypename.md) | The GetTypeName method returns the name of the type symbol specified by its type ID and module. |
| [GetTypeNameWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypenamewide.md) | The GetTypeNameWide method returns the name of the type symbol specified by its type ID and module. |
| [GetTypeOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypeoptions.md) | The GetTypeOptions method returns the type formatting options for output generated by the engine. |
| [GetTypeSize method](..\dbgeng\nf-dbgeng-idebugsymbols3-gettypesize.md) | The GetTypeSize method returns the number of bytes of memory an instance of the specified type requires. |
| [GetUlong method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getulong.md) | The GetUlong method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the ULONG value from the entry's data block. |
| [GetUlong64 method](..\extsfns\nf-extsfns-idebugfailureanalysis2-getulong64.md) | The GetUlong64 method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it gets the ULONG64 value from the entry's data block. |
| [GetValidRegionVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getvalidregionvirtual.md) | The GetValidRegionVirtual method locates the first valid region of memory in a specified memory range. |
| [GetValue method](..\dbgeng\nf-dbgeng-idebugregisters2-getvalue.md) | The GetValue method gets the value of one of the target's registers. |
| [GetValues method](..\dbgeng\nf-dbgeng-idebugregisters2-getvalues.md) | The GetValues method gets the value of several of the target's registers. |
| [GetValues2 method](..\dbgeng\nf-dbgeng-idebugregisters2-getvalues2.md) | The GetValues2 method fetches the value of several of the target's registers. |
| [GetVirtualTranslationPhysicalOffsets method](..\dbgeng\nf-dbgeng-idebugdataspaces4-getvirtualtranslationphysicaloffsets.md) | The GetVirtualTranslationPhysicalOffsets method returns the physical addresses of the system paging structures at different levels of the paging hierarchy. |
| [GetWindbgExtensionApis32 method](..\dbgeng\nf-dbgeng-idebugcontrol3-getwindbgextensionapis32.md) | The GetWindbgExtensionApis32 method returns a structure that facilitates using the WdbgExts API. |
| [GetWindbgExtensionApis64 method](..\dbgeng\nf-dbgeng-idebugcontrol3-getwindbgextensionapis64.md) | The GetWindbgExtensionApis64 method returns a structure that facilitates using the WdbgExts API. |
| [Input method](..\dbgeng\nf-dbgeng-idebugcontrol-input.md) | The Input method requests an input string from the debugger engine. |
| [InputWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-inputwide.md) | The InputWide method requests an input string from the debugger engine. |
| [IsKernelDebuggerEnabled method](..\dbgeng\nf-dbgeng-idebugclient5-iskerneldebuggerenabled.md) | The IsKernelDebuggerEnabled method checks whether kernel debugging is enabled for the local kernel. |
| [IsManagedModule method](..\dbgeng\nf-dbgeng-idebugsymbols3-ismanagedmodule.md) | Checks whether the engine is using managed debugging support when it retrieves information for a module. |
| [IsPointer64Bit method](..\dbgeng\nf-dbgeng-idebugcontrol3-ispointer64bit.md) | The IsPointer64Bit method determines if the effective processor uses 64-bit pointers. |
| [IsValidTagToSet method](..\extsfns\nf-extsfns-idebugfaentrytags-isvalidtagtoset.md) | The IsValidTagToSet method determines whether it is OK to set the data of a specified tag. |
| [LaunchAndDebugPlmAppWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-launchanddebugplmappwide.md) | Launches and attaches to a Process Lifecycle Management (PLM) application. |
| [LaunchPlmBgTaskForDebugWide method](..\dbgeng\nf-dbgeng-idebugplmclient2-launchplmbgtaskfordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) background task. |
| [LaunchPlmPackageForDebugWide method](..\dbgeng\nf-dbgeng-idebugplmclient-launchplmpackagefordebugwide.md) | Launches a suspended Process Lifecycle Management (PLM) application. |
| [LoadModule method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-loadmodule.md) | The LoadModule callback method is called by the engine when a module-load debugging event occurs in the target. |
| [LoadModule method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-loadmodule.md) | The LoadModule callback method is called by the engine when a module-load debugging event occurs in the target. |
| [NextEntry method](..\extsfns\nf-extsfns-idebugfailureanalysis2-nextentry.md) | The NextEntry method gets the next FA entry, after a given FA entry, in a DebugFailureAnalysis object. |
| [OpenDumpFile method](..\dbgeng\nf-dbgeng-idebugclient5-opendumpfile.md) | The OpenDumpFile method opens a dump file as a debugger target. |
| [OpenDumpFileWide method](..\dbgeng\nf-dbgeng-idebugclient5-opendumpfilewide.md) | The OpenDumpFileWide method opens a dump file as a debugger target. |
| [OpenLogFile method](..\dbgeng\nf-dbgeng-idebugcontrol3-openlogfile.md) | The OpenLogFile method opens a log file that will receive output from the client objects. |
| [OpenLogFile2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-openlogfile2.md) | The OpenLogFile2 method opens a log file that will receive output from the client objects. |
| [OpenLogFile2Wide method](..\dbgeng\nf-dbgeng-idebugcontrol4-openlogfile2wide.md) | The OpenLogFile2Wide method opens a log file that will receive output from the client objects. |
| [OpenLogFileWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-openlogfilewide.md) | The OpenLogFileWide method opens a log file that will receive output from the client objects. |
| [Output method](..\dbgeng\nf-dbgeng-idebugcontrol3-output.md) | The Output method formats a string and send the result to output callbacks that have been registered with the engine's clients. |
| [Output method](..\dbgeng\nf-dbgeng-idebugoutputcallbacks-output.md) | The Output callback method is called by the engine to send output from the client to the IDebugOutputCallbacks object that is registered with the client. |
| [Output method](..\dbgeng\nf-dbgeng-idebugoutputcallbacks2-output.md) | This method is not used. |
| [Output method](..\dbgeng\nf-dbgeng-idebugoutputcallbackswide-output.md) | The Output callback method is called by the engine to send output from the client to the IDebugOutputCallbacksWide object that is registered with the client. |
| [Output2 method](..\dbgeng\nf-dbgeng-idebugoutputcallbacks2-output2.md) | Returns notifications for the IDebugOutputCallbacks2 interface. |
| [OutputAsType method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-outputastype.md) | The OutputAsType method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. |
| [OutputAsTypeWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-outputastypewide.md) | The OutputAsTypeWide method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. |
| [OutputContextStackTrace method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputcontextstacktrace.md) | The OutputContextStackTrace method prints the call stack specified by an array of stack frames and corresponding register contexts. |
| [OutputContextStackTraceEx method](..\dbgeng\nf-dbgeng-idebugcontrol5-outputcontextstacktraceex.md) | The OutputContextStackTraceEx method prints the call stack specified by an array of stack frames and corresponding register contexts. |
| [OutputCurrentState method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputcurrentstate.md) | The OutputCurrentState method prints the current state of the current target to the debugger console. |
| [OutputDisassembly method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputdisassembly.md) | The OutputDisassembly method disassembles a processor instruction and sends the disassembly to the output callbacks. |
| [OutputDisassemblyLines method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputdisassemblylines.md) | The OutputDisassemblyLines method disassembles several processor instructions and sends the resulting assembly instructions to the output callbacks. |
| [OutputIdentity method](..\dbgeng\nf-dbgeng-idebugclient5-outputidentity.md) | The OutputIdentity method formats and outputs a string describing the computer and user this client represents. |
| [OutputIdentityWide method](..\dbgeng\nf-dbgeng-idebugclient5-outputidentitywide.md) | The OutputIdentityWide method formats and outputs a string describing the computer and user this client represents. |
| [OutputPrompt method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputprompt.md) | The OutputPrompt method formats and sends a user prompt to the output callback objects. |
| [OutputPromptVaList method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputpromptvalist.md) | The OutputPromptVaList method formats and sends a user prompt to the output callback objects. |
| [OutputPromptVaListWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputpromptvalistwide.md) | The OutputPromptVaListWide method formats and sends a user prompt to the output callback objects. |
| [OutputPromptWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputpromptwide.md) | The OutputPromptWide method formats and sends a user prompt to the output callback objects. |
| [OutputRegisters method](..\dbgeng\nf-dbgeng-idebugregisters2-outputregisters.md) | The OutputRegisters method formats and sends the target's registers to the clients as output. |
| [OutputRegisters2 method](..\dbgeng\nf-dbgeng-idebugregisters2-outputregisters2.md) | The OutputRegisters2 method formats and outputs the target's registers. |
| [OutputServers method](..\dbgeng\nf-dbgeng-idebugclient5-outputservers.md) | The OutputServers method lists the servers running on a given computer. |
| [OutputServersWide method](..\dbgeng\nf-dbgeng-idebugclient5-outputserverswide.md) | The OutputServersWide method lists the servers running on a given computer. |
| [OutputStackTrace method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputstacktrace.md) | The OutputStackTrace method outputs either the supplied stack frame or the current stack frames. |
| [OutputStackTraceEx method](..\dbgeng\nf-dbgeng-idebugcontrol5-outputstacktraceex.md) | The OutputStackTraceEx method outputs either the supplied stack frame or the current stack frames. |
| [OutputSymbolByInlineContext method](..\dbgeng\nf-dbgeng-idebugsymbols4-outputsymbolbyinlinecontext.md) | Specifies an output symbol by using an inline context. |
| [OutputSymbolByOffset method](..\dbgeng\nf-dbgeng-idebugsymbols3-outputsymbolbyoffset.md) | The OutputSymbolByOffset method looks up a symbol by address and prints the symbol name and other symbol information to the debugger console. |
| [OutputSymbols method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-outputsymbols.md) | The OutputSymbols method prints the specified symbols to the debugger console. |
| [OutputTextReplacements method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputtextreplacements.md) | The OutputTextReplacements method prints all the currently defined user-named aliases to the debugger's output stream. |
| [OutputTypedDataPhysical method](..\dbgeng\nf-dbgeng-idebugsymbols3-outputtypeddataphysical.md) | The OutputTypedDataPhysical method formats the contents of a variable in the target computer's physical memory, and then sends this to the output callbacks. |
| [OutputTypedDataVirtual method](..\dbgeng\nf-dbgeng-idebugsymbols3-outputtypeddatavirtual.md) | The OutputTypedDataVirtual method formats the contents of a variable in the target's virtual memory, and then sends this to the output callbacks. |
| [OutputVaList method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputvalist.md) | The OutputVaList method formats a string and sends the result to the output callbacks that are registered with the engine's clients. |
| [OutputVaListWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputvalistwide.md) | The OutputVaListWide method formats a string and sends the result to the output callbacks that are registered with the engine's clients. |
| [OutputVersionInformation method](..\dbgeng\nf-dbgeng-idebugcontrol3-outputversioninformation.md) | The OutputVersionInformation method prints version information about the debugger engine to the debugger console. |
| [OutputWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-outputwide.md) | The OutputWide method formats a string and send the result to output callbacks that have been registered with the engine's clients. |
| [PopOutputLinePrefix method](..\dbgeng\nf-dbgeng-idebugclient5-popoutputlineprefix.md) | Restores a previously saved output line prefix. |
| [PushOutputLinePrefix method](..\dbgeng\nf-dbgeng-idebugclient5-pushoutputlineprefix.md) | Saves an output line prefix. |
| [PushOutputLinePrefixWide method](..\dbgeng\nf-dbgeng-idebugclient5-pushoutputlineprefixwide.md) | Saves a wide string output line prefix. |
| [QueryPlmPackageList method](..\dbgeng\nf-dbgeng-idebugplmclient3-queryplmpackagelist.md) | Query a Process Lifecycle Management (PLM) package list. |
| [QueryPlmPackageWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-queryplmpackagewide.md) | Query a Process Lifecycle Management (PLM) package. |
| [QueryVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces2-queryvirtual.md) | The QueryVirtual method provides information about the specified pages in the target's virtual address space. |
| [ReadBugCheckData method](..\dbgeng\nf-dbgeng-idebugcontrol3-readbugcheckdata.md) | The ReadBugCheckData method reads the kernel bug check code and related parameters. |
| [ReadBusData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readbusdata.md) | The ReadBusData method reads data from a system bus. |
| [ReadControl method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readcontrol.md) | The ReadControl method reads implementation-specific system data. |
| [ReadDebuggerData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readdebuggerdata.md) | The ReadDebuggerData method returns information about the target that the debugger engine has queried or determined during the current session. |
| [ReadHandleData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readhandledata.md) | The ReadHandleData method retrieves information about a system object specified by a system handle. |
| [ReadImageNtHeaders method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readimagentheaders.md) | The ReadImageNtHeaders method returns the NT headers for the specified image loaded in the target. |
| [ReadIo method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readio.md) | The ReadIo method reads from the system and bus I/O memory. |
| [ReadMsr method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readmsr.md) | The ReadMsr method reads a specified Model-Specific Register (MSR). |
| [ReadMultiByteStringVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readmultibytestringvirtual.md) | The ReadMultiByteStringVirtual method reads a null-terminated, multibyte string from the target. |
| [ReadMultiByteStringVirtualWide method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readmultibytestringvirtualwide.md) | The ReadMultiByteStringVirtualWide method reads a null-terminated, multibyte string from the target and converts it to Unicode. |
| [ReadPhysical method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readphysical.md) | The ReadPhysical method reads the target's memory from the specified physical address. |
| [ReadPhysical2 method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readphysical2.md) | The ReadPhysical2 method reads the target's memory from the specified physical address. |
| [ReadPointersVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readpointersvirtual.md) | The ReadPointersVirtual method is a convenience method for reading pointers from the target's virtual address space. |
| [ReadProcessorSystemData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readprocessorsystemdata.md) | The ReadProcessorSystemData method returns data about the specified processor. |
| [ReadTagged method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readtagged.md) | The ReadTagged method reads the tagged data that might be associated with a debugger session. |
| [ReadTypedDataPhysical method](..\dbgeng\nf-dbgeng-idebugsymbols3-readtypeddataphysical.md) | The ReadTypedDataPhysical method reads the value of a variable from the target computer's physical memory. |
| [ReadTypedDataVirtual method](..\dbgeng\nf-dbgeng-idebugsymbols3-readtypeddatavirtual.md) | The ReadTypedDataVirtual method reads the value of a variable in the target's virtual memory. |
| [ReadUnicodeStringVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readunicodestringvirtual.md) | The ReadUnicodeStringVirtual method reads a null-terminated, Unicode string from the target and converts it to a multibyte string. |
| [ReadUnicodeStringVirtualWide method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readunicodestringvirtualwide.md) | The ReadUnicodeStringVirtualWide method reads a null-terminated, Unicode string from the target. |
| [ReadVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readvirtual.md) | The ReadVirtual method reads memory from the target's virtual address space. |
| [ReadVirtualUncached method](..\dbgeng\nf-dbgeng-idebugdataspaces4-readvirtualuncached.md) | The ReadVirtualUncached method reads memory from the target's virtual address space. |
| [Reload method](..\dbgeng\nf-dbgeng-idebugsymbols3-reload.md) | The Reload method deletes the engine's symbol information for the specified module and reload these symbols as needed. |
| [ReloadWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-reloadwide.md) | The ReloadWide method deletes the engine's symbol information for the specified module and reload these symbols as needed. |
| [RemoveAssemblyOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-removeassemblyoptions.md) | The RemoveAssemblyOptions method turns off some of the assembly and disassembly options. |
| [RemoveBreakpoint method](..\dbgeng\nf-dbgeng-idebugcontrol3-removebreakpoint.md) | The RemoveBreakpoint method removes a breakpoint. |
| [RemoveBreakpoint2 method](..\dbgeng\nf-dbgeng-idebugcontrol4-removebreakpoint2.md) | The RemoveBreakpoint2 method removes a breakpoint. |
| [RemoveEngineOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-removeengineoptions.md) | The RemoveEngineOptions method turns off some of the engine's options. |
| [RemoveExtension method](..\dbgeng\nf-dbgeng-idebugcontrol3-removeextension.md) | The RemoveExtension method unloads an extension library. |
| [RemoveFlags method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-removeflags.md) | The RemoveFlags method removes flags from a breakpoint. |
| [RemoveProcessOptions method](..\dbgeng\nf-dbgeng-idebugclient5-removeprocessoptions.md) | The RemoveProcessOptions method removes process options from those options that affect the current process. |
| [RemoveSymbolByIndex method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-removesymbolbyindex.md) | The RemoveSymbolByIndex method removes the specified symbol from a symbol group. |
| [RemoveSymbolByName method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-removesymbolbyname.md) | The RemoveSymbolByName method removes the specified symbol from a symbol group. |
| [RemoveSymbolByNameWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-removesymbolbynamewide.md) | The RemoveSymbolByNameWide method removes the specified symbol from a symbol group. |
| [RemoveSymbolOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-removesymboloptions.md) | The RemoveSymbolOptions method turns off some of the engine's global symbol options. |
| [RemoveSyntheticModule method](..\dbgeng\nf-dbgeng-idebugsymbols3-removesyntheticmodule.md) | The RemoveSyntheticModule method removes a synthetic module from the module list the debugger maintains for the current process. |
| [RemoveSyntheticSymbol method](..\dbgeng\nf-dbgeng-idebugsymbols3-removesyntheticsymbol.md) | The RemoveSyntheticSymbol method removes a synthetic symbol from a module in the current process. |
| [RemoveTextReplacements method](..\dbgeng\nf-dbgeng-idebugcontrol3-removetextreplacements.md) | The RemoveTextReplacements method removes all user-named aliases. |
| [RemoveTypeOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-removetypeoptions.md) | The RemoveTypeOptions method turns off some type formatting options for output generated by the engine. |
| [Request method](..\dbgeng\nf-dbgeng-idebugadvanced3-request.md) | The Request method performs a variety of different operations. |
| [ResetManagedStatus method](..\dbgeng\nf-dbgeng-idebugcontrol4-resetmanagedstatus.md) | Clears and reinitializes the engine's managed code debugging support of the runtime debugging APIs provided by the common language runtime (CLR). |
| [ResetScope method](..\dbgeng\nf-dbgeng-idebugsymbols3-resetscope.md) | The ResetScope method resets the current scope to the default scope of the current thread. |
| [ResumePlmPackageWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-resumeplmpackagewide.md) | Resumes a Process Lifecycle Management (PLM) package. |
| [ReturnInput method](..\dbgeng\nf-dbgeng-idebugcontrol3-returninput.md) | The ReturnInput method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input. |
| [ReturnInputWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-returninputwide.md) | The ReturnInputWide method is used by IDebugInputCallbacks objects to send an input string to the engine following a request for input. |
| [SearchVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-searchvirtual.md) | The SearchVirtual method searches the target's virtual memory for a specified pattern of bytes. |
| [SearchVirtual2 method](..\dbgeng\nf-dbgeng-idebugdataspaces4-searchvirtual2.md) | The SearchVirtual2 method searches the process's virtual memory for a specified pattern of bytes. |
| [SessionStatus method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-sessionstatus.md) | The SessionStatus callback method is called by the engine when a change occurs in the debugger session. |
| [SessionStatus method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-sessionstatus.md) | The SessionStatus callback method is called by the engine when a change occurs in the debugger session. |
| [SetAssemblyOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-setassemblyoptions.md) | The SetAssemblyOptions method sets the assembly and disassembly options that affect how the debugger engine assembles and disassembles processor instructions for the target. |
| [SetBuffer method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setbuffer.md) | The SetBuffer method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it overwrites the data block of the FA entry with the bytes in a specified buffer. |
| [SetClientContext method](..\dbgeng\nf-dbgeng-idebugclient7-setclientcontext.md) | The SetClientContext method is reserved for internal use. |
| [SetCodeLevel method](..\dbgeng\nf-dbgeng-idebugcontrol3-setcodelevel.md) | The SetCodeLevel method sets the current code level and is mainly used when stepping through code. |
| [SetCommand method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setcommand.md) | The SetCommand method sets the command that is executed when a breakpoint is triggered. |
| [SetCommandWide method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setcommandwide.md) | The SetCommandWide method sets the command that is executed when a breakpoint is triggered. |
| [SetCurrentProcessId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setcurrentprocessid.md) | The SetCurrentProcessId method makes the specified process the current process. |
| [SetCurrentSystemId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setcurrentsystemid.md) | The SetCurrentSystemId method makes the specified target the current target. |
| [SetCurrentThreadId method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setcurrentthreadid.md) | The SetCurrentThreadId method makes the specified thread the current thread. |
| [SetDataParameters method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setdataparameters.md) | The SetDataParameters method sets the parameters for a processor breakpoint. |
| [SetEffectiveProcessorType method](..\dbgeng\nf-dbgeng-idebugcontrol3-seteffectiveprocessortype.md) | The SetEffectiveProcessorType method sets the effective processor type of the processor of the computer that is running the target. |
| [SetEngineOptions method](..\dbgeng\nf-dbgeng-idebugcontrol3-setengineoptions.md) | The SetEngineOptions method changes the engine's options. |
| [SetEventCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-seteventcallbacks.md) | The SetEventCallbacks method registers an event callbacks object with this client. |
| [SetEventCallbacksWide method](..\dbgeng\nf-dbgeng-idebugclient5-seteventcallbackswide.md) | The SetEventCallbacksWide method registers an event callbacks object with this client. |
| [SetEventContextCallbacks method](..\dbgeng\nf-dbgeng-idebugclient6-seteventcontextcallbacks.md) | Registers an event callbacks object with this client. |
| [SetEventFilterCommand method](..\dbgeng\nf-dbgeng-idebugcontrol3-seteventfiltercommand.md) | The SetEventFilterCommand method sets a debugger command for the engine to execute when a specified event occurs. |
| [SetEventFilterCommandWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-seteventfiltercommandwide.md) | The SetEventFilterCommandWide method sets a debugger command for the engine to execute when a specified event occurs. |
| [SetExceptionFilterParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexceptionfilterparameters.md) | The SetExceptionFilterParameters method changes the break status and handling status for some exception filters. |
| [SetExceptionFilterSecondCommand method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexceptionfiltersecondcommand.md) | The SetExceptionFilterSecondCommand method sets the command that will be executed by the debugger engine on the second chance of a specified exception. |
| [SetExceptionFilterSecondCommandWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-setexceptionfiltersecondcommandwide.md) | The SetExceptionFilterSecondCommandWide method sets the command that will be executed by the debugger engine on the second chance of a specified exception. |
| [SetExecutionStatus method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexecutionstatus.md) | The SetExecutionStatus method requests that the debugger engine enter an executable state. Actual execution will not occur until the next time WaitForEvent is called. |
| [SetExpressionSyntax method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexpressionsyntax.md) | The SetExpressionSyntax method sets the syntax that the engine will use to evaluate expressions. |
| [SetExpressionSyntaxByName method](..\dbgeng\nf-dbgeng-idebugcontrol3-setexpressionsyntaxbyname.md) | The SetExpressionSyntaxByName method sets the syntax that the engine will use to evaluate expressions. |
| [SetExpressionSyntaxByNameWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-setexpressionsyntaxbynamewide.md) | The SetExpressionSyntaxByNameWide method sets the syntax that the engine will use to evaluate expressions. |
| [SetExtensionCommand method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setextensioncommand.md) | The SetExtensionCommand method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. |
| [SetFlags method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setflags.md) | The SetFlags method sets the flags for a breakpoint. |
| [SetImagePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-setimagepath.md) | The SetImagePath method sets the executable image path. |
| [SetImagePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-setimagepathwide.md) | The SetImagePathWide method sets the executable image path. |
| [SetImplicitProcessDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setimplicitprocessdataoffset.md) | The SetImplicitProcessDataOffset method sets the implicit process for the current target. |
| [SetImplicitThreadDataOffset method](..\dbgeng\nf-dbgeng-idebugsystemobjects4-setimplicitthreaddataoffset.md) | The SetImplicitThreadDataOffset method sets the implicit thread for the current process. |
| [SetInputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-setinputcallbacks.md) | The SetInputCallbacks method registers an input callbacks object with the client. |
| [SetInterrupt method](..\dbgeng\nf-dbgeng-idebugcontrol3-setinterrupt.md) | The SetInterrupt method registers a user interrupt or breaks into the debugger. |
| [SetInterruptTimeout method](..\dbgeng\nf-dbgeng-idebugcontrol3-setinterrupttimeout.md) | The SetInterruptTimeout method sets the number of seconds that the debugger engine should wait when requesting a break into the debugger. |
| [SetKernelConnectionOptions method](..\dbgeng\nf-dbgeng-idebugclient5-setkernelconnectionoptions.md) | The SetKernelConnectionOptions method updates some of the connection options for a live kernel target. |
| [SetKernelConnectionOptionsWide method](..\dbgeng\nf-dbgeng-idebugclient5-setkernelconnectionoptionswide.md) | The SetKernelConnectionOptionsWide method updates some of the connection options for a live kernel target. |
| [SetLogMask method](..\dbgeng\nf-dbgeng-idebugcontrol3-setlogmask.md) | The SetLogMask method sets the output mask for the currently open log file. |
| [SetMatchThreadId method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setmatchthreadid.md) | The SetMatchThreadId method sets the engine thread ID of the thread that can trigger a breakpoint. |
| [SetNextEventIndex method](..\dbgeng\nf-dbgeng-idebugcontrol3-setnexteventindex.md) | The SetNextEventIndex method sets the next event for the current target by selecting the event from the static list of events for the target, if such a list exists. |
| [SetNotifyEventHandle method](..\dbgeng\nf-dbgeng-idebugcontrol3-setnotifyeventhandle.md) | The SetNotifyEventHandle method sets the event that will be signaled after the next exception in a target. |
| [SetOffset method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setoffset.md) | The SetOffset method sets the location that triggers a breakpoint. |
| [SetOffsetExpression method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setoffsetexpression.md) | The SetOffsetExpression methods set an expression string that evaluates to the location that triggers a breakpoint. |
| [SetOffsetExpressionWide method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setoffsetexpressionwide.md) | The SetOffsetExpressionWide methods set an expression string that evaluates to the location that triggers a breakpoint. |
| [SetOtherOutputMask method](..\dbgeng\nf-dbgeng-idebugclient5-setotheroutputmask.md) | The SetOtherOutputMask method sets the output mask for another client. |
| [SetOutputCallbacks method](..\dbgeng\nf-dbgeng-idebugclient5-setoutputcallbacks.md) | The SetOutputCallbacks method registers an output callbacks object with this client. |
| [SetOutputCallbacksWide method](..\dbgeng\nf-dbgeng-idebugclient5-setoutputcallbackswide.md) | The SetOutputCallbacksWide method registers an output callbacks object with this client. |
| [SetOutputLinePrefix method](..\dbgeng\nf-dbgeng-idebugclient-setoutputlineprefix.md) | Sets a prefix for multiple lines of output. |
| [SetOutputLinePrefixWide method](..\dbgeng\nf-dbgeng-idebugclient5-setoutputlineprefixwide.md) | Sets a wide string prefix for output lines. |
| [SetOutputMask method](..\dbgeng\nf-dbgeng-idebugclient5-setoutputmask.md) | The SetOutputMask method sets the output mask for the client. |
| [SetOutputWidth method](..\dbgeng\nf-dbgeng-idebugclient-setoutputwidth.md) | Controls the width of an output line for commands that produce formatted output. |
| [SetPassCount method](..\dbgeng\nf-dbgeng-idebugbreakpoint2-setpasscount.md) | The SetPassCount method sets the number of times that the target must reach the breakpoint location before the breakpoint is triggered. |
| [SetProcessOptions method](..\dbgeng\nf-dbgeng-idebugclient5-setprocessoptions.md) | The SetProcessOptions method sets the process options affecting the current process. |
| [SetProperties method](..\extsfns\nf-extsfns-idebugfaentrytags-setproperties.md) | The SetProperties method sets the name or description (or both) of a tag in a DebugFailureAnalysisTags object. |
| [SetPseudoValues method](..\dbgeng\nf-dbgeng-idebugregisters2-setpseudovalues.md) | The SetPseudoValues method sets the value of several pseudo-registers. |
| [SetQuitLockString method](..\dbgeng\nf-dbgeng-idebugclient5-setquitlockstring.md) | Sets a quit lock string. |
| [SetQuitLockStringWide method](..\dbgeng\nf-dbgeng-idebugclient5-setquitlockstringwide.md) | Sets a quit lock Unicode character string. |
| [SetRadix method](..\dbgeng\nf-dbgeng-idebugcontrol3-setradix.md) | The SetRadix method sets the default radix (number base) used by the debugger engine when it evaluates and displays MASM expressions, and when it displays symbol information. |
| [SetScope method](..\dbgeng\nf-dbgeng-idebugsymbols3-setscope.md) | The SetScope method sets the current scope. |
| [SetScopeEx method](..\dbgeng\nf-dbgeng-idebugsymbols4-setscopeex.md) | Sets the scope as an extended frame structure. |
| [SetScopeFrameByIndex method](..\dbgeng\nf-dbgeng-idebugsymbols3-setscopeframebyindex.md) | The SetScopeFrameByIndex method sets the current scope to the scope of one of the frames on the call stack. |
| [SetScopeFrameByIndexEx method](..\dbgeng\nf-dbgeng-idebugsymbols5-setscopeframebyindexex.md) | Sets the current frame by using an index. |
| [SetScopeFromJitDebugInfo method](..\dbgeng\nf-dbgeng-idebugsymbols3-setscopefromjitdebuginfo.md) | Recovers just-in-time (JIT) debugging information and sets current debugger scope context based on that information. |
| [SetScopeFromStoredEvent method](..\dbgeng\nf-dbgeng-idebugsymbols3-setscopefromstoredevent.md) | The SetScopeFromStoredEvent method sets the current scope to the scope of the stored event. |
| [SetSourcePath method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsourcepath.md) | The SetSourcePath method sets the source path. |
| [SetSourcePathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsourcepathwide.md) | The SetSourcePathWide method sets the source path. |
| [SetSpecificFilterArgument method](..\dbgeng\nf-dbgeng-idebugcontrol3-setspecificfilterargument.md) | The SetSpecificFilterArgument method sets the value of filter argument for the specific filters that can have an argument. |
| [SetSpecificFilterArgumentWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-setspecificfilterargumentwide.md) | The SetSpecificFilterArgumentWide method sets the value of filter argument for the specific filters that can have an argument. |
| [SetSpecificFilterParameters method](..\dbgeng\nf-dbgeng-idebugcontrol3-setspecificfilterparameters.md) | The SetSpecificFilterParameters method changes the break status and handling status for some specific event filters. |
| [SetString method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setstring.md) | The SetString method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it sets (overwrites) the data block of the FA entry to a specified string value. |
| [SetSymbolOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsymboloptions.md) | The SetSymbolOptions method changes the engine's global symbol options. |
| [SetSymbolPath method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsymbolpath.md) | The SetSymbolPath method sets the symbol path. |
| [SetSymbolPathWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-setsymbolpathwide.md) | The SetSymbolPathWide method sets the symbol path. |
| [SetSystemErrorControl method](..\dbgeng\nf-dbgeng-idebugcontrol3-setsystemerrorcontrol.md) | The SetSystemErrorControl method sets the control values for handling system errors. |
| [SetTextMacro method](..\dbgeng\nf-dbgeng-idebugcontrol3-settextmacro.md) | The SetTextMacro method sets the value of a fixed-name alias. |
| [SetTextMacroWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-settextmacrowide.md) | The SetTextMacroWide method sets the value of a fixed-name alias. |
| [SetTextReplacement method](..\dbgeng\nf-dbgeng-idebugcontrol3-settextreplacement.md) | The SetTextReplacement method sets the value of a user-named alias. |
| [SetTextReplacementWide method](..\dbgeng\nf-dbgeng-idebugcontrol4-settextreplacementwide.md) | The SetTextReplacementWide method sets the value of a user-named alias. |
| [SetThreadContext method](..\dbgeng\nf-dbgeng-idebugadvanced3-setthreadcontext.md) | The SetThreadContext method sets the current thread context. |
| [SetType method](..\extsfns\nf-extsfns-idebugfaentrytags-settype.md) | The SetType method sets the data type that is associated with a tag in a DebugFailureAnalysisTags object. |
| [SetTypeOptions method](..\dbgeng\nf-dbgeng-idebugsymbols3-settypeoptions.md) | The SetTypeOptions method changes the type formatting options for output generated by the engine. |
| [SetUlong method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setulong.md) | The SetUlong method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it sets (overwrites) the data block of the FA entry to a specified ULONG value. |
| [SetUlong64 method](..\extsfns\nf-extsfns-idebugfailureanalysis2-setulong64.md) | The SetUlong64 method searches a DebugFailureAnalysis object for the first FA entry that has a specified tag. If it finds an FA entry with the specified tag, it sets (overwrites) the data block of the FA entry to a specified ULONG64 value. |
| [SetValue method](..\dbgeng\nf-dbgeng-idebugregisters2-setvalue.md) | The SetValue method sets the value of one of the target's registers. |
| [SetValues method](..\dbgeng\nf-dbgeng-idebugregisters2-setvalues.md) | The SetValues method sets the value of several of the target's registers. |
| [SetValues2 method](..\dbgeng\nf-dbgeng-idebugregisters2-setvalues2.md) | The SetValues2 method sets the value of several of the target's registers. |
| [StartEnumTagged method](..\dbgeng\nf-dbgeng-idebugdataspaces4-startenumtagged.md) | The StartEnumTagged method initializes a enumeration over the tagged data associated with a debugger session. |
| [StartInput method](..\dbgeng\nf-dbgeng-idebuginputcallbacks-startinput.md) | The StartInput callback method is called by the engine to indicate that it is waiting for a line of input. |
| [StartProcessServer method](..\dbgeng\nf-dbgeng-idebugclient5-startprocessserver.md) | The StartProcessServer method starts a process server. |
| [StartProcessServerWide method](..\dbgeng\nf-dbgeng-idebugclient5-startprocessserverwide.md) | The StartProcessServerWide method starts a process server. |
| [StartServer method](..\dbgeng\nf-dbgeng-idebugclient5-startserver.md) | The StartServer method starts a debugging server. |
| [StartServerWide method](..\dbgeng\nf-dbgeng-idebugclient5-startserverwide.md) | The StartServerWide method starts a debugging server. |
| [StartSymbolMatch method](..\dbgeng\nf-dbgeng-idebugsymbols3-startsymbolmatch.md) | The StartSymbolMatch method initializes a search for symbols whose names match a given pattern. |
| [StartSymbolMatchWide method](..\dbgeng\nf-dbgeng-idebugsymbols3-startsymbolmatchwide.md) | The StartSymbolMatchWide method initializes a search for symbols whose names match a given pattern. |
| [SuspendPlmPackageWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-suspendplmpackagewide.md) | Suspends a Process Lifecycle Management (PLM) package. |
| [SystemError method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-systemerror.md) | The SystemError callback method is called by the engine when a system error occurs in the target. |
| [SystemError method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-systemerror.md) | The SystemError callback method is called by the engine when a system error occurs in the target. |
| [TerminateCurrentProcess method](..\dbgeng\nf-dbgeng-idebugclient5-terminatecurrentprocess.md) | The TerminateCurrentProcess method attempts to terminate the current process. |
| [TerminatePlmPackageWide method](..\dbgeng\nf-dbgeng-idebugplmclient3-terminateplmpackagewide.md) | Ends a Process Lifecycle Management (PLM) package. |
| [TerminateProcesses method](..\dbgeng\nf-dbgeng-idebugclient5-terminateprocesses.md) | The TerminateProcesses method attempts to terminate all processes in all targets. |
| [UnloadModule method](..\dbgeng\nf-dbgeng-idebugeventcallbacks-unloadmodule.md) | The UnloadModule callback method is called by the engine when a module-unload debugging event occurs in the target. |
| [UnloadModule method](..\dbgeng\nf-dbgeng-idebugeventcallbackswide-unloadmodule.md) | The UnloadModule callback method is called by the engine when a module-unload debugging event occurs in the target. |
| [VirtualToPhysical method](..\dbgeng\nf-dbgeng-idebugdataspaces4-virtualtophysical.md) | The VirtualToPhysical method translates a location in the target's virtual address space into a physical memory address. |
| [WaitForEvent method](..\dbgeng\nf-dbgeng-idebugcontrol3-waitforevent.md) | The WaitForEvent method waits for an event that breaks into the debugger engine application. |
| [WaitForProcessServerEnd method](..\dbgeng\nf-dbgeng-idebugclient5-waitforprocessserverend.md) | The WaitForProcessServerEnd method waits for a local process server to exit. |
| [Write method](..\dbgeng\nf-dbgeng-idebugoutputstream-write.md) | Writes to the debug output stream. |
| [WriteBusData method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writebusdata.md) | The WriteBusData method writes data to a system bus. |
| [WriteControl method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writecontrol.md) | The WriteControl method writes implementation-specific system data. |
| [WriteDumpFile method](..\dbgeng\nf-dbgeng-idebugclient5-writedumpfile.md) | The WriteDumpFile method creates a user-mode or kernel-modecrash dump file. |
| [WriteDumpFile2 method](..\dbgeng\nf-dbgeng-idebugclient5-writedumpfile2.md) | The WriteDumpFile2 method creates a user-mode or kernel-modecrash dump file. |
| [WriteDumpFileWide method](..\dbgeng\nf-dbgeng-idebugclient5-writedumpfilewide.md) | The WriteDumpFileWide method creates a user-mode or kernel-modecrash dump file. |
| [WriteIo method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writeio.md) | The WriteIo method writes to the system and bus I/O memory. |
| [WriteMsr method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writemsr.md) | The WriteMsr method writes a value to the specified Model-Specific Register (MSR). |
| [WritePhysical method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writephysical.md) | The WritePhysical method writes data to the specified physical address in the target's memory. |
| [WritePhysical2 method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writephysical2.md) | The WritePhysical2 method writes data to the specified physical address in the target's memory. |
| [WritePointersVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writepointersvirtual.md) | The WritePointersVirtual method is a convenience method for writing pointers to the target's virtual address space. |
| [WriteSymbol method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-writesymbol.md) | The WriteSymbol methods set the value of the specified symbol. |
| [WriteSymbolWide method](..\dbgeng\nf-dbgeng-idebugsymbolgroup2-writesymbolwide.md) | The WriteSymbolWide method sets the value of the specified symbol. |
| [WriteTypedDataPhysical method](..\dbgeng\nf-dbgeng-idebugsymbols3-writetypeddataphysical.md) | The WriteTypedDataPhysical method writes the value of a variable in the target computer's physical memory. |
| [WriteTypedDataVirtual method](..\dbgeng\nf-dbgeng-idebugsymbols3-writetypeddatavirtual.md) | The WriteTypedDataVirtual method writes data to the target's virtual address space. The number of bytes written is the size of the specified type. |
| [WriteVirtual method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writevirtual.md) | The WriteVirtual method writes data to the target's virtual address space. |
| [WriteVirtualUncached method](..\dbgeng\nf-dbgeng-idebugdataspaces4-writevirtualuncached.md) | The WriteVirtualUncached method writes data to the target's virtual address space. |
