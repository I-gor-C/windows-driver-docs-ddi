---
UID: NS.bthioctl._BTH_LOCAL_RADIO_INFO
title: BTH_LOCAL_RADIO_INFO
author: windows-driver-content
description: The BTH_LOCAL_RADIO_INFO structure contains information about the local Bluetooth system and radio.
old-location: bltooth\bth_local_radio_info.htm
ms.assetid: 288863ca-1a11-456f-8d6b-b429668c2bf2
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: bltooth
req.header: bthioctl.h
req.include-header: Bthioctl.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BTH_LOCAL_RADIO_INFO
req.alt-loc: bthioctl.h
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
ms.keywords: BTH_LOCAL_RADIO_INFO, BTH_LOCAL_RADIO_INFO, *PBTH_LOCAL_RADIO_INFO
req.iface: 
---

# BTH_LOCAL_RADIO_INFO structure



## -description
<p>The BTH_LOCAL_RADIO_INFO structure contains information about the local Bluetooth system and
  radio.</p>


## -syntax

````
typedef struct _BTH_LOCAL_RADIO_INFO {
  BTH_DEVICE_INFO localInfo;
  ULONG           flags;
  USHORT          hciRevision;
  UCHAR           hciVersion;
  BTH_RADIO_INFO  radioInfo;
} BTH_LOCAL_RADIO_INFO, *PBTH_LOCAL_RADIO_INFO;
````


## -struct-fields
<dl>

### -field <b>localInfo</b>

<dd>
<p>A 
     <a href="http://go.microsoft.com/fwlink/p/?linkid=50713">BTH_DEVICE_INFO</a> structure that contains
     information about the local radio.</p>
</dd>

### -field <b>flags</b>

<dd>
<p>A flag that indicates the state of the local radio. Both flags can be set at the same time.
     Possible values include:
     </p>
<dl>
<dd>
<p>LOCAL_RADIO_DISCOVERABLE</p>
</dd>
<dd>
<p></p>
<p></p>
</dd>
<dd>
<p>LOCAL_RADIO_CONNECTABLE</p>
</dd>
</dl>
</dd>

### -field <b>hciRevision</b>

<dd>
<p>The minor version of the host controller interface (HCI).</p>
</dd>

### -field <b>hciVersion</b>

<dd>
<p>The major version of the HCI.</p>
</dd>

### -field <b>radioInfo</b>

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536646">BTH_RADIO_INFO</a> structure that contains
     information about the local radio device.</p>
</dd>
</dl>

## -remarks
<p>The 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff536684">IOCTL_BTH_GET_LOCAL_INFO</a> call's
    output buffer contains the information about the local Bluetooth system and radio.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows Vista, and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bthioctl.h (include Bthioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=50713">BTH_DEVICE_INFO</a></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536646">BTH_RADIO_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536684">IOCTL_BTH_GET_LOCAL_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20BTH_LOCAL_RADIO_INFO structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
