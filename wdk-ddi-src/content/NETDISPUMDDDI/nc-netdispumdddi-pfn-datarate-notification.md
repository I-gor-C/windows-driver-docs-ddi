---
UID: NC.netdispumdddi.PFN_DATARATE_NOTIFICATION
title: PFN_DATARATE_NOTIFICATION
author: windows-driver-content
description: Called by the operating system to notify the Miracast user-mode driver that the bit rate of the Miracast network link has changed. This function is registered with the operating system when the RegisterForDataRateNotifications function is called.
old-location: display\pfndataratenotify.htm
ms.assetid: 5eb004d1-7cf8-45a3-aad5-2932b1a83bb8
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnDataRateNotify
req.alt-loc: Netdispumdddi.h
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
ms.keywords: NDK_SRQ, NDK_SRQ
req.iface: 
---

# PFN_DATARATE_NOTIFICATION callback



## -description
<p>Called by the operating system to notify the Miracast user-mode driver that the bit rate of the Miracast network link has changed. This function is registered with the operating system when the <a href="https://msdn.microsoft.com/81500bb9-27f1-4688-b244-37dfd766f3c8">RegisterForDataRateNotifications</a> function is called.</p>


## -prototype

````
PFN_DATARATE_NOTIFICATION pfnDataRateNotify;

void NTAPI* pfnDataRateNotify(
  _In_     PVOID                   context,
  _In_opt_ MIRACAST_DATARATE_STATS *pDataRateStats
)
{ ... }
````


## -parameters
<dl>

### -param <i>context</i> [in]

<dd>
<p>A  pointer to a context block associated with a display adapter.</p>
<p>The context value is the value the driver passed in its call to the <a href="https://msdn.microsoft.com/81500bb9-27f1-4688-b244-37dfd766f3c8">RegisterForDataRateNotifications</a> function when it registered the <i>pfnDataRateNotify</i> function.</p>
</dd>

### -param <i>pDataRateStats</i> [in, optional]

<dd>
<p>An optional pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn265475">MIRACAST_DATARATE_STATS</a> structure that contains info on the audio/video encoder bit rate and failed or retried Wi-Fi frames.</p>
<p>Can be <b>NULL</b> if the network has an error. For more info, see Remarks.</p>
</dd>
</dl>

## -returns
<p>Does not return a value.</p>

## -remarks
<p>If data on the quality of service (QoS) of the network connection becomes unavailable, the <i>pDataRateStats</i> parameter will be set to <b>NULL</b>, and this function will not be called again.</p>

<p>If data on the quality of service (QoS) of the network connection becomes unavailable, the <i>pDataRateStats</i> parameter will be set to <b>NULL</b>, and this function will not be called again.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265475">MIRACAST_DATARATE_STATS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/81500bb9-27f1-4688-b244-37dfd766f3c8">RegisterForDataRateNotifications</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFN_DATARATE_NOTIFICATION callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
