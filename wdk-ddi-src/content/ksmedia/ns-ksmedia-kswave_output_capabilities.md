---
UID: NS:ksmedia.KSWAVE_OUTPUT_CAPABILITIES
title: KSWAVE_OUTPUT_CAPABILITIES
author: windows-driver-content
description: The KSWAVE_OUTPUT_CAPABILITIES structure is used to describe the output capabilities of a device.
old-location: stream\kswave_output_capabilities.htm
old-project: stream
ms.assetid: 3f7d534d-bfd8-4aca-a14d-97c047fb5aeb
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKSWAVE_OUTPUT_CAPABILITIES, KSWAVE_OUTPUT_CAPABILITIES, KSWAVE_OUTPUT_CAPABILITIES structure [Streaming Media Devices], PKSWAVE_OUTPUT_CAPABILITIES, PKSWAVE_OUTPUT_CAPABILITIES structure pointer [Streaming Media Devices], dvdref_7660f724-15c2-419f-a0d9-c432069547a3.xml, ksmedia/KSWAVE_OUTPUT_CAPABILITIES, ksmedia/PKSWAVE_OUTPUT_CAPABILITIES, stream.kswave_output_capabilities"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
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
-	ksmedia.h
api_name:
-	KSWAVE_OUTPUT_CAPABILITIES
product: Windows
targetos: Windows
req.typenames: KSWAVE_OUTPUT_CAPABILITIES, *PKSWAVE_OUTPUT_CAPABILITIES
---

# KSWAVE_OUTPUT_CAPABILITIES structure
The KSWAVE_OUTPUT_CAPABILITIES structure is used to describe the output capabilities of a device.

## Syntax
````
typedef struct {
  ULONG MaximumChannelsPerConnection;
  ULONG MinimumBitsPerSample;
  ULONG MaximumBitsPerSample;
  ULONG MinimumSampleFrequency;
  ULONG MaximumSampleFrequency;
  ULONG TotalConnections;
  ULONG StaticConnections;
  ULONG StreamingConnections;
  ULONG ActiveConnections;
  ULONG ActiveStaticConnections;
  ULONG ActiveStreamingConnections;
  ULONG Total3DConnections;
  ULONG Static3DConnections;
  ULONG Streaming3DConnections;
  ULONG Active3DConnections;
  ULONG ActiveStatic3DConnections;
  ULONG ActiveStreaming3DConnections;
  ULONG TotalSampleMemory;
  ULONG FreeSampleMemory;
  ULONG LargestFreeContiguousSampleMemory;
} KSWAVE_OUTPUT_CAPABILITIES, *PKSWAVE_OUTPUT_CAPABILITIES;
````

## Members


`MaximumChannelsPerConnection`

Specifies the maximum number of channels per connection.

`MinimumBitsPerSample`

Specifies the minimum bits per sample.

`MaximumBitsPerSample`

Specifies the maximum bits per sample.

`MinimumSampleFrequency`

Specifies the minimum sampling frequency.

`MaximumSampleFrequency`

Specifies the maximum sampling frequency.

`TotalConnections`

Indicates the total number of connections.

`StaticConnections`

Indicates the number of static connections.

`StreamingConnections`

Indicates the number of streaming connections.

`ActiveConnections`

Indicates the number of active connections.

`ActiveStaticConnections`

Indicates the number of active static connections.

`ActiveStreamingConnections`

Indicates the number of active streaming connections.

`Total3DConnections`

Indicates the total number of 3D connections.

`Static3DConnections`

Indicates the number of static 3D connections.

`Streaming3DConnections`

Indicates the number of streaming 3D connections.

`Active3DConnections`

Indicates the number of active 3D connections.

`ActiveStatic3DConnections`

Indicates the number of static 3D connections.

`ActiveStreaming3DConnections`

Indicates the number of streaming 3D connections.

`TotalSampleMemory`

Specifies the total amount of sample memory.

`FreeSampleMemory`

Specifies the available free sample memory.

`LargestFreeContiguousSampleMemory`

Specifies the largest, free contiguous amount of sample memory.

## Remarks
This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566523">KSPROPERTY_WAVE_OUTPUT_CAPABILITIES</a> property.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566523">KSPROPERTY_WAVE_OUTPUT_CAPABILITIES</a>