---
UID: NE.ehstorioctl._PDO_TYPE
title: PDO_TYPE
author: windows-driver-content
description: This enumeration describes the types of Physical Device Objects (PDOs).
old-location: storage\pdo_type.htm
old-project: storage
ms.assetid: 9695d55c-a214-4bba-aba9-38dfa7f54ec9
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SET_BAND_SECURITY_PARAMETERS, SET_BAND_SECURITY_PARAMETERS, *PSET_BAND_SECURITY_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ehstorioctl.h
req.include-header: EhStorIoctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PDO_TYPE
req.alt-loc: EhStorIoctl.h
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

# PDO_TYPE enumeration



## -description
<p>This enumeration describes the types of Physical Device Objects (PDOs).</p>


## -syntax

````
typedef enum _PDO_TYPE { 
  PDO_TYPE_UNDEFINED  = 0,
  PDO_TYPE_DISK       = 1,
  PDO_TYPE_CONTROL    = 2,
  PDO_TYPE_SILO       = 3,
  PDO_TYPE_THIS       = 256
} PDO_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PDO_TYPE_UNDEFINED"></a><a id="pdo_type_undefined"></a><b>PDO_TYPE_UNDEFINED</b>

<dd>
<p>Types either enumerated or provided as filter parameter to <a href="..\ehstorioctl\ni-ehstorioctl-ioctl-ehstor-device-enumerate-pdos.md">IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS</a>
</p>
</dd>

### -field <a id="PDO_TYPE_DISK"></a><a id="pdo_type_disk"></a><b>PDO_TYPE_DISK</b>

<dd>
<p>This value indicates the PDO is for a logical disk device.</p>
</dd>

### -field <a id="PDO_TYPE_CONTROL"></a><a id="pdo_type_control"></a><b>PDO_TYPE_CONTROL</b>

<dd>
<p>This value indicates the PDO is for a logical control device.</p>
</dd>

### -field <a id="PDO_TYPE_SILO"></a><a id="pdo_type_silo"></a><b>PDO_TYPE_SILO</b>

<dd>
<p>This value indicates the PDO is for a logical silo device.</p>
</dd>

### -field <a id="PDO_TYPE_THIS"></a><a id="pdo_type_this"></a><b>PDO_TYPE_THIS</b>

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
<dt>EhStorIoctl.h (include EhStorIoctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ehstorioctl\ni-ehstorioctl-ioctl-ehstor-device-enumerate-pdos.md">IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20PDO_TYPE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
