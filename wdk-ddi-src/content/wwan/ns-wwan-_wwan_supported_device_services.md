---
UID: NS.WWAN._WWAN_SUPPORTED_DEVICE_SERVICES
title: _WWAN_SUPPORTED_DEVICE_SERVICES
author: windows-driver-content
description: The WWAN_SUPPORTED_DEVICE_SERVICES structure describes information about device services supported by the miniport driver.
old-location: netvista\wwan_supported_device_services.htm
old-project: netvista
ms.assetid: CFCF122F-E971-4A6B-91C9-71A8030366A9
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _WWAN_SUPPORTED_DEVICE_SERVICES, WWAN_SUPPORTED_DEVICE_SERVICES, *PWWAN_SUPPORTED_DEVICE_SERVICES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
req.product: Windows 10 or later.
---

# _WWAN_SUPPORTED_DEVICE_SERVICES structure



## -description
The WWAN_SUPPORTED_DEVICE_SERVICES structure describes information about device services supported by the miniport driver.



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

### -field uMaxCommandDataSize

The maximum size, in bytes, of data that can be associated with a device service command.


### -field uMaxSessionDataSize

The maximum size, in bytes, of data that can be associated with a device service session.


### -field uMaxSessionCount

The maximum number of device service sessions supported by the miniport driver.


### -field ListHeader

A formatted WWAN_LIST_HEADER object that represents a list of supported device services and the number of services  in the list.

This member points to the list of the <a href="netvista.wwan_device_service_entry">WWAN_DEVICE_SERVICE_ENTRY</a> by using the WWAN_LIST_HEADER structure.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported starting with  Windows 8.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="netvista.wwan_device_service_entry">WWAN_DEVICE_SERVICE_ENTRY</a>
</dt>
<dt>
<a href="netvista.ndis_wwan_supported_device_services">NDIS_WWAN_SUPPORTED_DEVICE_SERVICES</a>
</dt>
<dt>
<a href="netvista.wwan_list_header">WWAN_LIST_HEADER</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SUPPORTED_DEVICE_SERVICES structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

