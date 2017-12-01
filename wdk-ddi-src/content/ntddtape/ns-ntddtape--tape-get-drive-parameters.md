---
UID: NS.ntddtape._TAPE_GET_DRIVE_PARAMETERS
title: TAPE_GET_DRIVE_PARAMETERS
author: windows-driver-content
description: The TAPE_GET_DRIVE_PARAMETERS structure is used in conjunction with the IOCTL_TAPE_GET_DRIVE_PARAMS request to retrieve information about capabilities of the tape drive.
old-location: storage\tape_get_drive_parameters.htm
old-project: storage
ms.assetid: 2b1b196f-f012-4136-983e-8c8192bdbd2f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: TAPE_GET_DRIVE_PARAMETERS, TAPE_GET_DRIVE_PARAMETERS, *PTAPE_GET_DRIVE_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddtape.h
req.include-header: Ntddtape.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TAPE_GET_DRIVE_PARAMETERS
req.alt-loc: ntddtape.h
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

# TAPE_GET_DRIVE_PARAMETERS structure



## -description
<p>The TAPE_GET_DRIVE_PARAMETERS structure is used in conjunction with the <a href="..\ntddtape\ni-ntddtape-ioctl-tape-get-drive-params.md">IOCTL_TAPE_GET_DRIVE_PARAMS</a> request to retrieve information about capabilities of the tape drive.</p>


## -syntax

````
typedef struct _TAPE_GET_DRIVE_PARAMETERS {
  BOOLEAN ECC;
  BOOLEAN Compression;
  BOOLEAN DataPadding;
  BOOLEAN ReportSetmarks;
  ULONG   DefaultBlockSize;
  ULONG   MaximumBlockSize;
  ULONG   MinimumBlockSize;
  ULONG   MaximumPartitionCount;
  ULONG   FeaturesLow;
  ULONG   FeaturesHigh;
  ULONG   EOTWarningZoneSize;
} TAPE_GET_DRIVE_PARAMETERS, *PTAPE_GET_DRIVE_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>ECC</b>

<dd>
<p>When set to <b>TRUE</b>, indicates that the device uses hardware error correction.</p>
</dd>

### -field <b>Compression</b>

<dd>
<p>When set to <b>TRUE</b>, indicates that compression is enabled on a device that supports it. When compression is enabled, the device compresses data prior to writing it. When set to <b>FALSE</b>, compression is not enabled on the device. </p>
</dd>

### -field <b>DataPadding</b>

<dd>
<p>When set to <b>TRUE</b>, indicates that data padding is enabled on a device that supports it. When padding is enabled, the device pads data with zeros to keep the tape streaming until data is ready. When set to <b>FALSE</b>, data padding is not enabled. </p>
</dd>

### -field <b>ReportSetmarks</b>

<dd>
<p>When set to <b>TRUE</b>, indicates that reporting setmarks is enabled on a device that supports it. The device reports setmarks encountered during read or space operations. When set to <b>FALSE</b>, reporting setmarks is not enabled. </p>
</dd>

### -field <b>DefaultBlockSize</b>

<dd>
<p>Indicates the default block size, in bytes. </p>
</dd>

### -field <b>MaximumBlockSize</b>

<dd>
<p>Indicates the maximum block size, in bytes, of either the tape device or the underlying host bus adapter (HBA), whichever is smaller. </p>
</dd>

### -field <b>MinimumBlockSize</b>

<dd>
<p>Indicates the minimum block size, in bytes. </p>
</dd>

### -field <b>MaximumPartitionCount</b>

<dd>
<p>Indicates the maximum number of partitions the device supports. </p>
</dd>

### -field <b>FeaturesLow</b>

<dd>
<p>Indicates the features supported by this drive. The miniport driver sets TAPE_DRIVE_<i>XXX</i> flags for features supported by the drive and clears flags for features not supported. Callers can use the TAPE_DRIVE_<i>XXX</i> masks defined in <i>minitape.h</i> to determine whether a drive supports a particular feature. The masks available are as follows:</p>
<table>
<tr>
<th>Mask</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_CLEAN_REQUESTS</p>
</td>
<td>
<p>The device can report whether it requires cleaning.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_COMPRESSION</p>
</td>
<td>
<p>The device supports hardware data compression.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_ECC</p>
</td>
<td>
<p>The device supports hardware error correction.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_EJECT_MEDIA</p>
</td>
<td>
<p>The device ejects the media. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_EOT_WZ_SIZE</p>
</td>
<td>
<p>The device can report the end of zone warning size. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_ERASE_BOP_ONLY</p>
</td>
<td>
<p>The device performs the erase operation from the beginning-of-partition marker only.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_ERASE_IMMEDIATE</p>
</td>
<td>
<p>The device performs an immediate erase operation ??  that is, it returns when the erase operation begins.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_ERASE_LONG</p>
</td>
<td>
<p>The device performs a long erase operation.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_ERASE_SHORT</p>
</td>
<td>
<p>The device performs a short erase operation.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_FIXED</p>
</td>
<td>
<p>The device creates fixed data partitions.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_FIXED_BLOCK</p>
</td>
<td>
<p>The device supports fixed-length block mode.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_INITIATOR</p>
</td>
<td>
<p>The device creates initiator-defined partitions.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_GET_ABSOLUTE_BLK</p>
</td>
<td>
<p>The device provides the current device-specific block address.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_GET_LOGICAL_BLK</p>
</td>
<td>
<p>The device provides the current logical block address (and logical tape partition).</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_PADDING</p>
</td>
<td>
<p>The device supports data padding.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_REPORT_SMKS</p>
</td>
<td>
<p>The device supports setmark reporting.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_RESERVED_BIT</p>
</td>
<td>
<p>A mask that identifies a reserved bit. Drivers must not set this bit. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SELECT</p>
</td>
<td>
<p>The device creates select data partitions.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SET_CMP_BOP_ONLY</p>
</td>
<td>
<p>The device only allows compression to be enabled when the read/write head is at the beginning of the partition.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SET_EOT_WZ_SIZE</p>
</td>
<td>
<p>The device supports setting the end-of-medium warning size.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_TAPE_CAPACITY</p>
</td>
<td>
<p>The device returns the maximum capacity of the tape.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_TAPE_REMAINING</p>
</td>
<td>
<p>The device returns the remaining capacity of the tape.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_VARIABLE_BLOCK</p>
</td>
<td>
<p>The device supports variable-length block mode.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_WRITE_PROTECT</p>
</td>
<td>
<p>The device returns an error if the tape is write-enabled or write-protected.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>FeaturesHigh</b>

