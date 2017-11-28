---
UID: NS.usbscan._USBSCAN_TIMEOUT
title: USBSCAN_TIMEOUT
author: windows-driver-content
description: The USBSCAN_TIMEOUT structure stores time-out values for USB bulk IN and bulk OUT operations, and interrupts.
old-location: image\usbscan_timeout.htm
old-project: image
ms.assetid: afa900fc-7297-425b-8308-18806d7d97d3
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: USBSCAN_TIMEOUT, USBSCAN_TIMEOUT, *PUSBSCAN_TIMEOUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbscan.h
req.include-header: Usbscan.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBSCAN_TIMEOUT
req.alt-loc: usbscan.h
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
req.iface: 
req.product: Windows 10 or later.
---

# USBSCAN_TIMEOUT structure



## -description
<p>The USBSCAN_TIMEOUT structure stores time-out values for USB bulk IN and bulk OUT operations, and interrupts.</p>


## -syntax

````
typedef struct _USBSCAN_TIMEOUT {
  ULONG TimeoutRead;
  ULONG TimeoutWrite;
  ULONG TimeoutEvent;
} USBSCAN_TIMEOUT, *PUSBSCAN_TIMEOUT;
````


## -struct-fields
<dl>

### -field <b>TimeoutRead</b>

<dd>
<p>Specifies the number of seconds to wait for a read operation to time out.</p>
</dd>

### -field <b>TimeoutWrite</b>

<dd>
<p>Specifies the number of seconds to wait for a write operation to time out.</p>
</dd>

### -field <b>TimeoutEvent</b>

<dd>
<p>Specifies the number of seconds to wait for an interrupt to occur.</p>
</dd>
</dl>

## -remarks
<p>A value of zero means to wait forever for the read or write operation or interrupt.</p>

<p>The USBSCAN_TIMEOUT structure is used as a parameter to <a href="base.deviceiocontrol">DeviceIoControl</a>, when the specified I/O control code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff542908">IOCTL_SET_TIMEOUT</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbscan.h (include Usbscan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542908">IOCTL_SET_TIMEOUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20USBSCAN_TIMEOUT structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
