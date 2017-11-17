---
UID: NS.evntrace._EVENT_TRACE_HEADER
title: EVENT_TRACE_HEADER
author: windows-driver-content
description: The EVENT_TRACE_HEADER structure is used to pass a WMI event to the WMI event logger.
old-location: kernel\event_trace_header.htm
ms.assetid: faddcf82-1025-458f-ab33-c96cd5699ca5
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: evntrace.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EVENT_TRACE_HEADER
req.alt-loc: Evntrace.h
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
ms.keywords: EVENT_TRACE_HEADER, EVENT_TRACE_HEADER, *PEVENT_TRACE_HEADER
req.iface: ExtRemoteTypedList
---

# EVENT_TRACE_HEADER structure



## -description
<p>The <b>EVENT_TRACE_HEADER</b> structure is used to pass a WMI event to the WMI event logger. It is overlaid on the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a> portion of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566373">WNODE_EVENT_ITEM</a> passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff550520">IoWMIWriteEvent</a>. Information contained in the <b>EVENT_TRACE_HEADER</b> is written to the WMI log file.</p>


## -syntax

````
typedef struct _EVENT_TRACE_HEADER {
  USHORT        Size;
  union {
    USHORT FieldTypeFlags;
    struct {
      UCHAR HeaderType;
      UCHAR MarkerFlags;
    };
  };
  union {
    ULONG  Version;
    struct {
      UCHAR  Type;
      UCHAR  Level;
      USHORT Version;
    } Class;
  };
  ULONG         ThreadId;
  ULONG         ProcessId;
  LARGE_INTEGER TimeStamp;
  union {
    GUID      Guid;
    ULONGLONG GuidPtr;
  };
  union {
    struct {
      ULONG KernelTime;
      ULONG UserTime;
    };
    ULONG64 ProcessorTime;
    struct {
      ULONG ClientContext;
      ULONG Flags;
    };
  };
} EVENT_TRACE_HEADER, *PEVENT_TRACE_HEADER;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size, in bytes, of the buffer that is allocated to hold event tracing information. The value that is specified must include both the size of the <b>EVENT_TRACE_HEADER</b> structure and the size of any driver-specific data. (<b>EVENT_TRACE_HEADER</b> is overlaid on a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a> structure, but the <b>Size</b> member of <b>EVENT_TRACE_HEADER</b> and the <b>BufferSize</b> member of <b>WNODE_HEADER</b> do not specify the same size. Do not use the <b>BufferSize</b> member of <b>WNODE_HEADER</b> to set the <b>Size</b> member.) </p>
</dd>

### -field <b>FieldTypeFlags</b>

<dd>
<p>Flags to indicate which fields in the <b>EVENT_TRACE_HEADER</b> structure are valid.</p>
</dd>

### -field <b>HeaderType</b>

<dd>
<p>Reserved for internal use.</p>
</dd>

### -field <b>MarkerFlags</b>

<dd>
<p>Reserved for internal use.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Drivers can use this member to store version information. This information is not interpreted by the event logger.</p>
</dd>

### -field <b>Class</b>

<dd>
<p>
       Event class information.</p>
<dl>

### -field <b>Type</b>

<dd>
<p>Trace event type. This can be one of the predefined EVENT_TRACE_TYPE_<i>XXX</i> values contained in Evntrace.h or can be a driver-defined value. Callers are free to define private event types with values greater than the reserved values in Evntrace.h.</p>
</dd>

### -field <b>Level</b>

<dd>
<p>Trace instrumentation level. A driver-defined value meant to represent the degree of detail of the trace instrumentation. Drivers are free to give this value meaning. This value should be 0 by default. More information about how consumers can request different levels of trace information will be provided in a future version of the documentation.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version of trace record. Version information that can be used by the driver to track different event formats.</p>
</dd>
</dl>
</dd>

### -field <b>ThreadId</b>

<dd>
<p>Thread identifier.</p>
</dd>

### -field <b>ProcessId</b>

<dd>
<p>Process identifier.</p>
</dd>

### -field <b>TimeStamp</b>

<dd>
<p>The time at which the driver event occurred. This time value is expressed in absolute system time format. Absolute system time is the number of 100-nanosecond intervals since the start of the year 1601 in the Gregorian calendar. If the WNODE_FLAG_USE_TIMESTAMP is set in <b>Flags,</b> the system logger will leave the value of <b>TimeStamp</b> unchanged. Otherwise, the system logger will set the value of <b>TimeStamp</b> at the time it receives the event. A driver can call <b>KeQuerySystemTime</b> to set the value of <b>TimeStamp</b>. </p>
</dd>

### -field <b>Guid</b>

<dd>
<p>The GUID that identifies the data block for the event. </p>
</dd>

### -field <b>GuidPtr</b>

<dd>
<p>If the WNODE_FLAG_USE_GUID_PTR flag bit is set in <b>Flags</b>, <b>GuidPtr</b> points to the GUID that identifies the data block for the event.</p>
</dd>

### -field <b>KernelTime</b>

<dd>
<p>Reserved for internal use.</p>
</dd>

### -field <b>UserTime</b>

<dd>
<p>Reserved for internal use.</p>
</dd>

### -field <b>ProcessorTime</b>

<dd>
<p>Reserved for internal use.</p>
</dd>

### -field <b>ClientContext</b>

<dd>
<p>Reserved for internal use.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Provides information about the contents of this structure. For information about <b>EVENT_TRACE_HEADER</b><b> Flags</b> values, see the <b>Flags</b> description in <a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a>.</p>
</dd>
</dl>

## -remarks
<p>A driver that supports trace events will use this structure to report events to the WMI event logger. Trace events should not be reported until the driver receives a request to enable events and the control GUID is one the driver supports. The driver should initialize an <b>EVENT_TRACE_HEADER</b> structure, fill in any user-defined event data at the end, and pass a pointer to the <b>EVENT_TRACE_HEADER</b> to <b>IoWMIWriteEvent</b>. The driver should continue reporting trace events until it receives a request to disable the control GUID for the trace events.</p>

<p>If the driver does not specify the WNODE_FLAG_USE_MOF_PTR flag in the <b>Flags</b> member of <b>EVENT_TRACE_HEADER</b>, the <b>EVENT_TRACE_HEADER</b> structure is followed in memory by event-specific data. In this case, the <b>Size</b> member must be <b>sizeof</b>(<b>EVENT_TRACE_HEADER</b>) plus the size of the event-specific data. </p>

<p>If the driver does specify the WNODE_FLAG_USE_MOF_PTR flag, the <b>EVENT_TRACE_HEADER</b> structure is followed in memory by an array of <b>MOF_FIELD</b> structures (which are defined in Evntrace.h) that contain pointers to the data and sizes rather than the event tracing data itself. In this case, the <b>Size</b> member must be <b>sizeof</b>(<b>EVENT_TRACE_HEADER</b>) plus the size of the array of <b>MOF_FIELD</b> structures.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Evntrace.h (include Wdm.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550520">IoWMIWriteEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566373">WNODE_EVENT_ITEM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566375">WNODE_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20EVENT_TRACE_HEADER structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
