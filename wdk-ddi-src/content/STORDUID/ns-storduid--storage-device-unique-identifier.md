---
UID: NS.storduid._STORAGE_DEVICE_UNIQUE_IDENTIFIER
title: STORAGE_DEVICE_UNIQUE_IDENTIFIER
author: windows-driver-content
description: The STORAGE_DEVICE_UNIQUE_IDENTIFIER structure defines a device unique identifier (DUID).
old-location: storage\storage_device_unique_identifier.htm
ms.assetid: 02de3382-031a-4d42-b349-786248da9c5c
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: storduid.h
req.include-header: Storduid.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_DEVICE_UNIQUE_IDENTIFIER
req.alt-loc: storduid.h
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
ms.keywords: STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
req.iface: 
req.product: Windows 10 or later.
---

# STORAGE_DEVICE_UNIQUE_IDENTIFIER structure



## -description
<p>The STORAGE_DEVICE_UNIQUE_IDENTIFIER structure defines a device unique identifier (DUID).</p>


## -syntax

````
typedef struct _STORAGE_DEVICE_UNIQUE_IDENTIFIER {
  ULONG Version;
  ULONG Size;
  ULONG StorageDeviceIdOffset;
  ULONG StorageDeviceOffset;
  ULONG DriveLayoutSignatureOffset;
} STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of the DUID.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of the identifier header and the identifiers (IDs) that follow the header.</p>
</dd>

### -field <b>StorageDeviceIdOffset</b>

<dd>
<p>The offset, in bytes, from the beginning of the header to the device ID descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff566972">STORAGE_DEVICE_ID_DESCRIPTOR</a>). The device ID descriptor contains the IDs that are extracted from page 0x83 of the device's vital product data (VPD).</p>
</dd>

### -field <b>StorageDeviceOffset</b>

<dd>
<p>The offset, in bytes, from the beginning of the header to the device descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff566971">STORAGE_DEVICE_DESCRIPTOR</a>). The device descriptor contains IDs that are extracted from non-VPD inquiry data.</p>
</dd>

### -field <b>DriveLayoutSignatureOffset</b>

<dd>
<p>The offset, in bytes, to the drive layout signature (<a href="https://msdn.microsoft.com/library/windows/hardware/ff566973">STORAGE_DEVICE_LAYOUT_SIGNATURE</a>).</p>
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
<dt>Storduid.h (include Storduid.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566971">STORAGE_DEVICE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566972">STORAGE_DEVICE_ID_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20STORAGE_DEVICE_UNIQUE_IDENTIFIER structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
