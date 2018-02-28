---
UID: NE:extsfns._DEBUG_FLR_PARAM_TYPE
title: "_DEBUG_FLR_PARAM_TYPE"
author: windows-driver-content
description: The values of DEBUG_FLR_PARAM_TYPE enumeration are tags that indicate the kind of information that is stored in failure analysis entry.
old-location: debugger\debug_flr_param_type.htm
old-project: debugger
ms.assetid: D57D356F-DC11-4C27-97D3-DF40BF2AB490
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "..., DEBUG_FLR_DRIVER_OBJECT, DEBUG_FLR_INVALID, DEBUG_FLR_MASK_ALL, DEBUG_FLR_PARAM_TYPE, DEBUG_FLR_PARAM_TYPE enumeration [Windows Debugging], DEBUG_FLR_RESERVED, FA_TAG, _DEBUG_FLR_PARAM_TYPE, debugger.debug_flr_param_type, extsfns/..., extsfns/DEBUG_FLR_DRIVER_OBJECT, extsfns/DEBUG_FLR_INVALID, extsfns/DEBUG_FLR_MASK_ALL, extsfns/DEBUG_FLR_PARAM_TYPE, extsfns/DEBUG_FLR_RESERVED"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: extsfns.h
req.include-header: 
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
-	HeaderDef
api_location:
-	extsfns.h
api_name:
-	DEBUG_FLR_PARAM_TYPE
product: Windows
targetos: Windows
req.typenames: DEBUG_FLR_PARAM_TYPE
---

# _DEBUG_FLR_PARAM_TYPE Enumeration
The values of <b>DEBUG_FLR_PARAM_TYPE</b> enumeration are tags that indicate the kind of information that is stored in <a href="https://msdn.microsoft.com/759DE159-F2A8-4BB1-AAF5-B2B91C4F91B0">failure analysis entry</a>.

The <b>DEBUG_FLR_PARAM_TYPE</b> enumeration is also called the <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/writing-an-analysis-extension-to-extend--analyze">FA_TAG</a> enumeration.

