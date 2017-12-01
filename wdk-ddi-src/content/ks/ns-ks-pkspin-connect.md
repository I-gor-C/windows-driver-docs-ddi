---
UID: NS.ks.PKSPIN_CONNECT
title: PKSPIN_CONNECT
author: windows-driver-content
description: Clients use the KSPIN_CONNECT structure to describe the connection they request from a driver in a KsCreatePin call.
old-location: stream\kspin_connect.htm
old-project: stream
ms.assetid: 62ce7a36-87ce-40d1-bdd4-8a4f4bc60b00
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPIN_CONNECT, KSPIN_CONNECT, *PKSPIN_CONNECT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPIN_CONNECT
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
req.iface: 
---

# PKSPIN_CONNECT structure



## -description
<p>Clients use the KSPIN_CONNECT structure to describe the connection they request from a driver in a <a href="..\ks\nf-ks-kscreatepin.md">KsCreatePin</a> call.</p>


## -syntax

````
typedef struct {
  KSPIN_INTERFACE Interface;
  KSPIN_MEDIUM    Medium;
  ULONG           PinId;
  HANDLE          PinToHandle;
  KSPRIORITY      Priority;
} KSPIN_CONNECT, *PKSPIN_CONNECT;
````


## -struct-fields
<dl>

### -field <b>Interface</b>

<dd>
<p>Specifies the <a href="stream.kspin_interface">KSPIN_INTERFACE</a> to use for this connection. </p>
</dd>

### -field <b>Medium</b>

<dd>
<p>A structure of type <a href="stream.kspin_medium">KSPIN_MEDIUM</a> that specifies the medium to use for this connection. </p>
</dd>

### -field <b>PinId</b>

<dd>
<p>Specifies the pin type ID number. If the PinToHandle field is not <b>NULL</b>, this field contains the identifier of the source pin to which the request is being sent. Otherwise this field refers to the sink pin that is being connected to. If a pin can support being both a source and sink in communications, then this is the implicit method of telling it how it should act in the connection.</p>
</dd>

### -field <b>PinToHandle</b>

<dd>
<p>Specifies what type of destination pin the create is intended for, and in the case of a source destination, what pin to connect to. This member is <b>NULL</b> when a client requests a connection to itself. Otherwise, it is the target of the connection request. In the case of a source destination, this contains the handle of the pin instance to establish a connection to. In the case of a sink destination, this field contains <b>NULL</b>, and is not otherwise used. </p>
</dd>

### -field <b>Priority</b>

<dd>
<p>A structure of type <a href="stream.kspriority">KSPRIORITY</a> that specifies the priority for the connection, usually KSPRIORITY_NORMAL. See the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565104">KSPROPERTY_CONNECTION_PRIORITY</a> property for details.</p>
</dd>
</dl>

## -remarks
<p>If the KSPIN_CONNECT.PinToHandle element is not <b>NULL</b>, IRP_MJ_CREATE instructs the device to connect the source KSPIN_CONNECT.PinId pin to the KSPIN_CONNECT.PinToHandle pin instance. Otherwise, this is a request from a client for connection to the KSPIN_CONNECT.PinId pin using the KSPIN_CONNECT.Medium method and a specific data format specified after the connection structure. In either case, the device driver may fail this request if this connection cannot be accepted.</p>

## -requirements
<table>
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
<a href="..\ks\nf-ks-kscreatepin.md">KsCreatePin</a>
</dt>
<dt>
<a href="stream.kspin_interface">KSPIN_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565104">KSPROPERTY_CONNECTION_PRIORITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPIN_CONNECT structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
