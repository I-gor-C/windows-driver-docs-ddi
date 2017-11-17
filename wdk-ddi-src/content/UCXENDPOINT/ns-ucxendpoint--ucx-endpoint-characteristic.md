---
UID: NS.ucxendpoint._UCX_ENDPOINT_CHARACTERISTIC
title: UCX_ENDPOINT_CHARACTERISTIC
author: windows-driver-content
description: Stores the characteristics of an endpoint.
old-location: buses\ucx_endpoint_characteristic.htm
ms.assetid: 4785D94B-271C-4F8E-B95B-87401E32CE42
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: ucxendpoint.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_ENDPOINT_CHARACTERISTIC
req.alt-loc: Ucxendpoint.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: UCX_ENDPOINT_CHARACTERISTIC, UCX_ENDPOINT_CHARACTERISTIC, *PUCX_ENDPOINT_CHARACTERISTIC
req.iface: 
req.product: Windows 10 or later.
---

# UCX_ENDPOINT_CHARACTERISTIC structure



## -description
<p>Stores the characteristics of an endpoint. </p>


## -syntax

````
typedef struct _UCX_ENDPOINT_CHARACTERISTIC {
  ULONG                            Size;
  UCX_ENDPOINT_CHARACTERISTIC_TYPE CharacteristicType;
  union {
    UCX_CONTROLLER_ENDPOINT_CHARACTERISTIC_PRIORITY Priority;
  };
} UCX_ENDPOINT_CHARACTERISTIC, *PUCX_ENDPOINT_CHARACTERISTIC;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Size of this structure.</p>
</dd>

### -field <b>CharacteristicType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/1F49C8CA-51CE-49B2-AC37-C114A688B1DB">UCX_ENDPOINT_CHARACTERISTIC_TYPE</a>-type value that indicates the type of endpoint characteristic.</p>
</dd>

### -field <b>Priority</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/43031BE8-B94A-4B22-B9E2-CBF59A31F3A2">UCX_CONTROLLER_ENDPOINT_CHARACTERISTIC_PRIORITY</a>-typed value that indicates the priority of the endpoint.</p>
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
<dt>Ucxendpoint.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/4FA3F175-52E4-472D-A9B3-B3B4B37E1701">EVT_UCX_ENDPOINT_SET_CHARACTERISTIC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/43031BE8-B94A-4B22-B9E2-CBF59A31F3A2">UCX_CONTROLLER_ENDPOINT_CHARACTERISTIC_PRIORITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_ENDPOINT_CHARACTERISTIC structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
