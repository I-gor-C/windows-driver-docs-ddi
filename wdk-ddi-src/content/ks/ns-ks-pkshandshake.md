---
UID: NS.ks.PKSHANDSHAKE
title: PKSHANDSHAKE
author: windows-driver-content
description: The KSHANDSHAKE structure is used to pass information back and forth while pins are handshaking in an attempt to negotiate a private interface.
old-location: stream\kshandshake.htm
ms.assetid: fe163d23-0eaf-4a3e-b371-2f65f2235251
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSHANDSHAKE
req.alt-loc: ks.h
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
ms.keywords: PKSHANDSHAKE, KSHANDSHAKE, *PKSHANDSHAKE
req.iface: 
---

# PKSHANDSHAKE structure



## -description
<p>The KSHANDSHAKE structure is used to pass information back and forth while pins are handshaking in an attempt to negotiate a private interface.</p>


## -syntax

````
typedef struct {
  GUID  ProtocolId;
  PVOID Argument1;
  PVOID Argument2;
} KSHANDSHAKE, *PKSHANDSHAKE;
````


## -struct-fields
<dl>

### -field <b>ProtocolId</b>

<dd>
<p>This member specifies the GUID that represents the interface or protocol being negotiated between two AVStream pins.</p>
</dd>

### -field <b>Argument1</b>

<dd>
<p>A pointer to an interface-dependent argument. Most often, this is used to pass back and forth COM-style interface pointers once a specific private interface or protocol has been agreed upon. </p>
</dd>

### -field <b>Argument2</b>

<dd>
<p>A pointer to an interface-dependent argument.</p>
</dd>
</dl>

## -remarks
<p>See <a href="https://msdn.microsoft.com/library/windows/hardware/ff563519">KsPinHandshake</a> for more information about negotiating private interfaces between AVStream pins.</p>

<p>Pin handshaking is a concept that is usable only between two pins that support IOCTL_KS_HANDSHAKE. Currently, only AVStream pins support this interface; thus this is only useful for negotiating private interfaces between two AVStream pins. Currently, connections between AVStream pins are negotiated via this mechanism.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563519">KsPinHandshake</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560813">IOCTL_KS_HANDSHAKE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSHANDSHAKE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