## Syntax
````
typedef enum _DEBUG_FLR_PARAM_TYPE { 
  DEBUG_FLR_INVALID        = 0,
  DEBUG_FLR_RESERVED,
  DEBUG_FLR_DRIVER_OBJECT,
  ...,
  DEBUG_FLR_MASK_ALL       = 0xFFFFFFFF
} DEBUG_FLR_PARAM_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>DEBUG_FLR_ACPI_EXTENSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ACPI_OBJECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ACPI_RESCONFLICT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ADD_PROCESS_IN_BUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ADDITIONAL_DEBUGTEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ALUREON</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ANALYSIS_REPROCESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ANALYSIS_SESSION_ELAPSED_TIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ANALYSIS_SESSION_HOST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ANALYSIS_SESSION_TIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ANALYSIS_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ANALYZAABLE_POOL_CORRUPTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_APPKILL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_APPLICATION_VERIFIER_LOADED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_APPS_NOT_TERMINATED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_APPVERIFERFLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ARM_WRITE_AV_CAVEAT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ASSERT_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ASSERT_FILE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ASSERT_INSTRUCTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BAD_HANDLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BAD_MEMORY_REFERENCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BAD_OBJECT_REFERENCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BAD_STACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BADPAGES_DETECTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BLOCKED_THREAD0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BLOCKED_THREAD1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BLOCKED_THREAD2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BLOCKING_PROCESSID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BLOCKING_THREAD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BOOST_FOLLOWUP_TO_SPECIFIC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_CHECKSUM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_FLAVOR_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_FUNC_OFFSET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_FUNCTION_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_IMAGE_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_MODULE_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_MODVER_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_OFFSET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_PREFIX_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_PRIVATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUCKET_ID_TIMEDATESTAMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECK_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECK_DESC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECK_P1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECK_P2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECK_P3</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECK_P4</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECK_SPECIFIER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECK_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECKING_DRIVER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUGCHECKING_DRIVER_IDTAG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUILD_FLAVOR_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUILD_OS_FULL_VERSION_STRING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUILD_VERSION_STRING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUILDDATESTAMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUILDDATESTAMP_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUILDLAB_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUILDNAME_IN_BUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_BUILDOSVER_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CANCELLATION_NOT_SUPPORTED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CHKIMG_EXTENSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CHPE_PROCESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CLIENT_DRIVER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_COLLECT_DATA_FOR_BUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_COMPUTER_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CONTEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CONTEXT_COMMAND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CONTEXT_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CONTEXT_FOLLOWUP_INDEX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CONTEXT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CONTEXT_METADATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CONTEXT_ORDER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CONTEXT_RESTORE_COMMAND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CONTEXT_SYSTEM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CORRUPT_MODULE_LIST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CORRUPT_SERVICE_TABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CORRUPTING_POOL_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CORRUPTING_POOL_TAG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_COVERAGE_BUILD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CPU_COUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CPU_FAMILY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CPU_MICROCODE_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CPU_MICROCODE_ZERO_INTEL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CPU_MODEL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CPU_OVERCLOCKED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CPU_SPEED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CPU_STEPPING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CPU_VENDOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CRITICAL_PROCESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CRITICAL_PROCESS_REPORTGUID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CRITICAL_SECTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CURRENT_IRQL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CUSTOM_ANALYSIS_TAG_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CUSTOM_ANALYSIS_TAG_MIN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CUSTOM_COMMAND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CUSTOM_COMMAND_OUTPUT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CUSTOMER_CRASH_COUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_CUSTOMREPORTTAG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DEADLOCK_INPROC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DEADLOCK_XPROC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DEFAULT_BUCKET_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DEFAULT_SOLUTION_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DERIVED_WAIT_CHAIN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DESKTOP_HEAP_MISSING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DETOURED_IMAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DEVICE_NODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DEVICE_OBJECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DISK_HARDWARE_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DISKIO_READ_FAILURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DISKIO_WRITE_FAILURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DPC_RUNTIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DPC_STACK_BASE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DPC_TIMELIMIT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DPC_TIMEOUT_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_HARDWARE_DEVICE_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_HARDWARE_ID_BUS_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_HARDWARE_REV_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_HARDWARE_SUBSYS_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_HARDWARE_VENDOR_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_HARDWAREID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_OBJECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_VERIFIER_IO_VIOLATION_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_XML_DESCRIPTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_XML_MANUFACTURER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_XML_PRODUCTNAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRIVER_XML_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DRVPOWERSTATE_SUBCODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DUMP_CLASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DUMP_FILE_ATTRIBUTES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DUMP_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DUMP_QUALIFIER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DUMP_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DUMPSTREAM_COMMENTA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_DUMPSTREAM_COMMENTW</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_END_MESSAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ERESOURCE_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EVENT_CODE_DATA_MISMATCH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_CODE_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_CODE_STR_deprecated</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_CONTEXT_RECURSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_DOESNOT_MATCH_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_MODULE_INFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_PARAMETER1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_PARAMETER2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_PARAMETER3</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_PARAMETER4</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_RECORD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXCEPTION_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_EXECUTE_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FA_ADHOC_ANALYSIS_ITEMS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FA_PERF_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FA_PERF_ELAPSED_MS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FA_PERF_ITEM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FA_PERF_ITEM_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FA_PERF_ITERATIONS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILED_INSTRUCTION_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_ANALYSIS_SOURCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_BUCKET_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_DISPLAY_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_EXCEPTION_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_FUNCTION_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_ID_HASH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_ID_HASH_STRING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_ID_REPORT_LINK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_IMAGE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_LIST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_MODULE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_PROBLEM_CLASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAILURE_SYMBOL_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULT_THREAD_SHA1_HASH_M</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULT_THREAD_SHA1_HASH_MF</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULT_THREAD_SHA1_HASH_MFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_INSTR_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_IP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_LOCAL_VARIABLE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_MODULE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_SERVICE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_SOURCE_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_SOURCE_FILE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_SOURCE_LINE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_SOURCE_LINE_NUMBER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FAULTING_THREAD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FEATURE_PATH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FILE_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FILE_IN_CAB</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FILE_LINE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FIXED_IN_OSVERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FOLLOWUP_BEFORE_RETRACER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FOLLOWUP_BUCKET_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FOLLOWUP_CONTEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FOLLOWUP_DRIVER_ONLY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FOLLOWUP_IP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FOLLOWUP_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FRAME_ONE_INVALID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FRAME_SOURCE_FILE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FRAME_SOURCE_FILE_PATH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FRAME_SOURCE_LINE_NUMBER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_FREED_POOL_TAG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_ANALYSIS_TEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_COOKIES_MATCH_EXH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_CORRUPTED_COOKIE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_CORRUPTED_EBP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_CORRUPTED_EBPESP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_FALSE_POSITIVE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_FRAME_COOKIE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_FRAME_COOKIE_COMPLEMENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_FUNCTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_MANAGED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_MANAGED_FRAMEID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_MANAGED_THREADID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_MEMORY_READ_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_MISSING_ESTABLISHER_FRAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_MODULE_COOKIE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_NOT_UP2DATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_OFF_BY_ONE_OVERRUN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_OVERRUN_LOCAL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_OVERRUN_LOCAL_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_POSITIVE_BUFFER_OVERFLOW</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_POSITIVELY_CORRUPTED_EBPESP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_PROBABLY_NOT_USING_GS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_RA_SMASHED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_GSFAILURE_UP2DATE_UNKNOWN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HANDLE_VALUE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HANG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HANG_DATA_NEEDED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HANG_REPORT_THREAD_IS_IDLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HARDWARE_BUCKET_TAG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HARDWARE_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HIGH_NONPAGED_POOL_USAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HIGH_PAGED_POOL_USAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HIGH_PROCESS_COMMIT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HIGH_SERVICE_COMMIT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HIGH_SHARED_COMMIT_USAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_ACTIVE_HOLD_COUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_ALWAYS_HOLD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_ALWAYS_IGNORE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_HISTORIC_HOLD_COUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_LAST_SEEN_HOLD_DATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_MANUAL_HOLD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_MAX_HOLD_LIMIT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_NOTIFICATION_ALIASES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_RECOMMEND_HOLD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_HOLDINFO_TENET_SOCRE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IGNORE_BUCKET_ID_OFFSET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IGNORE_LARGE_MODULE_CORRUPTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IGNORE_MODULE_HARDWARE_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IMAGE_CLASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IMAGE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IMAGE_TIMESTAMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IMAGE_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_CLIFAULT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_IN_FREE_BLOCK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_IN_MODULE_NOT_IN_LIST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_IN_PAGED_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_IN_RESERVED_BLOCK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_IN_UNLOADED_MODULE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_IN_VM_MAPPED_MODULE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_MISALIGNED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_NOT_IN_STREAM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_ON_HEAP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_POINTER_ON_STACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INSTR_SESSION_POOL_TAG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INTEL_CPU_BIOS_UPGRADE_NEEDED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INTERNAL_BUCKET_CONTINUABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INTERNAL_BUCKET_HITCOUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INTERNAL_BUCKET_STATUS_TEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INTERNAL_BUCKET_URL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INTERNAL_RAID_BUG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INTERNAL_RAID_BUG_DATABASE_STRING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INTERNAL_RESPONSE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INTERNAL_SOLUTION_TEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INVALID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INVALID_DPC_FOUND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INVALID_HEAP_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INVALID_KERNEL_CONTEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INVALID_OPCODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INVALID_PFN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INVALID_USER_CONTEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_INVALID_USEREVENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IO_ERROR_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IOCONTROL_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IOSB_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IRP_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IRP_CANCEL_ROUTINE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IRP_MAJOR_FN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_IRP_MINOR_FN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_KERNEL_LOG_PROCESS_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_KERNEL_LOG_STATUS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_KERNEL_VERIFIER_ENABLED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_KEY_VALUES_STRING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_KEY_VALUES_VARIANT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_KM_MODULE_LIST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LARGE_TICK_INCREMENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LAST_CONTROL_TRANSFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LCIE_ISO_AVAILABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LEAKED_SESSION_POOL_TAG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LEGACY_PAGE_TABLE_ACCESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LIVE_KERNEL_DUMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LOADERLOCK_BLOCKED_API</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LOADERLOCK_IN_WAIT_CHAIN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LOADERLOCK_OWNER_API</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LOP_STACKHASH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_LOW_SYSTEM_COMMIT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MACHINE_INFO_SHA1_HASH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_ANALYSIS_PROVIDER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_BITNESS_MISMATCH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_ENGINE_MODULE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_CALLSTACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_CMD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_CONTEXT_MESSAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_HRESULT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_INNER_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_INNER_CALLSTACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_INNER_HRESULT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_INNER_MESSAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_INNER_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_MESSAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_MESSAGEX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_NESTED_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_NESTED_CALLSTACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_NESTED_HRESULT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_NESTED_MESSAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_NESTED_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_OBJECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_EXCEPTION_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_FRAME_CHAIN_CORRUPTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_HRESULT_STRING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_KERNEL_DEBUGGER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_OBJECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_OBJECT_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_STACK_COMMAND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_STACK_STRING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_THREAD_CMD_CALLSTACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_THREAD_CMD_STACKOBJECTS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANAGED_THREAD_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MANUAL_BREAKIN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MARKER_BUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MARKER_FILE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MARKER_MODULE_FILE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MASK_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MEMDIAG_LASTRUN_STATUS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MEMDIAG_LASTRUN_TIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MEMORY_CORRUPTION_SIGNATURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MEMORY_CORRUPTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MILCORE_BREAK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MINUTES_SINCE_LAST_EVENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MINUTES_SINCE_LAST_EVENT_OF_THIS_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MISSING_CLR_SYMBOL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MISSING_IMPORTANT_SYMBOL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MM_INTERNAL_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MOD_SPECIFIC_DATA_ONLY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MODLIST_SHA1_HASH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MODLIST_TSCHKSUM_SHA1_HASH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MODLIST_UNLOADED_SHA1_HASH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MODULE_BUCKET_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MODULE_LIST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MODULE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_MODULE_PRODUCTNAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_NO_ARCH_IN_BUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_NO_BUGCHECK_IN_BUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_NO_IMAGE_IN_BUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_NO_IMAGE_TIMESTAMP_IN_BUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_NTGLOBALFLAG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OLD_OS_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ON_DPC_STACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ORIGINAL_CAB_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OS_BUILD_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OS_LOCALE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OS_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OS_NAME_EDITION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OS_PLATFORM_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OS_REVISION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OS_SKU</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OSBUILD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OSSERVICEPACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OSSERVICEPACK_NUMBER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OVERLAPPED_MODULE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_OVERLAPPED_UNLOADED_MODULE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PAGE_HASH_ERRORS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PG_MISMATCH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_APPID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_APPVERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_BOOTLOADERVERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_BUILDBRANCH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_BUILDER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_BUILDNUMBER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_BUILDTIMESTAMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_FIRMWAREREVISION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_HARDWAREREVISION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_LCID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_MCCMNC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_OPERATOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_QFE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_RADIOHARDWAREREVISION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_RADIOSOFTWAREREVISION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_RAM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_REPORTGUID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_REPORTTIMESTAMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_ROMVERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_SKUID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_SOCVERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_SOURCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_SOURCEEXTERNAL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_UIF_APPID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_UIF_APPNAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_UIF_CATEGORY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_UIF_COMMENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_UIF_ORIGIN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_USERALIAS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_VERSIONMAJOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PHONE_VERSIONMINOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PLATFORM_BUCKET_STRING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PNP_IRP_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PNP_TRIAGE_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_POISONED_TB</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_POOL_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_POOL_CORRUPTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_POSSIBLE_INVALID_CONTROL_TRANSFER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_POSSIBLE_STACK_OVERFLOW</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_POWERREQUEST_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PREVIOUS_IRQL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PREVIOUS_MODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PRIMARY_PROBLEM_CLASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PRIMARY_PROBLEM_CLASS_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROBLEM_CLASSES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROBLEM_CODE_PATH_HASH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROCESS_BAM_CURRENT_THROTTLED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROCESS_BAM_PREVIOUS_THROTTLED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROCESS_INFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROCESS_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROCESS_OBJECT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROCESS_PRODUCTNAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROCESSOR_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PROCESSOR_INFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_PRODUCT_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_RAISED_IRQL_USER_FAULT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_READ_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_RECURRING_STACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_REGISTRY_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_REGISTRYTXT_SOURCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_REGISTRYTXT_STRESS_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_REPORT_INFO_CREATION_TIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_REPORT_INFO_GUID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_REPORT_INFO_SOURCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_REQUESTED_IRQL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_RESERVED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_RESOURCE_CALL_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_RESOURCE_CALL_TYPE_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SEARCH_HANG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SECURITY_COOKIES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SERVICE_GROUP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SERVICE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SERVICETABLE_MODIFIED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SHOW_ERRORLOG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SHOW_LCIE_ISO_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SIMULTANEOUS_TELSVC_INSTANCES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SIMULTANEOUS_TELWP_INSTANCES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SINGLE_BIT_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SINGLE_BIT_PFN_PAGE_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SKIP_CORRUPT_MODULE_DETECTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SKIP_MODULE_SPECIFIC_BUCKET_INFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SKIP_STACK_ANALYSIS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SM_BUFFER_HASH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SM_COMPRESSION_FORMAT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SM_ONEBIT_SOLUTION_COUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SM_SOURCE_OFFSET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SM_SOURCE_PFN1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SM_SOURCE_PFN2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SM_SOURCE_SIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SM_TARGET_PFN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SOLUTION_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SOLUTION_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SPECIAL_POOL_CORRUPTION_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_COMMAND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_FUNCTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_IMAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_INSTRUCTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_MODULE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_MODULE_BASE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_NUMBER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_SRC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_SYMBOL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAME_SYMBOL_OFFSET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_FRAMES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_OVERFLOW</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_POINTER_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_POINTER_MISALIGNED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_POINTER_ONEBIT_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_SHA1_HASH_M</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_SHA1_HASH_MF</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_SHA1_HASH_MFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACK_TEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACKUSAGE_FUNCTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACKUSAGE_FUNCTION_SIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACKUSAGE_IMAGE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACKUSAGE_IMAGE_SIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STACKUSAGE_RECURSION_COUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STATUS_CODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_DEVELOPER_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_IS_MICROSOFT_PRODUCT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_LEGACY_PARENT_PRODUCT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_LEGACY_WINDOWS_PHONE_PRODUCT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_LEGACY_WINDOWS_STORE_PRODUCT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_LEGACY_XBOX_360_PRODUCT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_LEGACY_XBOX_ONE_PRODUCT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PACKAGE_FAMILY_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PACKAGE_IDENTITY_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PREFERRED_SKU_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PRIMARY_PARENT_PRODUCT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PRODUCT_DESCRIPTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PRODUCT_DISPLAY_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PRODUCT_EXTENDED_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PRODUCT_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PUBLISHER_CERTIFICATE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PUBLISHER_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_PUBLISHER_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_URL_APP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_URL_APPHEALTH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_STORE_XBOX_TITLE_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SUITE_MASK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SUSPECT_CODE_PATH_HASH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SVCHOST_GROUP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SWITCH_PROCESS_CONTEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYMBOL_FROM_RAW_STACK_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYMBOL_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYMBOL_ON_RAW_STACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYMBOL_ROUTINE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYMBOL_STACK_INDEX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_BASEBOARD_MANUFACTURER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_BASEBOARD_PRODUCT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_BASEBOARD_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_BIOS_DATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_BIOS_VENDOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_BIOS_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_SYSTEM_MANUFACTURER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_SYSTEM_PRODUCT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_SYSTEM_SKU</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSINFO_SYSTEM_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSTEM_LOCALE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSXML_CHECKSUM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_SYSXML_LOCALEID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_TARGET_MODE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_TARGET_TIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_TESTRESULTGUID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_TESTRESULTSERVER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_THREAD_ATTRIBUTES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_THREADPOOL_WAITER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_TRAP_FRAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_TRAP_FRAME_RECURSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_TSS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_TWO_BIT_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ULS_SCRIPT_EXCEPTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_UNALIGNED_STACK_POINTER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_UNKNOWN_MODULE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_UNRESPONSIVE_UI_FOLLOWUP_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_UNRESPONSIVE_UI_PROBLEM_CLASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_UNRESPONSIVE_UI_PROBLEM_CLASS_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_UNRESPONSIVE_UI_STACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_UNRESPONSIVE_UI_SYMBOL_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_UNRESPONSIVE_UI_THREAD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_UNUSED001</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_URL_ENTRY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_URL_LCIE_ENTRY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_URL_URLMON_ENTRY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_URL_XMLHTTPREQ_SYNC_ENTRY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_URLS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_URLS_DISCOVERED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USBPORT_OCADATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USE_DEFAULT_CONTEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_GLOBAL_ATTRIBUTES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_LCID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_LCID_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_EVENTTYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_INDEX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_P0</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_P1</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_P2</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_P3</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_P4</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_P5</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_P6</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_P7</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_REPORTCREATIONTIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_REPORTGUID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_MODE_BUCKET_STRING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_PROBLEM_CLASSES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USER_THREAD_ATTRIBUTES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USERBREAK_PEB_PAGEDOUT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_USERMODE_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_VERIFIER_DRIVER_ENTRY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_VERIFIER_FOUND_DEADLOCK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_VERIFIER_STOP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_VIDEO_TDR_CONTEXT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_VIRTUAL_MACHINE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WAIT_CHAIN_COMMAND</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_00</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_01</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_02</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_03</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_04</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_05</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_06</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_07</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_08</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_BUCKETING_09</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_GENERIC_EVENT_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_IBUCKET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_IBUCKET_S1_RESP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_IBUCKETTABLE_S1_RESP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_MODULE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_MODULE_OFFSET</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_MODULE_TIMESTAMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_MODULE_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_PROCESS_TIMESTAMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_PROCESS_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WATSON_STAGEONE_STR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WCT_XML_AVAILABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WER_DATA_COLLECTION_INFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WER_MACHINE_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WERCOLLECTION_DEFAULTCOLLECTION_FAILURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WERCOLLECTION_MINIDUMP_WRITE_FAILURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WERCOLLECTION_PROCESSHEAPDUMP_REQUEST_FAILURE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WERCOLLECTION_PROCESSTERMINATED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WHEA_ERROR_RECORD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WMI_QUERY_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WORK_ITEM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WORK_QUEUE_ITEM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WORKER_ROUTINE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WQL_EVENT_COUNT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WQL_EVENTLOG_INFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WRITE_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WRONG_SYMBOLS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WRONG_SYMBOLS_SIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_WRONG_SYMBOLS_TIMESTAMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XBOX_LIVE_ENVIRONMENT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XBOX_SYSTEM_CRASHTIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XBOX_SYSTEM_UPTIME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XCS_PATH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XDV_HELP_LINK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XDV_RULE_INFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XDV_STATE_VARIABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XDV_VIOLATED_CONDITION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XHCI_FIRMWARE_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_APPLICATION_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE_D1VALUE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE_D2VALUE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE_DOVALUE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE_FRAME_NUMBER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE_LIST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE_THREAD_INDEX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE_VALUE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ATTRIBUTE_VALUE_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_ENCODED_OFFSETS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_EVENTTYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_GLOBALATTRIBUTE_LIST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODERN_ASYNC_REQUEST_OUTSTANDING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_BASE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_CHECKSUM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_COMPANY_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_DRIVER_GROUP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_FILE_DESCRIPTION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_FILE_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_FIXED_FILE_VER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_FIXED_PROD_VER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_IMAGE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_IMAGE_PATH</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_INDEX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_INTERNAL_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_ON_STACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_ORIG_FILE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_PRODUCT_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_SIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_STRING_FILE_VER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_STRING_PROD_VER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_SYMBOL_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_SYMSRV_IMAGE_DETAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_SYMSRV_IMAGE_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_SYMSRV_IMAGE_STATUS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_SYMSRV_PDB_DETAIL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_SYMSRV_PDB_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_SYMSRV_PDB_STATUS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_TIMESTAMP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_INFO_UNLOADED</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_MODULE_LIST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PACKAGE_MONIKER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PACKAGE_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PACKAGE_RELATIVE_APPLICATION_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PACKAGE_VERSION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PROBLEMCLASS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PROBLEMCLASS_FRAME_NUMBER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PROBLEMCLASS_LIST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PROBLEMCLASS_NAME</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PROBLEMCLASS_THREAD_INDEX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PROBLEMCLASS_VALUE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_PROBLEMCLASS_VALUE_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_STACK_FRAME_TRIAGE_STATUS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_SYSTEMINFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_SYSTEMINFO_SYSTEMMANUFACTURER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_SYSTEMINFO_SYSTEMMARKER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XML_SYSTEMINFO_SYSTEMMODEL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XPROC_DUMP_AVAILABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_XPROC_HANG</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DEBUG_FLR_ZEROED_STACK</td>
                    <td></td>
                </tr>
</table>

## Remarks

There are several hundred tags in the <b>DEBUG_FLR_PARAM_TYPE</b> enumeration. You can see all the tags in the extsfns.h header file, which in the Debugging Tools for Windows package.

The tags are grouped by categories, with the first entry of a new category being assigned an explicit value.  For example, the tags that are used for structured data begin with DEBUG_FLR_STACK = 0x200000.

For more information about tags, see <a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Failure Analysis Entries, Tags, and Data Types</a>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | extsfns.h |

## See Also

<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/writing-an-analysis-extension-to-extend--analyze">FA_TAG enumeration</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/jj991807">Failure Analysis Entries</a>



<a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>



<a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">IDebugFailureAnalysis2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20DEBUG_FLR_PARAM_TYPE enumeration%20 RELEASE:%20(2/23/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>