---
UID: NS.hbapiwmi._MS_SMHBA_PORTATTRIBUTES
title: MS_SMHBA_PORTATTRIBUTES
author: windows-driver-content
description: The MS_SMHBA_PORTATTRIBUTES structure is used to report the port information.
old-location: storage\ms_smhba_portattributes.htm
old-project: storage
ms.assetid: ce967b15-723f-4ab7-8a79-8234291d1950
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MS_SMHBA_PORTATTRIBUTES, MS_SMHBA_PORTATTRIBUTES, *PMS_SMHBA_PORTATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MS_SMHBA_PORTATTRIBUTES
req.alt-loc: hbapiwmi.h
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

# MS_SMHBA_PORTATTRIBUTES structure



## -description
<p>The MS_SMHBA_PORTATTRIBUTES structure is used to report the port information.</p>


## -syntax

````
typedef struct _MS_SMHBA_PORTATTRIBUTES {
  ULONG     PortType;
  ULONG     PortState;
  ULONG     PortSpecificAttributesSize;
  WCHAR     OSDeviceName[256 + 1];
  ULONGLONG Reserved;
  UCHAR     PortSpecificAttributes[1];
} MS_SMHBA_PORTATTRIBUTES, *PMS_SMHBA_PORTATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>PortType</b>

<dd>
<p>An integer that indicates the port type of the SMHBA port.</p>
</dd>

### -field <b>PortState</b>

<dd>
<p>An integer that indicates the current state of the SMHBA port.</p>
</dd>

### -field <b>PortSpecificAttributesSize</b>

<dd></dd>

### -field <b>OSDeviceName</b>

<dd>
<p>A nonpersistent operating system target name, for example "\Device\HarddiskVolume1".</p>
</dd>

### -field <b>Reserved</b>

<dd></dd>

### -field <b>PortSpecificAttributes</b>

<dd></dd>
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
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>