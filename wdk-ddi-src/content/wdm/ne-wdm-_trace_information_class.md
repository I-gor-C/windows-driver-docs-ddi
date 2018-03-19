---
UID: NE:wdm._TRACE_INFORMATION_CLASS
title: "_TRACE_INFORMATION_CLASS"
author: windows-driver-content
description: The TRACE_INFORMATION_CLASS enumeration type is used to indicate types of information associated with a WMI event tracing session.
old-location: kernel\trace_information_class.htm
old-project: kernel
ms.assetid: 38fa1687-5ad6-4536-8930-8505e5960207
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: AllLoggerHandlesClass, DiskIoNotifyRoutinesClass, EventLoggerHandleClass, FltIoNotifyRoutinesClass, GlobalLoggerHandleClass, LoggerEventsLoggedClass, LoggerEventsLostClass, MaxTraceInformationClass, TRACE_INFORMATION_CLASS, TRACE_INFORMATION_CLASS enumeration [Kernel-Mode Driver Architecture], TraceEnableFlagsClass, TraceEnableLevelClass, TraceHandleByNameClass, TraceHandleClass, TraceIdClass, TraceInformationClassReserved1, TraceInformationClassReserved2, TraceSessionSettingsClass, WdfNotifyRoutinesClass, _TRACE_INFORMATION_CLASS, kernel.trace_information_class, sysenum_a5da840d-6bda-44cb-81b3-905ece3356cd.xml, wdm/AllLoggerHandlesClass, wdm/DiskIoNotifyRoutinesClass, wdm/EventLoggerHandleClass, wdm/FltIoNotifyRoutinesClass, wdm/GlobalLoggerHandleClass, wdm/LoggerEventsLoggedClass, wdm/LoggerEventsLostClass, wdm/MaxTraceInformationClass, wdm/TRACE_INFORMATION_CLASS, wdm/TraceEnableFlagsClass, wdm/TraceEnableLevelClass, wdm/TraceHandleByNameClass, wdm/TraceHandleClass, wdm/TraceIdClass, wdm/TraceInformationClassReserved1, wdm/TraceInformationClassReserved2, wdm/TraceSessionSettingsClass, wdm/WdfNotifyRoutinesClass
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	TRACE_INFORMATION_CLASS
product: Windows
targetos: Windows
req.typenames: TRACE_INFORMATION_CLASS
req.product: Windows 10 or later.
---

# _TRACE_INFORMATION_CLASS Enumeration
The <b>TRACE_INFORMATION_CLASS</b> enumeration type is used to indicate types of information associated with a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566350">WMI event tracing</a> session.

## Syntax
````
typedef enum _TRACE_INFORMATION_CLASS { 
  TraceIdClass                    = 0,
  TraceHandleClass,
  TraceEnableFlagsClass,
  TraceEnableLevelClass,
  GlobalLoggerHandleClass,
  EventLoggerHandleClass,
  AllLoggerHandlesClass,
  TraceHandleByNameClass,
  LoggerEventsLostClass,
  TraceSessionSettingsClass,
  LoggerEventsLoggedClass,
  DiskIoNotifyRoutinesClass,
  TraceInformationClassReserved1,
  FltIoNotifyRoutinesClass,
  TraceInformationClassReserved2,
  WdfNotifyRoutinesClass,
  MaxTraceInformationClass
} TRACE_INFORMATION_CLASS;
````

## Constants

<table>
            
                <tr>
                    <td>TraceIdClass</td>
                    <td>Retrieves the logger ID (ULONG) of an event tracing session given a caller-supplied Wnode.</td>
                </tr>
            
                <tr>
                    <td>TraceHandleClass</td>
                    <td>Retrieves a trace handle (TRACEHANDLE) for an event tracing session given a caller-supplied logger ID (ULONG).</td>
                </tr>
            
                <tr>
                    <td>TraceEnableFlagsClass</td>
                    <td>Retrieves the enable flags (ULONG) set on a caller-supplied event trace handle (TRACEHANDLE).</td>
                </tr>
            
                <tr>
                    <td>TraceEnableLevelClass</td>
                    <td>Retrieves the enable level (ULONG) set on a caller-supplied event trace handle (TRACEHANDLE).</td>
                </tr>
            
                <tr>
                    <td>GlobalLoggerHandleClass</td>
                    <td>Retrieves an event trace handle (TRACEHANDLE) for the global logger.</td>
                </tr>
            
                <tr>
                    <td>EventLoggerHandleClass</td>
                    <td>Reserved for use by the operating system.</td>
                </tr>
            
                <tr>
                    <td>AllLoggerHandlesClass</td>
                    <td>Retrieves an array of event trace handles (TRACEHANDLE array) for all valid loggers.</td>
                </tr>
            
                <tr>
                    <td>TraceHandleByNameClass</td>
                    <td>Retrieves an event trace handle (TRACEHANDLE) identified by a caller-supplied friendly name (<a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a> structure in buffer).</td>
                </tr>
            
                <tr>
                    <td>LoggerEventsLostClass</td>
                    <td>Retrieves the number (ULONG) of events lost for a logger session given a caller-supplied logger ID (ULONG).</td>
                </tr>
            
                <tr>
                    <td>TraceSessionSettingsClass</td>
                    <td>Retrieves the settings (<b>ETW_TRACE_SESSION_SETTINGS</b> structure) for a logger session given a caller-supplied trace handle (TRACEHANDLE).</td>
                </tr>
            
                <tr>
                    <td>LoggerEventsLoggedClass</td>
                    <td>Retrieves the number (ULONG) of events logged in a logger session given a caller-supplied logger ID (ULONG).</td>
                </tr>
            
                <tr>
                    <td>DiskIoNotifyRoutinesClass</td>
                    <td>Reserved for use by the operating system.</td>
                </tr>
            
                <tr>
                    <td>TraceInformationClassReserved1</td>
                    <td>Reserved for use by the operating system.</td>
                </tr>
            
                <tr>
                    <td>FltIoNotifyRoutinesClass</td>
                    <td>Reserved for use by the operating system.</td>
                </tr>
            
                <tr>
                    <td>TraceInformationClassReserved2</td>
                    <td>Reserved for use by the operating system.</td>
                </tr>
            
                <tr>
                    <td>WdfNotifyRoutinesClass</td>
                    <td>Reserved for use by the operating system.</td>
                </tr>
            
                <tr>
                    <td>MaxTraceInformationClass</td>
                    <td>The maximum value in this enumeration type.</td>
                </tr>
</table>

## Remarks

<b>TRACE_INFORMATION_CLASS</b> is provided primarily for use with the <a href="..\wdm\nf-wdm-wmiquerytraceinformation.md">WmiQueryTraceInformation</a> routine, which returns information about a WMI event tracing session.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="..\wmilib\nf-wmilib-wmifireevent.md">WmiFireEvent</a>



<a href="..\wdm\nf-wdm-wmitracemessage.md">WmiTraceMessage</a>



<a href="..\wdm\nf-wdm-wmiquerytraceinformation.md">WmiQueryTraceInformation</a>



<a href="..\wdm\nf-wdm-wmitracemessageva.md">WmiTraceMessageVa</a>