---
UID: NS.ntddstor._STORAGE_MINIPORT_DESCRIPTOR
title: STORAGE_MINIPORT_DESCRIPTOR
author: windows-driver-content
description: Reserved for system use.
old-location: storage\storage_miniport_descriptor.htm
old-project: storage
ms.assetid: 30497CA8-70B6-48F9-B5D5-45E606A3226E
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_MINIPORT_DESCRIPTOR, STORAGE_MINIPORT_DESCRIPTOR, *PSTORAGE_MINIPORT_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_MINIPORT_DESCRIPTOR
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

# STORAGE_MINIPORT_DESCRIPTOR structure



## -description
<p>Reserved for system use.</p>


## -syntax

````
typedef struct _STORAGE_MINIPORT_DESCRIPTOR {
  ULONG                 Version;
  ULONG                 Size;
  STORAGE_PORT_CODE_SET Portdriver;
  BOOLEAN               LUNResetSupported;
  BOOLEAN               TargetResetSupported;
  USHORT                IoTimeoutValue;
  BOOLEAN               ExtraIoInfoSupported;
  UCHAR                 Reserved0[3];
  UCHAR                 Reserved1;
} STORAGE_MINIPORT_DESCRIPTOR, *PSTORAGE_MINIPORT_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Contains the size of this structure, in bytes. The value of this member will change as members are added to 
      the structure.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the total size of the data returned, in bytes. This may include data that follows this 
      structure.</p>
</dd>

### -field <b>Portdriver</b>

<dd>
<p>Type of port driver as enumerated by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/mt668773">STORAGE_PORT_CODE_SET</a> enumeration.</p>
</dd>

### -field <b>LUNResetSupported</b>

<dd>
<p>Indicates whether a LUN reset is supported.</p>
</dd>

### -field <b>TargetResetSupported</b>

<dd>
<p>Indicates whether a target reset is supported.</p>
</dd>

### -field <b>IoTimeoutValue</b>

<dd>
<p><b>Introduced in Windows 8:  </b>Indicates the timeout value for the device, in milliseconds (ms).</p>
</dd>

### -field <b>ExtraIoInfoSupported</b>

<dd>
<p><b>Introduced in Windows 8.1:  </b>Indicates if extra I/O info is supported.</p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p><b>Introduced in Windows 8.1:  </b>Reserved for future use.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p><b>Introduced in Windows 8.1:  </b>Reserved for future use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows Vista</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2008</p>
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