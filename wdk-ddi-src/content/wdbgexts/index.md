---
UID : NA:wdbgexts
ms.assetid : 47d4ebbf-84ee-3898-8135-fa80fd566021
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# wdbgexts.h header



wdbgexts.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [PSYM_DUMP_FIELD_CALLBACK](nc-wdbgexts-psym_dump_field_callback.md) | The PSYM_DUMP_FIELD_CALLBACK callback function is called by the debugger engine during the IG_DUMP_SYMBOL_INFO Ioctl operation with information about a member in the specified symbol. |
| [PWINDBG_CHECK_VERSION](nc-wdbgexts-pwindbg_check_version.md) | The PWINDBG_CHECK_VERSION (CheckVersion) callback function verifies that the extension module version matches the debugger version, and outputs an warning message if there is a mismatch. |
| [PWINDBG_EXTENSION_API_VERSION](nc-wdbgexts-pwindbg_extension_api_version.md) | The PWINDBG_EXTENSION_API_VERSION (ExtensionApiVersion) callback function returns version information about the extension DLL. |
| [PWINDBG_EXTENSION_DLL_INIT](nc-wdbgexts-pwindbg_extension_dll_init.md) | The PWINDBG_EXTENSION_DLL_INIT ( WinDbgExtensionDllInit) callback function is used to load and initialize the extension module. |
| [PWINDBG_OUTPUT_ROUTINE](nc-wdbgexts-pwindbg_output_routine.md) | The callback function implements the functionality to print a formatted string to the Debugger Command window. |
| [GetCurrentProcessAddr](nf-wdbgexts-getcurrentprocessaddr.md) | The GetCurrentProcessAddr function returns the location of the system data that describes the current process. |
| [GetCurrentProcessHandle](nf-wdbgexts-getcurrentprocesshandle.md) | The GetCurrentProcessHandle function returns the system handle for the current process. |
| [GetCurrentThreadAddr](nf-wdbgexts-getcurrentthreadaddr.md) | The GetCurrentThreadAddr function returns the location of the system data that describes the current thread. |
| [GetDebuggerCacheSize](nf-wdbgexts-getdebuggercachesize.md) | The GetDebuggerCacheSize function returns the size of the cache that is used by the debugger to hold data that was obtained from the target. |
| [GetDebuggerData](nf-wdbgexts-getdebuggerdata.md) | The GetDebuggerData function retrieves information stored in a data block. |
| [GetExpressionEx](nf-wdbgexts-getexpressionex.md) | The GetExpressionEx function evaluates an expression. The expression is evaluated using the MASM evaluator, and can contain aliases. |
| [GetFieldData](nf-wdbgexts-getfielddata.md) | The GetFieldData function returns the value of a member in a structure. |
| [GetFieldOffset](nf-wdbgexts-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [GetFieldValue](nf-wdbgexts-getfieldvalue.md) | The GetFieldValue macro is a thin wrapper around the GetFieldData function. It is provided as a convenience for reading the value of a member in a structure. |
| [GetInputLine](nf-wdbgexts-getinputline.md) | The GetInputLine function requests an input string from the debugger. |
| [GetKdContext](nf-wdbgexts-getkdcontext.md) | The GetKdContext function returns the total number of processors and the number of the current processor in the structure ppi points to. |
| [GetPebAddress](nf-wdbgexts-getpebaddress.md) | The GetPebAddress function returns the address of the process environment block (PEB) for a system process. |
| [GetSetSympath](nf-wdbgexts-getsetsympath.md) | The GetSetSympath function can be used to either get or set the symbol search path. |
| [GetShortField](nf-wdbgexts-getshortfield.md) | The GetShortField function reads the value of a member in a structure if its size is less than or equal to 8 bytes, or initializes a structure so it can be read later. |
| [GetTebAddress](nf-wdbgexts-gettebaddress.md) | The GetTebAddress function returns the address of the thread environment block (TEB) for the current operating system thread. |
| [GetTypeSize](nf-wdbgexts-gettypesize.md) | The GetTypeSize function returns the size in the target's memory of an instance of the specified type. |
| [IsPtr64](nf-wdbgexts-isptr64.md) | The IsPtr64 function determines if the target uses 64-bit pointers. |
| [ListType](nf-wdbgexts-listtype.md) | The ListType function calls a specified callback function for every element in a linked list. |
| [ReadControlSpace](nf-wdbgexts-readcontrolspace.md) | The ReadControlSpace function reads the processor-specific control space into the array pointed to by buf. |
| [ReadControlSpace64](nf-wdbgexts-readcontrolspace64.md) | The ReadControlSpace64 function reads the processor-specific control space into the array pointed to by buf. |
| [ReadIoSpace](nf-wdbgexts-readiospace.md) | The ReadIoSpace function reads from the system I/O locations. |
| [ReadIoSpace64](nf-wdbgexts-readiospace64.md) | The ReadIoSpace64 function reads from the system I/O locations. |
| [ReadIoSpaceEx](nf-wdbgexts-readiospaceex.md) | The ReadIoSpaceEx function is an extended version of ReadIoSpace. |
| [ReadIoSpaceEx64](nf-wdbgexts-readiospaceex64.md) | The ReadIoSpaceEx64 function is an extended version of ReadIoSpace64. |
| [ReadListEntry](nf-wdbgexts-readlistentry.md) | The ReadListEntry function reads a doubly-linked list entry from the target's memory. |
| [ReadMsr](nf-wdbgexts-readmsr.md) | The ReadMsr function reads the contents of a Model-Specific Register (MSR). |
| [ReadPhysical](nf-wdbgexts-readphysical.md) | The ReadPhysical function reads from physical memory. |
| [ReadPhysicalWithFlags](nf-wdbgexts-readphysicalwithflags.md) | The ReadPhysicalWithFlags function reads from physical memory. |
| [ReadPointer](nf-wdbgexts-readpointer.md) | The ReadPointer function reads a pointer from the target. |
| [ReadPtr](nf-wdbgexts-readptr.md) | The ReadPtr function reads a pointer from the target. ReadPointer should be used instead of this function as the return value of ReadPointer is more consistent with the rest of the WdbgExts API. |
| [ReloadSymbols](nf-wdbgexts-reloadsymbols.md) | The ReloadSymbols function deletes symbol information from the debugger so that it can be reloaded as needed. This function behaves the same way as the debugger command .reload. |
| [SearchMemory](nf-wdbgexts-searchmemory.md) | The SearchMemory function searches the target's virtual memory for a specified pattern of bytes. |
| [SetThreadForOperation](nf-wdbgexts-setthreadforoperation.md) | The SetThreadForOperation function sets the thread to use for the next StackTrace call. |
| [SetThreadForOperation64](nf-wdbgexts-setthreadforoperation64.md) | The SetThreadForOperation64 function sets the thread to use for the next StackTrace call. |
| [TranslateVirtualToPhysical](nf-wdbgexts-translatevirtualtophysical.md) | The TranslateVirtualToPhysical function translates a virtual memory address into a physical memory address. |
| [WriteControlSpace](nf-wdbgexts-writecontrolspace.md) | The WriteControlSpace function writes to the processor-specific control space of the current target. |
| [WriteIoSpace](nf-wdbgexts-writeiospace.md) | The WriteIoSpace function writes to the system I/O locations. |
| [WriteIoSpace64](nf-wdbgexts-writeiospace64.md) | The WriteIoSpace64 function writes to the system I/O locations. |
| [WriteIoSpaceEx](nf-wdbgexts-writeiospaceex.md) | The WriteIoSpaceEx function is an extended version of WriteIoSpace. |
| [WriteIoSpaceEx64](nf-wdbgexts-writeiospaceex64.md) | The WriteIoSpaceEx64 function is an extended version of WriteIoSpace64. |
| [WriteMsr](nf-wdbgexts-writemsr.md) | The WriteMsr function writes to a Model-Specific Register (MSR). |
| [WritePhysical](nf-wdbgexts-writephysical.md) | The WritePhysical function writes to physical memory. |
| [WritePhysicalWithFlags](nf-wdbgexts-writephysicalwithflags.md) | The WritePhysicalWithFlags function writes to physical memory. |
| [WritePointer](nf-wdbgexts-writepointer.md) | The WritePointer function writes a pointer to the target. |



## Structures
| Title | Description |
| ---- |:---- |
| [_DBGKD_GET_VERSION64](ns-wdbgexts-_dbgkd_get_version64.md) | The IG_GET_KERNEL_VERSION Ioctl operation receives information related to the operating system version of the target. |
| [_DEBUG_TYPED_DATA](ns-wdbgexts-_debug_typed_data.md) | The DEBUG_TYPED_DATA structure describes typed data in the memory of the target. |
| [_EXT_TYPED_DATA](ns-wdbgexts-_ext_typed_data.md) | The EXT_TYPED_DATA structure is passed to and returned from the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation. It contains the input and output parameters for the operation as well as specifying which particular suboperation to perform. |
| [_FIELD_INFO](ns-wdbgexts-_field_info.md) | The FIELD_INFO structure is used by the IG_DUMP_SYMBOL_INFOIoctl operation to provide information about a member in a structure. |
| [_GETSETBUSDATA](ns-wdbgexts-_getsetbusdata.md) | The IG_GET_BUS_DATA Ioctl operation reads data from a system bus and the IG_SET_BUS_DATA Ioctl operation writes data to a system bus. |
| [_POINTER_SEARCH_PHYSICAL](ns-wdbgexts-_pointer_search_physical.md) | The IG_POINTER_SEARCH_PHYSICAL Ioctl operation searches the target's physical memory for pointers lying within a specified range. |
| [_SYM_DUMP_PARAM](ns-wdbgexts-_sym_dump_param.md) | The IG_DUMP_SYMBOL_INFO Ioctl operation provides information about the type of a symbol. |
| [_WDBGEXTS_THREAD_OS_INFO](ns-wdbgexts-_wdbgexts_thread_os_info.md) | The IG_GET_THREAD_OS_INFO Ioctl operation returns information about an operating system thread in the target. When calling Ioctl with IoctlType set to IG_GET_THREAD_OS_INFO, IpvData should contain an instance of the WDBGEXTS_THREAD_OS_INFO structure. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_EXT_TDOP](ne-wdbgexts-_ext_tdop.md) | The EXT_TDOP enumeration is used in the Operation member of the EXT_TYPED_DATA structure to specify which suboperation the DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Request operation will perform. |