---
UID: NS.WWAN._WWAN_DRIVER_CAPS
title: _WWAN_DRIVER_CAPS
author: windows-driver-content
description: The WWAN_DRIVER_CAPS structure represents the capabilities of the miniport driver.
old-location: netvista\wwan_driver_caps.htm
old-project: netvista
ms.assetid: c0696ac6-d35e-402a-8cb5-d4f23b3b8072
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _WWAN_DRIVER_CAPS, WWAN_DRIVER_CAPS, *PWWAN_DRIVER_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_DRIVER_CAPS
req.alt-loc: wwan.h
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
req.product: Windows 10 or later.
---

# _WWAN_DRIVER_CAPS structure



## -description
The WWAN_DRIVER_CAPS structure represents the capabilities of the miniport driver.



## -syntax

````
typedef struct _WWAN_DRIVER_CAPS {
  ULONG ulMajorVersion;
  ULONG ulMinorVersion;
  ULONG ulDriverCaps;
} WWAN_DRIVER_CAPS, *PWWAN_DRIVER_CAPS;
````


## -struct-fields

### -field ulMajorVersion

The major version of the MB driver model that the miniport driver supports. Miniport drivers
     should set this member to WWAN_MAJOR_VERSION.


### -field ulMinorVersion

The minor version of the MB driver model that the miniport driver supports. Miniport drivers
     should set this member to WWAN_MINOR_VERSION.


### -field ulDriverCaps

This member is reserved for future use. Miniport drivers should set this member to the value in
     the following table.
     




### -field WWAN_DRIVER_CAPS_NONE

The miniport driver has no special capabilities.

</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 7 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndis_wwan_driver_caps">NDIS_WWAN_DRIVER_CAPS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_DRIVER_CAPS structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

