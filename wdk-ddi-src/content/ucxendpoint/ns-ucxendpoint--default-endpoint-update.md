---
UID: NS.ucxendpoint._DEFAULT_ENDPOINT_UPDATE
title: DEFAULT_ENDPOINT_UPDATE
author: windows-driver-content
description: Contains the handle to the default endpoint to update in a framework request that is passed by UCX when it invokes EVT_UCX_DEFAULT_ENDPOINT_UPDATE callback function.
old-location: buses\_default_endpoint_update.htm
old-project: usbref
ms.assetid: 3E85D9AE-F8D3-4763-B1A2-51F95D00422D
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: DEFAULT_ENDPOINT_UPDATE, DEFAULT_ENDPOINT_UPDATE, *PDEFAULT_ENDPOINT_UPDATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxendpoint.h
req.include-header: Ucxclass.h, Ucxendpoint.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEFAULT_ENDPOINT_UPDATE
req.alt-loc: ucxendpoint.h
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
req.product: Windows 10 or later.
---

# DEFAULT_ENDPOINT_UPDATE structure



## -description
<p>Contains the handle to the default endpoint to update in a framework request that is passed by UCX when it invokes <a href="https://msdn.microsoft.com/library/windows/hardware/mt187824">EVT_UCX_DEFAULT_ENDPOINT_UPDATE</a> callback function.</p>


## -syntax

````
typedef struct _DEFAULT_ENDPOINT_UPDATE {
#if __cplusplus
  USBDEVICE_MGMT_HEADER Header;
#else 
  USBDEVICE_MGMT_HEADER ;
#endif 
  UCXENDPOINT           DefaultEndpoint;
  ULONG                 MaxPacketSize;
} DEFAULT_ENDPOINT_UPDATE, *P_DEFAULT_ENDPOINT_UPDATE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt188075">USBDEVICE_MGMT_HEADER</a> structure that contains header information related to the USB device or hub endpoint.</p>
</dd>

### -field <b>DefaultEndpoint</b>

<dd>
<p>A handle to the  default endpoint to update.</p>
</dd>

### -field <b>MaxPacketSize</b>

<dd>
<p>The maximum packet size of the default endpoint.</p>
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
<dt>Ucxendpoint.h (include Ucxclass.h or Ucxendpoint.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187824">EVT_UCX_DEFAULT_ENDPOINT_UPDATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20DEFAULT_ENDPOINT_UPDATE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
