---
UID: NS.ntddmmc._GET_CONFIGURATION_HEADER
title: GET_CONFIGURATION_HEADER
author: windows-driver-content
description: The GET_CONFIGURATION_HEADER structure is used to format the output data retrieved by the IOCTL_CDROM_GET_CONFIGURATION request.
old-location: storage\get_configuration_header.htm
old-project: storage
ms.assetid: 8de19f1b-faca-4b27-9287-20edc12f2c83
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GET_CONFIGURATION_HEADER, GET_CONFIGURATION_HEADER, *PGET_CONFIGURATION_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GET_CONFIGURATION_HEADER
req.alt-loc: ntddmmc.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# GET_CONFIGURATION_HEADER structure



## -description
<p>The GET_CONFIGURATION_HEADER structure is used to format the output data retrieved by the <a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-get-configuration.md">IOCTL_CDROM_GET_CONFIGURATION</a> request. </p>


## -syntax

````
typedef struct _GET_CONFIGURATION_HEADER {
  UCHAR DataLength[4];
  UCHAR Reserved[2];
  UCHAR CurrentProfile[2];
  UCHAR Data[];
} GET_CONFIGURATION_HEADER, *PGET_CONFIGURATION_HEADER;
````


## -struct-fields
<dl>

### -field <b>DataLength</b>

<dd>
<p>Indicates the amount of data, in bytes, that is being returned in the buffer area pointed to by the <b>Data</b> member. If the data length is greater than 65,530 bytes, multiple GET CONFIGURATION commands will be required for the Initiator to read all configuration data. The bytes in this array are arranged in big-endian order. <b>DataLength</b>[0] has the most significant byte, and  <b>DataLength</b>[3] has the least significant byte.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>CurrentProfile</b>

<dd>
<p>Contains an enumerator value of type <a href="..\ntddmmc\ne-ntddmmc--feature-profile-type.md">FEATURE_PROFILE_TYPE</a> that indicates the device's current profile. The bytes in this array are arranged in big-endian order. <b>CurrentProfile</b>[0] has the most significant byte, and  <b>CurrentProfile</b>[3] has the least significant byte.</p>
</dd>

### -field <b>Data</b>

<dd>
<p>Contains the feature data, beginning with the <a href="..\ntddmmc\ns-ntddmmc--feature-header.md">FEATURE_HEADER</a>.</p>
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
<dt>Ntddmmc.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-get-configuration.md">IOCTL_CDROM_GET_CONFIGURATION</a>
</dt>
<dt>
<a href="..\ntddmmc\ns-ntddmmc--feature-header.md">FEATURE_HEADER</a>
</dt>
<dt>
<a href="..\ntddmmc\ne-ntddmmc--feature-number.md">FEATURE_NUMBER</a>
</dt>
<dt>
<a href="..\ntddmmc\ne-ntddmmc--feature-profile-type.md">FEATURE_PROFILE_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GET_CONFIGURATION_HEADER structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
