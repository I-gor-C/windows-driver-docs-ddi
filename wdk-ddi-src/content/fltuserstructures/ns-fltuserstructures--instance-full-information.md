---
UID: NS.fltuserstructures._INSTANCE_FULL_INFORMATION
title: INSTANCE_FULL_INFORMATION
author: windows-driver-content
description: The INSTANCE_FULL_INFORMATION structure contains full information for a minifilter instance.
old-location: ifsk\instance_full_information.htm
old-project: ifsk
ms.assetid: 6c034749-c110-4623-8a7b-a19235cad298
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: INSTANCE_FULL_INFORMATION, INSTANCE_FULL_INFORMATION, *PINSTANCE_FULL_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltuserstructures.h
req.include-header: FltUserStructures.h, FltUser.h, FltKernel.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Microsoft Windows 2000 SP4 with Update Rollup, Windows XP SP2,  Microsoft Windows Server 2003 SP1, and Windows Vista or later versions of Windows operating systems,
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: INSTANCE_FULL_INFORMATION
req.alt-loc: fltuserstructures.h
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
req.iface: 
---

# INSTANCE_FULL_INFORMATION structure



## -description
<p>The INSTANCE_FULL_INFORMATION structure contains full information for a minifilter instance. </p>


## -syntax

````
typedef struct _INSTANCE_FULL_INFORMATION {
  ULONG  NextEntryOffset;
  USHORT InstanceNameLength;
  USHORT InstanceNameBufferOffset;
  USHORT AltitudeLength;
  USHORT AltitudeBufferOffset;
  USHORT VolumeNameLength;
  USHORT VolumeNameBufferOffset;
  USHORT FilterNameLength;
  USHORT FilterNameBufferOffset;
} INSTANCE_FULL_INFORMATION, *PINSTANCE_FULL_INFORMATION;
````


## -struct-fields
<dl>

### -field NextEntryOffset

<dd>
<p>A byte offset of the next INSTANCE_FULL_INFORMATION entry. If multiple entries are present in a buffer, the last entry contains a zero.  </p>
</dd>

### -field InstanceNameLength

<dd>
<p>The length, in bytes, of the instance name. </p>
</dd>

### -field InstanceNameBufferOffset

<dd>
<p>A byte offset of the first character of the instance name string. This character is followed in memory by the remainder of the string. </p>
</dd>

### -field AltitudeLength

<dd>
<p>The length, in bytes, of the altitude string. </p>
</dd>

### -field AltitudeBufferOffset

<dd>
<p>A byte offset of the first character of the altitude string. This character is followed in memory by the remainder of the string. </p>
</dd>

### -field VolumeNameLength

<dd>
<p>The length, in bytes, of the volume name. </p>
</dd>

### -field VolumeNameBufferOffset

<dd>
<p>A byte offset of the first character of the volume name string. This character is followed in memory by the remainder of the string (for example, "\Device\HarddiskVolume1"). </p>
</dd>

### -field FilterNameLength

<dd>
<p>The length, in bytes, of the minifilter name. </p>
</dd>

### -field FilterNameBufferOffset

<dd>
<p>A byte offset of the first character of the minifilter name string. This character is followed in memory by the remainder of the string. </p>
</dd>
</dl>

## -remarks
<p>This structure must be aligned on a LONGLONG (8-byte) boundary. If a buffer contains two or more of these structures, the <b>NextEntryOffset</b> value in each entry, except the last, falls on an 8-byte boundary.</p>

<p>The content of all character string buffers referenced by this structure are Unicode.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting with Microsoft Windows 2000 SP4 with Update Rollup, Windows XP SP2,  Microsoft Windows Server 2003 SP1, and Windows Vista or later versions of Windows operating systems,</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltuserstructures.h (include FltUserStructures.h, FltUser.h, or FltKernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.filterattachataltitude">FilterAttachAtAltitude</a>
</dt>
<dt>
<a href="ifsk.filterinstancefindclose">FilterInstanceFindClose</a>
</dt>
<dt>
<a href="ifsk.filterinstancefindfirst">FilterInstanceFindFirst</a>
</dt>
<dt>
<a href="ifsk.filterinstancefindnext">FilterInstanceFindNext</a>
</dt>
<dt>
<a href="ifsk.filterinstancegetinformation">FilterInstanceGetInformation</a>
</dt>
<dt>
<a href="ifsk.filtervolumeinstancefindclose">FilterVolumeInstanceFindClose</a>
</dt>
<dt>
<a href="ifsk.filtervolumeinstancefindfirst">FilterVolumeInstanceFindFirst</a>
</dt>
<dt>
<a href="ifsk.filtervolumeinstancefindnext">FilterVolumeInstanceFindNext</a>
</dt>
<dt>
<a href="..\fltuserstructures\ns-fltuserstructures--instance-aggregate-standard-information.md">INSTANCE_AGGREGATE_STANDARD_INFORMATION</a>
</dt>
<dt>
<a href="..\fltuserstructures\ns-fltuserstructures--instance-basic-information.md">INSTANCE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="..\fltuserstructures\ns-fltuserstructures--instance-partial-information.md">INSTANCE_PARTIAL_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20INSTANCE_FULL_INFORMATION structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
