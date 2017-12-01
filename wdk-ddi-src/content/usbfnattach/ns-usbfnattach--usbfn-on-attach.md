---
UID: NS.usbfnattach._USBFN_ON_ATTACH
title: USBFN_ON_ATTACH
author: windows-driver-content
description: Describes the detected port type and attach action.
old-location: buses\usbfn_on_attach.htm
old-project: usbref
ms.assetid: 2CD75FA9-F77E-4AC5-870E-69CF05DB9312
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_ON_ATTACH, USBFN_ON_ATTACH, *PUSBFN_ON_ATTACH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbfnattach.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_ON_ATTACH
req.alt-loc: usbfnattach.h
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
req.product: Windows 10 or later.
---

# USBFN_ON_ATTACH structure



## -description
<p>Describes the detected port type and attach action. </p>


## -syntax

````
typedef struct _USBFN_ON_ATTACH {
  USBFN_PORT_TYPE     PortType;
  USBFN_ATTACH_ACTION AttachAction;
} USBFN_ON_ATTACH, *PUSBFN_ON_ATTACH;
````


## -struct-fields
<dl>

### -field <b>PortType</b>

<dd>
<p>Detected port type defined by one of the <a href="buses.usbfn_port_type">USBFN_PORT_TYPE</a>-typed values.</p>
</dd>

### -field <b>AttachAction</b>

<dd>
<p>The operation that must be performed depending on the port type. This value is defined in the <a href="buses.usbfn_attach_action">USBFN_ATTACH_ACTION</a> enumeration.</p>
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
<dt>Usbfnattach.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usbfn_get_attach_action">USBFN_GET_ATTACH_ACTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBFN_ON_ATTACH structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
