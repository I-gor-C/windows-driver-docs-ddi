---
UID: NS.storport._STORPORT_TELEMETRY_EVENT
title: STORPORT_TELEMETRY_EVENT
author: windows-driver-content
description: The STORPORT_TELEMETRY_EVENT structure describes the miniport telemetry data payload.
old-location: storage\storport_telemetry_event.htm
old-project: storage
ms.assetid: 50A3EB6D-C485-4C04-8E88-9BD7D7ED0A62
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORPORT_TELEMETRY_EVENT, STORPORT_TELEMETRY_EVENT, *PSTORPORT_TELEMETRY_EVENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Storport.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORPORT_TELEMETRY_EVENT
req.alt-loc: storport.h
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
req.iface: 
req.product: Windows 10 or later.
---

# STORPORT_TELEMETRY_EVENT structure



## -description
<p>The <b>STORPORT_TELEMETRY_EVENT</b> structure describes the miniport telemetry data payload.</p>


## -syntax

````
typedef struct _STORPORT_TELEMETRY_EVENT {
  ULONG                                             DriverVersion;
  ULONG                                             EventId;
  UCHAR                                             EventName[EVENT_NAME_MAX_LENGTH];
  ULONG                                             EventVersion;
  ULONG                                             Flags;
  _Field_range_(0, EVENT_BUFFER_MAX_LENGTH)
  ULONG EventBufferLength;
  _Field_size_bytes_(EventBufferLength)
    PUCHAR  EventBuffer;
  UCHAR                                             ParameterName0[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue0;
  UCHAR                                             ParameterName1[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue1;
  UCHAR                                             ParameterName2[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue2;
  UCHAR                                             ParameterName3[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue3;
  UCHAR                                             ParameterName4[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue4;
  UCHAR                                             ParameterName5[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue5;
  UCHAR                                             ParameterName6[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue6;
  UCHAR                                             ParameterName7[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG                                         ParameterValue7;
} STORPORT_TELEMETRY_EVENT, *PSTORPORT_TELEMETRY_EVENT;
````


## -struct-fields
<dl>

### -field DriverVersion

<dd>
<p>Miniport driver version.</p>
</dd>

### -field EventId

<dd>
<p>A miniport defined identifier for the telemetry event.</p>
</dd>

### -field EventName

<dd>
<p>A miniport defined name for the telemetry event, which has the maximum length of <b>EVENT_NAME_MAX_LENGTH</b>.</p>
</dd>

### -field EventVersion

<dd>
<p>A miniport defined version for the telemetry event.</p>
</dd>

### -field Flags

<dd>
<p>Reserved.</p>
</dd>

### -field EventBufferLength

<dd>
<p>The length of <b>EventBuffer</b>, which should be not larger than <b>EVENT_BUFFER_MAX_LENGTH</b> that is 4KB.</p>
</dd>

### -field EventBuffer

<dd>
<p>A miniport defined telemetry payload, the length of which is <b>EventBufferLength</b>.</p>
</dd>

### -field ParameterName0

<dd>
<p>A description of the of the meaning of ParameterValue0. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.</p>
</dd>

### -field ParameterValue0

<dd>
<p>The value for parameter 0.</p>
</dd>

### -field ParameterName1

<dd>
<p>A description of the of the meaning of ParameterValue1. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.</p>
</dd>

### -field ParameterValue1

<dd>
<p>The value for parameter 1.</p>
</dd>

### -field ParameterName2

<dd>
<p>A description of the of the meaning of ParameterValue2. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.</p>
</dd>

### -field ParameterValue2

<dd>
<p>The value for parameter 2.</p>
</dd>

### -field ParameterName3

<dd>
<p>A description of the of the meaning of ParameterValue3. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.</p>
</dd>

### -field ParameterValue3

<dd>
<p>The value for parameter 3.</p>
</dd>

### -field ParameterName4

<dd>
<p>A description of the of the meaning of ParameterValue4. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.</p>
</dd>

### -field ParameterValue4

<dd>
<p>The value for parameter 4.</p>
</dd>

### -field ParameterName5

<dd>
<p>A description of the of the meaning of ParameterValue5. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.</p>
</dd>

### -field ParameterValue5

<dd>
<p>The value for parameter 5.</p>
</dd>

### -field ParameterName6

<dd>
<p>A description of the of the meaning of ParameterValue6. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.</p>
</dd>

### -field ParameterValue6

<dd>
<p>The value for parameter 6.</p>
</dd>

### -field ParameterName7

<dd>
<p>A description of the of the meaning of ParameterValue7. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.</p>
</dd>

### -field ParameterValue7

<dd>
<p>The value for parameter 7.</p>
</dd>
</dl>

## -remarks
<p>A <b>STORPORT_TELEMETRY_EVENT</b> structure describes the miniport telemetry data payload. The miniport should fill it when calling StorPortLogTelemetry.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1703</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\storport\nf-storport-storportlogtelemetry.md">StorPortLogTelemetry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORPORT_TELEMETRY_EVENT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
