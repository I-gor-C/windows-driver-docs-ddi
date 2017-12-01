---
UID: NE.wdm._TRACE_INFORMATION_CLASS
title: TRACE_INFORMATION_CLASS
author: windows-driver-content
description: The TRACE_INFORMATION_CLASS enumeration type is used to indicate types of information associated with a WMI event tracing session.
old-location: kernel\trace_information_class.htm
old-project: kernel
ms.assetid: 38fa1687-5ad6-4536-8930-8505e5960207
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
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
req.alt-api: TRACE_INFORMATION_CLASS
req.alt-loc: Wdm.h
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
req.iface: 
req.product: Windows 10 or later.
---

# TRACE_INFORMATION_CLASS enumeration



## -description
<p>The <b>TRACE_INFORMATION_CLASS</b> enumeration type is used to indicate types of information associated with a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566350">WMI event tracing</a> session.</p>


## -syntax

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


## -enum-fields
<dl>

### -field <a id="TraceIdClass"></a><a id="traceidclass"></a><a id="TRACEIDCLASS"></a><b>TraceIdClass</b>

<dd>
<p>Retrieves the logger ID (ULONG) of an event tracing session given a caller-supplied Wnode.</p>
</dd>

### -field <a id="TraceHandleClass"></a><a id="tracehandleclass"></a><a id="TRACEHANDLECLASS"></a><b>TraceHandleClass</b>

<dd>
<p>Retrieves a trace handle (TRACEHANDLE) for an event tracing session given a caller-supplied logger ID (ULONG).</p>
</dd>

### -field <a id="TraceEnableFlagsClass"></a><a id="traceenableflagsclass"></a><a id="TRACEENABLEFLAGSCLASS"></a><b>TraceEnableFlagsClass</b>

<dd>
<p>Retrieves the enable flags (ULONG) set on a caller-supplied event trace handle (TRACEHANDLE).</p>
</dd>

### -field <a id="TraceEnableLevelClass"></a><a id="traceenablelevelclass"></a><a id="TRACEENABLELEVELCLASS"></a><b>TraceEnableLevelClass</b>

<dd>
<p>Retrieves the enable level (ULONG) set on a caller-supplied event trace handle (TRACEHANDLE).</p>
</dd>

### -field <a id="GlobalLoggerHandleClass"></a><a id="globalloggerhandleclass"></a><a id="GLOBALLOGGERHANDLECLASS"></a><b>GlobalLoggerHandleClass</b>

<dd>
<p>Retrieves an event trace handle (TRACEHANDLE) for the global logger.</p>
</dd>

### -field <a id="EventLoggerHandleClass"></a><a id="eventloggerhandleclass"></a><a id="EVENTLOGGERHANDLECLASS"></a><b>EventLoggerHandleClass</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>

### -field <a id="AllLoggerHandlesClass"></a><a id="allloggerhandlesclass"></a><a id="ALLLOGGERHANDLESCLASS"></a><b>AllLoggerHandlesClass</b>

<dd>
<p>Retrieves an array of event trace handles (TRACEHANDLE array) for all valid loggers.</p>
</dd>

### -field <a id="TraceHandleByNameClass"></a><a id="tracehandlebynameclass"></a><a id="TRACEHANDLEBYNAMECLASS"></a><b>TraceHandleByNameClass</b>

<dd>
<p>Retrieves an event trace handle (TRACEHANDLE) identified by a caller-supplied friendly name (<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure in buffer).</p>
</dd>

### -field <a id="LoggerEventsLostClass"></a><a id="loggereventslostclass"></a><a id="LOGGEREVENTSLOSTCLASS"></a><b>LoggerEventsLostClass</b>

<dd>
<p>Retrieves the number (ULONG) of events lost for a logger session given a caller-supplied logger ID (ULONG).</p>
</dd>

### -field <a id="TraceSessionSettingsClass"></a><a id="tracesessionsettingsclass"></a><a id="TRACESESSIONSETTINGSCLASS"></a><b>TraceSessionSettingsClass</b>

<dd>
<p>Retrieves the settings (<b>ETW_TRACE_SESSION_SETTINGS</b> structure) for a logger session given a caller-supplied trace handle (TRACEHANDLE).</p>
</dd>

### -field <a id="LoggerEventsLoggedClass"></a><a id="loggereventsloggedclass"></a><a id="LOGGEREVENTSLOGGEDCLASS"></a><b>LoggerEventsLoggedClass</b>

<dd>
<p>Retrieves the number (ULONG) of events logged in a logger session given a caller-supplied logger ID (ULONG).</p>
</dd>

### -field <a id="DiskIoNotifyRoutinesClass"></a><a id="diskionotifyroutinesclass"></a><a id="DISKIONOTIFYROUTINESCLASS"></a><b>DiskIoNotifyRoutinesClass</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>

### -field <a id="TraceInformationClassReserved1"></a><a id="traceinformationclassreserved1"></a><a id="TRACEINFORMATIONCLASSRESERVED1"></a><b>TraceInformationClassReserved1</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>

### -field <a id="FltIoNotifyRoutinesClass"></a><a id="fltionotifyroutinesclass"></a><a id="FLTIONOTIFYROUTINESCLASS"></a><b>FltIoNotifyRoutinesClass</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>

### -field <a id="TraceInformationClassReserved2"></a><a id="traceinformationclassreserved2"></a><a id="TRACEINFORMATIONCLASSRESERVED2"></a><b>TraceInformationClassReserved2</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>

### -field <a id="WdfNotifyRoutinesClass"></a><a id="wdfnotifyroutinesclass"></a><a id="WDFNOTIFYROUTINESCLASS"></a><b>WdfNotifyRoutinesClass</b>

<dd>
<p>Reserved for use by the operating system.</p>
</dd>

### -field <a id="MaxTraceInformationClass"></a><a id="maxtraceinformationclass"></a><a id="MAXTRACEINFORMATIONCLASS"></a><b>MaxTraceInformationClass</b>

<dd>
<p>The maximum value in this enumeration type.</p>
</dd>
</dl>

## -remarks
<p><b>TRACE_INFORMATION_CLASS</b> is provided primarily for use with the <a href="..\wdm\nf-wdm-wmiquerytraceinformation.md">WmiQueryTraceInformation</a> routine, which returns information about a WMI event tracing session.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wmilib\nf-wmilib-wmifireevent.md">WmiFireEvent</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-wmiquerytraceinformation.md">WmiQueryTraceInformation</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-wmitracemessage.md">WmiTraceMessage</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-wmitracemessageva.md">WmiTraceMessageVa</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TRACE_INFORMATION_CLASS enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
