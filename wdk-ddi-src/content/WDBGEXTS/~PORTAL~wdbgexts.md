# Declarations in the wdbgexts header
This header Wdbgexts contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [DBGKD_DEBUG_DATA_HEADER64 structure](ns-wdbgexts--dbgkd-debug-data-header64.md) | TBD |
| [VIRTUAL_TO_PHYSICAL structure](ns-wdbgexts--virtual-to-physical.md) | TBD |
| [GET_CONTEXT_EX structure](ns-wdbgexts--get-context-ex.md) | TBD |
| [PROCESSORINFO structure](ns-wdbgexts--processorinfo.md) | TBD |
| [DBGKD_GET_VERSION64 structure](ns-wdbgexts--dbgkd-get-version64.md) | The IG_GET_KERNEL_VERSION Ioctl operation receives information related to the operating system version of the target. |
| [READCONTROLSPACE structure](ns-wdbgexts--readcontrolspace.md) | TBD |
| [DBGKD_DEBUG_DATA_HEADER32 structure](ns-wdbgexts--dbgkd-debug-data-header32.md) | TBD |
| [READCONTROLSPACE32 structure](ns-wdbgexts--readcontrolspace32.md) | TBD |
| [KDDEBUGGER_DATA64 structure](ns-wdbgexts--kddebugger-data64.md) | TBD |
| [GET_EXPRESSION_EX structure](ns-wdbgexts--get-expression-ex.md) | TBD |
| [READ_WRITE_MSR structure](ns-wdbgexts--read-write-msr.md) | TBD |
| [EXTSTACKTRACE64 structure](ns-wdbgexts--extstacktrace64.md) | TBD |
| [WINDBG_OLDKD_EXTENSION_APIS structure](ns-wdbgexts--windbg-oldkd-extension-apis.md) | TBD |
| [WDBGEXTS_QUERY_INTERFACE structure](ns-wdbgexts--wdbgexts-query-interface.md) | TBD |
| [PHYSICAL structure](ns-wdbgexts--physical.md) | TBD |
| [DBGKD_GET_VERSION32 structure](ns-wdbgexts--dbgkd-get-version32.md) | TBD |
| [WINDBG_EXTENSION_APIS structure](ns-wdbgexts--windbg-extension-apis.md) | TBD |
| [EXT_TYPED_DATA structure](ns-wdbgexts--ext-typed-data.md) | The EXT_TYPED_DATA structure is passed to and returned from the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation. It contains the input and output parameters for the operation as well as specifying which particular suboperation to perform. |
| [WDBGEXTS_DISASSEMBLE_BUFFER structure](ns-wdbgexts--wdbgexts-disassemble-buffer.md) | TBD |
| [GETSETBUSDATA structure](ns-wdbgexts--getsetbusdata.md) | The IG_GET_BUS_DATA Ioctl operation reads data from a system bus and the IG_SET_BUS_DATA Ioctl operation writes data to a system bus. |
| [GET_SET_SYMPATH structure](ns-wdbgexts--get-set-sympath.md) | TBD |
| [POINTER_SEARCH_PHYSICAL structure](ns-wdbgexts--pointer-search-physical.md) | The IG_POINTER_SEARCH_PHYSICAL Ioctl operation searches the target's physical memory for pointers lying within a specified range. |
| [DEBUG_TYPED_DATA structure](ns-wdbgexts--debug-typed-data.md) | The DEBUG_TYPED_DATA structure describes typed data in the memory of the target. |
| [IOSPACE structure](ns-wdbgexts--iospace.md) | TBD |
| [PHYSICAL_WITH_FLAGS structure](ns-wdbgexts--physical-with-flags.md) | TBD |
| [EXT_FIND_FILE structure](ns-wdbgexts--ext-find-file.md) | TBD |
| [GET_CURRENT_PROCESS_ADDRESS structure](ns-wdbgexts--get-current-process-address.md) | TBD |
| [GET_INPUT_LINE structure](ns-wdbgexts--get-input-line.md) | TBD |
| [WDBGEXTS_THREAD_OS_INFO structure](ns-wdbgexts--wdbgexts-thread-os-info.md) | The IG_GET_THREAD_OS_INFO Ioctl operation returns information about an operating system thread in the target. When calling Ioctl with IoctlType set to IG_GET_THREAD_OS_INFO, IpvData should contain an instance of the WDBGEXTS_THREAD_OS_INFO structure. |
| [IOSPACE32 structure](ns-wdbgexts--iospace32.md) | TBD |
| [READCONTROLSPACE64 structure](ns-wdbgexts--readcontrolspace64.md) | TBD |
| [WDBGEXTS_MODULE_IN_RANGE structure](ns-wdbgexts--wdbgexts-module-in-range.md) | TBD |
| [EXT_MATCH_PATTERN_A structure](ns-wdbgexts--ext-match-pattern-a.md) | TBD |
| [IOSPACE64 structure](ns-wdbgexts--iospace64.md) | TBD |
| [SEARCHMEMORY structure](ns-wdbgexts--searchmemory.md) | TBD |
| [IOSPACE_EX32 structure](ns-wdbgexts--iospace-ex32.md) | TBD |
| [EXTSTACKTRACE32 structure](ns-wdbgexts--extstacktrace32.md) | TBD |
| [GET_CURRENT_THREAD_ADDRESS structure](ns-wdbgexts--get-current-thread-address.md) | TBD |
| [WINDBG_EXTENSION_APIS32 structure](ns-wdbgexts--windbg-extension-apis32.md) | TBD |
| [SYM_DUMP_PARAM structure](ns-wdbgexts--sym-dump-param.md) | The IG_DUMP_SYMBOL_INFO Ioctl operation provides information about the type of a symbol. |
| [WDBGEXTS_CLR_DATA_INTERFACE structure](ns-wdbgexts--wdbgexts-clr-data-interface.md) | TBD |
| [TRANSLATE_VIRTUAL_TO_PHYSICAL structure](ns-wdbgexts--translate-virtual-to-physical.md) | TBD |
| [GET_TEB_ADDRESS structure](ns-wdbgexts--get-teb-address.md) | TBD |
| [IOSPACE_EX structure](ns-wdbgexts--iospace-ex.md) | TBD |
| [KDDEBUGGER_DATA32 structure](ns-wdbgexts--kddebugger-data32.md) | TBD |
| [WINDBG_OLD_EXTENSION_APIS structure](ns-wdbgexts--windbg-old-extension-apis.md) | TBD |
| [FIELD_INFO structure](ns-wdbgexts--field-info.md) | The FIELD_INFO structure is used by the IG_DUMP_SYMBOL_INFOIoctl operation to provide information about a member in a structure. |
| [EXT_API_VERSION structure](ns-wdbgexts-ext-api-version.md) | TBD |
| [WINDBG_EXTENSION_APIS64 structure](ns-wdbgexts--windbg-extension-apis64.md) | TBD |
| [PHYSICAL_TO_VIRTUAL structure](ns-wdbgexts--physical-to-virtual.md) | TBD |
| [GET_PEB_ADDRESS structure](ns-wdbgexts--get-peb-address.md) | TBD |
| [EXTSTACKTRACE structure](ns-wdbgexts--extstacktrace.md) | TBD |
| [IOSPACE_EX64 structure](ns-wdbgexts--iospace-ex64.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PWINDBG_OLD_EXTENSION_ROUTINE callback function](nc-wdbgexts-pwindbg-old-extension-routine.md) | TBD |
| [PWINDBG_READ_PROCESS_MEMORY_ROUTINE callback function](nc-wdbgexts-pwindbg-read-process-memory-routine.md) | TBD |
| [PWINDBG_GET_EXPRESSION64 callback function](nc-wdbgexts-pwindbg-get-expression64.md) | TBD |
| [PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE callback function](nc-wdbgexts-pwindbg-write-process-memory-routine.md) | TBD |
| [PWINDBG_READ_PROCESS_MEMORY_ROUTINE64 callback function](nc-wdbgexts-pwindbg-read-process-memory-routine64.md) | TBD |
| [PWINDBG_EXTENSION_ROUTINE callback function](nc-wdbgexts-pwindbg-extension-routine.md) | TBD |
| [PWINDBG_GET_EXPRESSION32 callback function](nc-wdbgexts-pwindbg-get-expression32.md) | TBD |
| [PWINDBG_EXTENSION_API_VERSION callback function](nc-wdbgexts-pwindbg-extension-api-version.md) | TBD |
| [PWINDBG_OUTPUT_ROUTINE callback function](nc-wdbgexts-pwindbg-output-routine.md) | TBD |
| [PWINDBG_EXTENSION_DLL_INIT64 callback function](nc-wdbgexts-pwindbg-extension-dll-init64.md) | TBD |
| [PWINDBG_EXTENSION_ROUTINE32 callback function](nc-wdbgexts-pwindbg-extension-routine32.md) | TBD |
| [PWINDBG_READ_PROCESS_MEMORY_ROUTINE32 callback function](nc-wdbgexts-pwindbg-read-process-memory-routine32.md) | TBD |
| [PWINDBG_IOCTL_ROUTINE callback function](nc-wdbgexts-pwindbg-ioctl-routine.md) | TBD |
| [PWINDBG_STACKTRACE_ROUTINE64 callback function](nc-wdbgexts-pwindbg-stacktrace-routine64.md) | TBD |
| [PWINDBG_SET_THREAD_CONTEXT_ROUTINE callback function](nc-wdbgexts-pwindbg-set-thread-context-routine.md) | TBD |
| [PWINDBG_GET_EXPRESSION callback function](nc-wdbgexts-pwindbg-get-expression.md) | TBD |
| [PWINDBG_CHECK_CONTROL_C callback function](nc-wdbgexts-pwindbg-check-control-c.md) | TBD |
| [PWINDBG_EXTENSION_ROUTINE64 callback function](nc-wdbgexts-pwindbg-extension-routine64.md) | TBD |
| [PWINDBG_STACKTRACE_ROUTINE callback function](nc-wdbgexts-pwindbg-stacktrace-routine.md) | TBD |
| [PWINDBG_OLDKD_EXTENSION_ROUTINE callback function](nc-wdbgexts-pwindbg-oldkd-extension-routine.md) | TBD |
| [PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE32 callback function](nc-wdbgexts-pwindbg-write-process-memory-routine32.md) | TBD |
| [PWINDBG_EXTENSION_DLL_INIT callback function](nc-wdbgexts-pwindbg-extension-dll-init.md) | TBD |
| [PWINDBG_DISASM callback function](nc-wdbgexts-pwindbg-disasm.md) | TBD |
| [PWINDBG_DISASM64 callback function](nc-wdbgexts-pwindbg-disasm64.md) | TBD |
| [PWINDBG_EXTENSION_DLL_INIT32 callback function](nc-wdbgexts-pwindbg-extension-dll-init32.md) | TBD |
| [PSYM_DUMP_FIELD_CALLBACK callback](nc-wdbgexts-psym-dump-field-callback.md) | The PSYM_DUMP_FIELD_CALLBACK callback function is called by the debugger engine during the IG_DUMP_SYMBOL_INFO Ioctl operation with information about a member in the specified symbol. |
| [PWINDBG_CHECK_VERSION callback function](nc-wdbgexts-pwindbg-check-version.md) | TBD |
| [PWINDBG_GET_SYMBOL callback function](nc-wdbgexts-pwindbg-get-symbol.md) | TBD |
| [PWINDBG_OLDKD_WRITE_PHYSICAL_MEMORY callback function](nc-wdbgexts-pwindbg-oldkd-write-physical-memory.md) | TBD |
| [PWINDBG_GET_THREAD_CONTEXT_ROUTINE callback function](nc-wdbgexts-pwindbg-get-thread-context-routine.md) | TBD |
| [PWINDBG_OLDKD_READ_PHYSICAL_MEMORY callback function](nc-wdbgexts-pwindbg-oldkd-read-physical-memory.md) | TBD |
| [PWINDBG_STACKTRACE_ROUTINE32 callback function](nc-wdbgexts-pwindbg-stacktrace-routine32.md) | TBD |
| [PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE64 callback function](nc-wdbgexts-pwindbg-write-process-memory-routine64.md) | TBD |
| [PWINDBG_GET_SYMBOL32 callback function](nc-wdbgexts-pwindbg-get-symbol32.md) | TBD |
| [PWINDBG_DISASM32 callback function](nc-wdbgexts-pwindbg-disasm32.md) | TBD |
| [PWINDBG_GET_SYMBOL64 callback function](nc-wdbgexts-pwindbg-get-symbol64.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [ReadControlSpace32 function](nf-wdbgexts-readcontrolspace32.md) | TBD |
| [ReadIoSpace64 function](nf-wdbgexts-readiospace64.md) | The ReadIoSpace64 function reads from the system I/O locations. |
| [WritePhysical function](nf-wdbgexts-writephysical.md) | The WritePhysical function writes to physical memory. |
| [SetThreadForOperation32 function](nf-wdbgexts-setthreadforoperation32.md) | TBD |
| [GetSetSympath function](nf-wdbgexts-getsetsympath.md) | The GetSetSympath function can be used to either get or set the symbol search path. |
| [InitTypeReadPhysical function](nf-wdbgexts-inittypereadphysical.md) | TBD |
| [GetFieldOffset function](nf-wdbgexts-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [WriteIoSpaceEx32 function](nf-wdbgexts-writeiospaceex32.md) | TBD |
| [ExtMatchPatternA function](nf-wdbgexts-extmatchpatterna.md) | TBD |
| [DBGKD_MAJOR_TYPE function](nf-wdbgexts-dbgkd-major-type.md) | TBD |
| [GetPebAddress function](nf-wdbgexts-getpebaddress.md) | The GetPebAddress function returns the address of the process environment block (PEB) for a system process. |
| [GetTebAddress function](nf-wdbgexts-gettebaddress.md) | The GetTebAddress function returns the address of the thread environment block (TEB) for the current operating system thread. |
| [GetDebuggerData function](nf-wdbgexts-getdebuggerdata.md) | The GetDebuggerData function retrieves information stored in a data block. |
| [WritePointer function](nf-wdbgexts-writepointer.md) | The WritePointer function writes a pointer to the target. |
| [ReadControlSpace64 function](nf-wdbgexts-readcontrolspace64.md) | The ReadControlSpace64 function reads the processor-specific control space into the array pointed to by buf. |
| [GetFieldValue function](nf-wdbgexts-getfieldvalue.md) | The GetFieldValue macro is a thin wrapper around the GetFieldData function. It is provided as a convenience for reading the value of a member in a structure. |
| [WriteControlSpace function](nf-wdbgexts-writecontrolspace.md) | The WriteControlSpace function writes to the processor-specific control space of the current target. |
| [ReadField function](nf-wdbgexts-readfield.md) | TBD |
| [WriteIoSpace32 function](nf-wdbgexts-writeiospace32.md) | TBD |
| [ListType function](nf-wdbgexts-listtype.md) | The ListType function calls a specified callback function for every element in a linked list. |
| [InitTypeRead function](nf-wdbgexts-inittyperead.md) | TBD |
| [ReadTypedControlSpace64 function](nf-wdbgexts-readtypedcontrolspace64.md) | TBD |
| [ReadIoSpaceEx32 function](nf-wdbgexts-readiospaceex32.md) | TBD |
| [GetTypeSize function](nf-wdbgexts-gettypesize.md) | The GetTypeSize function returns the size in the target's memory of an instance of the specified type. |
| [GetKdContext function](nf-wdbgexts-getkdcontext.md) | The GetKdContext function returns the total number of processors and the number of the current processor in the structure ppi points to. |
| [GetExpressionEx function](nf-wdbgexts-getexpressionex.md) | The GetExpressionEx function evaluates an expression. The expression is evaluated using the MASM evaluator, and can contain aliases. |
| [ReadFieldStr function](nf-wdbgexts-readfieldstr.md) | TBD |
| [ReadIoSpace32 function](nf-wdbgexts-readiospace32.md) | TBD |
| [GetFieldData function](nf-wdbgexts-getfielddata.md) | The GetFieldData function returns the value of a member in a structure. |
| [ReadMsr function](nf-wdbgexts-readmsr.md) | The ReadMsr function reads the contents of a Model-Specific Register (MSR). |
| [DECLARE_API function](nf-wdbgexts-declare-api.md) | TBD |
| [GetShortField function](nf-wdbgexts-getshortfield.md) | The GetShortField function reads the value of a member in a structure if its size is less than or equal to 8 bytes, or initializes a structure so it can be read later. |
| [ReadPhysical function](nf-wdbgexts-readphysical.md) | The ReadPhysical function reads from physical memory. |
| [GetInputLine function](nf-wdbgexts-getinputline.md) | The GetInputLine function requests an input string from the debugger. |
| [ReadPhysicalWithFlags function](nf-wdbgexts-readphysicalwithflags.md) | The ReadPhysicalWithFlags function reads from physical memory. |
| [ReloadSymbols function](nf-wdbgexts-reloadsymbols.md) | The ReloadSymbols function deletes symbol information from the debugger so that it can be reloaded as needed. This function behaves the same way as the debugger command .reload. |
| [WriteIoSpaceEx64 function](nf-wdbgexts-writeiospaceex64.md) | The WriteIoSpaceEx64 function is an extended version of WriteIoSpace64. |
| [SetThreadForOperation function](nf-wdbgexts-setthreadforoperation.md) | The SetThreadForOperation function sets the thread to use for the next StackTrace call. |
| [GetCurrentThreadAddr function](nf-wdbgexts-getcurrentthreadaddr.md) | The GetCurrentThreadAddr function returns the location of the system data that describes the current thread. |
| [InitTypeStrReadPhysical function](nf-wdbgexts-inittypestrreadphysical.md) | TBD |
| [DECLARE_API32 function](nf-wdbgexts-declare-api32.md) | TBD |
| [GetCurrentProcessAddr function](nf-wdbgexts-getcurrentprocessaddr.md) | The GetCurrentProcessAddr function returns the location of the system data that describes the current process. |
| [ReadPointer function](nf-wdbgexts-readpointer.md) | The ReadPointer function reads a pointer from the target. |
| [WritePhysicalWithFlags function](nf-wdbgexts-writephysicalwithflags.md) | The WritePhysicalWithFlags function writes to physical memory. |
| [ReadTypedControlSpace32 function](nf-wdbgexts-readtypedcontrolspace32.md) | TBD |
| [ReadControlSpace function](nf-wdbgexts-readcontrolspace.md) | The ReadControlSpace function reads the processor-specific control space into the array pointed to by buf. |
| [TranslateVirtualToPhysical function](nf-wdbgexts-translatevirtualtophysical.md) | The TranslateVirtualToPhysical function translates a virtual memory address into a physical memory address. |
| [SearchMemory function](nf-wdbgexts-searchmemory.md) | The SearchMemory function searches the target's virtual memory for a specified pattern of bytes. |
| [IsPtr64 function](nf-wdbgexts-isptr64.md) | The IsPtr64 function determines if the target uses 64-bit pointers. |
| [GetDebuggerCacheSize function](nf-wdbgexts-getdebuggercachesize.md) | The GetDebuggerCacheSize function returns the size of the cache that is used by the debugger to hold data that was obtained from the target. |
| [DECLARE_API64 function](nf-wdbgexts-declare-api64.md) | TBD |
| [WriteIoSpace function](nf-wdbgexts-writeiospace.md) | The WriteIoSpace function writes to the system I/O locations. |
| [WriteMsr function](nf-wdbgexts-writemsr.md) | The WriteMsr function writes to a Model-Specific Register (MSR). |
| [ReadListEntry function](nf-wdbgexts-readlistentry.md) | The ReadListEntry function reads a doubly-linked list entry from the target's memory. |
| [ReadPtr function](nf-wdbgexts-readptr.md) | The ReadPtr function reads a pointer from the target. ReadPointer should be used instead of this function as the return value of ReadPointer is more consistent with the rest of the WdbgExts API. |
| [ReadIoSpace function](nf-wdbgexts-readiospace.md) | The ReadIoSpace function reads from the system I/O locations. |
| [WriteIoSpaceEx function](nf-wdbgexts-writeiospaceex.md) | The WriteIoSpaceEx function is an extended version of WriteIoSpace. |
| [InitTypeStrRead function](nf-wdbgexts-inittypestrread.md) | TBD |
| [ReadIoSpaceEx64 function](nf-wdbgexts-readiospaceex64.md) | The ReadIoSpaceEx64 function is an extended version of ReadIoSpace64. |
| [WriteIoSpace64 function](nf-wdbgexts-writeiospace64.md) | The WriteIoSpace64 function writes to the system I/O locations. |
| [DBG_DUMP_RECUR_LEVEL function](nf-wdbgexts-dbg-dump-recur-level.md) | TBD |
| [ReadIoSpaceEx function](nf-wdbgexts-readiospaceex.md) | The ReadIoSpaceEx function is an extended version of ReadIoSpace. |
| [GetCurrentProcessHandle function](nf-wdbgexts-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
| [SetThreadForOperation64 function](nf-wdbgexts-setthreadforoperation64.md) | The SetThreadForOperation64 function sets the thread to use for the next StackTrace call. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [unnamed_enum_0acf_1 enumeration](ne-wdbgexts---unnamed-enum-0acf-1.md) | TBD |
| [DBGKD_MAJOR_TYPES enumeration](ne-wdbgexts--dbgkd-major-types.md) | TBD |
| [EXT_TDOP enumeration](ne-wdbgexts--ext-tdop.md) | The EXT_TDOP enumeration is used in the Operation member of the EXT_TYPED_DATA structure to specify which suboperation the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation will perform. |

This header is used in these topics:

- [debugger](..content/_debugger)
