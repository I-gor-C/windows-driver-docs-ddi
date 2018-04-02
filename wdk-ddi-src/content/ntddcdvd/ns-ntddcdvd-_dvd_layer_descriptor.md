---
UID: NS:ntddcdvd._DVD_LAYER_DESCRIPTOR
title: "_DVD_LAYER_DESCRIPTOR"
author: windows-driver-content
description: The DVD_LAYER_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD layer descriptor.
old-location: storage\dvd_layer_descriptor.htm
old-project: storage
ms.assetid: dd981cc1-ab82-49de-8cf1-ba2b7451c7ef
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDVD_LAYER_DESCRIPTOR, DVD_LAYER_DESCRIPTOR, DVD_LAYER_DESCRIPTOR structure [Storage Devices], PDVD_LAYER_DESCRIPTOR, PDVD_LAYER_DESCRIPTOR structure pointer [Storage Devices], _DVD_LAYER_DESCRIPTOR, ntddcdvd/DVD_LAYER_DESCRIPTOR, ntddcdvd/PDVD_LAYER_DESCRIPTOR, storage.dvd_layer_descriptor, structs-DVD_94f08da1-fe98-47cd-989a-b3f574874d6b.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
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
-	ntddcdvd.h
api_name:
-	DVD_LAYER_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: DVD_LAYER_DESCRIPTOR, *PDVD_LAYER_DESCRIPTOR
---

# _DVD_LAYER_DESCRIPTOR structure
The DVD_LAYER_DESCRIPTOR structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560426">IOCTL_DVD_READ_STRUCTURE</a> request to retrieve a DVD layer descriptor.

## Syntax
```
typedef struct _DVD_LAYER_DESCRIPTOR {
  UCHAR  : 4 BookVersion;
  UCHAR  : 4 BookType;
  UCHAR  : 4 MinimumRate;
  UCHAR  : 4 DiskSize;
  UCHAR  : 4 LayerType;
  UCHAR  : 1 TrackPath;
  UCHAR  : 2 NumberOfLayers;
  UCHAR  : 1 Reserved1;
  UCHAR  : 4 TrackDensity;
  UCHAR  : 4 LinearDensity;
  ULONG      StartingDataSector;
  ULONG      EndDataSector;
  ULONG      EndLayerZeroSector;
  UCHAR  : 7 Reserved5;
  UCHAR  : 1 BCAFlag;
} *PDVD_LAYER_DESCRIPTOR, DVD_LAYER_DESCRIPTOR;
```

## Members


`BookVersion`

Specifies the version of the specified book that this media complies with.

`BookType`

Specifies the DVD book this media complies with. This member can have one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
0

</td>
<td>
DVD-ROM

</td>
</tr>
<tr>
<td>
1

</td>
<td>
DVD-RAM

</td>
</tr>
<tr>
<td>
2

</td>
<td>
DVD-R

</td>
</tr>
<tr>
<td>
3

</td>
<td>
DVD-RW

</td>
</tr>
<tr>
<td>
9

</td>
<td>
DVD+RW

</td>
</tr>
</table>

`MinimumRate`

Specifies the read rate to use for the media. This member can have one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
0

</td>
<td>
DVD-ROM

</td>
</tr>
<tr>
<td>
1

</td>
<td>
DVD-RAM

</td>
</tr>
<tr>
<td>
2

</td>
<td>
DVD-R

</td>
</tr>
<tr>
<td>
3

</td>
<td>
DVD-RW

</td>
</tr>
<tr>
<td>
9

</td>
<td>
DVD+RW

</td>
</tr>
</table>

`DiskSize`

Specifies the physical size of the media. A value of zero indicates 120 mm. A value of 1 indicates a size of 80 mm.

`LayerType`

Indicates the type of layer. This member can have one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
1

</td>
<td>
Read-only layer

</td>
</tr>
<tr>
<td>
2

</td>
<td>
Recordable layer

</td>
</tr>
<tr>
<td>
4

</td>
<td>
Rewritable layer

</td>
</tr>
</table>

`TrackPath`

Specifies the direction of the layers when more than one layer is used. If the <b>TrackPath</b> member is zero, this media uses a parallel track path (PTP). With PTP, each layer is independent and has its own lead-in and lead-out areas. If <b>TrackPath</b> is 1, the media uses opposite track path (OTP). With opposite track path, the two layers are united, and there is only one lead-in and lead-out area. For further details, see the <i>SCSI Multimedia Commands - 3 (MMC-3) </i>specification.

`NumberOfLayers`

Specifies the number of layers present on the side of the media being read. A value of zero indicates that the media has one layer. A value of 1 indicates that the media has two layers.

`Reserved1`

Reserved.

`TrackDensity`

Indicates the track width used for this media in units of micrometers per track. This member can have one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
0

</td>
<td>
0.74 m/track

</td>
</tr>
<tr>
<td>
1

</td>
<td>
0.80 m/track

</td>
</tr>
<tr>
<td>
2

</td>
<td>
0.615 m/track

</td>
</tr>
</table>

`LinearDensity`

Indicates the minimum/maximum pit length used for this layer in units of micrometers per bit. This member can have one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
0

</td>
<td>
0.267 m/bit

</td>
</tr>
<tr>
<td>
1

</td>
<td>
0.293 m/bit

</td>
</tr>
<tr>
<td>
2

</td>
<td>
0.409 to 0.435 m/bit

</td>
</tr>
<tr>
<td>
4

</td>
<td>
0.280 to 0.291 m/bit

</td>
</tr>
<tr>
<td>
8

</td>
<td>
0.353 m/bit

</td>
</tr>
</table>

`StartingDataSector`

Specifies the first block that contains user data. This member can have one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
0x30000

</td>
<td>
An initial block value of 0x30000 indicates that the media type is DVD-ROM or DVD-R/-RW

</td>
</tr>
<tr>
<td>
0x31000

</td>
<td>
An initial block value of 0x30000 indicates that the media type is DVD-RAM or DVD+RW

</td>
</tr>
</table>

`EndDataSector`

Specifies the last sector of the user data in the last layer of the media.

`EndLayerZeroSector`

Specifies the last sector of the user data in layer zero. If this media does not use the opposite track path method and contains multiple layers, this value is set to zero.

`Reserved5`

Reserved.

`BCAFlag`

Indicates, if set to 1, the presence of data in the burst cutting area (BCA). If set to zero, it indicates that there is no BCA data.

## Remarks
For more information, see the <i>SCSI Multimedia Commands - 3 (MMC-3) </i>specification.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdvd.h (include Ntddcdvd.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560426">IOCTL_DVD_READ_STRUCTURE</a>