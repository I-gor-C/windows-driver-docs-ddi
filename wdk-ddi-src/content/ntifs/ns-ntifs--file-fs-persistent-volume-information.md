---
UID: NS.ntifs._FILE_FS_PERSISTENT_VOLUME_INFORMATION
title: FILE_FS_PERSISTENT_VOLUME_INFORMATION
author: windows-driver-content
description: The FILE_FS_PERSISTENT_VOLUME_INFORMATION structure is used to control persistent settings for a file system volume. Persistent settings persist on a file system volume between reboots of the computer.
old-location: ifsk\file_fs_persistent_volume_information.htm
old-project: ifsk
ms.assetid: f1c7785e-e135-4060-8cf7-5c985b37ff83
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_FS_PERSISTENT_VOLUME_INFORMATION, FILE_FS_PERSISTENT_VOLUME_INFORMATION, *PFILE_FS_PERSISTENT_VOLUME_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_FS_PERSISTENT_VOLUME_INFORMATION
req.alt-loc: ntifs.h
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

# FILE_FS_PERSISTENT_VOLUME_INFORMATION structure



## -description
<p>The <b>FILE_FS_PERSISTENT_VOLUME_INFORMATION</b> structure is used to control persistent settings for a file system volume. Persistent settings persist on a file system volume between reboots of the computer. </p>


## -syntax

````
typedef struct _FILE_FS_PERSISTENT_VOLUME_INFORMATION {
  ULONG VolumeFlags;
  ULONG FlagMask;
  ULONG Version;
  ULONG Reserved;
} FILE_FS_PERSISTENT_VOLUME_INFORMATION, *PFILE_FS_PERSISTENT_VOLUME_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>VolumeFlags</b>

<dd>
<p>The persistent state settings for a file system volume. This value is a bitwise OR combination of the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="PERSISTENT_VOLUME_STATE_SHORT_NAME_CREATION_DISABLED"></a><a id="persistent_volume_state_short_name_creation_disabled"></a><dl>

### -field <b>PERSISTENT_VOLUME_STATE_SHORT_NAME_CREATION_DISABLED</b>


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>A 0 for this bit indicates that the creation of 8.3 short names is enabled, and a 1 indicates that short name creation is disabled. 8.3 short file names have at most eight characters, followed by a period "." and a file name extension of at most three characters.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PERSISTENT_VOLUME_STATE_VOLUME_SCRUB_DISABLED"></a><a id="persistent_volume_state_volume_scrub_disabled"></a><dl>

### -field <b>PERSISTENT_VOLUME_STATE_VOLUME_SCRUB_DISABLED</b>


### -field 0x00000002

</dl>
</td>
<td width="60%">
<p>When set, this flag indicates that the volume scrub is disabled for the volume.</p>
<p>This flag is valid starting with Windows 8.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PERSISTENT_VOLUME_STATE_GLOBAL_METADATA_NO_SEEK_PENALTY"></a><a id="persistent_volume_state_global_metadata_no_seek_penalty"></a><dl>

### -field <b>PERSISTENT_VOLUME_STATE_GLOBAL_METADATA_NO_SEEK_PENALTY</b>


### -field 0x00000004

</dl>
</td>
<td width="60%">
<p>Global no seek penalty is enabled for a tiered volume.</p>
<p>This flag is valid starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PERSISTENT_VOLUME_STATE_LOCAL_METADATA_NO_SEEK_PENALTY"></a><a id="persistent_volume_state_local_metadata_no_seek_penalty"></a><dl>

### -field <b>PERSISTENT_VOLUME_STATE_LOCAL_METADATA_NO_SEEK_PENALTY</b>


### -field 0x00000008

</dl>
</td>
<td width="60%">
<p>Local no seek penalty is enabled for a tiered volume.</p>
<p>This flag is valid starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PERSISTENT_VOLUME_STATE_NO_HEAT_GATHERING"></a><a id="persistent_volume_state_no_heat_gathering"></a><dl>

### -field <b>PERSISTENT_VOLUME_STATE_NO_HEAT_GATHERING</b>


### -field 0x00000010

</dl>
</td>
<td width="60%">
<p>When set, heat gathering is not enabled for the tiered volume.</p>
<p>This flag is valid starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PERSISTENT_VOLUME_STATE_CONTAINS_BACKING_WIM"></a><a id="persistent_volume_state_contains_backing_wim"></a><dl>

### -field <b>PERSISTENT_VOLUME_STATE_CONTAINS_BACKING_WIM</b>


### -field 0x00000020

</dl>
</td>
<td width="60%">
<p>Indicates that this volume is backing the system volume with files  from a Windows Image Format (WIM) file.</p>
<p>This flag is valid starting with Windows 8.1 Update.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="PERSISTENT_VOLUME_STATE_BACKED_BY_WIM"></a><a id="persistent_volume_state_backed_by_wim"></a><dl>

### -field <b>PERSISTENT_VOLUME_STATE_BACKED_BY_WIM</b>


### -field 0x00000040

</dl>
</td>
<td width="60%">
<p>Indicates that this volume is dependent on another volume to provide system critical boot files. The other  volume contains a WIM file that backs the files on this volume. This flag is read only.</p>
<p>This flag is valid starting with Windows 8.1 Update.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>FlagMask</b>

<dd>
<p>A mask value for the valid flags that can appear in <b>VolumeFlags</b>. This is a bitwise OR combination of the desired flags described for <b>VolumeFlags</b>.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>The version number of this structure. Set to 1.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Set to 0;</p>
</dd>
</dl>

## -remarks
<p>The <b>FILE_FS_PERSISTENT_VOLUME_INFORMATION</b> structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545564">FSCTL_SET_PERSISTENT_VOLUME_STATE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545496">FSCTL_QUERY_PERSISTENT_VOLUME_STATE</a> control codes.</p>

<p>To query the state flags, <b>FlagMask</b> is set to a combination of flags to check for. For example, if the only the seek penalty flags are of interest, <b>FlagMask</b> = PERSISTENT_VOLUME_STATE_GLOBAL_METADATA_NO_SEEK_PENALTY | PERSISTENT_VOLUME_STATE_LOCAL_METADATA_NO_SEEK_PENALTY. Also, if only short name support is queried, then set <b>FlagMask</b> = PERSISTENT_VOLUME_STATE_SHORT_NAME_CREATION_DISABLED.</p>

<p>When setting or clearing the persistent volume state flags, using <a href="https://msdn.microsoft.com/library/windows/hardware/ff545564">FSCTL_SET_PERSISTENT_VOLUME_STATE</a>, <b>FlagMask</b> is set to all of the flags in <b>VolumeFlags</b> that will be affected for the volume. <b>VolumeFlags</b> contains the actual persistent state flags to set for the volume. The following example shows how to set the members of <b>FILE_FS_PERSISTENT_VOLUME_INFORMATION</b> to enable short name creation for a volume.</p>

<p>The <b>Version</b> member must be set to the current version of 1 for both a query and  a set  request.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 7.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545496">FSCTL_QUERY_PERSISTENT_VOLUME_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545564">FSCTL_SET_PERSISTENT_VOLUME_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_FS_PERSISTENT_VOLUME_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
