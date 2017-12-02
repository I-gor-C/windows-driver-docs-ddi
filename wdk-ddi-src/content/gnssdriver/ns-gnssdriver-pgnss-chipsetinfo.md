---
UID: NS.gnssdriver.PGNSS_CHIPSETINFO
title: PGNSS_CHIPSETINFO
author: windows-driver-content
description: This structure defines the specific data elements associated with the GNSS hardware.
old-location: sensors\gnss_chipsetinfo.htm
old-project: sensors
ms.assetid: DE45805C-09E6-44B8-A4DA-BF73EC444AA9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PGNSS_CHIPSETINFO, GNSS_CHIPSETINFO, *PGNSS_CHIPSETINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_CHIPSETINFO
req.alt-loc: gnssdriver.h
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

# PGNSS_CHIPSETINFO structure



## -description
<p>This structure defines the specific data elements associated with the GNSS hardware.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Version;
  WCHAR ManufacturerID[25];
  WCHAR HardwareID[25];
  WCHAR FirmwareVersion[20];
  BYTE  Unused[512];
} GNSS_CHIPSETINFO, *PGNSS_CHIPSETINFO;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Structure size.</p>
</dd>

### -field Version

<dd>
<p>Version number.</p>
</dd>

### -field ManufacturerID[25]

<dd>
<p>String containing an identifier for the manufacturer.</p>
</dd>

### -field HardwareID[25]

<dd>
<p>String containing an identifier for the specific GNSS chipset or combo chipset.</p>
</dd>

### -field FirmwareVersion[20]

<dd>
<p>Version for the firmware for the. This would be a string, typically of the format NNNN.NNNN.NNNN.NNNN.</p>
</dd>

### -field Unused[512]

<dd>
<p>Padding buffer.</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>