---
UID: NE.wwan._WWAN_DEVICE_SERVICE_SESSION_STATE
title: WWAN_DEVICE_SERVICE_SESSION_STATE
author: windows-driver-content
description: The WWAN_DEVICE_SERVICE_SESSION_STATE enumeration specifies the state of device service session. It can be used in a set operation to set the state of a session or can be used in an indication to report the state of a session.
old-location: netvista\wwan_device_service_session_state.htm
ms.assetid: E2527150-2F62-4729-BC6A-FE6027BCCA35
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_DEVICE_SERVICE_SESSION_STATE
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
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_DEVICE_SERVICE_SESSION_STATE enumeration



## -description
<p>The WWAN_DEVICE_SERVICE_SESSION_STATE enumeration specifies the state of device service session. It can be used in a set operation to set the state of a session or can be used in an indication to report the state of a session.</p>


## -syntax

````
typedef enum _WWAN_DEVICE_SERVICE_SESSION_STATE { 
  WwanDeviceServiceSessionOpen    = 0x01,
  WwanDeviceServiceSessionClosed  = 0x02
} WWAN_DEVICE_SERVICE_SESSION_STATE;
````


## -enum-fields
<dl>

### -field <a id="WwanDeviceServiceSessionOpen"></a><a id="wwandeviceservicesessionopen"></a><a id="WWANDEVICESERVICESESSIONOPEN"></a><b>WwanDeviceServiceSessionOpen</b>

<dd>
<p>The device service session is closed or should be closed.</p>
</dd>

### -field <a id="WwanDeviceServiceSessionClosed"></a><a id="wwandeviceservicesessionclosed"></a><a id="WWANDEVICESERVICESESSIONCLOSED"></a><b>WwanDeviceServiceSessionClosed</b>

<dd>
<p>The device service session is open or should be opened.</p>
</dd>
</dl>

## -remarks
<p>The WWAN_DEVICE_SERVICE_SESSION structure uses the WWAN_DEVICE_SERVICE_SESSION_STATE enumeration to set or report the state of a session.</p>

<p>The WWAN_DEVICE_SERVICE_SESSION structure uses the WWAN_DEVICE_SERVICE_SESSION_STATE enumeration to set or report the state of a session.</p>

<p>The WWAN_DEVICE_SERVICE_SESSION structure uses the WWAN_DEVICE_SERVICE_SESSION_STATE enumeration to set or report the state of a session.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh831873">WWAN_DEVICE_SERVICE_SESSION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_DEVICE_SERVICE_SESSION_STATE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
