---
UID: NS.ntddmmc._FEATURE_DATA_RANDOM_WRITABLE
title: FEATURE_DATA_RANDOM_WRITABLE
author: windows-driver-content
description: The FEATURE_DATA_RANDOM_WRITABLE structure holds information about the Random Writable feature.
old-location: storage\feature_data_random_writable.htm
ms.assetid: b2637f5e-15b0-44ae-8cd0-98712e735998
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FEATURE_DATA_RANDOM_WRITABLE
req.alt-loc: ntddmmc.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: FEATURE_DATA_RANDOM_WRITABLE, FEATURE_DATA_RANDOM_WRITABLE, *PFEATURE_DATA_RANDOM_WRITABLE
req.iface: 
---

# FEATURE_DATA_RANDOM_WRITABLE structure



## -description
<p>The FEATURE_DATA_RANDOM_WRITABLE structure holds information about the Random Writable feature.</p>


## -syntax

````
typedef struct _FEATURE_DATA_RANDOM_WRITABLE {
  FEATURE_HEADER Header;
  UCHAR          LastLBA[4];
  UCHAR          LogicalBlockSize[4];
  UCHAR          Blocking[2];
  UCHAR          ErrorRecoveryPagePresent  :1;
  UCHAR          Reserved1  :7;
  UCHAR          Reserved2;
} FEATURE_DATA_RANDOM_WRITABLE, *PFEATURE_DATA_RANDOM_WRITABLE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor. </p>
</dd>

### -field <b>LastLBA</b>

<dd>
<p>Contains the logical block address of the last addressable block on the medium. The bytes of this array are arranged in big-endian order. <b>LastLBA</b>[0] contains the most significant byte, and <b>LastLBA</b>[3] contains the least significant byte. </p>
</dd>

### -field <b>LogicalBlockSize</b>

<dd>
<p>Specifies the number of bytes per logical block. The bytes of this array are arranged in big-endian order. <b>LogicalBlockSize</b>[0] contains the most significant byte, and <b>LogicalBlockSize</b>[3] contains the least significant byte. </p>
</dd>

### -field <b>Blocking</b>

<dd>
<p>Indicates the number of logical blocks per device. The bytes of this array are arranged in big-endian order. <b>Blocking</b>[0] contains the most significant byte, and <b>Blocking</b>[1] contains the least significant byte. </p>
</dd>

### -field <b>ErrorRecoveryPagePresent</b>

<dd>
<p>Indicates, when set to zero, that the Read/Write Error Recovery Mode Page might not be present. See the <i>SCSI Multimedia -3 </i>(<i>MMC-3</i>) specification for an explanation of this page. </p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. </p>
</dd>
</dl>

## -remarks
<p>This structure holds data for the feature named "Random Writable" by the <i>MMC-3 </i>specification. Devices that support this feature can write blocks of data to random locations on the disk. These devices do not require that the initiator address disk locations in any particular order. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddmmc.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553850">FEATURE_NUMBER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20FEATURE_DATA_RANDOM_WRITABLE structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
