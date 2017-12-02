---
UID: NS.hwnclx._CLIENT_DEVICE_INFORMATION
title: CLIENT_DEVICE_INFORMATION
author: windows-driver-content
description: The CLIENT_DEVICE_INFORMATION structure is used by the hardware notification callback HWN_CLIENT_QUERY_DEVICE_INFORMATION to return the total number of hardware notifications that the client device driver provides.
old-location: gpiobtn\_client_device_information.htm
old-project: gpiobtn
ms.assetid: ae438f89-27b7-423f-9f82-b103ba70b7b5
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: CLIENT_DEVICE_INFORMATION, CLIENT_DEVICE_INFORMATION, *PCLIENT_DEVICE_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hwnclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CLIENT_DEVICE_INFORMATION
req.alt-loc: Hwnclx.h
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

# CLIENT_DEVICE_INFORMATION structure



## -description
<p>
<p>The <b>CLIENT_DEVICE_INFORMATION</b> structure is used by the hardware notification callback <a href="..\hwnclx\nc-hwnclx-hwn-client-query-device-information.md">HWN_CLIENT_QUERY_DEVICE_INFORMATION</a> to return the total number of hardware notifications that the client device driver provides.</p>
</p>
<p>The <b>CLIENT_DEVICE_INFORMATION</b> structure is used by the hardware notification callback <a href="..\hwnclx\nc-hwnclx-hwn-client-query-device-information.md">HWN_CLIENT_QUERY_DEVICE_INFORMATION</a> to return the total number of hardware notifications that the client device driver provides.</p>


## -syntax

````
typedef struct _CLIENT_DEVICE_INFORMATION {
  USHORT  Version;
  USHORT  Size;
  USHORT  TotalHwNs;
} CLIENT_DEVICE_INFORMATION, CLIENT_DEVICE_INFORMATION;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>Specifies the version number of this structure. This value must be provided by the client driver to the class extension. The class extension is responsible for verifying that this version is supported. The hardware notification payload version number is <b>HWN_DEVICE_INFORMATION_VERSION</b>. </p>
</dd>

### -field Size

<dd>
<p>The size, in bytes, of the <b>CLIENT_DEVICE_INFORMATION</b> data structure.</p>
</dd>

### -field TotalHwNs

<dd>
<p>The total number of hardware notifications that the client device driver provides.</p>
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
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
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
<dt>Hwnclx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn789335">Hardware notifications support</a></dt>
<dt>
<a href="gpiobtn.hardware_notifications_reference">Hardware notifications reference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [gpiobtn\gpiobtn]:%20CLIENT_DEVICE_INFORMATION structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
