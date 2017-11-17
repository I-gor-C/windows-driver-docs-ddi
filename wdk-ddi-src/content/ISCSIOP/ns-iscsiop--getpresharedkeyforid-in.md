---
UID: NS.iscsiop._GetPresharedKeyForId_IN
title: GetPresharedKeyForId_IN
author: windows-driver-content
description: The GetPresharedKeyForId_IN structure holds the input data for the GetPresharedKeyForId method.
old-location: storage\getpresharedkeyforid_in.htm
ms.assetid: 4b3d3c5d-c34c-4ed8-bf62-1d885442ee1e
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetPresharedKeyForId_IN
req.alt-loc: iscsiop.h
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
ms.keywords: GetPresharedKeyForId_IN, GetPresharedKeyForId_IN, *PGetPresharedKeyForId_IN
req.iface: 
---

# GetPresharedKeyForId_IN structure



## -description
<p>The GetPresharedKeyForId_IN structure holds the input data for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554970">GetPresharedKeyForId</a> method. This method is required if the initiator supports Internet Key Exchange (IKE). It can help to determine whether IKE identification payload is configured with a preshared key.</p>


## -syntax

````
typedef struct _GetPresharedKeyForId_IN {
  ULONG PortNumber;
  UCHAR IdType;
  ULONG IdSize;
  UCHAR Id[1];
} GetPresharedKeyForId_IN, *PGetPresharedKeyForId_IN;
````


## -struct-fields
<dl>

### -field <b>PortNumber</b>

<dd>
<p>The number of the port that the connection was made through. A value of -1 indicates that the connection can be made through any available port.</p>
</dd>

### -field <b>IdType</b>

<dd>
<p>The type of identifier that the initiator puts in the Internet Key Exchange (IKE) identification payload to identify itself to the target. </p>
<table>
<tr>
<th>Identification payload type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ID_IPV4_ADDR</p>
</td>
<td>
<p>The initiator identifies itself to the target during the key exchange with a single 4-byte version 4 IP address.</p>
</td>
</tr>
<tr>
<td>
<p>ID_FQDN</p>
</td>
<td>
<p>The initiator identifies itself to the target during the key exchange with a fully qualified domain name string (for example, "website.com"). </p>
</td>
</tr>
<tr>
<td>
<p>ID_USER_FQDN</p>
</td>
<td>
<p>The initiator identifies itself to the target during the key exchange with a fully qualified user name string (for example, "someone@example.com"). </p>
</td>
</tr>
<tr>
<td>
<p>ID_IPV6_ADDR</p>
</td>
<td>
<p>The initiator identifies itself to the target during the key exchange with a single 16-byte version 6 IP address.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>IdSize</b>

<dd>
<p>The size, in bytes, of the identifier in <b>Id</b><i>.</i></p>
</dd>

### -field <b>Id</b>

<dd>
<p>The identifier that the initiator uses to identify itself to the target during key exchange. </p>
</dd>
</dl>

## -remarks
<p>You must implement this method if the initiator supports IKE.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsiop.h (include Iscsiop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554970">GetPresharedKeyForId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554975">GetPresharedKeyForId_OUT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563135">MSiSCSI_SecurityConfigOperations WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20GetPresharedKeyForId_IN structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
