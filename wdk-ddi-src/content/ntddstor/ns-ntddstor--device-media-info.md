---
UID: NS.ntddstor._DEVICE_MEDIA_INFO
title: DEVICE_MEDIA_INFO
author: windows-driver-content
description: A storage class driver returns an array of DEVICE_MEDIA_INFO structures, embedded in a GET_MEDIA_TYPES structure, in response to an IOCTL_STORAGE_GET_MEDIA_TYPES_EX device-control request.
old-location: storage\device_media_info.htm
old-project: storage
ms.assetid: 87906511-7bcb-4f4d-9383-44b0501536e3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DEVICE_MEDIA_INFO, DEVICE_MEDIA_INFO, *PDEVICE_MEDIA_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_MEDIA_INFO
req.alt-loc: ntddstor.h
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

# DEVICE_MEDIA_INFO structure



## -description
<p>A storage class driver returns an array of <b>DEVICE_MEDIA_INFO</b> structures, embedded in a <a href="..\ntddstor\ns-ntddstor--get-media-types.md">GET_MEDIA_TYPES</a> structure, in response to an <a href="..\ntddstor\ni-ntddstor-ioctl-storage-get-media-types-ex.md">IOCTL_STORAGE_GET_MEDIA_TYPES_EX</a> device-control request.</p>


## -syntax

````
typedef struct _DEVICE_MEDIA_INFO {
  union {
    struct {
      LARGE_INTEGER      Cylinders;
      STORAGE_MEDIA_TYPE MediaType;
      ULONG              TracksPerCylinder;
      ULONG              SectorsPerTrack;
      ULONG              BytesPerSector;
      ULONG              NumberMediaSides;
      ULONG              MediaCharacteristics;
    } DiskInfo;
    struct {
      LARGE_INTEGER      Cylinders;
      STORAGE_MEDIA_TYPE MediaType;
      ULONG              TracksPerCylinder;
      ULONG              SectorsPerTrack;
      ULONG              BytesPerSector;
      ULONG              NumberMediaSides;
      ULONG              MediaCharacteristics;
    } RemovableDiskInfo;
    struct {
      STORAGE_MEDIA_TYPE MediaType;
      ULONG              MediaCharacteristics;
      ULONG              CurrentBlockSize;
      STORAGE_BUS_TYPE   BusType;
      union {
        struct {
          UCHAR MediumType;
          UCHAR DensityCode;
        } ScsiInformation;
      } BusSpecificData;
    } TapeInfo;
  } DeviceSpecific;
} DEVICE_MEDIA_INFO, *PDEVICE_MEDIA_INFO;
````


## -struct-fields
<dl>

### -field <b>DeviceSpecific</b>

<dd>
<dl>

### -field <b>DiskInfo</b>

<dd>
<p>Describes a nonremovable (fixed) disk.</p>
<dl>

### -field <b>Cylinders</b>

<dd>
<p>Specifies the number of cylinders on this disk. </p>
</dd>

### -field <b>MediaType</b>

<dd>
<p>Specifies a <a href="storage.media_type">MEDIA_TYPE</a> of <b>FixedMedia</b>. </p>
</dd>

### -field <b>TracksPerCylinder</b>

<dd>
<p>Specifies the number of tracks per cylinder.</p>
</dd>

### -field <b>SectorsPerTrack</b>

<dd>
<p>Specifies the number of sectors per track.</p>
</dd>

### -field <b>BytesPerSector</b>

<dd>
<p>Specifies the number of bytes per sector.</p>
</dd>

### -field <b>NumberMediaSides</b>

<dd>
<p>Specifies the number of sides of the disk that can contain data: either 1 for one-sided media or 2 for two-sided media.</p>
</dd>

### -field <b>MediaCharacteristics</b>

<dd>
<p>Specifies characteristics of the disk indicated by one or more of the following flags.</p>
<dl><a id="MEDIA_CURRENTLY_MOUNTED_"></a><a id="media_currently_mounted_"></a>
### -field <b>MEDIA_CURRENTLY_MOUNTED
</b>
<a id="MEDIA_ERASEABLE_"></a><a id="media_eraseable_"></a>
### -field <b>MEDIA_ERASEABLE
</b>
<a id="MEDIA_READ_ONLY_"></a><a id="media_read_only_"></a>
### -field <b>MEDIA_READ_ONLY
</b>
<a id="MEDIA_READ_WRITE_"></a><a id="media_read_write_"></a>
### -field <b>MEDIA_READ_WRITE
</b>
<a id="MEDIA_WRITE_ONCE_"></a><a id="media_write_once_"></a>
### -field <b>MEDIA_WRITE_ONCE
</b>
<a id="MEDIA_WRITE_PROTECTED_"></a><a id="media_write_protected_"></a>
### -field <b>MEDIA_WRITE_PROTECTED
</b>

