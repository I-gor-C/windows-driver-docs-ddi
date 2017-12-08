---
UID: NS.STRMINI._STREAM_DATA_INTERSECT_INFO
title: _STREAM_DATA_INTERSECT_INFO
author: windows-driver-content
description: STREAM_DATA_INTERSECT_INFO describes the parameters of a data intersection operation.
old-location: stream\stream_data_intersect_info.htm
old-project: stream
ms.assetid: 92a37945-4b7c-4d10-a071-ae1584590692
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _STREAM_DATA_INTERSECT_INFO, STREAM_DATA_INTERSECT_INFO, *PSTREAM_DATA_INTERSECT_INFO
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
req.alt-api: STREAM_DATA_INTERSECT_INFO
req.alt-loc: strmini.h
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
req.product: Windows 10 or later.
---

# _STREAM_DATA_INTERSECT_INFO structure



## -description
STREAM_DATA_INTERSECT_INFO describes the parameters of a data intersection operation.


## -syntax

````
typedef struct _STREAM_DATA_INTERSECT_INFO {
  ULONG        StreamNumber;
  PKSDATARANGE DataRange;
  PVOID        DataFormatBuffer;
  ULONG        SizeOfDataFormatBuffer;
} STREAM_DATA_INTERSECT_INFO, *PSTREAM_DATA_INTERSECT_INFO;
````


## -struct-fields

### -field StreamNumber

Specifies the stream number. This corresponds to the offset of the stream within the minidriver's array of <a href="stream.hw_stream_information">HW_STREAM_INFORMATION</a> structures. The possible data formats depend on the stream type.

### -field DataRange

Pointer to the data ranges to be examined for a match.

### -field DataFormatBuffer

Pointer to the buffer the minidriver fills in with the matching data format.

### -field SizeOfDataFormatBuffer

Specifies the size in bytes of the <b>DataFormatBuffer</b>.

## -remarks
The class driver passes this data structure when it submits a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568168">SRB_GET_DATA_INTERSECTION</a> request to the minidriver's <a href="stream.strminireceivedevicepacket">StrMiniReceiveDevicePacket</a>.

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
</table>