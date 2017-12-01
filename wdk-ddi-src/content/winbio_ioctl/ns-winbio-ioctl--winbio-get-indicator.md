---
UID: NS.winbio_ioctl._WINBIO_GET_INDICATOR
title: WINBIO_GET_INDICATOR
author: windows-driver-content
description: The WINBIO_GET_INDICATOR structure is the OUT payload for IOCTL_BIOMETRIC_GET_INDICATOR.
old-location: biometric\winbio_get_indicator.htm
old-project: biometric
ms.assetid: e0920576-de0f-44bd-8d95-85dde4ee6817
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.keywords: WINBIO_GET_INDICATOR, WINBIO_GET_INDICATOR, *PWINBIO_GET_INDICATOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winbio_ioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WINBIO_GET_INDICATOR
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
req.iface: IWiaTransferCallback
req.product: Windows 10 or later.
---

# WINBIO_GET_INDICATOR structure



## -description
<p>The WINBIO_GET_INDICATOR structure is the OUT payload for <a href="..\winbio_ioctl\ni-winbio-ioctl-ioctl-biometric-get-indicator.md">IOCTL_BIOMETRIC_GET_INDICATOR</a>.</p>


## -syntax

````
typedef struct _WINBIO_GET_INDICATOR {
  DWORD                   PayloadSize;
  HRESULT                 WinBioHresult;
  WINBIO_INDICATOR_STATUS IndicatorStatus;
} WINBIO_GET_INDICATOR, *PWINBIO_GET_INDICATOR;
````


## -struct-fields
<dl>

### -field <b>PayloadSize</b>

<dd>
<p>Specifies the total size of the payload, which includes the fixed length structure and any variable data at the end.</p>
</dd>

### -field <b>WinBioHresult</b>

<dd>
<p>Specifies an HRESULT that contains the status of the I/O operation. See <a href="..\winbio_ioctl\ni-winbio-ioctl-ioctl-biometric-get-indicator.md">IOCTL_BIOMETRIC_GET_INDICATOR</a> for possible values.</p>
</dd>

### -field <b>IndicatorStatus</b>

<dd>
<p>Specifies a WINBIO_INDICATOR_STATUS, which indicates whether the indicator light is on or off.</p>
<p> Possible values are shown in the following table. </p>
<table>
<tr>
<td>
<p>Indicator status code</p>
</td>
<td>
<p>Description</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_INDICATOR_ON</p>
</td>
<td>
<p>The indicator light is on, and changes according to the sensor status.  To be able to set WINBIO_INDICATOR_ON, you must set WINBIO_CAPABILITY_INDICATOR in the <b>Capabilities</b> member of the WINBIO_SENSOR_ATTRIBUTES structure.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_INDICATOR_OFF</p>
</td>
<td>
<p>The sensor indicator light is off.  Sensors that do not have an indicator light will always return this value in IOCTL_GET_SENSOR_STATUS. </p>
</td>
</tr>
</table>
<p> </p>
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
<a href="..\winbio_ioctl\ns-winbio-ioctl--winbio-set-indicator.md">WINBIO_SET_INDICATOR</a>
</dt>
<dt>
<a href="..\winbio_ioctl\ni-winbio-ioctl-ioctl-biometric-get-indicator.md">IOCTL_BIOMETRIC_GET_INDICATOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [biometric\biometric]:%20WINBIO_GET_INDICATOR structure%20 RELEASE:%20(11/13/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
