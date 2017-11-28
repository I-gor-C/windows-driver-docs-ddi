---
UID: NS.fltuserstructures._INSTANCE_AGGREGATE_STANDARD_INFORMATION
title: INSTANCE_AGGREGATE_STANDARD_INFORMATION
author: windows-driver-content
description: The caller-allocated INSTANCE_AGGREGATE_STANDARD_INFORMATION structure contains information for either a minifilter driver instance or a legacy filter driver.
old-location: ifsk\instance_aggregate_standard_information.htm
old-project: ifsk
ms.assetid: 35311ee7-d023-4b04-b510-a949ab9a40ca
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: INSTANCE_AGGREGATE_STANDARD_INFORMATION, INSTANCE_AGGREGATE_STANDARD_INFORMATION, *PINSTANCE_AGGREGATE_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: fltuserstructures.h
req.include-header: FltUser.h, FltKernel.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: INSTANCE_AGGREGATE_STANDARD_INFORMATION
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

# INSTANCE_AGGREGATE_STANDARD_INFORMATION structure



## -description
<p>The caller-allocated INSTANCE_AGGREGATE_STANDARD_INFORMATION structure contains information for either a minifilter driver instance or a legacy filter driver.</p>


## -syntax

````
typedef struct _INSTANCE_AGGREGATE_STANDARD_INFORMATION {
  ULONG NextEntryOffset;
  ULONG Flags;
  union {
    struct {
      ULONG               Flags;
      ULONG               FrameID;
      FLT_FILESYSTEM_TYPE VolumeFileSystemType;
      USHORT              InstanceNameLength;
      USHORT              InstanceNameBufferOffset;
      USHORT              AltitudeLength;
      USHORT              AltitudeBufferOffset;
      USHORT              VolumeNameLength;
      USHORT              VolumeNameBufferOffset;
      USHORT              FilterNameLength;
      USHORT              FilterNameBufferOffset;
#if FLT_MGR_WIN8
      ULONG               SupportedFeatures;
    } MiniFilter;
#endif 
    struct {
      ULONG  Flags;
      USHORT AltitudeLength;
      USHORT AltitudeBufferOffset;
      USHORT VolumeNameLength;
      USHORT VolumeNameBufferOffset;
      USHORT FilterNameLength;
      USHORT FilterNameBufferOffset;
#if FLT_MGR_WIN8
      ULONG  SupportedFeatures;
#endif 
    } LegacyFilter;
  } Type;
} INSTANCE_AGGREGATE_STANDARD_INFORMATION, *PINSTANCE_AGGREGATE_STANDARD_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>NextEntryOffset</b>

<dd>
<p>Byte offset of the next INSTANCE_AGGREGATE_STANDARD_INFORMATION structure if multiple structures are present in a buffer. This member is zero if no other structures follow this one.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Indicates whether the filter driver is a legacy filter driver or a minifilter driver.  This member must contain one of the following flags.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FLTFL_IASI_IS_MINIFILTER</p>
</td>
<td>
<p>The filter driver is a minifilter driver - use the <b>MiniFilter</b> portion of the union.</p>
</td>
</tr>
<tr>
<td>
<p>FLTFL_IASI_IS_LEGACYFILTER</p>
</td>
<td>
<p>The filter driver is a legacy filter driver - use the <b>LegacyFilter</b> portion of the union.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Type</b>

<dd>
<dl>

### -field <b>MiniFilter</b>

<dd>
<p>Nested structure variable with the following members.</p>
<dl>

### -field <b>Flags</b>

<dd>
<p>A bitmask of flags that describe attributes of the minifilter instance. The following are valid flag values.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>FLTFL_IASIM_DETACHED_VOLUME</td>
<td>The volume is not currently attached to a storage stack.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>FrameID</b>

<dd>
<p>Zero-based index used to identify the filter manager frame that the minifilter instance is in. </p>
</dd>

### -field <b>VolumeFileSystemType</b>

<dd>
<p>Identifies the type of file system the minifilter instance is attached to.  The possible values for this member are listed in <a href="https://msdn.microsoft.com/library/windows/hardware/ff625876">FLT_FILESYSTEM_TYPE</a>.</p>
</dd>

### -field <b>InstanceNameLength</b>

<dd>
<p>Length, in bytes, of the minifilter instance name. </p>
</dd>

### -field <b>InstanceNameBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode minifilter instance name string. This string is not NULL-terminated. </p>
</dd>

### -field <b>AltitudeLength</b>

<dd>
<p>Length, in bytes, of the minifilter instance altitude string. </p>
</dd>

### -field <b>AltitudeBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode minifilter instance altitude string. This string is not NULL-terminated. </p>
</dd>

### -field <b>VolumeNameLength</b>

<dd>
<p>Length, in bytes, of the volume name of the volume that the minifilter instance is attached to. 
</p>
</dd>

### -field <b>VolumeNameBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode volume name string for the volume that the minifilter instance is attached to. This string is not NULL-terminated.</p>
</dd>

