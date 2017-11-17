---
UID: NS.ntddstor._STORAGE_PHYSICAL_DEVICE_DATA
title: STORAGE_PHYSICAL_DEVICE_DATA
author: windows-driver-content
description: Specifies the physical device data of a storage device.
old-location: storage\storage_physical_device_data.htm
ms.assetid: 9D8E67D1-EB7C-4EED-8BDD-43D5E012B99C
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_PHYSICAL_DEVICE_DATA
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
ms.keywords: STORAGE_PHYSICAL_DEVICE_DATA, STORAGE_PHYSICAL_DEVICE_DATA, *PSTORAGE_PHYSICAL_DEVICE_DATA
req.iface: 
---

# STORAGE_PHYSICAL_DEVICE_DATA structure



## -description
<p>Specifies the physical device data of a storage device.</p>


## -syntax

````
typedef struct _STORAGE_PHYSICAL_DEVICE_DATA {
  ULONG                           DeviceId;
  ULONG                           Role;
  STORAGE_COMPONENT_HEALTH_STATUS HealthStatus;
  STORAGE_PROTOCOL_TYPE           CommandProtocol;
  STORAGE_SPEC_VERSION            SpecVersion;
  STORAGE_DEVICE_FORM_FACTOR      FormFactor;
  UCHAR                           Vendor[8];
  UCHAR                           Model[40];
  UCHAR                           FirmwareRevision[16];
  ULONGLONG                       Capacity;
  UCHAR                           PhysicalLocation[32];
  ULONG                           Reserved[2];
} STORAGE_PHYSICAL_DEVICE_DATA, *PSTORAGE_PHYSICAL_DEVICE_DATA;
````


## -struct-fields
<dl>

### -field <b>DeviceId</b>

<dd>
<p>The hardware ID of the storage device.</p>
</dd>

### -field <b>Role</b>

<dd>
<p>The role of the storage device. A bitmask can be use to specify multiple roles, including <b>STORAGE_COMPONENT_ROLE_CACHE</b> (0x00000001), <b>STORAGE_COMPONENT_ROLE_TIERING</b> (0x00000002), and <b>STORAGE_COMPONENT_ROLE_DATA</b> (0x00000004).</p>
</dd>

### -field <b>HealthStatus</b>

<dd>
<p>Indicates the health status of a storage device, of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt653957">STORAGE_COMPONENT_HEALTH_STATUS</a>.</p>
</dd>

### -field <b>CommandProtocol</b>

<dd>
<p>Specifies the storage command protocols that are used between software and hardware, of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn931818">STORAGE_PROTOCOL_TYPE</a>.</p>
</dd>

### -field <b>SpecVersion</b>

<dd>
<p>Indicates the specification of the storage device, of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt653963">STORAGE_SPEC_VERSION</a>.</p>
</dd>

### -field <b>FormFactor</b>

<dd>
<p>Indicates the form factor of a storage device, of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt653958">STORAGE_DEVICE_FORM_FACTOR</a>.</p>
</dd>

### -field <b>Vendor[8]</b>

<dd>
<p>The vendor name of the storage device.</p>
</dd>

### -field <b>Model[40]</b>

<dd>
<p>The model name of the storage device.</p>
</dd>

### -field <b>FirmwareRevision[16]</b>

<dd>
<p>The revision number of the storage device.</p>
</dd>

### -field <b>Capacity</b>

<dd>
<p>The capacity of the storage device in units of kilobytes (1024 bytes).</p>
</dd>

### -field <b>PhysicalLocation[32]</b>

<dd>
<p>This member is reserved for future use.</p>
</dd>

### -field <b>Reserved[2]</b>

<dd>
<p>Specifies if the storage device is reserved.</p>
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
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>