---
UID: NS.ucxendpoint._ENDPOINT_RESET
title: ENDPOINT_RESET
author: windows-driver-content
description: Describes information required to reset an endpoint. This structure is passed by UCX in the EVT_UCX_ENDPOINT_RESET callback function.
old-location: buses\_endpoint_reset.htm
old-project: usbref
ms.assetid: 99F65058-8718-4D2A-9C7F-D442BA8DA527
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: ENDPOINT_RESET, ENDPOINT_RESET, *PENDPOINT_RESET
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
req.alt-api: ENDPOINT_RESET
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

# ENDPOINT_RESET structure



## -description
<p>Describes information required to reset an endpoint. This structure is passed by UCX in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187828">EVT_UCX_ENDPOINT_RESET</a> callback function.</p>


## -syntax

````
typedef struct _ENDPOINT_RESET {
#if _cplusplus
  USBDEVICE_MGMT_HEADER Header;
#else 
  USBDEVICE_MGMT_HEADER ;
#endif 
  UCXENDPOINT           Endpoint;
  ENDPOINT_RESET_FLAGS  Flags;
} ENDPOINT_RESET, *P_ENDPOINT_RESET;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt188075">USBDEVICE_MGMT_HEADER</a> structure that stores handles to the USB hub or device whose endpoints.</p>
</dd>

### -field <b>Endpoint</b>

<dd>
<p>A handle to the device endpoint to reset.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt187817">ENDPOINT_RESET_FLAGS</a> value that indicates reset parameters.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187817">ENDPOINT_RESET_FLAGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20ENDPOINT_RESET structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
