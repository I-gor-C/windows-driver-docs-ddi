---
UID: NS:strmini._HW_STREAM_INFORMATION
title: "_HW_STREAM_INFORMATION"
author: windows-driver-content
description: The HW_STREAM_INFORMATION structure describes the kernel streaming semantics supported by individual streams, as part of an HW_STREAM_DESCRIPTOR structure.
old-location: stream\hw_stream_information.htm
old-project: stream
ms.assetid: d1163185-4cae-4f14-ae99-78795da89fb8
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PHW_STREAM_INFORMATION, HW_STREAM_INFORMATION, HW_STREAM_INFORMATION structure [Streaming Media Devices], PHW_STREAM_INFORMATION, PHW_STREAM_INFORMATION structure pointer [Streaming Media Devices], _HW_STREAM_INFORMATION, strclass-struct_df196092-33e4-4b19-b45c-0986b262f2e9.xml, stream.hw_stream_information, strmini/HW_STREAM_INFORMATION, strmini/PHW_STREAM_INFORMATION"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: strmini.h
req.include-header: Strmini.h
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
-	strmini.h
api_name:
-	HW_STREAM_INFORMATION
product: Windows
targetos: Windows
req.typenames: HW_STREAM_INFORMATION, *PHW_STREAM_INFORMATION
req.product: Windows 10 or later.
---

# _HW_STREAM_INFORMATION structure
The HW_STREAM_INFORMATION structure describes the kernel streaming semantics supported by individual streams, as part of an <a href="..\strmini\ns-strmini-_hw_stream_descriptor.md">HW_STREAM_DESCRIPTOR</a> structure.

## Syntax
````
typedef struct _HW_STREAM_INFORMATION {
  ULONG              NumberOfPossibleInstances;
  KSPIN_DATAFLOW     DataFlow;
  BOOLEAN            DataAccessible;
  ULONG              NumberOfFormatArrayEntries;
  PKSDATAFORMAT      *StreamFormatsArray;
  PVOID              ClassReserved[4];
  ULONG              NumStreamPropArrayEntries;
  PKSPROPERTY_SET    StreamPropertiesArray;
  ULONG              NumStreamEventArrayEntries;
  PKSEVENT_SET       StreamEventsArray;
  GUID               *Category;
  GUID               *Name;
  ULONG              MediumsCount;
  const KSPIN_MEDIUM *Mediums;
  BOOLEAN            BridgeStream;
  ULONG              Reserved[2];
} HW_STREAM_INFORMATION, *PHW_STREAM_INFORMATION;
````

## Members


`NumberOfPossibleInstances`

Specifies the number of possible instances of this stream that can be opened.

`DataFlow`

The direction that data can travel on this stream. For unidirectional data flow, <b>DataFlow</b> has the value <b>KSPIN_DATAFLOW_IN</b> or KSPIN_DATAFLOW_OUT.

`DataAccessible`

Specifies <b>TRUE</b> if the stream data is accessible to the class driver.

`NumberOfFormatArrayEntries`

The number of entries in the array that begins at the address in the <b>StreamFormatsArray</b> member.

`StreamFormatsArray`

Pointer to the beginning of the array of data ranges that this stream supports. (The name of this member is deceptive. This member points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structures, not KSDATAFORMAT structures.)

`ClassReserved`

Reserved for use by the class driver. Do not use.

`NumStreamPropArrayEntries`

The number of entries in the array that begins at the address in the <b>StreamPropertiesArray</b> member.

`StreamPropertiesArray`

Pointer to the beginning of the array of property sets supported by this stream.

`NumStreamEventArrayEntries`

The number of entries in the array that begins at the address in the <b>StreamEventsArray</b> field.

`StreamEventsArray`

Pointer to the beginning of the array of event sets supported by this stream.

`Category`

Specifies the GUID of the pin category.

`Name`

Specifies the GUID of the localized Unicode string name for the pin type, stored in the Registry.

`MediumsCount`

The number of entries in the array that begins at the address in the <b>Mediums</b> field.

`Mediums`

Pointer to the beginning of the array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a> structures supported by this stream. If the minidriver does not specify a medium, the class driver uses the KSMEDIUMSETID_STANDARD, KSMEDIUM_TYPE_ANYINSTANCE medium as the default.

`BridgeStream`

If <b>TRUE</b>, the communications type of this stream's underlying pin type is KSPIN_COMMUNICATION_BRIDGE. Otherwise, the default communications type of a stream is KSPIN_COMMUNICATION_SINK.

Most minidrivers will set this member to <b>FALSE</b>. See KSPROPERTY_PIN_COMMUNICATIONS for a description of communication types.

`Reserved`

Reserved for use by the class driver. Do not use.

## Remarks
The class driver uses the elements of HW_STREAM_INFORMATION to handle the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566584">KSPROPSETID_Pin</a> property requests. The index within the <a href="..\strmini\ns-strmini-_hw_stream_descriptor.md">HW_STREAM_DESCRIPTOR</a> structure serves as the pin type ID number.

Note that the class driver does not use this data to handle the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565198">KSPROPERTY_PIN_DATAINTERSECTION</a> property. See <a href="..\strmini\ns-strmini-_stream_data_intersect_info.md">STREAM_DATA_INTERSECT_INFO</a> for a description of how the class driver handles this property.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | strmini.h (include Strmini.h) |

## See Also

<a href="..\strmini\ns-strmini-_hw_stream_header.md">HW_STREAM_HEADER</a>



<a href="..\strmini\ns-strmini-_hw_stream_descriptor.md">HW_STREAM_DESCRIPTOR</a>