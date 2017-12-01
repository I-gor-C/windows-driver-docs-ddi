---
UID: NS.wwan._WWAN_SIGNAL_STATE
title: WWAN_SIGNAL_STATE
author: windows-driver-content
description: The WWAN_SIGNAL_STATE structure represents the signal state of the MB device.
old-location: netvista\wwan_signal_state.htm
old-project: netvista
ms.assetid: ba5632bb-c1d7-47b1-b6b4-88c67710149f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WWAN_SIGNAL_STATE, WWAN_SIGNAL_STATE, *PWWAN_SIGNAL_STATE
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
req.alt-api: WWAN_SIGNAL_STATE
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
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_SIGNAL_STATE structure



## -description
<p>The WWAN_SIGNAL_STATE structure represents the signal state of the MB device.</p>


## -syntax

````
typedef struct _WWAN_SIGNAL_STATE {
  ULONG Rssi;
  ULONG ErrorRate;
  ULONG RssiInterval;
  ULONG RssiThreshold;
} WWAN_SIGNAL_STATE, *PWWAN_SIGNAL_STATE;
````


## -struct-fields
<dl>

### -field <b>Rssi</b>

<dd>
<p>A value that represents the strength of the wireless signal. Miniport drivers that report their
     WWAN_CELLULAR_CLASS to be 
     <b>WwanCellularClassGSM</b> or 
     <b>WwanCellularClassCDMA</b> must report Rssi in decibels above the device's sensitivity noise floor.
     </p>
<table>
<tr>
<th>Signal Strength (in dBm)</th>
<th>Coded Value (Minimum=0, Maximum=31)</th>
</tr>
<tr>
<td>
<p>-113 or less</p>
</td>
<td>
<p>0</p>
</td>
</tr>
<tr>
<td>
<p>-111</p>
</td>
<td>
<p>1</p>
</td>
</tr>
<tr>
<td>
<p>-109</p>
</td>
<td>
<p>2</p>
</td>
</tr>
<tr>
<td>
<p>...</p>
</td>
<td>
<p>...</p>
</td>
</tr>
<tr>
<td>
<p>-51 or greater</p>
</td>
<td>
<p>31</p>
</td>
</tr>
<tr>
<td>
<p>Unknown or undetectable</p>
</td>
<td>
<p>WWAN_RSSI_UNKNOWN</p>
</td>
</tr>
</table>
<p> </p>
<p>CDMA-based devices must report signal strength based on compensated RSSI (accounts for noise) and not
     based on raw RSSI.</p>
</dd>

### -field <b>ErrorRate</b>

<dd>
<p>A coded value that represents a percentage range of error rates. For GSM-based devices, use the
     values from the Channel bit error rate column in the following table. For CDMA-based devices, use the
     values from the Frame error rate column. For both cases, use WWAN_ERROR_RATE_UNKNOWN to denote an
     unknown error rate.
     </p>
<table>
<tr>
<th>Channel bit error rate (in %)</th>
<th>Frame error rate (in %)</th>
<th>Coded value (Min=0, Max=7)</th>
</tr>
<tr>
<td>
<p>&lt; 0.2</p>
</td>
<td>
<p>&lt; 0.01</p>
</td>
<td>
<p>0</p>
</td>
</tr>
<tr>
<td>
<p>0.2-0.4</p>
</td>
<td>
<p>0.01-0.1</p>
</td>
<td>
<p>1</p>
</td>
</tr>
<tr>
<td>
<p>0.4-0.8</p>
</td>
<td>
<p>0.1-0.5</p>
</td>
<td>
<p>2</p>
</td>
</tr>
<tr>
<td>
<p>0.8-1.6</p>
</td>
<td>
<p>0.5-1.0</p>
</td>
<td>
<p>3</p>
</td>
</tr>
<tr>
<td>
<p>- 3.2</p>
</td>
<td>
<p>1.0 - -2.0</p>
</td>
<td>
<p>4</p>
</td>
</tr>
<tr>
<td>
<p>- 6.4</p>
</td>
<td>
<p>2.0-4.0</p>
</td>
<td>
<p>5</p>
</td>
</tr>
<tr>
<td>
<p>6.4-12.8</p>
</td>
<td>
<p>4.0-8.0</p>
</td>
<td>
<p>6</p>
</td>
</tr>
<tr>
<td>
<p>&gt; 12.8</p>
</td>
<td>
<p>&gt; 8.0</p>
</td>
<td>
<p>7</p>
</td>
</tr>
<tr>
<td colspan="2">
<p>Unknown or undetectable</p>
</td>
<td>
<p>WWAN_ERROR_RATE_UNKNOWN</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>RssiInterval</b>

<dd>
<p>The current interval, in seconds, at which the miniport driver has been set to (or the default
     interval, if one has not been set), that the miniport driver will provide updates about the signal
     state. Specify WWAN_RSSI_DISABLE to indicate that the miniport driver does not implement interval-based
     reporting. Miniport drivers should populate this member with the interval in response to an earlier
     request from the MB Service for WWAN_RSSI_DEFAULT.</p>
</dd>

### -field <b>RssiThreshold</b>

<dd>
<p>The current threshold, in threshold units, at which the miniport driver has been set to (or the
     default interval, if one has not been set), that the miniport driver will provide updates about the
     signal state. Specify WWAN_RSSI_DISABLE to indicate that the miniport driver does not implement
     threshold-based reporting. Miniport drivers should populate this member with the threshold units in
     response to an earlier request from the MB Service for WWAN_RSSI_DEFAULT.</p>
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
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-signal-state.md">NDIS_WWAN_SIGNAL_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SIGNAL_STATE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
