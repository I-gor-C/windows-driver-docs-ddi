---
UID: NS.wwan._WWAN_SUPPORTED_DEVICE_SERVICES
title: WWAN_SUPPORTED_DEVICE_SERVICES
author: windows-driver-content
description: The WWAN_SUPPORTED_DEVICE_SERVICES structure describes information about device services supported by the miniport driver.
old-location: netvista\wwan_supported_device_services.htm
ms.assetid: CFCF122F-E971-4A6B-91C9-71A8030366A9
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_SUPPORTED_DEVICE_SERVICES
req.alt-loc: wwan.h
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
ms.keywords: WWAN_SUPPORTED_DEVICE_SERVICES, WWAN_SUPPORTED_DEVICE_SERVICES, *PWWAN_SUPPORTED_DEVICE_SERVICES
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_SUPPORTED_DEVICE_SERVICES structure



## -description
<p>The WWAN_SUPPORTED_DEVICE_SERVICES structure describes information about device services supported by the miniport driver.</p>


## -syntax

````
typedef struct _WWAN_SUPPORTED_DEVICE_SERVICES {
  ULONG            uMaxCommandDataSize;
  ULONG            uMaxSessionDataSize;
  ULONG            uMaxSessionCount;
  WWAN_LIST_HEADER ListHeader;
} WWAN_SUPPORTED_DEVICE_SERVICES, *PWWAN_SUPPORTED_DEVICE_SERVICES;
````


## -struct-fields
<dl>

### -field <b>uMaxCommandDataSize</b>

<dd>
<p>The maximum size, in bytes, of data that can be associated with a device service command.</p>
</dd>

### -field <b>uMaxSessionDataSize</b>

<dd>
<p>The maximum size, in bytes, of data that can be associated with a device service session.</p>
</dd>

### -field <b>uMaxSessionCount</b>

<dd>
<p>The maximum number of device service sessions supported by the miniport driver.</p>
</dd>

### -field <b>ListHeader</b>

<dd>
<p>A formatted WWAN_LIST_HEADER object that represents a list of supported device services and the number of services  in the list.</p>
<p>This member points to the list of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh831870">WWAN_DEVICE_SERVICE_ENTRY</a> by using the WWAN_LIST_HEADER structure.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh831870">WWAN_DEVICE_SERVICE_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh831867">NDIS_WWAN_SUPPORTED_DEVICE_SERVICES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571208">WWAN_LIST_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SUPPORTED_DEVICE_SERVICES structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
