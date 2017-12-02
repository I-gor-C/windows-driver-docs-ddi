---
UID: NS.ntddcdrm._VOLUME_CONTROL
title: VOLUME_CONTROL
author: windows-driver-content
description: The VOLUME_CONTROL structure is used in conjunction with the IOCTL_CDROM_GET_VOLUME request to retrieve volume values for up to four audio ports.
old-location: storage\volume_control.htm
old-project: storage
ms.assetid: 47512360-60fe-43f2-8052-58ca78e36d86
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: VOLUME_CONTROL, VOLUME_CONTROL, *PVOLUME_CONTROL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VOLUME_CONTROL
req.alt-loc: ntddcdrm.h
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

# VOLUME_CONTROL structure



## -description
<p>The VOLUME_CONTROL structure is used in conjunction with the <a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-get-volume.md">IOCTL_CDROM_GET_VOLUME</a> request to retrieve volume values for up to four audio ports.</p>


## -syntax

````
typedef struct _VOLUME_CONTROL {
  UCHAR PortVolume[4];
} VOLUME_CONTROL, *PVOLUME_CONTROL;
````


## -struct-fields
<dl>

### -field PortVolume

<dd>
<p>Pointer to an array of volume values, one for each of the ports, with a maximum of four ports. </p>
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
<a href="..\ntddcdrm\ni-ntddcdrm-ioctl-cdrom-get-volume.md">IOCTL_CDROM_GET_VOLUME</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20VOLUME_CONTROL structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
