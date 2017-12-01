---
UID: NS.ntddstor._STORAGE_LB_PROVISIONING_MAP_RESOURCES
title: STORAGE_LB_PROVISIONING_MAP_RESOURCES
author: windows-driver-content
description: The STORAGE_LB_PROVISIONING_MAP_RESOURCES structure contains, when valid, the count of available and used bytes mapped to a storage device. This structure is returned from an IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES request.
old-location: storage\storage_lb_provisioning_map_resources.htm
old-project: storage
ms.assetid: 6F7DE233-D002-4927-80FC-307A3A33653A
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_LB_PROVISIONING_MAP_RESOURCES, STORAGE_LB_PROVISIONING_MAP_RESOURCES, *PSTORAGE_LB_PROVISIONING_MAP_RESOURCES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h, Scsi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_LB_PROVISIONING_MAP_RESOURCES
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

# STORAGE_LB_PROVISIONING_MAP_RESOURCES structure



## -description
<p>The <b>STORAGE_LB_PROVISIONING_MAP_RESOURCES</b> structure contains, when valid, the count of available and used bytes mapped to a storage device. This structure is returned from an <a href="..\ntddstor\ni-ntddstor-ioctl-storage-get-lb-provisioning-map-resources.md">IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES</a> request.</p>


## -syntax

````
typedef struct _STORAGE_LB_PROVISIONING_MAP_RESOURCES {
  ULONG     Size;
  ULONG     Version;
  UCHAR     AvailableMappingResourcesValid  :1;
  UCHAR     UsedMappingResourcesValid  :1;
  UCHAR     Reserved0  :6;
  UCHAR     Reserved1[3];
  UCHAR     AvailableMappingResourcesScope  :2;
  UCHAR     UsedMappingResourcesScope  :2;
  UCHAR     Reserved2  :4;
  UCHAR     Reserved3[3];
  ULONGLONG AvailableMappingResources;
  ULONGLONG UsedMappingResources;
} STORAGE_LB_PROVISIONING_MAP_RESOURCES, *PSTORAGE_LB_PROVISIONING_MAP_RESOURCES;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure. This is set to <b>sizeof</b>(STORAGE_LB_PROVISIONING_MAP_RESOURCES).</p>
</dd>

### -field <b>Version</b>

<dd>
<p>The version of this structure.</p>
</dd>

### -field <b>AvailableMappingResourcesValid</b>

<dd>
<p>The validity of the <b>AvailableMappingResources</b> member.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p><b>AvailableMappingResources</b> is not valid.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p><b>AvailableMappingResources</b> is valid.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>UsedMappingResourcesValid</b>

<dd>
<p>The validity of the <b>UsedMappingResources</b> member.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p><b>UsedMappingResources</b> is not valid.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p><b>UsedMappingResources</b> is valid.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>AvailableMappingResourcesScope</b>

<dd>
<p>Resources scope available to a LUN or a LUN pool.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_REPORTED"></a><a id="log_page_lbp_resource_scope_not_reported"></a><dl>

### -field <b>LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_REPORTED</b>


### -field 0

</dl>
</td>
<td width="60%">
<p>Mapping resources are not reported.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="LOG_PAGE_LBP_RESOURCE_SCOPE_DEDICATED_TO_LUN"></a><a id="log_page_lbp_resource_scope_dedicated_to_lun"></a><dl>

### -field <b>LOG_PAGE_LBP_RESOURCE_SCOPE_DEDICATED_TO_LUN</b>


### -field 1

</dl>
</td>
<td width="60%">
<p>Mapping resources dedicated to a LUN.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_DEDICATED_TO_LUN"></a><a id="log_page_lbp_resource_scope_not_dedicated_to_lun"></a><dl>

### -field <b>LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_DEDICATED_TO_LUN</b>


### -field 2

</dl>
</td>
<td width="60%">
<p>Mapping resources dedicated to a LUN pool.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>UsedMappingResourcesScope</b>

<dd>
<p>Resources scope used by a LUN or LUN pool.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_REPORTED"></a><a id="log_page_lbp_resource_scope_not_reported"></a><dl>

### -field <b>LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_REPORTED</b>


### -field 0

</dl>
</td>
<td width="60%">
<p>Mapping resources are not reported.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="LOG_PAGE_LBP_RESOURCE_SCOPE_DEDICATED_TO_LUN"></a><a id="log_page_lbp_resource_scope_dedicated_to_lun"></a><dl>

### -field <b>LOG_PAGE_LBP_RESOURCE_SCOPE_DEDICATED_TO_LUN</b>


### -field 1

</dl>
</td>
<td width="60%">
<p>Mapping resources dedicated to a LUN.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_DEDICATED_TO_LUN"></a><a id="log_page_lbp_resource_scope_not_dedicated_to_lun"></a><dl>

### -field <b>LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_DEDICATED_TO_LUN</b>


### -field 2

</dl>
</td>
<td width="60%">
<p>Mapping resources dedicated to a LUN pool.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>AvailableMappingResources</b>

<dd>
<p>The count, in bytes, of the available mapping resources for a disk.</p>
</dd>

### -field <b>UsedMappingResources</b>

<dd>
<p>The count, in bytes, of the used mapping resources for a disk.</p>
</dd>
</dl>

## -remarks
<p>As a managed storage element, resource usage for a thinly provisioned LUN is tracked. Resource allocation is logged for the device by the storage subsystem. A storage application can query for this resource usage  information using the <a href="..\ntddstor\ni-ntddstor-ioctl-storage-get-lb-provisioning-map-resources.md"> IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES</a> request.</p>

<p>Logging of mapped resource counts is dependent on support from the storage device. The <b>AvailableMappingResources</b> and <b>UsedMappingResources</b> members contain resource counts when their respective validity fields are set.</p>

<p>Resource counts are in bytes instead of totals of blocks or slabs.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h or Scsi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddstor\ni-ntddstor-ioctl-storage-get-lb-provisioning-map-resources.md"> IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_LB_PROVISIONING_MAP_RESOURCES structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
