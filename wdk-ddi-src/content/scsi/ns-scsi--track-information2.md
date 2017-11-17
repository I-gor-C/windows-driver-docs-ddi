---
UID: NS.scsi._TRACK_INFORMATION2
title: TRACK_INFORMATION2
author: windows-driver-content
description: The TRACK_INFORMATION2 structure is used to report track information.
old-location: storage\track_information2.htm
ms.assetid: 2fea2f8a-eb55-409c-80d2-c3f49ab6bfdf
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: scsi.h
req.include-header: Scsi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRACK_INFORMATION2
req.alt-loc: scsi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: TRACK_INFORMATION2, TRACK_INFORMATION2, *PTRACK_INFORMATION2
req.iface: 
req.product: Windows 10 or later.
---

# TRACK_INFORMATION2 structure



## -description
<p>The TRACK_INFORMATION2 structure is used to report track information.</p>


## -syntax

````
typedef struct _TRACK_INFORMATION2 {
  UCHAR Length[2];
  UCHAR TrackNumberLsb;
  UCHAR SessionNumberLsb;
  UCHAR Reserved4;
  UCHAR TrackMode  :4;
  UCHAR Copy  :1;
  UCHAR Damage  :1;
  UCHAR Reserved5  :2;
  UCHAR DataMode  :4;
  UCHAR FixedPacket  :1;
  UCHAR Packet  :1;
  UCHAR Blank  :1;
  UCHAR ReservedTrack  :1;
  UCHAR NWA_V  :1;
  UCHAR LRA_V  :1;
  UCHAR Reserved6  :6;
  UCHAR TrackStartAddress[4];
  UCHAR NextWritableAddress[4];
  UCHAR FreeBlocks[4];
  UCHAR FixedPacketSize[4];
  UCHAR TrackSize[4];
  UCHAR LastRecordedAddress[4];
  UCHAR TrackNumberMsb;
  UCHAR SessionNumberMsb;
  UCHAR Reserved7[2];
} TRACK_INFORMATION2, *PTRACK_INFORMATION2;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>The length, in bytes, of this structure.</p>
</dd>

### -field <b>TrackNumberLsb</b>

<dd>
<p>The least significant byte of the track number.</p>
</dd>

### -field <b>SessionNumberLsb</b>

<dd>
<p>The least significant byte of the session number.</p>
</dd>

### -field <b>Reserved4</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>TrackMode</b>

<dd>
<p>The track mode. See the <i>SCSI-3 Multi-Media </i>specification for an explanation of meaning of this member.</p>
</dd>

### -field <b>Copy</b>

<dd>
<p>The copy bit indicates whether the track is a copy or not. If this bit is 1, the track is a copy. If it is 0, the track is not a copy.</p>
</dd>

### -field <b>Damage</b>

<dd>
<p>The damage bit indicates, together with the NWA_V bit, whether a write to the media is complete or not, and what sort of methods the CD-ROM class driver can use to complete the write. See the <i>SCSI-3 Multi-Media </i>specification for an explanation of how to interpret the values in the <b>Damage</b> and <b>NWA_V</b> members.</p>
</dd>

### -field <b>Reserved5</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>DataMode</b>

<dd>
<p>The data mode. This member can have any of the following values:</p>
<table>
<tr>
<td>
<p><b>Value</b></p>
</td>
<td>
<p><b>Meaning</b></p>
</td>
</tr>
<tr>
<td>
<p>0x1</p>
</td>
<td>
<p>The track uses data mode 1 (ISO/IEC 10149)</p>
</td>
</tr>
<tr>
<td>
<p>0x2</p>
</td>
<td>
<p>The track uses data mode 2 (ISO/IEC 10149 or CD-ROM XA)</p>
</td>
</tr>
<tr>
<td>
<p>0xf</p>
</td>
<td>
<p>There is no track descriptor block, and therefore the data block type of the track is unknown.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>FixedPacket</b>

<dd>
<p>The fixed packet bit indicates, under some circumstances, when set to 1, that write operations to the track must must use fixed packets. For a complete explanation of the meaning of this bit, see the <i>SCSI Multimedia Commands - 3 (MMC-3)</i> specification.</p>
</dd>

### -field <b>Packet</b>

<dd>
<p>The fixed packet bit indicates, under some circumstances, when set to 1, that write operations to the track must must use fixed packets. For a complete explanation of the meaning of this bit, see the <i>SCSI Multimedia Commands - 3 (MMC-3)</i> specification.</p>
</dd>

### -field <b>Blank</b>

<dd>
<p>The blank bit, when set to 1, indicates that the track contains no written data and last recorded address field is invalid. For a complete explanation of the meaning of this bit, see the <i>SCSI Multimedia Commands - 3 (MMC-3)</i> specification.</p>
</dd>

### -field <b>ReservedTrack</b>

<dd>
<p>The reserved track bit, when 1, indicates that the track is reserved.</p>
</dd>

### -field <b>NWA_V</b>

<dd>
<p>A boolean value that indicates, when 1, that the value in <b>NextWritableAddress</b> is valid. If 0, the value in <b>NextWritableAddress</b> is invalid.</p>
</dd>

### -field <b>LRA_V</b>

<dd>
<p>A boolean value that indicates whether the <b>LastRecordedAddress</b> member is valid or not. If <b>LRA_V</b> is 1, the <b>LastRecordedAddress</b> member is valid. If 0, the <b>LastRecordedAddress</b> member is not valid.</p>
</dd>

### -field <b>Reserved6</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>TrackStartAddress</b>

<dd>
<p>The starting address of the specified track.</p>
</dd>

### -field <b>NextWritableAddress</b>

<dd>
<p>The logical block address of the next writable user block in the track specified by the track number (<b>TrackNumberLsb</b> and <b>TrackNumberMsb</b>).</p>
</dd>

### -field <b>FreeBlocks</b>

<dd>
<p>The maximum number of user data blocks that are available for recording in the track.</p>
</dd>

### -field <b>FixedPacketSize</b>

<dd>
<p>The blocking factor. This value The fixed packet size is valid only when the Packet and the FP bits are both set to one.</p>
</dd>

### -field <b>TrackSize</b>

<dd>
<p>Track Size is the number of user data blocks in the track.</p>
</dd>

### -field <b>LastRecordedAddress</b>

<dd></dd>

### -field <b>TrackNumberMsb</b>

<dd>
<p>The most significant byte of the track number.</p>
</dd>

### -field <b>SessionNumberMsb</b>

<dd>
<p>The most significant byte of the session number.</p>
</dd>

### -field <b>Reserved7</b>

<dd>
<p>Reserved7</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Scsi.h (include Scsi.h)</dt>
</dl>
</td>
</tr>
</table>