<dd>
<p>Indicates the additional features supported by this drive if TAPE_DRIVE_HIGH_FEATURES is set in <b>FeaturesLow</b>. The miniport driver sets TAPE_DRIVE_<i>XXX</i> flags for features supported by the drive and clears flags for features not supported. Callers can use the TAPE_DRIVE_<i>XXX</i> masks defined in <i>minitape.h </i>to determine whether a drive supports a particular feature. </p>
<table>
<tr>
<th>Mask</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_ABS_BLK_IMMED</p>
</td>
<td>
<p>The device moves the tape to a device-specific block address and returns as soon as the move begins.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_ABSOLUTE_BLK</p>
</td>
<td>
<p>The device moves the tape to a device specific block address.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_END_OF_DATA</p>
</td>
<td>
<p>The device moves the tape to the end-of-data marker in a partition.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_FILEMARKS</p>
</td>
<td>
<p>The device moves the tape forward (or backward) a specified number of filemarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_FORMAT</p>
</td>
<td>
<p>The device can format the media. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_FORMAT_IMMEDIATE</p>
</td>
<td>
<p>The device can format the media as an immediate command.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_HIGH_FEATURES</p>
</td>
<td>
<p>A bitmask that indicates those bits which correspond to high features. </p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_LOAD_UNLOAD</p>
</td>
<td>
<p>The device enables and disables the device for further operations.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_LOAD_UNLD_IMMED</p>
</td>
<td>
<p>The device supports immediate load and unload operations.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_LOCK_UNLOCK</p>
</td>
<td>
<p>The device enables and disables the tape ejection mechanism.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_LOCK_UNLK_IMMED</p>
</td>
<td>
<p>The device supports immediate lock and unlock operations.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_LOG_BLK_IMMED</p>
</td>
<td>
<p>The device moves the tape to a logical block address in a partition and returns as soon as the move begins.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_LOGICAL_BLK</p>
</td>
<td>
<p>The device moves the tape to a logical block address in a partition.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_RELATIVE_BLKS</p>
</td>
<td>
<p>The device moves the tape forward (or backward) a specified number of blocks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_REVERSE_POSITION</p>
</td>
<td>
<p>The device moves the tape backward over blocks, filemarks, or setmarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_REWIND_IMMEDIATE</p>
</td>
<td>
<p>The device supports immediate rewind operation.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SEQUENTIAL_FMKS</p>
</td>
<td>
<p>The device moves the tape forward (or backward) to the first occurrence of a specified number of consecutive filemarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SEQUENTIAL_SMKS</p>
</td>
<td>
<p>The device moves the tape forward (or backward) to the first occurrence of a specified number of consecutive setmarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SET_BLOCK_SIZE</p>
</td>
<td>
<p>The device supports setting the size of a fixed-length logical block or setting the variable-length block mode.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SET_COMPRESSION</p>
</td>
<td>
<p>The device enables and disables hardware data compression.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SET_ECC</p>
</td>
<td>
<p>The device enables and disables hardware error correction.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SET_PADDING</p>
</td>
<td>
<p>The device enables and disables data padding.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SET_REPORT_SMKS</p>
</td>
<td>
<p>The device enables and disables the reporting of setmarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SETMARKS</p>
</td>
<td>
<p>The device moves the tape forward (or reverse) a specified number of setmarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_SPACE_IMMEDIATE</p>
</td>
<td>
<p>The device supports immediate spacing.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_TENSION</p>
</td>
<td>
<p>The device supports tape tensioning.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_TENSION_IMMED</p>
</td>
<td>
<p>The device supports immediate tape tensioning.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_WRITE_FILEMARKS</p>
</td>
<td>
<p>The device writes filemarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_WRITE_LONG_FMKS</p>
</td>
<td>
<p>The device writes long filemarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_WRITE_MARK_IMMED</p>
</td>
<td>
<p>The device supports immediate writing of short and long filemarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_WRITE_SETMARKS</p>
</td>
<td>
<p>The device writes setmarks.</p>
</td>
</tr>
<tr>
<td>
<p>TAPE_DRIVE_WRITE_SHORT_FMKS</p>
</td>
<td>
<p>The device writes short filemarks.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>EOTWarningZoneSize</b>

<dd>
<p>Indicates the size in bytes of the early warning zone toward the end of the tape. The device returns a check condition when it enters the zone. </p>
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
<dt>Ntddtape.h (include Ntddtape.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddtape\ni-ntddtape-ioctl-tape-get-drive-params.md">IOCTL_TAPE_GET_DRIVE_PARAMS</a>
</dt>
<dt>
<a href="storage.tapeminigetdriveparameters">TapeMiniGetDriveParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TAPE_GET_DRIVE_PARAMETERS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
