---
UID: NS.ntddstor._DEVICE_DSM_NOTIFICATION_PARAMETERS
title: DEVICE_DSM_NOTIFICATION_PARAMETERS
author: windows-driver-content
description: The DEVICE_DSM_NOTIFICATION_PARAMETERS structure specifies the parameters for a notification action related to the data-set attributes for a device.
old-location: storage\device_dsm_notification_parameters.htm
old-project: storage
ms.assetid: 57885E58-C7EC-493E-9AB8-B9DABC6CEA2A
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DEVICE_DSM_NOTIFICATION_PARAMETERS, DEVICE_DSM_NOTIFICATION_PARAMETERS, *PDEVICE_DSM_NOTIFICATION_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 7
req.target-min-winversvr: Windows Server 2008 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_DSM_NOTIFICATION_PARAMETERS
req.alt-loc: Ntddstor.h
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

# DEVICE_DSM_NOTIFICATION_PARAMETERS structure



## -description
<p>The <b>DEVICE_DSM_NOTIFICATION_PARAMETERS</b> structure specifies the parameters for a notification action related to the data-set attributes for a device. </p>
<p>The notification  action is specified in the <a href="..\ntddstor\ns-ntddstor--device-manage-data-set-attributes.md">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a> structure that is contained in the system buffer of an <a href="..\ntddstor\ni-ntddstor-ioctl-storage-manage-data-set-attributes.md">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a> request.</p>


## -syntax

````
typedef struct _DEVICE_DSM_NOTIFICATION_PARAMETERS {
  DWORD Size;
  DWORD Flags;
  DWORD NumFileTypeIDs;
  GUID  FileTypeIDs[1];
} DEVICE_DSM_NOTIFICATION_PARAMETERS, *PDEVICE_DSM_NOTIFICATION_PARAMETERS;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Specifies the total size, in bytes, of this structure. The value of this member must include the total size, in bytes, of the <b>FileTypeIDs</b> member.</p>
</dd>

### -field Flags

<dd>
<p>A flag that specifies the characteristics of the notification operation. The  <b>Flags</b> member must be set to one of the following values:</p>
<p></p>
<dl>

### -field DEVICE_DSM_NOTIFY_FLAG_BEGIN

<dd>
<p>The Logical Block Address (LBA) range is currently being used by the file types that are specified in the <b>FileTypeIDs</b> member. </p>
<div class="alert"><b>Note</b>  The LBA range is specified by the data set range of the <a href="..\ntddstor\ns-ntddstor--device-manage-data-set-attributes.md">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a> structure.</div>
<div> </div>
</dd>

### -field DEVICE_DSM_NOTIFY_FLAG_END

<dd>
<p>The LBA range is no longer being used by the file types that are specified in the <b>FileTypeIDs</b> member. </p>
</dd>
</dl>
</dd>

### -field NumFileTypeIDs

<dd>
<p>The number of entries in the <b>FileTypeIDs</b> member.</p>
</dd>

### -field FileTypeIDs

<dd>
<p>One or more <a href="wdkgloss.g#wdkgloss.guid#wdkgloss.guid"><i>GUID</i></a> values that specify the file type for the notification operation. The following table describes the <b>FileTypeIDs</b> GUID values.</p>
<table>
<tr>
<th>GUID value</th>
<th>Description</th>
</tr>
<tr>
<td>FILE_TYPE_NOTIFICATION_GUID_PAGE_FILE</td>
<td>Specifies a notification operation for a page file.</td>
</tr>
<tr>
<td>FILE_TYPE_NOTIFICATION_GUID_HIBERNATION_FILE</td>
<td>Specifies a notification operation for the system hibernation file.</td>
</tr>
<tr>
<td>FILE_TYPE_NOTIFICATION_GUID_CRASHDUMP_FILE</td>
<td>Specifies a notification operation for a system crash dump file.</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>Starting with Windows 7, the NTFS file system notifies the storage stack when the LBA data set range changes for  a specified set of files. The file system issues this notification by sending the storage stack an <a href="..\ntddstor\ni-ntddstor-ioctl-storage-manage-data-set-attributes.md">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a> request with a system buffer that contains a <a href="..\ntddstor\ns-ntddstor--device-manage-data-set-attributes.md">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a> structure. For the notification operation, the file system sets the members of the <b>DEVICE_MANAGE_DATA_SET_ATTRIBUTES</b> structure as follows:</p>

<p>The <b>Action</b> member is set to <b>DeviceDsmAction_Notification</b>.</p>

<p>The <b>ParameterBlockOffset</b> and <b>ParameterBlockLength</b> members specify the location and size of the parameter block for the notification operation. The parameter block is formatted as a <b>DEVICE_DSM_NOTIFICATION_PARAMETERS</b> structure.</p>

<p>If the <b>Flags</b> member is set to zero, the <b>DataSetRangesOffset</b> and <b>DataSetRangesLength</b> members specify the data set range block within the IOCTL payload.</p>

<p>If the <b>Flags</b> member is set to <b>DEVICE_DSM_FLAG_ENTIRE_DATA_SET_RANGE</b>, the <b>DataSetRangesOffset</b> and <b>DataSetRangesLength</b> members are set to zero and the notification action includes the entire data set range for the specified files.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 7</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2008 R2</p>
</td>
</tr>
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
<a href="..\ntddstor\ns-ntddstor--device-manage-data-set-attributes.md">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntddstor\ni-ntddstor-ioctl-storage-manage-data-set-attributes.md">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DEVICE_DSM_NOTIFICATION_PARAMETERS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
