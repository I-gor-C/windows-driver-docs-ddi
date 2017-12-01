---
UID: NS.bthioctl._BTH_RADIO_INFO
title: BTH_RADIO_INFO
author: windows-driver-content
description: The BTH_RADIO_INFO structure contains information about a remote radio.
old-location: bltooth\bth_radio_info.htm
old-project: bltooth
ms.assetid: 24e28912-13d1-460f-8d32-78bb3715adc6
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: BTH_RADIO_INFO, BTH_RADIO_INFO, *PBTH_RADIO_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthioctl.h
req.include-header: Bthioctl.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BTH_RADIO_INFO
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
req.iface: 
---

# BTH_RADIO_INFO structure



## -description
<p>The BTH_RADIO_INFO structure contains information about a remote radio.</p>


## -syntax

````
typedef struct _BTH_RADIO_INFO {
  ULONGLONG lmpSupportedFeatures;
  USHORT    mfg;
  USHORT    lmpSubversion;
  UCHAR     lmpVersion;
} BTH_RADIO_INFO, *PBTH_RADIO_INFO;
````


## -struct-fields
<dl>

### -field <b>lmpSupportedFeatures</b>

<dd>
<p>A bitmap of Link Management Protocol (LMP) features that are supported by the local radio.</p>
</dd>

### -field <b>mfg</b>

<dd>
<p>The identification of the manufacturer.</p>
</dd>

### -field <b>lmpSubversion</b>

<dd>
<p>The minor version number for the LMP that is used by the local radio.</p>
</dd>

### -field <b>lmpVersion</b>

<dd>
<p>The major version number for the LMP that is used by the local radio.</p>
</dd>
</dl>

## -remarks
<p>The BTH_RADIO_INFO structure is returned as part of the output buffer of 
    <a href="..\bthioctl\ni-bthioctl-ioctl-bth-get-local-info.md">IOCTL_BTH_GET_LOCAL_INFO</a>. The local
    radio information is returned in the 
    <b>radioInfo</b> member of the 
    <a href="..\bthioctl\ns-bthioctl--bth-local-radio-info.md">BTH_LOCAL_RADIO_INFO</a> structure.</p>

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
<dt>
<a href="..\bthioctl\ni-bthioctl-ioctl-bth-get-local-info.md">IOCTL_BTH_GET_LOCAL_INFO</a>
</dt>
<dt>
<a href="..\bthioctl\ns-bthioctl--bth-local-radio-info.md">BTH_LOCAL_RADIO_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20BTH_RADIO_INFO structure%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
