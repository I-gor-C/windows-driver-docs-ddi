---
UID: NS:storport._STORPORT_TELEMETRY_EVENT
title: "_STORPORT_TELEMETRY_EVENT"
author: windows-driver-content
description: The STORPORT_TELEMETRY_EVENT structure describes the miniport telemetry data payload.
old-location: storage\storport_telemetry_event.htm
old-project: storage
ms.assetid: 50A3EB6D-C485-4C04-8E88-9BD7D7ED0A62
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSTORPORT_TELEMETRY_EVENT, PSTORPORT_TELEMETRY_EVENT, PSTORPORT_TELEMETRY_EVENT structure pointer [Storage Devices], STORPORT_TELEMETRY_EVENT, STORPORT_TELEMETRY_EVENT structure [Storage Devices], _STORPORT_TELEMETRY_EVENT, storage.storport_telemetry_event, storport/PSTORPORT_TELEMETRY_EVENT, storport/STORPORT_TELEMETRY_EVENT"
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
-	storport.h
api_name:
-	STORPORT_TELEMETRY_EVENT
product:
- Windows
targetos: Windows
req.typenames: STORPORT_TELEMETRY_EVENT, *PSTORPORT_TELEMETRY_EVENT
req.product: Windows 10 or later.
---

# _STORPORT_TELEMETRY_EVENT structure
The <b>STORPORT_TELEMETRY_EVENT</b> structure describes the miniport telemetry data payload.

## Syntax
```
typedef struct _STORPORT_TELEMETRY_EVENT {
  ULONG     DriverVersion;
  ULONG     EventId;
  UCHAR     EventName[EVENT_NAME_MAX_LENGTH];
  ULONG     EventVersion;
  ULONG     Flags;
  ULONG     EventBufferLength;
  PUCHAR    EventBuffer;
  UCHAR     ParameterName0[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG ParameterValue0;
  UCHAR     ParameterName1[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG ParameterValue1;
  UCHAR     ParameterName2[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG ParameterValue2;
  UCHAR     ParameterName3[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG ParameterValue3;
  UCHAR     ParameterName4[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG ParameterValue4;
  UCHAR     ParameterName5[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG ParameterValue5;
  UCHAR     ParameterName6[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG ParameterValue6;
  UCHAR     ParameterName7[EVENT_MAX_PARAM_NAME_LEN];
  ULONGLONG ParameterValue7;
} STORPORT_TELEMETRY_EVENT, *PSTORPORT_TELEMETRY_EVENT;
```

## Members


`DriverVersion`

Miniport driver version.

`EventId`

A miniport defined identifier for the telemetry event.

`EventName`

A miniport defined name for the telemetry event, which has the maximum length of <b>EVENT_NAME_MAX_LENGTH</b>.

`EventVersion`

A miniport defined version for the telemetry event.

`Flags`

Reserved.

`EventBufferLength`

The length of <b>EventBuffer</b>, which should be not larger than <b>EVENT_BUFFER_MAX_LENGTH</b> that is 4KB.

`EventBuffer`

A miniport defined telemetry payload, the length of which is <b>EventBufferLength</b>.

`ParameterName0`

A description of the of the meaning of ParameterValue0. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.

`ParameterValue0`

The value for parameter 0.

`ParameterName1`

A description of the of the meaning of ParameterValue1. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.

`ParameterValue1`

The value for parameter 1.

`ParameterName2`

A description of the of the meaning of ParameterValue2. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.

`ParameterValue2`

The value for parameter 2.

`ParameterName3`

A description of the of the meaning of ParameterValue3. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.

`ParameterValue3`

The value for parameter 3.

`ParameterName4`

A description of the of the meaning of ParameterValue4. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.

`ParameterValue4`

The value for parameter 4.

`ParameterName5`

A description of the of the meaning of ParameterValue5. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.

`ParameterValue5`

The value for parameter 5.

`ParameterName6`

A description of the of the meaning of ParameterValue6. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.

`ParameterValue6`

The value for parameter 6.

`ParameterName7`

A description of the of the meaning of ParameterValue7. This parameter name string must be &lt;= EVENT_MAX_PARAM_NAME_LEN.

`ParameterValue7`

The value for parameter 7.

## Remarks
A <b>STORPORT_TELEMETRY_EVENT</b> structure describes the miniport telemetry data payload. The miniport should fill it when calling StorPortLogTelemetry.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1703 Windows 10, version 1703 |
| **Header** | storport.h (include Storport.h) |

## See Also

<a href="https://msdn.microsoft.com/3B32F31C-3850-43D4-9C6E-40D35B8AF4D4">StorPortLogTelemetry</a>