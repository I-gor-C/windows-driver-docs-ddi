---
UID: NS.usbfnbase._USBFN_CLASS_INTERFACE
title: USBFN_CLASS_INTERFACE
author: windows-driver-content
description: Describes an interface and its endpoints.
old-location: buses\usbfn_class_interface.htm
old-project: usbref
ms.assetid: D7173157-D532-4E71-A4E5-55A3B9626DB8
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_CLASS_INTERFACE, USBFN_CLASS_INTERFACE, *PUSBFN_CLASS_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbfnbase.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_CLASS_INTERFACE
req.alt-loc: usbfnbase.h
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

# USBFN_CLASS_INTERFACE structure



## -description
<p>Describes an interface and its endpoints.</p>


## -syntax

````
typedef struct _USBFN_CLASS_INTERFACE {
  UINT8                  InterfaceNumber;
  UINT8                  PipeCount;
  USBFN_PIPE_INFORMATION PipeArr[MAX_NUM_USBFN_PIPES];
} USBFN_CLASS_INTERFACE, *PUSBFN_CLASS_INTERFACE;
````


## -struct-fields
<dl>

### -field InterfaceNumber

<dd>
<p>The index number of the interface.</p>
</dd>

### -field PipeCount

<dd>
<p>The number of endpoints contained in  the interface.</p>
</dd>

### -field PipeArr

<dd>
<p>An array of <a href="..\usbfnbase\ns-usbfnbase--usbfn-pipe-information.md">USBFN_PIPE_INFORMATION</a> structures that describes the endpoints in the interface.</p>
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
<dt>Usbfnbase.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbfnbase\ns-usbfnbase--usbfn-pipe-information.md">USBFN_PIPE_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBFN_CLASS_INTERFACE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
