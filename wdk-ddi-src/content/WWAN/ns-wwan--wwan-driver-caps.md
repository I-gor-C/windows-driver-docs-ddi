---
UID: NS.wwan._WWAN_DRIVER_CAPS
title: WWAN_DRIVER_CAPS
author: windows-driver-content
description: The WWAN_DRIVER_CAPS structure represents the capabilities of the miniport driver.
old-location: netvista\wwan_driver_caps.htm
ms.assetid: c0696ac6-d35e-402a-8cb5-d4f23b3b8072
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: WWAN_DRIVER_CAPS, WWAN_DRIVER_CAPS, *PWWAN_DRIVER_CAPS
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_DRIVER_CAPS structure



## -description
<p>The WWAN_DRIVER_CAPS structure represents the capabilities of the miniport driver.</p>


## -syntax

````
typedef struct _WWAN_DRIVER_CAPS {
  ULONG ulMajorVersion;
  ULONG ulMinorVersion;
  ULONG ulDriverCaps;
} WWAN_DRIVER_CAPS, *PWWAN_DRIVER_CAPS;
````


## -struct-fields
<dl>

### -field <b>ulMajorVersion</b>

<dd>
<p>The major version of the MB driver model that the miniport driver supports. Miniport drivers
     should set this member to WWAN_MAJOR_VERSION.</p>
</dd>

### -field <b>ulMinorVersion</b>

<dd>
<p>The minor version of the MB driver model that the miniport driver supports. Miniport drivers
     should set this member to WWAN_MINOR_VERSION.</p>
</dd>

### -field <b>ulDriverCaps</b>

<dd>
<p>This member is reserved for future use. Miniport drivers should set this member to the value in
     the following table.
     </p>
<p></p>
<dl>

### -field <a id="WWAN_DRIVER_CAPS_NONE"></a><a id="wwan_driver_caps_none"></a>WWAN_DRIVER_CAPS_NONE

<dd>
<p>The miniport driver has no special capabilities.</p>
</dd>
</dl>
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
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567908">NDIS_WWAN_DRIVER_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_DRIVER_CAPS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
