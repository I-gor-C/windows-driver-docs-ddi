---
UID: NS.ntddcdvd._DVD_LAYER_DESCRIPTOR
title: DVD_LAYER_DESCRIPTOR
author: windows-driver-content
description: The DVD_LAYER_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD layer descriptor.
old-location: storage\dvd_layer_descriptor.htm
old-project: storage
ms.assetid: dd981cc1-ab82-49de-8cf1-ba2b7451c7ef
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DVD_LAYER_DESCRIPTOR, DVD_LAYER_DESCRIPTOR, *PDVD_LAYER_DESCRIPTOR
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
req.alt-api: DVD_LAYER_DESCRIPTOR
req.alt-loc: ntddcdvd.h
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
---

# DVD_LAYER_DESCRIPTOR structure



## -description
<p>The DVD_LAYER_DESCRIPTOR structure is used in conjunction with the <a href="..\ntddcdvd\ni-ntddcdvd-ioctl-dvd-read-structure.md">IOCTL_DVD_READ_STRUCTURE</a> request to retrieve a DVD layer descriptor. </p>


## -syntax

````
typedef struct _DVD_LAYER_DESCRIPTOR {
  UCHAR BookVersion  :4;
  UCHAR BookType  :4;
  UCHAR MinimumRate  :4;
  UCHAR DiskSize  :4;
  UCHAR LayerType  :4;
  UCHAR TrackPath  :1;
  UCHAR NumberOfLayers  :2;
  UCHAR Reserved1  :1;
  UCHAR TrackDensity  :4;
  UCHAR LinearDensity  :4;
  ULONG StartingDataSector;
  ULONG EndDataSector;
  ULONG EndLayerZeroSector;
  UCHAR Reserved5  :7;
  UCHAR BCAFlag  :1;
} DVD_LAYER_DESCRIPTOR, *PDVD_LAYER_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>BookVersion</b>

<dd>
<p>Specifies the version of the specified book that this media complies with.</p>
</dd>

### -field <b>BookType</b>

<dd>
<p>Specifies the DVD book this media complies with. This member can have one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>DVD-ROM</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>DVD-RAM</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>DVD-R</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>DVD-RW</p>
</td>
</tr>
<tr>
<td>
<p>9</p>
</td>
<td>
<p>DVD+RW</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MinimumRate</b>

<dd>
<p>Specifies the read rate to use for the media. This member can have one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>DVD-ROM</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>DVD-RAM</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>DVD-R</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>DVD-RW</p>
</td>
</tr>
<tr>
<td>
<p>9</p>
</td>
<td>
<p>DVD+RW</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DiskSize</b>

<dd>
<p>Specifies the physical size of the media. A value of zero indicates 120 mm. A value of 1 indicates a size of 80 mm.</p>
</dd>

### -field <b>LayerType</b>

<dd>
<p>Indicates the type of layer. This member can have one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Read-only layer</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Recordable layer</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>Rewritable layer</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>TrackPath</b>

<dd>
<p>Specifies the direction of the layers when more than one layer is used. If the <b>TrackPath</b> member is zero, this media uses a parallel track path (PTP). With PTP, each layer is independent and has its own lead-in and lead-out areas. If <b>TrackPath</b> is 1, the media uses opposite track path (OTP). With opposite track path, the two layers are united, and there is only one lead-in and lead-out area. For further details, see the <i>SCSI Multimedia Commands - 3 (MMC-3) </i>specification. </p>
</dd>

### -field <b>NumberOfLayers</b>

<dd>
<p>Specifies the number of layers present on the side of the media being read. A value of zero indicates that the media has one layer. A value of 1 indicates that the media has two layers. </p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>TrackDensity</b>

<dd>
<p>Indicates the track width used for this media in units of micrometers per track. This member can have one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>0.74 m/track</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>0.80 m/track</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>0.615 m/track</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>LinearDensity</b>

<dd>
<p>Indicates the minimum/maximum pit length used for this layer in units of micrometers per bit. This member can have one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>0.267 m/bit</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>0.293 m/bit</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>0.409 to 0.435 m/bit</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>0.280 to 0.291 m/bit</p>
</td>
</tr>
<tr>
<td>
<p>8</p>
</td>
<td>
<p>0.353 m/bit</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>StartingDataSector</b>

<dd>
<p>Specifies the first block that contains user data. This member can have one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0x30000</p>
</td>
<td>
<p>An initial block value of 0x30000 indicates that the media type is DVD-ROM or DVD-R/-RW</p>
</td>
</tr>
<tr>
<td>
<p>0x31000</p>
</td>
<td>
<p>An initial block value of 0x30000 indicates that the media type is DVD-RAM or DVD+RW</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>EndDataSector</b>

<dd>
<p>Specifies the last sector of the user data in the last layer of the media. </p>
</dd>

### -field <b>EndLayerZeroSector</b>

<dd>
<p>Specifies the last sector of the user data in layer zero. If this media does not use the opposite track path method and contains multiple layers, this value is set to zero.</p>
</dd>

### -field <b>Reserved5</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>BCAFlag</b>

<dd>
<p>Indicates, if set to 1, the presence of data in the burst cutting area (BCA). If set to zero, it indicates that there is no BCA data.</p>
</dd>
</dl>

## -remarks
<p>For more information, see the <i>SCSI Multimedia Commands - 3 (MMC-3) </i>specification. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddcdvd.h (include Ntddcdvd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddcdvd\ni-ntddcdvd-ioctl-dvd-read-structure.md">IOCTL_DVD_READ_STRUCTURE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DVD_LAYER_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
