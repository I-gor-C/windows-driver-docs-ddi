---
UID: NS.kbdmou._CONNECT_DATA
title: CONNECT_DATA
author: windows-driver-content
description: CONNECT_DATA specifies information that Kbdclass and Mouclass use to connect to a keyboard or mouse port.
old-location: hid\connect_data__kbdclass_.htm
ms.assetid: 8fdb5b1d-bbdb-4774-875a-7cdd047286f5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: hid
req.header: kbdmou.h
req.include-header: Kbdmou.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CONNECT_DATA
req.alt-loc: kbdmou.h
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
ms.keywords: CONNECT_DATA, CONNECT_DATA, *PCONNECT_DATA
req.iface: 
---

# CONNECT_DATA structure



## -description
<p>CONNECT_DATA specifies information that Kbdclass and Mouclass use to connect to a keyboard or mouse port.</p>


## -syntax

````
typedef struct _CONNECT_DATA {
  PDEVICE_OBJECT ClassDeviceObject;
  PVOID          ClassService;
} CONNECT_DATA, *PCONNECT_DATA;
````


## -struct-fields
<dl>

### -field <b>ClassDeviceObject</b>

<dd>
<p>Pointer to an upper-level class <a href="wdkgloss.f#wdkgloss.filter_device_object#wdkgloss.filter_device_object"><i>filter device object</i></a> (filter DO).</p>
</dd>

### -field <b>ClassService</b>

<dd>
<p>Specifies the class service routine. See  <a href="https://msdn.microsoft.com/library/windows/hardware/ff542274">PSERVICE_CALLBACK_ROUTINE</a>.</p>
</dd>
</dl>

## -remarks
<p>The keyboard class driver uses this structure with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff541273">IOCTL_INTERNAL_KEYBOARD_CONNECT</a> request; the mouse class driver uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff541294">IOCTL_INTERNAL_MOUSE_CONNECT</a> .</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Kbdmou.h (include Kbdmou.h)</dt>
</dl>
</td>
</tr>
</table>