---
UID: NS.iscsiop._SetPresharedKeyForId_IN
title: SetPresharedKeyForId_IN
author: windows-driver-content
description: The SetPresharedKeyForId_IN structure holds the input data for the SetPresharedKeyForId method.
old-location: storage\setpresharedkeyforid_in.htm
old-project: storage
ms.assetid: f941bc28-f906-4399-be54-09e2bc12e443
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SetPresharedKeyForId_IN, SetPresharedKeyForId_IN, *PSetPresharedKeyForId_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetPresharedKeyForId_IN
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
req.iface: 
---

# SetPresharedKeyForId_IN structure



## -description
<p>The SetPresharedKeyForId_IN structure holds the input data for the <a href="storage.setpresharedkeyforid">SetPresharedKeyForId</a> method.</p>


## -syntax

````
typedef struct _SetPresharedKeyForId_IN {
  ULONG     PortNumber;
  ULONGLONG SecurityFlags;
  UCHAR     IdType;
  ULONG     IdSize;
  ULONG     KeySize;
  UCHAR     Id[1];
} SetPresharedKeyForId_IN, *PSetPresharedKeyForId_IN;
````


## -struct-fields
<dl>

### -field PortNumber

<dd>
<p>The number of the port that the initiator uses the preshared key with. A value of 0xffffffff indicates all ports.</p>
</dd>

### -field SecurityFlags

<dd>
<p>A bitwise OR of flags that indicate the security requirements of a target.  For a list of possible values for this member, see <a href="storage.security_flag_qualifiers">SECURITY_FLAG_QUALIFIERS</a>.</p>
</dd>

### -field IdType

<dd>
<p>The type of identifier to associate with the preshared key. The initiator puts this identifier (ID) in the Internet key exchange (IKE) identification payload to identify itself to the target. The following table describes the possible identification payload types.</p>
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
<p>The initiator identifies itself to the target during the key exchange with a fully qualified user name string (for example, "sample@example.com"). </p>
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

### -field IdSize

<dd>
<p>The size, in bytes, of the identifier in <b>Id</b><i>.</i></p>
</dd>

### -field KeySize

<dd>
<p>The size, in bytes, of the key in <b>Key</b><i>.</i></p>
</dd>

### -field Id

<dd>
<p>The ID to associate with the key. The initiator uses this ID to identify itself to the target during key exchange.</p>
</dd>
</dl>

## -remarks
<p>You must implement this method.</p>

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
<a href="storage.security_flag_qualifiers">SECURITY_FLAG_QUALIFIERS</a>
</dt>
<dt>
<a href="storage.setpresharedkeyforid">SetPresharedKeyForId</a>
</dt>
<dt>
<a href="..\iscsiop\ns-iscsiop--setpresharedkeyforid-out.md">SetPresharedKeyForId_OUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SetPresharedKeyForId_IN structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
