---
UID: NE.sffdisk.SFFDISK_DCMD
title: SFFDISK_DCMD
author: windows-driver-content
description: The SFFDISK_DCMD enumeration identifies the type of Secure Digital (SD) card operation.
old-location: sd\sffdisk_dcmd.htm
old-project: SD
ms.assetid: 145e460e-6988-4e61-bb33-6f1b1df54629
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SERCX_BUFFER_DESCRIPTOR,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sffdisk.h
req.include-header: Sffdisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SFFDISK_DCMD
req.alt-loc: sffdisk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level.
req.iface: 
req.product: Windows 10 or later.
---

# SFFDISK_DCMD enumeration



## -description
<p>The SFFDISK_DCMD enumeration identifies the type of Secure Digital (SD) card operation.</p>


## -syntax

````
typedef enum  { 
  SFFDISK_DC_GET_VERSION     = 0,
  SFFDISK_DC_LOCK_CHANNEL    = 1,
  SFFDISK_DC_UNLOCK_CHANNEL  = 2,
  SFFDISK_DC_DEVICE_COMMAND  = 3
} SFFDISK_DCMD;
````


## -enum-fields
<dl>

### -field <a id="SFFDISK_DC_GET_VERSION"></a><a id="sffdisk_dc_get_version"></a><b>SFFDISK_DC_GET_VERSION</b>

<dd>
<p>The operations retrieves the version of the card.</p>
</dd>

### -field <a id="SFFDISK_DC_LOCK_CHANNEL"></a><a id="sffdisk_dc_lock_channel"></a><b>SFFDISK_DC_LOCK_CHANNEL</b>

<dd>
<p>The operation locks the interface channel.</p>
</dd>

### -field <a id="SFFDISK_DC_UNLOCK_CHANNEL"></a><a id="sffdisk_dc_unlock_channel"></a><b>SFFDISK_DC_UNLOCK_CHANNEL</b>

<dd>
<p>The operation unlocks the interface channel.</p>
</dd>

### -field <a id="SFFDISK_DC_DEVICE_COMMAND"></a><a id="sffdisk_dc_device_command"></a><b>SFFDISK_DC_DEVICE_COMMAND</b>

<dd>
<p>The operation executes a device command.</p>
</dd>
</dl>

## -remarks
<p>Applications that submit IOCTL_SFFDISK_DEVICE_COMMAND requests to the SD stack use this enumeration to specify the type of operation. The application must assign one of the values of this enumeration to the <b>Command</b> member of the <a href="https://msdn.microsoft.com/68205c17-5ff6-45a3-83c7-e106b314f9a5">SFFDISK_DEVICE_COMMAND_DATA</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sffdisk.h (include Sffdisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/68205c17-5ff6-45a3-83c7-e106b314f9a5">SFFDISK_DEVICE_COMMAND_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SD\buses]:%20SFFDISK_DCMD enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
