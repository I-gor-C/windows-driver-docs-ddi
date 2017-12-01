---
UID: NE.gnssdriver.GNSS_NI_NOTIFICATION_TYPE
title: GNSS_NI_NOTIFICATION_TYPE
author: windows-driver-content
description: GNSS_NI_NOTIFICATION_TYPE enumerates network-initialized (NI) notification types.
old-location: sensors\gnss_ni_notification_type.htm
old-project: sensors
ms.assetid: EC5FB722-F182-44A5-944C-ED81E43492AE
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_, FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_NI_NOTIFICATION_TYPE
req.alt-loc: gnssdriver.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# GNSS_NI_NOTIFICATION_TYPE enumeration



## -description
<p>GNSS_NI_NOTIFICATION_TYPE enumerates network-initialized (NI) notification types.</p>


## -syntax

````
typedef enum  { 
  GNSS_NI_NoNotifyNoVerify             = 0x01,
  GNSS_NI_NotifyOnly                   = 0x02,
  GNSS_NI_NotifyVerifyDefaultAllow     = 0x03,
  GNSS_NI_NotifyVerifyDefaultNotAllow  = 0x04,
  GNSS_NI_PrivacyOverride              = 0x05
} GNSS_NI_NOTIFICATION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="GNSS_NI_NoNotifyNoVerify"></a><a id="gnss_ni_nonotifynoverify"></a><a id="GNSS_NI_NONOTIFYNOVERIFY"></a><b>GNSS_NI_NoNotifyNoVerify</b>

<dd>
<p>No notification and no verification.</p>
</dd>

### -field <a id="GNSS_NI_NotifyOnly"></a><a id="gnss_ni_notifyonly"></a><a id="GNSS_NI_NOTIFYONLY"></a><b>GNSS_NI_NotifyOnly</b>

<dd>
<p>Notification only.</p>
</dd>

### -field <a id="GNSS_NI_NotifyVerifyDefaultAllow"></a><a id="gnss_ni_notifyverifydefaultallow"></a><a id="GNSS_NI_NOTIFYVERIFYDEFAULTALLOW"></a><b>GNSS_NI_NotifyVerifyDefaultAllow</b>

<dd>
<p>Notification and verification allowed on no answer.</p>
</dd>

### -field <a id="GNSS_NI_NotifyVerifyDefaultNotAllow"></a><a id="gnss_ni_notifyverifydefaultnotallow"></a><a id="GNSS_NI_NOTIFYVERIFYDEFAULTNOTALLOW"></a><b>GNSS_NI_NotifyVerifyDefaultNotAllow</b>

<dd>
<p>Notification and verification denied on no answer.</p>
</dd>

### -field <a id="GNSS_NI_PrivacyOverride"></a><a id="gnss_ni_privacyoverride"></a><a id="GNSS_NI_PRIVACYOVERRIDE"></a><b>GNSS_NI_PrivacyOverride</b>

<dd>
<p>Privacy override.</p>
<p>This is used for preventing notification and verification without leaving any traces of a performed position fix or position fix attempt.</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>