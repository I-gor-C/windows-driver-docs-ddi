---
UID: NS.ntddstor._STORAGE_HW_FIRMWARE_INFO
title: STORAGE_HW_FIRMWARE_INFO
author: windows-driver-content
description: This structure contains information about the device firmware.
old-location: storage\storage_hw_firmware_info.htm
ms.assetid: 5A85A7EC-2333-4161-A1E7-55D3420E730C
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_HW_FIRMWARE_INFO
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
ms.keywords: STORAGE_HW_FIRMWARE_INFO, STORAGE_HW_FIRMWARE_INFO, *PSTORAGE_HW_FIRMWARE_INFO
req.iface: 
---

# STORAGE_HW_FIRMWARE_INFO structure



## -description
<p>This structure contains information about the device firmware.</p>


## -syntax

````
typedef struct _STORAGE_HW_FIRMWARE_INFO {
  ULONG                         Version;
  ULONG                         Size;
  UCHAR                         SupportUpgrade  :1;
  UCHAR                         Reserved0  :7;
  UCHAR                         SlotCount;
  UCHAR                         ActiveSlot;
  UCHAR                         PendingActivateSlot;
  BOOLEAN                       FirmwareShared;
  UCHAR                         Reserved[3];
  ULONG                         ImagePayloadAlignment;
  ULONG                         ImagePayloadMaxSize;
  STORAGE_HW_FIRMWARE_SLOT_INFO Slot[ANYSIZE_ARRAY];
} STORAGE_HW_FIRMWARE_INFO, *PSTORAGE_HW_FIRMWARE_INFO;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure. This should be set to sizeof(STORAGE_HW_FIRMWARE_INFO)</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure as a buffer including slot.</p>
</dd>

### -field <b>SupportUpgrade</b>

<dd>
<p>Indicates that this firmware supports an upgrade.</p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>SlotCount</b>

<dd>
<p>The number of firmware slots on the device. This is the dimension of the Slot array.</p>
<div class="alert"><b>Note</b>   Some devices can store more than 1 firmware image, if they have more than 1 firmware slot.</div>
<div> </div>
</dd>

### -field <b>ActiveSlot</b>

<dd>
<p>The firmware slot containing the currently active/running firmware image.</p>
</dd>

### -field <b>PendingActivateSlot</b>

<dd>
<p>The firmware slot that is pending activation.</p>
</dd>

### -field <b>FirmwareShared</b>

<dd>
<p>Indicates that the firmware applies to both the device and controller/adapter, e.g. NVMe SSD.

</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>ImagePayloadAlignment</b>

<dd>
<p>The alignment of the image payload, in number of bytes. The maximum is PAGE_SIZE. The transfer size is a mutliple of this size. Some protocols require at least sector size. When this value is set to 0, this means that this value is invalid.</p>
</dd>

### -field <b>ImagePayloadMaxSize</b>

<dd>
<p>The image payload maximum size, this is used for a single command.</p>
</dd>

### -field <b>Slot</b>

<dd>
<p>Contains the slot information for each slot on the device.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h</dt>
</dl>
</td>
</tr>
</table>