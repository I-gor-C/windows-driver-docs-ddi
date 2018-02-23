---
UID: NS:ksmedia.KSWAVE_OUTPUT_CAPABILITIES
title: KSWAVE_OUTPUT_CAPABILITIES
author: windows-driver-content
description: The KSWAVE_OUTPUT_CAPABILITIES structure is used to describe the output capabilities of a device.
old-location: stream\kswave_output_capabilities.htm
old-project: stream
ms.assetid: 3f7d534d-bfd8-4aca-a14d-97c047fb5aeb
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: dvdref_7660f724-15c2-419f-a0d9-c432069547a3.xml, ksmedia/PKSWAVE_OUTPUT_CAPABILITIES, *PKSWAVE_OUTPUT_CAPABILITIES, KSWAVE_OUTPUT_CAPABILITIES structure [Streaming Media Devices], PKSWAVE_OUTPUT_CAPABILITIES structure pointer [Streaming Media Devices], stream.kswave_output_capabilities, PKSWAVE_OUTPUT_CAPABILITIES, KSWAVE_OUTPUT_CAPABILITIES, ksmedia/KSWAVE_OUTPUT_CAPABILITIES
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ksmedia.h
apiname:
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


`Active3DConnections`

Indicates the number of active 3D connections.

`ActiveConnections`

Indicates the number of active connections.

`ActiveStatic3DConnections`

Indicates the number of static 3D connections.

`ActiveStaticConnections`

Indicates the number of active static connections.

`ActiveStreaming3DConnections`

Indicates the number of streaming 3D connections.

`ActiveStreamingConnections`

Indicates the number of active streaming connections.

`FreeSampleMemory`

Specifies the available free sample memory.

`LargestFreeContiguousSampleMemory`

Specifies the largest, free contiguous amount of sample memory.

`MaximumBitsPerSample`

Specifies the maximum bits per sample.

`MaximumChannelsPerConnection`

Specifies the maximum number of channels per connection.

`MaximumSampleFrequency`

Specifies the maximum sampling frequency.

`MinimumBitsPerSample`

Specifies the minimum bits per sample.

`MinimumSampleFrequency`

Specifies the minimum sampling frequency.

`Static3DConnections`

Indicates the number of static 3D connections.

`StaticConnections`

Indicates the number of static connections.

`Streaming3DConnections`

Indicates the number of streaming 3D connections.

`StreamingConnections`

Indicates the number of streaming connections.

`Total3DConnections`

Indicates the total number of 3D connections.

`TotalConnections`

Indicates the total number of connections.

`TotalSampleMemory`

Specifies the total amount of sample memory.

## Remarks
This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566523">KSPROPERTY_WAVE_OUTPUT_CAPABILITIES</a> property.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566523">KSPROPERTY_WAVE_OUTPUT_CAPABILITIES</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSWAVE_OUTPUT_CAPABILITIES structure%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>