</dl>
</dd>
</dl>
</dd>

### -field <b>RemovableDiskInfo</b>

<dd>
<p>Describes a removable (nonfixed) disk.</p>
<dl>

### -field <b>Cylinders</b>

<dd>
<p>Specifies the number of cylinders on this disk. </p>
</dd>

### -field <b>MediaType</b>

<dd>
<p>Specifies a <a href="storage.media_type">MEDIA_TYPE</a> or <a href="..\ntddstor\ne-ntddstor--storage-media-type.md">STORAGE_MEDIA_TYPE</a> value that indicates the type of removable disk. </p>
</dd>

### -field <b>TracksPerCylinder</b>

<dd>
<p>Specifies the number of tracks per cylinder.</p>
</dd>

### -field <b>SectorsPerTrack</b>

<dd>
<p>Specifies the number of sectors per track.</p>
</dd>

### -field <b>BytesPerSector</b>

<dd>
<p>Specifies the number of bytes per sector.</p>
</dd>

### -field <b>NumberMediaSides</b>

<dd>
<p>Specifies the number of sides of the disk that can contain data: 1 for one-sided media or 2 for two-sided media.</p>
</dd>

### -field <b>MediaCharacteristics</b>

<dd>
<p>Specifies characteristics of the disk, indicated by MEDIA_<i>XXX</i> flags ORed together. For a list of these flags, see the <b>DeviceSpecific.DiskInfo.MediaCharacteristics</b> member of the <b>DeviceSpecific.DiskInfo</b> structure.</p>
</dd>
</dl>
</dd>

### -field <b>TapeInfo</b>

<dd>
<p>Describes a tape.</p>
<dl>

### -field <b>MediaType</b>

<dd>
<p>Specifies a <a href="..\ntddstor\ne-ntddstor--storage-media-type.md">STORAGE_MEDIA_TYPE</a> value that indicates the type of tape described in this structure. </p>
</dd>

### -field <b>MediaCharacteristics</b>

<dd>
<p>Specifies characteristics of the tape, indicated by MEDIA_<i>XXX</i> flags ORed together. For a list of these flags, see the <b>DeviceSpecific.DiskInfo.MediaCharacteristics</b> member of the <b>DeviceSpecific.DiskInfo</b> structure.</p>
</dd>

### -field <b>CurrentBlockSize</b>

<dd>
<p>Specifies the current block size, in bytes.</p>
</dd>

### -field <b>BusType</b>

<dd>
<p>Specifies a value of type <a href="storage.storage_bus_type">STORAGE_BUS_TYPE</a> that indicates the bus type.</p>
</dd>

### -field <b>BusSpecificData</b>

<dd>
<dl>

### -field <b>ScsiInformation</b>

<dd>
<p>Specifies bus-specific information from mode page data that describes the medium supported by the tape drive. Values for other bus types will be supplied in a later release.</p>
<dl>

### -field <b>MediumType</b>

<dd>
<p>Specifies the SCSI-specific medium type.</p>
</dd>

### -field <b>DensityCode</b>

<dd>
<p>Specifies the SCSI-specific current operating density for read/write operations.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>This structure is used by a storage driver to indicate the types of media supported by a device and which type is currently mounted, if any. A driver must provide this information if it might control drives in a media library or changer or if its device might be accessed by the Removable Storage Manager (RSM). </p>

<p>The driver fills in an array of <b>DEVICE_MEDIA_INFO</b> structures, one for each medium type supported by the device, embedded in a <a href="..\ntddstor\ns-ntddstor--get-media-types.md">GET_MEDIA_TYPES</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.tapeminigetmediatypes">TapeMiniGetMediaTypes</a>
</dt>
<dt>
<a href="..\ntddstor\ne-ntddstor--storage-media-type.md">STORAGE_MEDIA_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DEVICE_MEDIA_INFO structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