### -field <b>FilterNameLength</b>

<dd>
<p>Length, in bytes, of the minifilter name of the minifilter from which the minifilter instance was derived.</p>
</dd>

### -field <b>FilterNameBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode minifilter name string for the minifilter from which the minifilter instance was derived. This string is not NULL-terminated.</p>
</dd>

### -field <b>SupportedFeatures</b>

<dd>
<p>The supported feature flags for the filter.</p>
<p>
<p>The supported features are a bitwise OR combination of the following flags.</p>
</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="SUPPORTED_FS_FEATURES_OFFLOAD_READ"></a><a id="supported_fs_features_offload_read"></a><dl>

### -field <b>SUPPORTED_FS_FEATURES_OFFLOAD_READ</b>


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>The volume supports offloaded read operations</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SUPPORTED_FS_FEATURES_OFFLOAD_WRITE"></a><a id="supported_fs_features_offload_write"></a><dl>

### -field <b>SUPPORTED_FS_FEATURES_OFFLOAD_WRITE</b>


### -field 0x00000002

</dl>
</td>
<td width="60%">
<p>The volume supports offloaded write operations</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
</dd>

### -field <b>LegacyFilter</b>

<dd>
<p>
       Nested structure variable with the following members.
       
      </p>
<dl>

### -field <b>Flags</b>

<dd>
<p>A bitmask of flags that describe attributes of the legacy filter. The following are valid flag values.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>FLTFL_IASIL_DETACHED_VOLUME</td>
<td>The volume is not currently attached to a storage stack.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>AltitudeLength</b>

<dd>
<p>Length, in bytes, of the legacy filter altitude string.</p>
</dd>

### -field <b>AltitudeBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode legacy filter altitude string. This string is not NULL-terminated.
</p>
<p>Starting with Windows Vista, altitudes are assigned to legacy filter drivers based on the driver's load order group. This ensures that minifilter drivers will layer properly above and below legacy filter drivers even if one or more of the filter drivers are loaded out-of-order.</p>
</dd>

### -field <b>VolumeNameLength</b>

<dd>
<p> 
Length, in bytes, of the volume name of the volume that the legacy filter is attached to.</p>
</dd>

### -field <b>VolumeNameBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode volume name string for the volume that the legacy filter is attached to. This string is not NULL-terminated.</p>
</dd>

### -field <b>FilterNameLength</b>

<dd>
<p>Length, in bytes, of the legacy filter name.</p>
</dd>

### -field <b>FilterNameBufferOffset</b>

<dd>
<p>Byte offset (relative to the beginning of the structure) of the first character of the Unicode legacy filter name string. This string is not NULL-terminated.</p>
</dd>

### -field <b>SupportedFeatures</b>

<dd>
<p>The supported feature flags for the filter.</p>
<p>
<p>The supported features are a bitwise OR combination of the following flags.</p>
</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="SUPPORTED_FS_FEATURES_OFFLOAD_READ"></a><a id="supported_fs_features_offload_read"></a><dl>

### -field <b>SUPPORTED_FS_FEATURES_OFFLOAD_READ</b>


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>The volume supports offloaded read operations</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SUPPORTED_FS_FEATURES_OFFLOAD_WRITE"></a><a id="supported_fs_features_offload_write"></a><dl>

### -field <b>SUPPORTED_FS_FEATURES_OFFLOAD_WRITE</b>


### -field 0x00000002

</dl>
</td>
<td width="60%">
<p>The volume supports offloaded write operations</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>A structure of type INSTANCE_AGGREGATE_STANDARD_INFORMATION can be allocated from paged or nonpaged pool.  This structure is passed as a parameter to routines such as the following:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540541">FilterInstanceFindFirst</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541493">FilterInstanceFindNext</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541499">FilterInstanceGetInformation</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541541">FilterVolumeInstanceFindFirst</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541551">FilterVolumeInstanceFindNext</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542071">FltEnumerateInstanceInformationByFilter</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543062">FltGetInstanceInformation</a>
</p>

<p>The INSTANCE_AGGREGATE_STANDARD_INFORMATION structure must be aligned on a LONGLONG (8-byte) boundary. If a buffer contains two or more of these structures, the <b>NextEntryOffset</b> value in each entry falls on an 8-byte boundary.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltuserstructures.h (include FltUser.h or FltKernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540541">FilterInstanceFindFirst</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541493">FilterInstanceFindNext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541499">FilterInstanceGetInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541541">FilterVolumeInstanceFindFirst</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541551">FilterVolumeInstanceFindNext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542071">FltEnumerateInstanceInformationByFilter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542082">FltEnumerateInstanceInformationByVolume</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543062">FltGetInstanceInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548176">INSTANCE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548185">INSTANCE_FULL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548190">INSTANCE_PARTIAL_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20INSTANCE_AGGREGATE_STANDARD_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
