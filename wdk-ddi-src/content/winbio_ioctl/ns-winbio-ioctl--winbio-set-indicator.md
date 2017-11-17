---
UID: NS.winbio_ioctl._WINBIO_SET_INDICATOR
title: WINBIO_SET_INDICATOR
author: windows-driver-content
description: The WINBIO_SET_INDICATOR structure is the IN payload for IOCTL_BIOMETRIC_SET_INDICATOR.
old-location: biometric\winbio_set_indicator.htm
ms.assetid: c4410845-3c7b-445e-80ec-25694b122a0e
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: biometric
req.header: winbio_ioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WINBIO_SET_INDICATOR
req.alt-loc: winbio_ioctl.h
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
ms.keywords: WINBIO_SET_INDICATOR, WINBIO_SET_INDICATOR, *PWINBIO_SET_INDICATOR
req.iface: 
req.product: Windows 10 or later.
---

# WINBIO_SET_INDICATOR structure



## -description
<p>The WINBIO_SET_INDICATOR structure is the IN payload for <a href="https://msdn.microsoft.com/library/windows/hardware/ff536441">IOCTL_BIOMETRIC_SET_INDICATOR</a>.</p>


## -syntax

````
typedef struct _WINBIO_SET_INDICATOR {
  DWORD                   PayloadSize;
  WINBIO_INDICATOR_STATUS IndicatorStatus;
} WINBIO_SET_INDICATOR, *PWINBIO_SET_INDICATOR;
````


## -struct-fields
<dl>

### -field <b>PayloadSize</b>

<dd>
<p>Specifies the total size of the payload, which includes the fixed length structure and any variable data at the end.</p>
</dd>

### -field <b>IndicatorStatus</b>

<dd>
<p>Specifies a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536472">WINBIO_INDICATOR_STATUS</a> that indicates whether the indicator light should be set on or off.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winbio_ioctl.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536471">WINBIO_GET_INDICATOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536441">IOCTL_BIOMETRIC_SET_INDICATOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [biometric\biometric]:%20WINBIO_SET_INDICATOR structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
