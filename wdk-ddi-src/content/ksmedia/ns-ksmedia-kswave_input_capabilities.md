---
UID: NS:ksmedia.KSWAVE_INPUT_CAPABILITIES
title: KSWAVE_INPUT_CAPABILITIES
author: windows-driver-content
description: The KSWAVE_INPUT_CAPABILITIES structure is used to describe the input capabilities of a device.
old-location: stream\kswave_input_capabilities.htm
old-project: stream
ms.assetid: 8bed3cec-1779-4b3c-9ba2-aa4a335fecd1
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKSWAVE_INPUT_CAPABILITIES, KSWAVE_INPUT_CAPABILITIES, KSWAVE_INPUT_CAPABILITIES structure [Streaming Media Devices], PKSWAVE_INPUT_CAPABILITIES, PKSWAVE_INPUT_CAPABILITIES structure pointer [Streaming Media Devices], dvdref_cc35df03-82e2-4b12-a08f-26aa0fde1279.xml, ksmedia/KSWAVE_INPUT_CAPABILITIES, ksmedia/PKSWAVE_INPUT_CAPABILITIES, stream.kswave_input_capabilities"
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
-	KSWAVE_INPUT_CAPABILITIES
product: Windows
targetos: Windows
req.typenames: KSWAVE_INPUT_CAPABILITIES, *PKSWAVE_INPUT_CAPABILITIES
---

# KSWAVE_INPUT_CAPABILITIES structure
The KSWAVE_INPUT_CAPABILITIES structure is used to describe the input capabilities of a device.

## Syntax
````
typedef struct {
  ULONG MaximumChannelsPerConnection;
  ULONG MinimumBitsPerSample;
  ULONG MaximumBitsPerSample;
  ULONG MinimumSampleFrequency;
  ULONG MaximumSampleFrequency;
  ULONG TotalConnections;
  ULONG ActiveConnections;
} KSWAVE_INPUT_CAPABILITIES, *PKSWAVE_INPUT_CAPABILITIES;
````

## Members


`MaximumChannelsPerConnection`

Specifies the maximum channels per connection.

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

`ActiveConnections`

Indicates the number of active connections.

## Remarks
This structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566521">KSPROPERTY_WAVE_INPUT_CAPABILITIES</a> property.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566521">KSPROPERTY_WAVE_INPUT_CAPABILITIES</a>