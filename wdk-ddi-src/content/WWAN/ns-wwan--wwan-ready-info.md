---
UID: NS.wwan._WWAN_READY_INFO
title: WWAN_READY_INFO
author: windows-driver-content
description: The WWAN_READY_INFO structure represents the ready-state of the MB device.
old-location: netvista\wwan_ready_info.htm
ms.assetid: 6db8730e-a1da-428b-9938-fd9f3f71283a
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
req.alt-api: WWAN_READY_INFO
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
ms.keywords: WWAN_READY_INFO, WWAN_READY_INFO, *PWWAN_READY_INFO
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_READY_INFO structure



## -description
<p>The WWAN_READY_INFO structure represents the ready-state of the MB device.</p>


## -syntax

````
typedef struct _WWAN_READY_INFO {
  WWAN_READY_STATE    ReadyState;
  WWAN_EMERGENCY_MODE EmergencyMode;
  WCHAR               SubscriberId[WWAN_SUBSCRIBERID_LEN];
  WCHAR               SimIccId[WWAN_SIMICCID_LEN];
  BYTE                CdmaShortMsgSize;
  WWAN_LIST_HEADER    TNListHeader;
} WWAN_READY_INFO, *PWWAN_READY_INFO;
````


## -struct-fields
<dl>

### -field <b>ReadyState</b>

<dd>
<p>The ready-state of the device.</p>
</dd>

### -field <b>EmergencyMode</b>

<dd>
<p>The emergency mode of the device. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff571207">WWAN_EMERGENCY_MODE</a>.</p>
</dd>

### -field <b>SubscriberId</b>

<dd>
<p>A NULL-terminated string of digits that represents the identity of the subscriber.</p>
<p>For GSM-based devices, this member represents the International Mobile Subscriber Identity (IMSI) string (up to 15 digits in length).</p>
<p>For CDMA-based devices, this represents the Mobile Identification Number (MIN) string or the International Roaming MIN (IRM) string (both 10 digits in length).</p>
<p>Miniport drivers must specify this string when the device ready-state changes to <b>WwanReadyStateInitialized</b>. Miniport drivers should also specify this string when the device ready-state changes to <b>WwanReadyStateBadSim</b>, <b>WwanReadyStateFailure</b>, or <b>WwanReadyStateDeviceLocked</b>, if possible, for identification purposes.</p>
<p>For single-carrier multi-mode functions, the GSM <b>SubscriberId</b> format must be used.  This does not apply to multi-carrier multi-mode functions as the <b>SubscriberId</b> may change.</p>
</dd>

### -field <b>SimIccId</b>

<dd>
<p>A NULL-terminated string of digits that represents the International Circuit Card (ICC) ID of the SIM. The ICC ID varies from between 15 to 20 digits in length and is represented in alphanumeric characters. Miniport drivers must specify this string when the device ready-state changes to <b>WwanReadyStateInitialized</b> and also when the device is locked, waiting for entry of PIN1 and PUK1 keys.</p>
<p>Miniport drivers must specify this value for all devices where <b>WwanCellularClass</b> equals <b>WwanCellularClassGsm</b>. Miniport drivers of CDMA-based devices must specify this value for devices where <b>SimClass</b> equals <b>WwanSimClassSimRemovable</b>.</p>
</dd>

### -field <b>CdmaShortMsgSize</b>

<dd>
<p>The SMS character length that is supported by the network or the device, whichever is less, if the device is CDMA-based.</p>
<p>CDMA-based devices that support SMS should specify their carrier-specific maximum SMS character length to be greater than WWAN_CDMA_SHORT_MSG_SIZE_UNKNOWN and less than WWAN_CDMA_SHORT_MSG_SIZE_MAX.</p>
<p>CDMA-based devices that do not support SMS should set this member to WWAN_CDMA_SHORT_MSG_SIZE_UNKNOWN.</p>
<p>This member does not apply to GSM-based devices. Miniport drivers of GSM-based devices should specify WWAN_CDMA_SHORT_MSG_SIZE_UNKNOWN.</p>
</dd>

### -field <b>TNListHeader</b>

<dd>
<p>A list of telephone numbers (TNs) that are assigned to the subscriber identity.</p>
<p>Each element in the list is a string of WCHARs, with a fixed size of WWAN_TN_LEN.</p>
<p>Each TN stored in a list element is a NULL-terminated value.</p>
<p>In GSM-based devices the TNs are called Mobile Station ISDN Number (MSISDNs). In CDMA-based devices they are called Mobile Directory Numbers (MDNs).</p>
<p>Miniport drivers should not specify this value until the device ready-state changes to <b>WwanReadyStateInitialized</b>.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571227">WWAN_READY_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571207">WWAN_EMERGENCY_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571208">WWAN_LIST_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567916">NDIS_WWAN_READY_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_READY_INFO structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
