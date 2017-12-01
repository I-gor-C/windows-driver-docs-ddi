---
UID: NS.usbsidebandaudio._USBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR
title: USBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR
author: windows-driver-content
description: TBD.
old-location: audio\usbsidebandaudio_endpoint_descriptor.htm
old-project: audio
ms.assetid: 552986F7-AEE9-4CBF-A932-629885F99487
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: USBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR, USBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR, *PUSBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbsidebandaudio.h
req.include-header: Usbsidebandaudio.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR
req.alt-loc: 
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

# USBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>TBD</p>


## -syntax

````
typedef struct _USBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR {
  ULONG                                   Reserved 0;
  GUID                                    Reserved 1;
  KSPIN_DATAFLOW                          Reserved 2;
   USBSIDEBANDAUDIO_ENDPOINT_CAPABILITIES Reserved 3;
  UNICODE_STRING                          Reserved 4;
  ULONG                                   Reserved 5;
  ULONG                                   Reserved 6;
} USBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR, *PUSBSIDEBANDAUDIO_ENDPOINT_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Reserved 0</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Reserved 1</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Reserved 2</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Reserved 3</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Reserved 4</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Reserved 5</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Reserved 6</b>

<dd>
<p>TBD</p>
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
<dt>Usbsidebandaudio.h (include Usbsidebandaudio.h)</dt>
</dl>
</td>
</tr>
</table>