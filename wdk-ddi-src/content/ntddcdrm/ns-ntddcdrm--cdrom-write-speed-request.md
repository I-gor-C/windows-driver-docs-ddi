---
UID: NS.ntddcdrm._CDROM_WRITE_SPEED_REQUEST
title: CDROM_WRITE_SPEED_REQUEST
author: windows-driver-content
description: The CDROM_WRITE_SPEED_REQUEST structure is used as an input parameter to the IOCTL_CDROM_GET_PERFORMANCE IOCTL and for requesting write speed descriptors.
old-location: storage\cdrom_write_speed_request.htm
ms.assetid: A7F8AFAE-AFFA-4022-8C04-2BF9177FE9EB
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CDROM_WRITE_SPEED_REQUEST
req.alt-loc: Ntddcdrm.h
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
ms.keywords: CDROM_WRITE_SPEED_REQUEST, CDROM_WRITE_SPEED_REQUEST, *PCDROM_WRITE_SPEED_REQUEST
req.iface: 
---

# CDROM_WRITE_SPEED_REQUEST structure



## -description
<p>The <b>CDROM_WRITE_SPEED_REQUEST</b> structure is used as an input parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/gg441242">IOCTL_CDROM_GET_PERFORMANCE</a> IOCTL and for requesting write speed descriptors.</p>


## -syntax

````
typedef struct _CDROM_WRITE_SPEED_REQUEST {
  CDROM_PERFORMANCE_REQUEST_TYPE    RequestType;
} CDROM_WRITE_SPEED_REQUEST, *PCDROM_WRITE_SPEED_REQUEST;
````


## -struct-fields
<dl>

### -field <b>RequestType</b>

<dd>
<p>As defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/gg441234">CDROM_PERFORMANCE_REQUEST_TYPE</a>    enumeration.</p>
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
<dt>Ntddcdrm.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/gg441242">IOCTL_CDROM_GET_PERFORMANCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/gg441234">CDROM_PERFORMANCE_REQUEST_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20CDROM_WRITE_SPEED_REQUEST structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
